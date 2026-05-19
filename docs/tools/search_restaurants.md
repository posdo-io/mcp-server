# `search_restaurants`

Search restaurants in a given city with optional cuisine, price, and feature filters.

## Description

> Search restaurants in a specific city. Filter by cuisine type, price range, and features like outdoor seating, WiFi, delivery. Returns up to 20 results with name, rating, cuisine, price range, address, coordinates, photo, amenities, and current Flow offers.

## Input schema

- **`city`** — `string` **(required)** — City name. Examples: 'Madrid', 'New York', 'Milano', 'Barcelona'.
- **`query`** — `string` — Free-text search: cuisine, occasion, features (e.g. 'romantic italian terrace').
- **`cuisine`** — `string` — Cuisine filter. Examples: 'italian', 'mexican', 'sushi', 'spanish', 'indian'.
- **`price_max`** — `integer` (min=1, max=4) — Max price level 1=budget, 4=fine dining.
- **`features`** — `string` — Comma-separated feature filters: terrace, wifi, parking, delivery, accessible.
- **`limit`** — `integer` (min=1, max=20, default=10)

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search_restaurants",
      "arguments": {
    "city": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
