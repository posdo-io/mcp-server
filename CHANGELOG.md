# Changelog

All notable changes to the POS.DO MCP Server are recorded here. The server endpoint follows semantic versioning at the `/.well-known/mcp.json` manifest level.

## [0.1.0] — 2026-05-19

### Added
- Initial public release of the proxy repository
- 7 tools exposed via MCP 2024-11-05 over `https://pos.do/mcp`:
  - `search_restaurants`
  - `get_restaurant_details`
  - `get_restaurant_reviews`
  - `get_flow_offers`
  - `book_flow_reservation`
  - `find_restaurants_near_landmark`
  - `get_cultural_context_around_restaurant`
- Atomic idempotency on `book_flow_reservation` via `Idempotency-Key` header (UNIQUE constraint backstop)
- Rate limits: 60 req/min + 10K/day per IP (anonymous tier)
- Reservation rate limits: 10/min per IP + 5/day per email
- 4 discovery manifest paths served:
  - `/.well-known/mcp.json` (official spec)
  - `/.well-known/webmcp.json`
  - `/.well-known/mcp/server-card.json`
  - `/mcp/manifest.json`
- Coverage at launch: 356,780 restaurants, 14.1M reviews, 20 countries, 7 languages

[0.1.0]: https://github.com/posdo-io/mcp-server/releases/tag/v0.1.0
