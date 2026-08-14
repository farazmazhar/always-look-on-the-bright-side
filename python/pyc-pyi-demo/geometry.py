"""A tiny geometry module with NO type annotations on purpose.

The whole point: real-world libraries are often compiled (C extensions) or
untyped. The type information lives only in the sibling geometry.pyi stub,
and that stub is what tools like mypy actually read.
"""


def area_of_square(side):
    return side * side


def perimeter_of_rectangle(length, width):
    return 2 * (length + width)


PI = 3.141592653589793
