# geopy

**geopy** is a Python client for geocoding and geographical math. It gives you:

- **Geocoders** — turn addresses into coordinates (and back) via services like
  Nominatim (OpenStreetMap), Google, Bing, etc.
- **Distance** — geodesic and great-circle distance between coordinates, plus
  destination points given a start point, bearing, and distance.

## Why use it?

- One consistent API in front of many different geocoding providers.
- Accurate geodesic math (WGS-84 ellipsoid) — not the flat-earth approximation
  you get from naive haversine code.
- `Point` parsing handles the many coordinate formats people actually use
  (`"41.5, -71.3"`, `(lat, lon)`, DMS strings, …).

## Key features

- `geopy.geocoders.Nominatim` (free, OpenStreetMap) and many others.
- `geocode(address)` / `reverse(lat, lon)` to convert both directions.
- `geopy.distance.distance` (geodesic), `great_circle`, `geodesic`.
- `.km`, `.miles`, `.meters`, `.nautical` on distance objects.
- `distance(...).destination(point, bearing)` to project a point.
- `geopy.point.Point` for parsing/formatting coordinates.
- `geopy.Location` bundles a point + address + raw provider response.

## Install

```bash
pip install geopy
```

## Use cases

- "Find me coffee shops near this address" (geocode → radius search).
- Distance between two cities / delivery cost estimation.
- Reverse geocoding GPS traces into street names.
- Geo-fencing and "nearest X" calculations.

## Things you can achieve

- Distance from New York to London in km/miles.
- Find the point 100 km due east of a coordinate (great for bounding boxes).
- Geocode "Eiffel Tower" to (48.8584, 2.2945) — *requires network access*.

## References

- Docs: https://geopy.readthedocs.io/
- PyPI: https://pypi.org/project/geopy/
- GitHub: https://github.com/geopy/geopy
