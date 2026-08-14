# whenever

**whenever** is a modern datetime library for Python. It gives you *typed,
DST-safe* datetime handling with separate types for different notions of time,
fixing the classic pitfalls of the standard library's `datetime`.

## Why use it?

Python's `datetime` has well-known traps: arithmetic that silently ignores DST,
no distinction between naive and aware datetimes, equality edge cases, and a
single type trying to mean everything. `whenever` (and older libs like arrow /
pendulum) don't fully fix these. `whenever` does:

- **DST-safe arithmetic** — "same time tomorrow" means *wall clock* time.
- **Typesafe** — you cannot accidentally mix naive and aware datetimes.
- **Fast** — a Rust extension (with a pure-Python fallback), ~2-4× faster than
  the stdlib and 10-100× faster than arrow/pendulum.

## Key features

- Distinct types: `Instant`, `ZonedDateTime`, `OffsetDateTime`, `PlainDateTime`.
- Partial types: `Date`, `Time`, `YearMonth`, `MonthDay`, `IsoWeekDate`.
- Delta types: `TimeDelta` (exact) and `ItemizedDelta` (months/years-aware).
- DST-aware arithmetic and explicit handling of ambiguous/skipped times.
- Nanosecond precision, unix timestamps, ISO 8601 parsing/formatting.
- Custom format patterns and stdlib interop (`to_stdlib`, `py_datetime`).
- Comparison/sorting across the "exact" types.
- `patch_current_time` for testing.

## Install

```bash
pip install whenever
```

## Use cases

- Scheduling/booking systems that must be correct across DST boundaries.
- APIs that exchange ISO 8601 timestamps (in UTC or with offsets).
- Calculating durations, ages, countdowns, and flight/transit times.
- Storing and sorting event times from many time zones.

## Things you can achieve

- `Instant.now().to_tz("America/New_York")` — convert UTC to any zone.
- `date.add(months=6)` — sane month arithmetic (Jan 31 → Jul 31).
- `arrival - departure` across time zones gives a correct `TimeDelta`.
- Explicit choice (`disambiguate=`) when a local time occurs twice.
- Round-trip `str(d) -> type(d)(s)` that is always reversible.

## References

- Docs: https://whenever.readthedocs.io/
- PyPI: https://pypi.org/project/whenever/
- GitHub: https://github.com/ariebovenberg/whenever
