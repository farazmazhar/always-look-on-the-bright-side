"""
geopy demo — geocoding & geodesic distance.

Run with:  .venv/bin/python 10-geopy/demo.py

The distance/Point parts work offline. The geocoder part needs internet, so it
is wrapped in try/except and skipped gracefully when you are offline.
"""

from geopy import distance as geo_distance
from geopy.distance import geodesic, great_circle
from geopy.point import Point


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. Parsing coordinates with Point
# ---------------------------------------------------------------------------
show("1. Point: parse many coordinate formats")

for raw in ["41.49008, -71.312796", (48.8584, 2.2945), "40.7128° N, 74.0060° W"]:
    p = Point(raw)
    print(f"   {raw!r:40} -> lat={p.latitude}, lon={p.longitude}")


# ---------------------------------------------------------------------------
# 2. Geodesic distance between two points
# ---------------------------------------------------------------------------
show("2. Distance between two places")

newport = Point("41.49008, -71.312796")     # Newport, RI
new_york = Point("40.7128, -74.0060")       # New York, NY

# `distance` is the geodesic (ellipsoidal) distance by default.
d = geo_distance.distance(newport, new_york)
print(f"   Newport -> New York: {d.km:.2f} km  /  {d.miles:.2f} miles")

# geodesic (accurate) vs great_circle (simpler sphere) can differ slightly.
print(f"   geodesic:    {geodesic(newport, new_york).km:.3f} km")
print(f"   great_circle:{great_circle(newport, new_york).km:.3f} km")


# ---------------------------------------------------------------------------
# 3. Destination: project a point by bearing + distance
# ---------------------------------------------------------------------------
show("3. Destination point (projection)")

start = Point("41.49008, -71.312796")
# 100 km due east (bearing 90°) — useful for bounding boxes / geo-fences.
dest = geo_distance.distance(kilometers=100).destination(start, bearing=90)
print(f"   start: {start.format()}")
print(f"   100 km east -> {dest.format()}")


# ---------------------------------------------------------------------------
# 4. Building a distance object from a unit
# ---------------------------------------------------------------------------
show("4. Distance arithmetic")

a = geo_distance.distance(kilometers=5)
b = geo_distance.distance(miles=3)
print(f"   5 km + 3 miles = {(a + b).km:.2f} km")
print(f"   5 km in nautical miles = {a.nautical:.2f}")


# ---------------------------------------------------------------------------
# 5. Geocoding (address <-> coordinates) — needs internet
# ---------------------------------------------------------------------------
show("5. Geocoding with Nominatim (OpenStreetMap)")

try:
    from geopy.geocoders import Nominatim

    # A User-Agent string is required by the Nominatim usage policy.
    geolocator = Nominatim(user_agent="random_lib_demos")

    # Forward geocode: address -> coordinates.
    location = geolocator.geocode("Eiffel Tower, Paris")
    print("   forward geocode 'Eiffel Tower':", location.address)
    print("      ->", (location.latitude, location.longitude))

    # Reverse geocode: coordinates -> address.
    rev = geolocator.reverse("48.8584, 2.2945")
    print("   reverse geocode (48.8584, 2.2945):", rev.address)

except Exception as exc:  # no network, rate-limited, etc.
    print(f"   skipped (needs internet): {type(exc).__name__}")


print("\nDone — coordinates stayed typed and the math stayed on the ellipsoid.")
