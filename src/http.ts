import express, { type Request, type Response, type NextFunction } from "express";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { createServer } from "./server.js";

const PORT = Number(process.env.PORT) || 3000;
const API_KEY = process.env.API_KEY;

if (!API_KEY) {
  console.error("Fatal: API_KEY environment variable is not set.");
  process.exit(1);
}

function requireBearerToken(req: Request, res: Response, next: NextFunction) {
  const header = req.header("authorization");
  const token = header?.startsWith("Bearer ") ? header.slice("Bearer ".length) : undefined;

  if (!token || token !== API_KEY) {
    res.status(401).json({
      jsonrpc: "2.0",
      error: { code: -32001, message: "Unauthorized: missing or invalid bearer token" },
      id: null,
    });
    return;
  }

  next();
}

const app = express();
app.use(express.json());

// Stateless mode: a fresh MCP server + transport per request, no session
// state kept between calls. Simpler and safe for multiple concurrent clients.
app.post("/mcp", requireBearerToken, async (req: Request, res: Response) => {
  try {
    const server = createServer();
    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: undefined,
    });

    res.on("close", () => {
      transport.close();
      server.close();
    });

    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (err) {
    console.error("Error handling MCP request:", err);
    if (!res.headersSent) {
      res.status(500).json({
        jsonrpc: "2.0",
        error: { code: -32603, message: "Internal server error" },
        id: null,
      });
    }
  }
});

// Stateless mode has no server-to-client stream or session to terminate.
app.get("/mcp", requireBearerToken, (_req: Request, res: Response) => {
  res.status(405).json({
    jsonrpc: "2.0",
    error: { code: -32000, message: "Method not allowed: this server runs in stateless mode" },
    id: null,
  });
});

app.delete("/mcp", requireBearerToken, (_req: Request, res: Response) => {
  res.status(405).json({
    jsonrpc: "2.0",
    error: { code: -32000, message: "Method not allowed: this server runs in stateless mode" },
    id: null,
  });
});

app.listen(PORT, () => {
  console.log(`component-mcp-server (Streamable HTTP) listening on port ${PORT}`);
  console.log(`MCP endpoint: POST http://localhost:${PORT}/mcp`);
});