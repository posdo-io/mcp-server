# `get_cultural_context_around_restaurant`

Get cultural context (monuments, museums, parks, heritage sites) around a restaurant.

## Description

> Get cultural context around a restaurant: nearby monuments, museums, parks, historical sites with distance and heritage status. Powered by Wikidata.

## Input schema

- **`slug`** — `string` **(required)** — Restaurant URL slug.

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "get_cultural_context_around_restaurant",
      "arguments": {
    "slug": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
