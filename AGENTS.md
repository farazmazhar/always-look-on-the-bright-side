# Repo Overview

Personal learning repo organized by language/platform. No shared build system — each leaf project/directory is self-contained.

## Structure

- **`go/learning_golang/`** — Go language learning
  - `benchmark/` — cross-language benchmarks (Go vs Python vs Rust)
  - `coursework/` — numbered lesson folders (1_IntroductionAndSetup, 2_YourFirstGoFile, …)
  - `projects/` — standalone Go projects (currently `bill_generator_api`)

- **`azure/`** — Azure cloud learning
  - `AZ-900/` — Microsoft Azure Fundamentals (AZ-900) study notes, organized as numbered markdown files covering cloud concepts, architecture, compute, networking, storage, identity/security, management/governance, plus a cheatsheet and index

- **`python/`** — Python learning & experiments
  - `enhancing-maingate-ipcam-with-opencv/` — Jupyter notebook for OpenCV + face_recognition on IP camera
  - `prettymaps-demo/` — Jupyter notebook for prettymaps experimentation

## Conventions

- No centralized package manager or build orchestration
- Each project/subfolder manages its own dependencies
- Go projects use `go.mod` / `go.sum`
- Python projects are standalone Jupyter notebooks or scripts
- Coursework folders follow `N_TopicName` naming for linear progression
