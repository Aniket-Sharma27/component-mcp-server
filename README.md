# component-mcp-server

A standalone [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server that exposes design system component documentation to LLM clients. It reads Markdown files with YAML frontmatter from [`contexts/`](./contexts) and serves them over two MCP tools — `list_components` and `get_component_context` — so an LLM can look up a real component's props, design tokens, and events before generating code against it.

This guide covers deploying it standalone (no Docker) to a fresh AWS EC2 instance, running under [PM2](https://pm2.keithcirkel.co.uk/).

## 1. What this service is

- An MCP server, reachable over HTTP, that answers two questions for an LLM client: "what components are documented?" (`list_components`) and "give me everything you know about component X" (`get_component_context`).
- Stateless: every `/mcp` request spins up a fresh MCP server + transport internally, so it's safe to run behind a load balancer with multiple concurrent clients and no session affinity required.
- Read-only against `contexts/` — there's no database, no write path; updating documentation means editing/adding a Markdown file in that directory (see [§9](#9-adding-or-updating-a-component)).

## 2. Prerequisites

- **Node.js 18 or later** (LTS recommended — 20.x or newer). The build uses `NodeNext` module resolution and ES2022 target, which need a reasonably current Node.
- **npm** (ships with Node).
- **PM2**, installed globally on the instance:
  ```bash
  npm install -g pm2
  ```

## 3. Environment variables

Copy [`.env.example`](./.env.example) to `.env` and fill in real values — or export the same variables directly in the shell/systemd unit that starts PM2 (PM2 does not read `.env` files itself unless you load them into the shell first; see [§5](#5-starting-the-server-under-pm2)).

| Variable | Required | Purpose | How to set it |
|---|---|---|---|
| `API_KEY` | Yes — the server exits immediately at startup if this is unset | Bearer token that every `/mcp` request must present in `Authorization: Bearer <value>`. This is the only thing standing between the internet and your component docs, so it must be a real secret, not a memorable string. | Generate a random 32-byte hex token: `openssl rand -hex 32`. Store the result somewhere your deploy process can read it (a secrets manager, an untracked `.env`, or an EC2 instance's environment) — never commit it to git. |
| `PORT` | No (defaults to `3000`) | TCP port the Node process listens on. | Pick anything free on the instance; `3000` is fine if nothing else uses it. Combined with the reverse proxy in [§7](#7-tlshttps-required-before-any-public-exposure), this port should only ever be reached from `localhost`, never exposed directly to the internet. |

## 4. Install and build

From the repo root, in order:

```bash
npm install
npm run build
```

`npm run build` runs `tsc` and compiles `src/` to `dist/`. Confirm it produced output:

```bash
ls dist/
# expect: http.js  index.js  server.js  tools/
```

The HTTP entrypoint is `dist/http.js`.

## 5. Starting the server under PM2

Export the environment variables from [§3](#3-environment-variables) into the shell before starting PM2 — PM2 captures and persists the environment of the process that starts it, reusing it on subsequent `restart`/`resurrect`:

```bash
export API_KEY=$(cat /path/to/your/secret)   # or however you're sourcing it
export PORT=3000

pm2 start ecosystem.config.cjs
```

> The config file is `ecosystem.config.cjs` (not `.js`) — this package is `"type": "module"` in `package.json`, and PM2's config loader needs CommonJS, so `.cjs` is required, not a style choice.

Confirm it's actually running:

```bash
pm2 list
# expect a row for "component-mcp-server" with status "online"

pm2 logs component-mcp-server --lines 20
# expect: "component-mcp-server (Streamable HTTP) listening on port 3000"
```

### Surviving an instance reboot

Starting it once isn't enough — by default PM2 doesn't survive a reboot. Set up both of these, once:

```bash
pm2 save                # snapshots the current process list
pm2 startup              # prints an OS-specific command
# copy/paste and run the command pm2 startup prints, as root (e.g. via sudo) —
# this registers a systemd (or equivalent) service that resurrects
# "pm2 save"'s snapshot on boot
```

After any future change to what's running under PM2 (new app, changed env, etc.), re-run `pm2 save` so the snapshot stays current.

### Other PM2 commands you'll use

| Action | Command |
|---|---|
| Stop | `pm2 stop component-mcp-server` |
| Restart (drops in-flight connections) | `pm2 restart component-mcp-server` |
| Reload (zero-downtime) | `pm2 reload component-mcp-server` |
| Remove from PM2 entirely | `pm2 delete component-mcp-server` |
| Tail logs | `pm2 logs component-mcp-server` |

Logs also land in `logs/out.log` and `logs/error.log` in the repo root (gitignored), independent of `pm2 logs`.

## 6. Verifying it's working

A process showing "online" in `pm2 list` only proves Node is alive — it doesn't prove the service actually works. Do both of these:

**Health check** (confirms `contexts/` is present and readable, not just that the process exists):

```bash
curl -s http://localhost:3000/health
# expect: {"status":"ok","components":20}
# (component count will match whatever's actually in contexts/)
```

A `503` here means `contexts/` is missing or unreadable — investigate before moving on.

**A real end-to-end MCP call** — this exercises the actual tool logic, not just connectivity:

```bash
curl -s -X POST http://localhost:3000/mcp \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "get_component_context",
      "arguments": { "componentName": "button" }
    }
  }'
```

Expect a `text/event-stream` response containing the button component's frontmatter, body, and raw content. If you'd rather click through it interactively, point the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) at `http://localhost:3000/mcp` with the same bearer token.

Also confirm auth is actually enforced — this should return `401`, not the component data:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"ping"}'
# expect: 401
```

## 7. TLS/HTTPS — required before any public exposure

**This server speaks plain HTTP only. It does not terminate TLS itself.** Do not point a public DNS record or security-group rule directly at port `3000` — put a reverse proxy in front that handles HTTPS, and only expose *that*.

The simplest option is [Caddy](https://caddyserver.com/): it gets you automatic HTTPS via Let's Encrypt with a few lines of config and no manual certificate renewal.

```bash
# Install Caddy (Debian/Ubuntu example — see caddyserver.com for other distros)
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install caddy
```

Minimal `Caddyfile` (typically `/etc/caddy/Caddyfile`):

```
component-docs.yourdomain.com {
    reverse_proxy localhost:3000
}
```

Reload Caddy after editing:

```bash
sudo systemctl reload caddy
```

That's it — Caddy provisions and renews the Let's Encrypt certificate automatically as long as the domain's DNS points at this instance and ports 80/443 are open in your security group. Clients then connect to `https://component-docs.yourdomain.com/mcp`, never to the bare Node port.

## 8. Security notes

- **Rate limiting** is enabled: `/mcp` allows 100 requests/minute per IP; `/health` allows 300/minute (it's expected to be polled more often by uptime checks).
- **Bearer token auth is required** on all `/mcp` requests (`POST`, `GET`, `DELETE`) — a missing or incorrect `Authorization` header gets a `401`, never a peek at component data. `/health` does not require auth (it reveals no component content, just a readiness signal).
- The `API_KEY` value is the shared secret every consuming team needs. Distribute it out-of-band (a secrets manager, a password manager entry, a DM) — **never** in a committed config file, a Slack message that gets indexed, or a public repo. Rotate it by updating the deployed environment variable and restarting PM2 with `pm2 restart component-mcp-server --update-env` (after re-exporting the new `API_KEY` — see [§5](#5-starting-the-server-under-pm2)), then redistributing the new value to consumers.

  **`--update-env` is not optional here.** PM2 caches the environment a process was originally started with and reuses it on a plain `restart`, even if you've re-exported a new value in your shell first — the old key keeps working and the new one is rejected until you pass `--update-env` to force PM2 to reread the environment. Confirmed by testing directly: after re-exporting `API_KEY` and running plain `pm2 restart`, the *old* key still returned `200` and the *new* key returned `401`; re-running with `pm2 restart component-mcp-server --update-env` reversed both — old key `401`, new key `200`.

## 9. Adding or updating a component

1. Gather the component's full source material (Angular source, TS interfaces, design tokens, docs, Storybook stories, usage samples).
2. Feed [`extraction-prompt.md`](./extraction-prompt.md) to an LLM along with that material. It produces a single Markdown file (YAML frontmatter + body) in the format the rest of `contexts/` uses.
3. Save it as `contexts/<componentName>.md`.
4. **Run the validator — this is mandatory, not optional:**
   ```bash
   python3 validate_component.py contexts/<componentName>.md
   ```
   A new or updated component file is not considered done until this exits `0`. Fix every blocking issue it reports and re-run. Review warnings too — they're not always errors, but each should be a deliberate, explainable choice, not something overlooked.
5. No deploy or restart needed — `contexts/` is read at request time, so the change is live as soon as the file is saved on the running instance.

## 10. How teams connect once deployed

The server speaks MCP Streamable HTTP at `POST https://<your-deployed-host>/mcp` (through the reverse proxy from [§7](#7-tlshttps-required-before-any-public-exposure)), authenticated with the shared bearer token from [§8](#8-security-notes).

### Claude Code

```bash
claude mcp add --transport http component-docs https://<your-deployed-host>/mcp \
  --header "Authorization: Bearer <API_KEY>"
```

Or directly in `.mcp.json`:

```json
{
  "mcpServers": {
    "component-docs": {
      "type": "http",
      "url": "https://<your-deployed-host>/mcp",
      "headers": {
        "Authorization": "Bearer <API_KEY>"
      }
    }
  }
}
```

### opencode

```json
{
  "mcp": {
    "component-docs": {
      "type": "remote",
      "url": "https://<your-deployed-host>/mcp",
      "headers": {
        "Authorization": "Bearer <API_KEY>"
      },
      "enabled": true
    }
  }
}
```

See [`docs/opencode.md`](./docs/opencode.md) for opencode-specific notes (secret handling, config file location).

Replace `<your-deployed-host>` with the real domain from [§7](#7-tlshttps-required-before-any-public-exposure) and `<API_KEY>` with the real token from [§3](#3-environment-variables) — never commit either into a shared config file.
