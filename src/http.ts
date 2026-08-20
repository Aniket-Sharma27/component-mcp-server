import express, { type Request, type Response, type NextFunction } from "express";
import rateLimit from "express-rate-limit";
import compression from "compression";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { createServer } from "./server.js";
import { scanComponentNames } from "./tools/listComponents.js";

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

const mcpLimiter = rateLimit({
  windowMs: 60 * 1000,
  limit: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: {
    jsonrpc: "2.0",
    error: { code: -32000, message: "Too many requests" },
    id: null,
  },
});

// More generous since health checks are polled far more frequently than MCP calls.
const healthLimiter = rateLimit({
  windowMs: 60 * 1000,
  limit: 300,
  standardHeaders: true,
  legacyHeaders: false,
});

const app = express();
app.use(
  // Skip SSE responses: compression buffers chunks internally, which
  // works against the Streamable HTTP transport's own flushing.
  compression({
    filter: (req, res) => {
      if (res.getHeader("Content-Type") === "text/event-stream") return false;
      return compression.filter(req, res);
    },
  })
);
app.use(express.json());

app.get("/health", healthLimiter, async (_req: Request, res: Response) => {
  try {
    const names = await scanComponentNames();
    if (names.length === 0) {
      res.status(503).json({ status: "error", reason: "contexts/ directory is empty" });
      return;
    }
    res.status(200).json({ status: "ok", components: names.length });
  } catch (err) {
    console.error("Health check failed:", err);
    res.status(503).json({ status: "error", reason: "contexts/ directory is not readable" });
  }
});

// Stateless mode: a fresh MCP server + transport per request, no session
// state kept between calls. Simpler and safe for multiple concurrent clients.
app.post("/mcp", mcpLimiter, requireBearerToken, async (req: Request, res: Response) => {
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
app.get("/mcp", mcpLimiter, requireBearerToken, (_req: Request, res: Response) => {
  res.status(405).json({
    jsonrpc: "2.0",
    error: { code: -32000, message: "Method not allowed: this server runs in stateless mode" },
    id: null,
  });
});

app.delete("/mcp", mcpLimiter, requireBearerToken, (_req: Request, res: Response) => {
  res.status(405).json({
    jsonrpc: "2.0",
    error: { code: -32000, message: "Method not allowed: this server runs in stateless mode" },
    id: null,
  });
});

// Catches anything unhandled above (e.g. malformed JSON bodies from
// express.json()) — logs the real error server-side, never leaks it to the client.
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
  console.error("Unhandled error:", err);
  if (res.headersSent) {
    return;
  }
  res.status(500).json({
    jsonrpc: "2.0",
    error: { code: -32603, message: "Internal server error" },
    id: null,
  });
});

app.listen(PORT, () => {
  console.log(`component-mcp-server (Streamable HTTP) listening on port ${PORT}`);
  console.log(`MCP endpoint: POST http://localhost:${PORT}/mcp`);
});