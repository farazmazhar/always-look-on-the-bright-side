use std::time::Instant;

fn sieve_of_eratosthenes(limit: usize) -> Vec<usize> {
    let mut is_prime = vec![true; limit + 1];
    is_prime[0] = false;
    is_prime[1] = false;
    let mut i = 2;
    while i * i <= limit {
        if is_prime[i] {
            let mut j = i * i;
            while j <= limit {
                is_prime[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    is_prime
        .iter()
        .enumerate()
        .filter(|(_, &p)| p)
        .map(|(i, _)| i)
        .collect()
}

fn fibonacci_recursive(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
}

fn main() {
    println!("=== Rust Benchmark (no black_box) ===");

    // Test 1: Sieve of Eratosthenes
    let start = Instant::now();
    for _ in 0..100 {
        sieve_of_eratosthenes(1_000_000);
    }
    let elapsed = start.elapsed();
    println!("Sieve of Eratosthenes (100x 1M): {:?}", elapsed);

    // Test 2: Fibonacci (recursive)
    let start = Instant::now();
    for _ in 0..5 {
        fibonacci_recursive(40);
    }
    let elapsed = start.elapsed();
    println!("Fibonacci recursive (5x 40): {:?}", elapsed);

    // Test 3: Vector operations
    let start = Instant::now();
    for _ in 0..1000 {
        let data: Vec<i32> = (0..10000).collect();
        let sum: i32 = data.iter().sum();
        let _ = sum;
    }
    let elapsed = start.elapsed();
    println!("Vector ops (1000x 10k elements): {:?}", elapsed);
}
