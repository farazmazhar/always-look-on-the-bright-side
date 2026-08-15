from functools import lru_cache


@lru_cache(maxsize=100)
def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))
