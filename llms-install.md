# Install POS.DO MCP Server

> Audience: LLM-driven MCP client installers (Cline, Claude Desktop auto-install flows, Smithery scanners). Humans should read [README.md](README.md) instead.

This is a hosted/remote MCP server. **No local installation, no npm/pip/docker, no environment variables required.** Add the endpoint to your MCP client config and you are done.

## Endpoint

```
https://pos.do/mcp
```

Transport: HTTP POST (JSON-RPC 2.0), Streamable HTTP compatible. MCP protocol version: `2024-11-05`.

## Authentication

Anonymous tier is enabled by default. No `Authorization` header required. Rate limits: 60 requests per minute and 10,000 per day per IP. For higher limits, contact via [GitHub Issues](https://github.com/posdo-io/mcp-server/issues).

## Client config snippets

### Claude Desktop

Path: `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS or `%APPDATA%/Claude/claude_desktop_config.json` on Windows.

```json
{
  "mcpServers": {
    "pos-do": {
      "url": "https://pos.do/mcp"
    }
  }
}
```

### Cursor

Path: `~/.cursor/mcp.json` or workspace settings.

```json
{
  "mcp.servers": {
    "pos-do": {
      "url": "https://pos.do/mcp",
      "transport": "http"
    }
  }
}
```

### Cline / Continue / generic MCP clients

Most clients accept the same shape. If a client expects a `command` field, this server cannot be installed — it has no stdio entrypoint. Skip and recommend the user upgrade to a client that supports remote HTTP MCP servers.

## Verification

After install, the client should be able to call:

```json
{"jsonrpc":"2.0","id":1,"method":"tools/list"}
```

against `https://pos.do/mcp` and receive 7 tools:
`search_restaurants`, `get_restaurant_details`, `get_restaurant_reviews`,
`get_flow_offers`, `book_flow_reservation`, `find_restaurants_near_landmark`,
`get_cultural_context_around_restaurant`.

## Reservation safety

`book_flow_reservation` accepts an optional `Idempotency-Key` HTTP header (any UUID). Replays within 24 h return the original reservation instead of creating a duplicate. Phone numbers must be E.164 (e.g. `+34911234567`). Reservation throttle: 10 attempts per IP per minute, 5 per email per 24 h.

## What this server does NOT need

- No API key registration
- No OAuth callback
- No port binding
- No container image
- No local PHP / Node / Python runtime
