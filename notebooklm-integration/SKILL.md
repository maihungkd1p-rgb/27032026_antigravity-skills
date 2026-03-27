---
name: notebooklm-integration
description: Interacts with Google NotebookLM via MCP. Use when the user asks to list, query, summarize, or create content from their NotebookLM notebooks.
---

# NotebookLM Integration

## When to use this skill
- User asks to "list my notebooks" or "show my NotebookLM"
- User wants to query/search content in a specific notebook
- User provides a NotebookLM URL and asks for a summary
- User wants to create study guides, flashcards, or audio overviews from notebooks

## Prerequisites
- NotebookLM MCP server must be installed and authenticated
- Auth tokens stored at `~/.notebooklm-mcp/auth.json`

## Available MCP Tools

| Tool | Purpose |
|------|---------|
| `notebook_list` | List all notebooks |
| `notebook_get` | Get notebook by ID |
| `notebook_describe` | Get AI-generated summary of a notebook |
| `source_describe` | Describe a specific source in a notebook |
| `source_get_content` | Get full content of a source |
| `notebook_add_url` | Add a URL as a source |
| `notebook_add_text` | Add text as a source |

## Workflow

### Listing Notebooks
```
1. Call `notebook_list` tool
2. Display results as a formatted list with names and IDs
```

### Querying a Notebook
```
1. If user provides URL, extract notebook ID from: notebooklm.google.com/notebook/{ID}
2. Call `notebook_describe` with `notebook_id` parameter
3. Parse JSON response and present summary in user's language
```

### Getting Source Content
```
1. Call `notebook_get` to list sources in the notebook
2. For each relevant source, call `source_get_content`
3. Synthesize information based on user's query
```

## Important Notes
- All tool arguments use **snake_case** (e.g., `notebook_id`, not `notebookId`)
- If `notebook_list` returns empty, ask user for the direct notebook URL
- Extract ID from URL pattern: `notebooklm.google.com/notebook/{UUID}`

## Error Handling
- If auth fails: Run `notebooklm-mcp-auth` command in terminal
- If notebook not found: Verify user is logged into correct Google account
