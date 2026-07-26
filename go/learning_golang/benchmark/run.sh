#!/usr/bin/env bash
set -euo pipefail

echo "=========================================="
echo "  Go vs Python vs Rust Benchmark"
echo "=========================================="
echo ""

# Build Go binary
echo "[1/4] Building Go benchmark..."
go build -o /tmp/go_bench go_bench.go

# Build Rust binary
echo "[2/4] Building Rust benchmark..."
cargo build --release --manifest-path rust_bench/Cargo.toml 2>&1

# Run Go benchmark
echo "[3/4] Running Go benchmark..."
echo ""
/tmp/go_bench 2>&1
echo ""

# Run Rust benchmark
echo ""
echo "---"
rust_bench/target/release/rust_bench 2>&1
echo ""

# Run Python benchmark
echo "[4/4] Running Python benchmark..."
python3 python_bench.py 2>&1
echo ""

echo "=========================================="
echo "  Done!"
echo "=========================================="
