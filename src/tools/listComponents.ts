import { readdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const CONTEXTS_DIR = path.resolve(__dirname, "..", "..", "contexts");

/**
 * Scans the contexts/ directory and returns component names (without .md extension).
 */
export async function scanComponentNames(): Promise<string[]> {
  let entries: string[];
  try {
    entries = await readdir(CONTEXTS_DIR);
  } catch (err) {
    throw new Error(
      `Failed to read contexts directory at "${CONTEXTS_DIR}": ${
        err instanceof Error ? err.message : String(err)
      }`
    );
  }

  return entries
    .filter((name) => name.toLowerCase().endsWith(".md"))
    .map((name) => name.slice(0, -3))
    .sort((a, b) => a.localeCompare(b));
}

export async function listComponentsHandler() {
  const names = await scanComponentNames();
  return {
    content: [
      {
        type: "text" as const,
        text: JSON.stringify(names, null, 2),
      },
    ],
  };
}
