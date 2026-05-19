#!/usr/bin/env bash
# Search restaurants in Madrid that are Italian + have outdoor seating.
# Uses the JSON-RPC tools/call interface against https://pos.do/mcp.

set -euo pipefail

curl -sS -X POST https://pos.do/mcp \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search_restaurants",
      "arguments": {
        "city": "Madrid",
        "cuisine": "italian",
        "features": "terrace",
        "limit": 5
      }
    }
  }' | jq '.result.content[0].text | fromjson | .restaurants[] | {name, cuisine_type, google_rating, address}'
