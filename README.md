<p align="center">
  <img src="https://img.shields.io/badge/Quack_quack...-F7D794?style=for-the-badge&logo=duckduckgo&logoColor=222" alt="Quack quack"/>
</p>

<h1 align="center">Always Look on the Bright Side</h1>

<p align="center">
  My personal playground of learning — everything I explore, tests, notes, and tiny experiments,
  kept in one place so I can find them quickly and reuse them anywhere, anytime.
</p>

<p align="center">
  <a href="#-whats-inside"><b>What's Inside</b></a> ·
  <a href="#-quick-start"><b>Quick Start</b></a> ·
  <a href="#-structuring-principles"><b>Structuring Principles</b></a> ·
  <a href="#-conventions"><b>Conventions</b></a>
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust"/>
  <img src="https://img.shields.io/badge/HTML-1572B6?style=for-the-badge&logo=html5&logoColor=white" alt="HTML"/>
  <img src="https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css3&logoColor=white" alt="CSS"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=212121" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/>
  <img src="https://img.shields.io/badge/OpenAI-black?style=for-the-badge&logo=openai&logoColor=41CC8A" alt="AI"/>
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON"/>
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/farazmazhar/always-look-on-the-bright-side" alt="License"/>
  <img src="https://img.shields.io/github/last-commit/farazmazhar/always-look-on-the-bright-side" alt="Last commit"/>
  <img src="https://img.shields.io/github/stars/farazmazhar/always-look-on-the-bright-side" alt="Stars"/>
  <img src="https://img.shields.io/github/repo-size/farazmazhar/always-look-on-the-bright-side" alt="Repo size"/>
</p>

---

## 🤔 What is this?

This repo is my **digital learning garden**. Instead of scattered notes and throwaway repos
living in five different places, everything lands here: study notes, language coursework,
mini-projects, demos of random libraries, and interactive prototypes.

The goal is simple — **learn things, keep them in one place, and be able to reach back for
them whenever and wherever I need to.**

> Every leaf project is **self-contained**. There's no shared build system and no centralized
> package management. Each folder manages its own dependencies and can be opened or run in
> isolation.

<br>

## 🗺️ What's Inside

An overview of the main areas. Anything nested deeper is described in its own sub-README.

### 🐹 Go — `go/learning_golang/`
My journey from first Go file to real projects.

| Area | Description |
|------|-------------|
| `coursework/` | 23 numbered lessons covering syntax, functions, slices, pointers, structs, interfaces, file I/O, and more |
| `projects/` | Standalone projects built while learning (currently `bill_generator_api`) |
| `benchmark/` | Cross-language performance benchmarks — **Go vs Python vs Rust** |

### 🐍 Python — `python/`
Notebooks, experiments, and demos of libraries I'm exploring.

| Folder | Description |
|--------|-------------|
| `random_lib_demos/` | 19 demos of random Python libraries (pydantic, FastAPI streaming, Django, DRF, dishka, nicegui, faker, graphlib, and more) |
| `enhancing-maingate-ipcam-with-opencv/` | OpenCV + `face_recognition` running against an IP camera (Jupyter notebook) |
| `prettymaps-demo/` | Experimenting with the `prettymaps` mapping library (Jupyter notebook) |
| `cython-demo/` | Cython experiment |
| `heapq-demos/` | Working through the `heapq` stdlib module |
| `pyc-pyi-demo/` | Playing with `.pyc` / `.pyi` artifacts |

### ☁️ Azure — `azure/AZ-900/`
Complete **Microsoft Azure Fundamentals (AZ-900)** study notes as numbered markdown files —
cloud concepts, architecture, compute, networking, storage, identity & security, management &
governance — plus a cheatsheet and a master index.

### 🤖 AI — `ai/`
Course notes from Udemy & other platforms, organized by course:

- **AI A-Z [2026]** — prompt engineering, generative AI foundations, and more
- **LangChain — Agentic AI Engineering** — building agentic systems with LangChain

Each course uses a consistent note structure (`COURSEDETAILS.md`, `sNN-` sections,
`lecture-NN-` notes) so I can jump straight to any lecture.

### 🧪 Agent Coding Testing — `coding-agent-testing/`
A sandbox for testing coding agents (command-code, opencode) — mockup creation, throwaway
scripts, and experiments like a Fibonacci demo.

### 🧑‍💻 Zed — `zed/`
Zed editor experiments, like an inline prediction test and Ollama integration.

<br>

## 🚀 Quick Start

Since this is a **collection of self-contained projects**, there's no single install or build
step. Instead, treat each folder as its own mini-project:

```bash
# Explore the structure
du -sh */ && ls

# Go projects carry their own module
cd go/learning_golang/projects/bill_generator_api
go mod tidy
go run .

# Reproduce a Python benchmark
cd go/learning_golang/benchmark
./run.sh

# Open a course or Azure notes in any markdown viewer
code azure/AZ-900/az-900-01-cloud-concepts.md

# Serve an interactive mockup
python3 -m http.server 8000 --directory coding-agent-testing/commandcode/mockup-creation-testing
# -> http://localhost:8000
```

<br>

## 🧱 Structuring Principles

- **Language/platform first** — top-level folders are by technology (`go/`, `python/`, `azure/`).
- **Each leaf is self-contained** — its own deps, its own `.go.mod` / `.venv` / `package.json`.
- **Linear when it makes sense** — coursework folders follow `N_TopicName` for a clear progression.
- **Self-documenting** — `COURSEDETAILS.md`, per-section `README.md`, and the `AGENTS.md`
  describe every corner so future-me never has to reverse-engineer anything.

<br>

## 📜 Conventions

| Rule | Convention |
|------|-----------|
| **Build orchestration** | None — no shared monorepo tooling |
| **Dependencies** | Managed per-folder |
| **Go modules** | `go.mod` / `go.sum` per project |
| **Python demos** | Standalone notebooks, scripts, or `.venv` |
| **Course notes** | `COURSEDETAILS.md` + `sNN-topic/` sections + `lecture-NN-name.md` files |

<br>

## 💭 Keeping it fresh

The only hard rule: **new learning lands here, not in yet another throwaway repo.**
When I pick up a new language, library, or certification, it gets a folder, a little structure,
and a note — then it's always one `git clone` away.

---

<p align="center">
  <sub>Made to learn, one bright side at a time. 🦆</sub>
</p>