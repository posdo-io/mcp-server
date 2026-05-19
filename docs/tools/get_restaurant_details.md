# `get_restaurant_details`

Fetch the full profile of a restaurant by its URL slug.

## Description

> Get the full profile of a restaurant by URL slug. Returns name, address, coordinates, rating, reviews count, phone, opening hours, photos, services, cuisine type, price level, current Flow offers, and cultural context.

## Input schema

- **`slug`** — `string` **(required)** — Restaurant URL slug. Example: 'anima-e-cuore-osteria-bilbao'.

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "get_restaurant_details",
      "arguments": {
    "slug": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
