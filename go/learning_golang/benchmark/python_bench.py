import time


def sieve_of_eratosthenes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start : limit + 1 : step] = [False] * ((limit - start) // step + 1)
    return [i for i, prime in enumerate(is_prime) if prime]


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    print("=== Python Benchmark ===")

    # Test 1: Sieve of Eratosthenes
    start = time.perf_counter()
    for _ in range(100):
        sieve_of_eratosthenes(1_000_000)
    elapsed = time.perf_counter() - start
    print(f"Sieve of Eratosthenes (100x 1M): {elapsed:.4f}s")

    # Test 2: Fibonacci (recursive)
    start = time.perf_counter()
    for _ in range(5):
        fibonacci_recursive(40)
    elapsed = time.perf_counter() - start
    print(f"Fibonacci recursive (5x 40): {elapsed:.4f}s")

    # Test 3: List operations
    start = time.perf_counter()
    for _ in range(1000):
        data = list(range(10000))
        total = sum(data)
        _ = total
    elapsed = time.perf_counter() - start
    print(f"List ops (1000x 10k elements): {elapsed:.4f}s")


if __name__ == "__main__":
    main()
