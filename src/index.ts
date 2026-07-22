import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { listComponentsHandler } from "./tools/listComponents.js";
import { getComponentContextHandler } from "./tools/getComponentContext.js";

const server = new McpServer({
  name: "component-mcp-server",
  version: "1.0.0",
});

server.registerTool(
  "list_components",
  {
    description:
      "Scans the contexts/ directory and returns the names of all available design system components (without the .md extension), so a caller can discover what's available before requesting details.",
    inputSchema: {},
  },
  async () => {
    try {
      return await listComponentsHandler();
    } catch (err) {
      return {
        isError: true,
        content: [
          {
            type: "text" as const,
            text: `Failed to list components: ${err instanceof Error ? err.message : String(err)}`,
          },
        ],
      };
    }
  }
);

server.registerTool(
  "get_component_context",
  {
    description:
      "Looks up contexts/<componentName>.md (case-insensitive) and returns its parsed frontmatter, raw markdown body, and full raw file content. If the component isn't found, returns an error listing the currently available component names.",
    inputSchema: {
      componentName: z.string().describe("The name of the component to fetch context for, e.g. 'button'"),
    },
  },
  async ({ componentName }) => {
    try {
      return await getComponentContextHandler({ componentName });
    } catch (err) {
      return {
        isError: true,
        content: [
          {
            type: "text" as const,
            text: `Failed to get component context for "${componentName}": ${
              err instanceof Error ? err.message : String(err)
            }`,
          },
        ],
      };
    }
  }
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error("Fatal error starting component-mcp-server:", err);
  process.exit(1);
});
