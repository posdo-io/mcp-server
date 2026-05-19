<div align="center">
  <img src="logo.png" alt="POS.DO MCP Server" width="200" height="200"/>

  # PosDO MCP Server

  **Discovery of 356K+ restaurants across 20 countries via the Model Context Protocol.**

  [![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
  [![MCP](https://img.shields.io/badge/MCP-2024--11--05-8b5cf6.svg)](https://modelcontextprotocol.io)
  [![Endpoint](https://img.shields.io/badge/endpoint-pos.do%2Fmcp-3b82f6.svg)](https://pos.do/mcp)
</div>

---

POS.DO is a discovery platform with global coverage of restaurants — names, addresses, reviews, photos, opening hours, cuisines, neighbourhoods, cultural context, and real-time availability with time-based offers. This MCP server exposes that catalogue to AI agents over the Model Context Protocol.

## What this server provides

- **356,780 restaurants** in **20 countries** (US, ES, IT, MX, FR, CO, DE, GB, DO, PR, AU, CA, PT, JP, BE, CH, HK, VE, NZ, PY)
- **7 languages** of content (ES, EN, IT, FR, DE, PT, CA)
- **14.1M+ user reviews** with author, rating, text, language, photos
- **Cultural context** — nearby monuments, museums, parks, and heritage sites from Wikidata, per restaurant
- **Flow time-based offers** — off-peak discounts at participating restaurants, with real seat availability
- **Reservation booking** with idempotent semantics (safe retries via `Idempotency-Key` header)

This is a **proxy repository**. The MCP endpoint runs at `https://pos.do/mcp` and is operated by EZZYPUSH SL. No local installation of the server is required — agents just point at the URL.

## Quick start

### Claude Desktop

Add to `claude_desktop_config.json`:

```jsonc
{
  "mcpServers": {
    "pos-do": {
      "url": "https://pos.do/mcp"
    }
  }
}
```

Restart Claude Desktop. The 7 tools below become available.

### Cursor / Cline / Continue

Most MCP clients accept a remote HTTP server entry of the same shape. For Cursor:

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

### Generic MCP client (raw JSON-RPC over HTTP)

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Tools

| Tool | Purpose | Docs |
|---|---|---|
| `search_restaurants` | Search restaurants in a city, with cuisine/price/feature filters | [docs](docs/tools/search_restaurants.md) |
| `get_restaurant_details` | Full profile for a restaurant by slug | [docs](docs/tools/get_restaurant_details.md) |
| `get_restaurant_reviews` | Paginated reviews with star and date filters | [docs](docs/tools/get_restaurant_reviews.md) |
| `get_flow_offers` | Today's time-based discount slots for a restaurant | [docs](docs/tools/get_flow_offers.md) |
| `book_flow_reservation` | Reserve a seat at a Flow-discounted slot | [docs](docs/tools/book_flow_reservation.md) |
| `find_restaurants_near_landmark` | Restaurants within walking distance of a famous landmark | [docs](docs/tools/find_restaurants_near_landmark.md) |
| `get_cultural_context_around_restaurant` | Monuments, museums, parks near a restaurant (Wikidata) | [docs](docs/tools/get_cultural_context_around_restaurant.md) |

Full tool inventory with `inputSchema` is served live at [`/.well-known/mcp.json`](https://pos.do/.well-known/mcp.json).

## Endpoint and transport

- **Production URL**: `https://pos.do/mcp`
- **Protocol**: MCP 2024-11-05
- **Transport**: HTTP POST (JSON-RPC 2.0), Streamable HTTP compatible
- **Discovery manifests**:
  - `https://pos.do/.well-known/mcp.json` — official MCP discovery (full `tools[]` with `inputSchema`)
  - `https://pos.do/.well-known/webmcp.json` — webmcp.link manifest
  - `https://pos.do/.well-known/mcp/server-card.json` — Smithery-style server card
  - `https://pos.do/mcp/manifest.json` — alias

## Authentication and rate limits

The server runs in **anonymous tier** by default. No API key required.

| Tier | Per minute | Per day |
|---|---|---|
| Anonymous (default) | 60 req/min per IP | 10,000 req/day per IP |
| Reservation attempts | 10/min per IP | 5/day per email |

Higher-rate API keys are available on request — open an issue.

For idempotent reservations, send an `Idempotency-Key` HTTP header (any UUID or stable client-side key). Replays within 24 h return the original reservation instead of creating a duplicate.

## Coverage and data sources

See [`docs/data-coverage.md`](docs/data-coverage.md) for per-country counts and source attributions.

## Examples

- [Python](examples/python/search_example.py)
- [Node](examples/node/search_example.js)
- [curl](examples/curl/search_example.sh)

## Status

Stable. Backwards-compatible changes only at this point. Breaking changes will be announced via [CHANGELOG.md](CHANGELOG.md) and bumped to `2.x`.

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Contact

- **Issues / feature requests**: [github.com/posdo-io/mcp-server/issues](https://github.com/posdo-io/mcp-server/issues)
- **Operator**: EZZYPUSH SL (Spain)
- **Website**: [pos.do](https://pos.do)
