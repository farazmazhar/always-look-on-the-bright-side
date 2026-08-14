"""Consumer of the geometry module — type-checked against geometry.pyi."""

import geometry

# Correct usage: mypy should be silent.
ok: float = geometry.area_of_square(4.0)

# Wrong usage: mypy flags this BECAUSE the stub says side is a float.
bad: float = geometry.area_of_square("four")

print(ok, bad, geometry.PI)
