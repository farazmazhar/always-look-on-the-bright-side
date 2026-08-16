"""The most overengineered recursive Fibonacci implementation known to man.

Why? Because ``def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)``
was far too comprehensible, maintainable, and performant.

This module proves that with enough abstraction layers, decorators,
metaclasses, and design patterns, even adding two numbers can require
an entire enterprise architecture.
"""

from __future__ import annotations

import functools
import logging
import time
from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import IntEnum
from typing import Callable, Protocol, TypeVar, cast, override

logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")
_logger = logging.getLogger("FibonacciEnterprise")


# --------------------------------------------------------------------------- #
# 1. A singleton metaclass, because of course we need one.
# --------------------------------------------------------------------------- #
_InstanceT = TypeVar("_InstanceT")


class SingletonMeta(ABCMeta):
    """Metaclass ensuring a single instance per class, for thread-safety vibes."""

    _instances: dict[type, object] = {}

    @override
    def __call__(
        cls: type[_InstanceT], *args: object, **kwargs: object
    ) -> _InstanceT:
        instance = SingletonMeta._instances.get(cls)
        if instance is None:
            instance = cast(_InstanceT, super().__call__(*args, **kwargs))
            SingletonMeta._instances[cls] = instance
        return cast(_InstanceT, instance)


# --------------------------------------------------------------------------- #
# 2. An enum for the base cases, because magic numbers are a code smell.
# --------------------------------------------------------------------------- #
class BaseCase(IntEnum):
    """Enumeration of the terminal conditions of the Fibonacci recurrence."""

    ZERO = 0
    ONE = 1


# --------------------------------------------------------------------------- #
# 3. Configuration dataclass.
# --------------------------------------------------------------------------- #
@dataclass(frozen=True, slots=True)
class RecursionPolicy:
    """Immutable configuration describing how recursion should behave."""

    max_depth: int = 900
    enable_memoization: bool = True
    enable_tracing: bool = True


# --------------------------------------------------------------------------- #
# 4. The strategy interface: "one must be able to swap recursion strategies".
# --------------------------------------------------------------------------- #
class FibonacciStrategy(ABC, metaclass=SingletonMeta):
    """Abstract base class for Fibonacci computation strategies."""

    policy: RecursionPolicy = RecursionPolicy()

    @abstractmethod
    def compute(self, n: int) -> int:
        """Compute the n-th Fibonacci number."""


# --------------------------------------------------------------------------- #
# 5. Decorators: tracing, timing, validation, memoization. All of them.
# --------------------------------------------------------------------------- #
class _RecursiveState(Protocol):
    """Structural contract the decorators demand of their `self`."""

    policy: RecursionPolicy
    memo: dict[int, int]


_S = TypeVar("_S", bound=_RecursiveState)


def validate_input(
    func: Callable[[_S, int, int], int],
) -> Callable[[_S, int, int], int]:
    """Reject negative and absurd inputs before any recursion happens."""

    @functools.wraps(func)
    def wrapper(self: _S, n: int, _depth: int) -> int:
        if n < 0:
            raise ValueError(f"Fibonacci is undefined for negative n (got {n})")
        if n > self.policy.max_depth:
            raise RecursionError(
                f"n={n} exceeds policy max_depth={self.policy.max_depth}"
            )
        return func(self, n, _depth)

    return wrapper


def trace_recursion(
    func: Callable[[_S, int, int], int],
) -> Callable[[_S, int, int], int]:
    """Log every recursive call, complete with indentation for depth."""

    @functools.wraps(func)
    def wrapper(self: _S, n: int, _depth: int) -> int:
        if self.policy.enable_tracing:
            _logger.info("%scomputing fib(%d)", "  " * _depth, n)
        result = func(self, n, _depth)
        if self.policy.enable_tracing:
            _logger.info("%s=> fib(%d) = %d", "  " * _depth, n, result)
        return result

    return wrapper


def timed(func: Callable[[_S, int, int], int]) -> Callable[[_S, int, int], int]:
    """Measure how long we can make two additions take."""

    @functools.wraps(func)
    def wrapper(self: _S, n: int, _depth: int) -> int:
        start = time.perf_counter()
        result = func(self, n, _depth)
        elapsed = time.perf_counter() - start
        if _depth == 0:
            _logger.info("Total compute time: %.6fs", elapsed)
        return result

    return wrapper


def memoized(func: Callable[[_S, int, int], int]) -> Callable[[_S, int, int], int]:
    """Cache results keyed by n, but only if the policy permits it."""

    @functools.wraps(func)
    def wrapper(self: _S, n: int, _depth: int) -> int:
        if not self.policy.enable_memoization:
            return func(self, n, _depth)
        if n in self.memo:
            if self.policy.enable_tracing:
                _logger.info("%s(cache hit for %d)", "  " * _depth, n)
            return self.memo[n]
        self.memo[n] = func(self, n, _depth)
        return self.memo[n]

    return wrapper


# --------------------------------------------------------------------------- #
# 6. The concrete strategy: pure recursion, garnished with everything.
# --------------------------------------------------------------------------- #
class RecursiveFibonacci(FibonacciStrategy):
    """A recursively-defined Fibonacci computation, exquisitely decorated."""

    policy: RecursionPolicy
    memo: dict[int, int]

    def __init__(self, policy: RecursionPolicy | None = None) -> None:
        self.policy = policy if policy is not None else RecursionPolicy()
        self.memo = {}

    @override
    def compute(self, n: int) -> int:
        """Return the n-th Fibonacci number via (you guessed it) recursion."""
        return self._recurse(n, 0)

    @validate_input
    @memoized
    @trace_recursion
    @timed
    def _recurse(self, n: int, _depth: int) -> int:
        if n == BaseCase.ZERO:
            return 0
        if n == BaseCase.ONE:
            return 1
        return self._recurse(n - 1, _depth + 1) + self._recurse(n - 2, _depth + 1)


# --------------------------------------------------------------------------- #
# 7. A service locator / facade, so callers never touch the strategy directly.
# --------------------------------------------------------------------------- #
class FibonacciService:
    """Facade exposing the Fibonacci computation to the outside world."""

    _strategy: FibonacciStrategy

    def __init__(self, strategy: FibonacciStrategy | None = None) -> None:
        self._strategy = strategy if strategy is not None else RecursiveFibonacci()

    def nth(self, n: int) -> int:
        """Return the n-th number in the Fibonacci sequence."""
        return self._strategy.compute(n)


# --------------------------------------------------------------------------- #
# 8. The actual public API, hidden behind one more indirection.
# --------------------------------------------------------------------------- #
_service = FibonacciService()


def fibonacci(n: int) -> int:
    """Return the corresponding number in the Fibonacci sequence.

    Args:
        n: Zero-based index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.
    """
    return _service.nth(n)


if __name__ == "__main__":
    for i in range(10, 1, -1):
        print(f"fib({i}) = {fibonacci(i)}")
