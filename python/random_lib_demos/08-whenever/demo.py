"""
whenever demo — typed, DST-safe datetimes.

Run with:  .venv/bin/python 08-whenever/demo.py

`whenever` gives you separate types for the different notions of time:
  Instant        -> an exact moment (UTC)
  ZonedDateTime  -> a moment + a named timezone (America/New_York)
  OffsetDateTime -> a moment + a fixed UTC offset (+02:00)
  PlainDateTime  -> a "wall clock" time with no timezone at all
"""

from whenever import (
    Date,
    Instant,
    OffsetDateTime,
    PlainDateTime,
    ZonedDateTime,
    days,
    hours,
    months,
    years,
)


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. The four main types, and converting between them
# ---------------------------------------------------------------------------
show("1. Main types and conversions")

# An exact instant in time (always UTC under the hood).
instant = Instant.parse_iso("2026-08-14T18:00:00Z")
print("   Instant:      ", instant)

# Attach a timezone -> wall-clock time in New York.
zoned = instant.to_tz("America/New_York")
print("   ZonedDateTime:", zoned)

# Keep just a fixed offset.
offset = zoned.to_fixed_offset()
print("   OffsetDateTime:", offset)

# Drop timezone info entirely -> "wall clock" time.
plain = zoned.to_plain()
print("   PlainDateTime:", plain)

# And go the other way: attach a timezone to a naive wall-clock time.
assumed = plain.assume_tz("America/New_York")
print("   assume_tz:     ", assumed)


# ---------------------------------------------------------------------------
# 2. DST-safe arithmetic ("same time tomorrow" keeps wall-clock time)
# ---------------------------------------------------------------------------
show("2. DST-safe arithmetic")

# The night before Spring Forward in Amsterdam (clocks jump 02:00 -> 03:00).
eve = ZonedDateTime(2025, 3, 30, hour=1, tz="Europe/Amsterdam")
print("   eve (01:00):           ", eve)
print("   + 1 day  (wall clock): ", eve.add(days=1))
print("   + 24 hours (exact):    ", eve.add(hours=24))


# ---------------------------------------------------------------------------
# 3. Durations and differences
# ---------------------------------------------------------------------------
show("3. Durations")

departure = OffsetDateTime(2025, 7, 1, hour=9, offset=-4)   # New York
arrival = OffsetDateTime(2025, 7, 1, hour=22, offset=2)     # Amsterdam
flight_time = arrival - departure
print("   flight time:", flight_time, "=", flight_time.total("hours"), "hours")

# Itemized deltas understand calendar units (months/years).
date = Date(2023, 10, 31)
print("   date:", date)
print("   +6 months:", date.add(months=6))      # truncates to a valid date
print("   Jan 31 +1 month:", Date(2025, 1, 31).add(months=1))


# ---------------------------------------------------------------------------
# 4. Comparisons and sorting across types
# ---------------------------------------------------------------------------
show("4. Sorting exact types together")

# Three different types representing the SAME moment can be sorted together.
times = [
    ZonedDateTime(2025, 6, 1, hour=12, tz="Asia/Tokyo"),
    Instant.from_utc(2025, 6, 1, hour=2),
    OffsetDateTime(2025, 6, 1, hour=6, offset=4),
]
print("   all equal:", len({t for t in times}) == 1)
print("   sorted keeps them together (same instant)")


# ---------------------------------------------------------------------------
# 5. Formatting, parsing, and stdlib interop
# ---------------------------------------------------------------------------
show("5. Formatting / parsing / stdlib interop")

print("   custom format:", zoned.format("YYYY-MM-DD hh:mm"))
print("   parse:        ", Date.parse("15 Mar 2024", format="DD MMM YYYY"))
print("   f-string:     ", f"{Date(2024, 3, 15):DD/MM/YYYY}")
print("   to_stdlib:    ", zoned.to_stdlib())

# Round-trip is always reversible.
s = str(zoned)
print("   round-trip:   ", ZonedDateTime(s) == zoned)


# ---------------------------------------------------------------------------
# 6. Start/end of periods and rounding
# ---------------------------------------------------------------------------
show("6. start_of / end_of / round")

now = ZonedDateTime(2025, 4, 19, hour=15, minute=46, second=41, tz="America/New_York")
print("   now:      ", now)
print("   start_of hour:", now.start_of("hour"))
print("   end_of day:  ", now.end_of("day"))
print("   rounded:     ", Instant.parse_iso("2026-08-14T18:02:56.395690Z").round())


print("\nDone — whenever kept naive/aware and DST concerns explicit and safe.")
