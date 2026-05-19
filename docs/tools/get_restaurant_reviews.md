# `get_restaurant_reviews`

Get paginated reviews for a restaurant, filterable by star rating and sort order.

## Description

> Get paginated reviews for a restaurant. Filter by star rating, sort by date or rating. Returns review text, author, rating, date, photos, language, owner response, and rating distribution.

## Input schema

- **`slug`** — `string` **(required)** — Restaurant URL slug.
- **`rating`** — `integer` (min=1, max=5) — Filter by exact star rating.
- **`sort`** — `string` (default="recent", enum=["recent", "rating_high", "rating_low"])
- **`limit`** — `integer` (min=1, max=30, default=10)
- **`offset`** — `integer` (min=0, default=0)

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "get_restaurant_reviews",
      "arguments": {
    "slug": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
