import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import matter from "gray-matter";
import { CONTEXTS_DIR, scanComponentNames } from "./listComponents.js";

interface GetComponentContextInput {
  componentName: string;
}

async function findFileCaseInsensitive(componentName: string): Promise<string | null> {
  const target = `${componentName.toLowerCase()}.md`;
  const entries = await readdir(CONTEXTS_DIR);
  const match = entries.find((name) => name.toLowerCase() === target);
  return match ?? null;
}

export async function getComponentContextHandler({ componentName }: GetComponentContextInput) {
  const fileName = await findFileCaseInsensitive(componentName);

  if (!fileName) {
    const available = await scanComponentNames();
    return {
      isError: true,
      content: [
        {
          type: "text" as const,
          text: JSON.stringify(
            {
              error: `No component context found for "${componentName}".`,
              availableComponents: available,
            },
            null,
            2
          ),
        },
      ],
    };
  }

  const filePath = path.join(CONTEXTS_DIR, fileName);
  const rawContent = await readFile(filePath, "utf-8");

  let parsed;
  try {
    parsed = matter(rawContent);
  } catch (err) {
    return {
      isError: true,
      content: [
        {
          type: "text" as const,
          text: JSON.stringify(
            {
              error: `Failed to parse YAML frontmatter in "${fileName}".`,
              details: err instanceof Error ? err.message : String(err),
            },
            null,
            2
          ),
        },
      ],
    };
  }

  return {
    content: [
      {
        type: "text" as const,
        text: JSON.stringify(
          {
            frontmatter: parsed.data,
            body: parsed.content,
            raw: rawContent,
          },
          null,
          2
        ),
      },
    ],
  };
}
