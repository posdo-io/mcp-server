# Data Coverage

Snapshot at 2026-05-19. Live counts always served at [`/.well-known/mcp.json`](https://pos.do/.well-known/mcp.json).

## Totals

| Metric | Value |
|---|---|
| Restaurants | 356,780 |
| Reviews | 14,193,158 |
| Countries with coverage | 20 |
| Content languages | 7 |

## Countries

Ordered by restaurant count (top 20):

```
US, ES, IT, MX, FR, CO, DE, GB, DO, PR, AU, CA, PT, JP, BE, CH, HK, VE, NZ, PY
```

The full country list, including long-tail markets with smaller counts, is served by the live manifest under `data_coverage.countries`.

## Languages

Server content (descriptions, cultural context, opening hours text) is translated and indexed in:

```
ES (Spanish), EN (English), IT (Italian), FR (French), DE (German), PT (Portuguese), CA (Catalan)
```

The `Accept-Language` header on requests is honoured by the underlying REST endpoints; agents typically don't need to set it explicitly since each tool returns content in the most appropriate language for the restaurant's locale.

## Data sources and freshness

| Field family | Source | Refresh cadence |
|---|---|---|
| Name, address, coordinates, hours, phone | First-party + Outscraper + Google Maps | Continuous (varies per restaurant) |
| Photos | Google Places + first-party CDN | Continuous; expired Google photo tokens rotated |
| Reviews | Google Places + first-party UGC | Continuous; UGC posted via reservations |
| Cuisine, category | Google Places + Bing Local + curated | Periodic |
| Cultural context | Wikidata SPARQL | Cached 30 days per restaurant |
| Flow offers + availability | First-party real-time | Live (per-restaurant timezone aware) |

## Per-tool coverage hints

- **`search_restaurants`** — works in any of the 20 listed countries. Best results when `city` is a major metro (Madrid, Barcelona, Rome, NYC, Mexico City, Paris). Returns up to 20 results sorted by relevance + distance from city centroid.
- **`get_restaurant_details`** — every restaurant indexed has a slug. The slug is returned by `search_restaurants` in the `slug` field.
- **`get_restaurant_reviews`** — 93%+ of restaurants have at least one review. Average is ~40 reviews per restaurant.
- **`get_flow_offers`** / **`book_flow_reservation`** — only the subset of restaurants enrolled in Flow yield management. Currently a few thousand restaurants in ES + IT. The tool returns `offers_count: 0` for restaurants not enrolled; do not assume booking is universally available.
- **`find_restaurants_near_landmark`** — landmarks are resolved against Wikidata. Recognises monuments, museums, parks, stadiums, neighbourhoods. Returns landmark info + nearby restaurants sorted by walking distance.
- **`get_cultural_context_around_restaurant`** — returns nearby heritage sites, monuments, museums, parks with distance + heritage status (UNESCO, national, regional). Quality is best in European cities with dense Wikidata coverage.
