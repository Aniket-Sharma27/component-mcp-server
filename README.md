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

## Running locally (stdio)

```bash
npm install
npm run dev