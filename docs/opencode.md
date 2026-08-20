# Connecting to component-mcp-server from opencode

This server exposes MCP tools over Streamable HTTP at `POST /mcp`, guarded by a bearer token.

Add it as a remote MCP server in your `opencode.json`:

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

Notes:

- `url` must point at the `/mcp` path specifically (not the bare host).
- `<API_KEY>` is the same bearer token the server was started with (`API_KEY` env var) — get it from whoever deployed the server, never commit it into `opencode.json`. If your `opencode.json` is checked into a shared repo, put the header value in opencode's own secret/env substitution mechanism instead of a literal string.
- If the server sits behind the recommended Caddy reverse proxy (see the main [README](../README.md#7-tlshttps-required-before-any-public-exposure)), `<your-deployed-host>` is the public HTTPS domain, not the internal `localhost:3000` the Node process actually listens on.
