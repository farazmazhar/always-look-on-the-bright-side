"""
pint demo — physical quantities and unit conversion.

Run with:  .venv/bin/python 09-pint/demo.py

pint attaches units to numbers so math stays dimensionally correct: you can
add meters to feet (auto-converted) but never meters to seconds.
"""

import pint

# The UnitRegistry is where all units live. `ureg` is the conventional alias.
# Units are accessed as attributes: ureg.meter, ureg.second, ...
ureg = pint.UnitRegistry()

# Use the short "~" format by default, e.g. "kg·m/s²" instead of the long
# "kilogram * meter / second ** 2" representation.
ureg.default_format = "~"


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. Creating quantities
# ---------------------------------------------------------------------------
show("1. Creating quantities")

length = 5 * ureg.meter
duration = 3.5 * ureg.second
speed = 60 * ureg.mile_per_hour

print("   length:  ", length)
print("   duration:", duration)
print("   speed:   ", speed)

# A quantity has a magnitude (the number) and units (the dimension).
print("   magnitude:", length.magnitude, "| units:", length.units)


# ---------------------------------------------------------------------------
# 2. Conversion
# ---------------------------------------------------------------------------
show("2. Conversion")

print("   5 m in feet:   ", length.to(ureg.feet))
print("   60 mph in km/h: ", speed.to(ureg.kilometer_per_hour))
print("   3.5 s in ms:   ", duration.to(ureg.millisecond))


# ---------------------------------------------------------------------------
# 3. Dimensional analysis — compatible units combine automatically
# ---------------------------------------------------------------------------
show("3. Dimensional analysis")

# Adding compatible units auto-converts, then reports the result.
total = 5 * ureg.meter + 2 * ureg.foot
print("   5 m + 2 ft =", total)

# Multiplying/dividing builds compound units.
area = 3 * ureg.meter * 4 * ureg.meter
print("   3 m * 4 m =", area, "->", area.to(ureg.square_feet))

# Incompatible units raise DimensionalityError instead of silently misbehaving.
try:
    bad = 5 * ureg.meter + 3 * ureg.second
except pint.errors.DimensionalityError as exc:
    print("   blocked: 5 m + 3 s ->", type(exc).__name__)


# ---------------------------------------------------------------------------
# 4. Prefixes and temperature (an offset unit)
# ---------------------------------------------------------------------------
show("4. Prefixes and temperature")

print("   1 kilometer in meters:", (1 * ureg.kilometer).to(ureg.meter))
print("   250 mg in grams:     ", (250 * ureg.milligram).to(ureg.gram))

# Temperature is special (has an offset), so use the dedicated conversion.
temp = 100 * ureg.degC
print("   100 °C in °F:", temp.to(ureg.degF))
print("   100 °C in K: ", temp.to(ureg.kelvin))


# ---------------------------------------------------------------------------
# 5. Defining custom units
# ---------------------------------------------------------------------------
show("5. Custom units")

# Define a unit that pint doesn't ship with by default.
ureg.define("furlong = 201.168 * meter = fur")
distance = 10 * ureg.furlong
print("   10 furlongs in meters:", distance.to(ureg.meter))


# ---------------------------------------------------------------------------
# 6. Formatting for humans
# ---------------------------------------------------------------------------
show("6. Formatting")

q = (1 * ureg.kilogram * ureg.meter / ureg.second**2).to(ureg.newton)
print("   1 kg·m/s² =", q)
print("   formatted with ~:", format(q, "~"))
print("   f-string .2f~:", f"{q:.2f~}")

print("\nDone — units stayed attached to every number above.")
