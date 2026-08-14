"""Consumer of the compiled fastmath extension — checked against fastmath.pyi."""

import fastmath

# Correct usage: mypy should be silent.
ok: int = fastmath.fib(10)

# Wrong usage: mypy flags this because the stub says fib takes an int.
bad: int = fastmath.fib("ten")

print(ok, fastmath.sum_of_squares(4), fastmath.PI)
