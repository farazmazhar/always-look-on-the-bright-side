# fastmath.pyx — Cython source.
#
# This is the "implementation" we want to ship WITHOUT exposing as Python
# source. Cython compiles it to C, then to a native .so extension. At the end
# of the pipeline only fastmath.c (C) and fastmath.*.so (binary) exist — the
# readable Python source is gone.
#
# Note the `cdef` declarations: those are C-level types, so the loops run as
# fast native code, not interpreted Python. That is the whole selling point
# of Cython besides hiding the source.

def fib(n):
    """nth Fibonacci number, computed with a fast C loop."""
    cdef int a = 0
    cdef int b = 1
    cdef int i
    for i in range(n):
        a, b = b, a + b
    return a


def sum_of_squares(n):
    """Sum 1^2 + 2^2 + ... + n^2 using a typed C loop."""
    cdef int i
    cdef long total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


PI = 3.141592653589793
