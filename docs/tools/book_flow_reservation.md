# `book_flow_reservation`

Make a reservation at a Flow-discounted time slot, with idempotent retry semantics.

## Description

> Make a reservation at a Flow-discounted time slot. Phone must be E.164 (e.g. +34911234567). To make retries safe, send the same Idempotency-Key HTTP header on retries (any UUID); replays within 24h return the original reservation. Rate limited to 5 reservations per email per day and 10 attempts per IP per minute.

## Input schema

- **`slug`** — `string` **(required)** — Restaurant URL slug.
- **`yield_offer_id`** — `integer` **(required)** — Offer ID returned by get_flow_offers.
- **`guest_name`** — `string` **(required)**
- **`guest_email`** — `string` **(required)**
- **`guest_phone`** — `string` **(required)** (pattern=`^\+[1-9]\d{7,14}$`) — E.164 format, e.g. +34911234567.
- **`party_size`** — `integer` (min=1, max=20, default=2)
- **`notes`** — `string`

## JSON-RPC call shape

```bash
curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "book_flow_reservation",
      "arguments": {
    "slug": "...",
    "yield_offer_id": "...",
    "guest_name": "...",
    "guest_email": "...",
    "guest_phone": "..."
}
    }
  }'
```

## Rate limits

Inherits server limits (anonymous tier: 60 req/min, 10K req/day per IP).

Additional reservation limits: 10 attempts/min per IP, 5 per email per 24 h. Send `Idempotency-Key` header for safe retries.
