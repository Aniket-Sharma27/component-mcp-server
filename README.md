# component-mcp-server

A standalone [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server that exposes our design system's component documentation to LLM clients.

Component docs live as Markdown files (with YAML frontmatter) in [`contexts/`](./contexts). The server reads them at request time — no build step is needed to add or update a component.

## Tools

### `list_components`

No input. Scans the `contexts/` directory for all `.md` files and returns their names (without the `.md` extension) as a JSON array. Use this to discover what components are documented before requesting one.

### `get_component_context`

Input: `{ componentName: string }`

Looks up `contexts/<componentName>.md` (case-insensitive). If found, returns:

- `frontmatter` — the parsed YAML frontmatter as structured JSON
- `body` — the raw markdown body (frontmatter stripped)
- `raw` — the full original file content (frontmatter + body together), so a caller can just read it as plain documentation

If the component isn't found, returns an error object listing the currently available component names so the caller can retry with a valid one.

## Running locally

```bash
npm install
npm run dev
```

`npm run dev` runs the server directly via `tsx` (fast iteration, no build step). The server communicates over stdio, so it won't print anything on its own — it's meant to be driven by an MCP client.

Other scripts:

```bash
npm run build   # compile TypeScript to dist/
npm run start   # run the compiled server (node dist/index.js)
```

## Testing standalone with MCP Inspector

```bash
npx @modelcontextprotocol/inspector npx tsx src/index.ts
```

This opens a web UI where you can call `list_components` and `get_component_context` directly and inspect the responses.

## Connecting to Claude Code

```bash
claude mcp add --transport stdio component-mcp -- npx tsx <absolute path to src/index.ts>
```

Replace `<absolute path to src/index.ts>` with the full path on your machine, e.g. `C:\Users\you\path\to\component-mcp-server\src\index.ts`. Once added, Claude Code can call `list_components` and `get_component_context` directly.

## Adding a new component

Drop a new `<name>.md` file into `contexts/`, following the same frontmatter + markdown body structure as `contexts/button.md`. No code changes are required — `list_components` and `get_component_context` will pick it up automatically.
