package main

import (
	"fmt"
	"time"
)

func sieveOfEratosthenes(limit int) []int {
	isPrime := make([]bool, limit+1)
	for i := 2; i <= limit; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= limit; i++ {
		if isPrime[i] {
			for j := i * i; j <= limit; j += i {
				isPrime[j] = false
			}
		}
	}
	var primes []int
	for i := 2; i <= limit; i++ {
		if isPrime[i] {
			primes = append(primes, i)
		}
	}
	return primes
}

func fibonacciRecursive(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
}

func main() {
	fmt.Println("=== Go Benchmark ===")

	// Test 1: Sieve of Eratosthenes
	start := time.Now()
	for range 100 {
		sieveOfEratosthenes(1_000_000)
	}
	elapsed := time.Since(start)
	fmt.Printf("Sieve of Eratosthenes (100x 1M): %v\n", elapsed)

	// Test 2: Fibonacci (recursive)
	start = time.Now()
	for range 5 {
		fibonacciRecursive(40)
	}
	elapsed = time.Since(start)
	fmt.Printf("Fibonacci recursive (5x 40): %v\n", elapsed)

	// Test 3: Slice operations
	start = time.Now()
	for range 1000 {
		data := make([]int, 0, 10000)
		for i := range 10000 {
			data = append(data, i)
		}
		sum := 0
		for _, v := range data {
			sum += v
		}
		_ = sum
	}
	elapsed = time.Since(start)
	fmt.Printf("Slice ops (1000x 10k elements): %v\n", elapsed)
}
