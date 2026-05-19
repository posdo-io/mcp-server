# `find_restaurants_near_landmark`

Find restaurants within walking distance of a famous landmark (Wikidata-backed).

## Description

> Find restaurants near a famous landmark (monument, museum, park). Returns landmark info from Wikidata + nearby restaurants sorted by walking distance. Examples: 'Sagrada Familia', 'Colosseum', 'Central Park', 'Tour Eiffel'.

## Input schema

- **`landmark`** — `string` **(required)** — Landmark name.
- **`city`** — `string` — City hint for landmark disambiguation.
- **`radius`** — `integer` (min=200, max=5000, default=1000) — Search radius in meters.
- **`limit`** — `integer` (min=1, max=15, default=10)

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "find_restaurants_near_landmark",
      "arguments": {
    "landmark": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
