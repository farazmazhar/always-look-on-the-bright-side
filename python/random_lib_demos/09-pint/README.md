# pint

**pint** is a Python library for working with **physical quantities**: numbers
with units. It lets you write `3 * ureg.meter`, add it to `2 * ureg.foot`, and
convert the result to miles — with the units carried through automatically and
checked for consistency.

## Why use it?

- Avoid the Mars Climate Orbiter class of bug (mixing metric and imperial).
- Units become part of the *type*, so the library rejects nonsensical math
  like `5 meters + 3 seconds`.
- Automatic unit conversion between compatible units.
- Great for science, engineering, finance (currency), and any domain with
  units of measure.

## Key features

- `UnitRegistry` (often aliased `ureg`) — the factory for units/quantities.
- `Quantity` objects: `3.5 * ureg.kilometers`.
- `.to(other_unit)` for conversion; `.magnitude` and `.units` accessors.
- Dimensional analysis: mismatched units raise `DimensionalityError`.
- Prefix support (`kilo`, `milli`, …) and custom unit definitions.
- `~` formatting for a short, human-readable representation.
- `Contexts` for domain-specific conversions (e.g. spectroscopy, energy).
- Integration with NumPy/Pandas for arrays with units.

## Install

```bash
pip install pint
```

## Use cases

- Unit-safe physics/chemistry/engineering calculations.
- Converting measurements between metric/imperial systems.
- Validating units in scientific data pipelines.
- Currency, length, mass, time, temperature, and compound units.

## Things you can achieve

- `(60 * ureg.mile_per_hour).to(ureg.kilometer_per_hour)` — instant conversion.
- Catch `5 * ureg.meter + 3 * ureg.second` as an error at runtime.
- Define your own units (`furlong = 201.168 * meter`).
- Compute areas/volumes and reduce them to base units.

## References

- Docs: https://pint.readthedocs.io/
- PyPI: https://pypi.org/project/pint/
- GitHub: https://github.com/hgrecco/pint
