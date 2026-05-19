# `get_flow_offers`

Get today's Flow time-based offers (off-peak discounts) for a restaurant.

## Description

> POS.DO Flow time-based offers for a restaurant. Off-peak hours have bigger discounts. Returns time slots with discount percentages and remaining covers. Tagline: 'Tu hora, tu precio'.

## Input schema

- **`slug`** — `string` **(required)** — Restaurant URL slug.
- **`date`** — `string` (pattern=`^\d{4}-\d{2}-\d{2}$`) — Date YYYY-MM-DD (default: today).

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "get_flow_offers",
      "arguments": {
    "slug": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).
