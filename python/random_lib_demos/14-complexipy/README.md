# complexipy

**complexipy** measures the **cognitive complexity** of Python code. Unlike
cyclomatic complexity (which counts decision points), cognitive complexity
models *how hard code is for a human to understand* — penalizing deep nesting,
flow breaks, and hard-to-follow logic. It is written in Rust for speed.

## Why use it?

- Cyclomatic complexity counts branches but ignores *nesting*, which is what
  actually hurts readability. Cognitive complexity captures both.
- Catch "clever" but unmaintainable code during review/CI.
- Get actionable, per-function and per-line reports to target refactoring.
- It is extremely fast (Rust core), so you can run it on large codebases.

## Key features

- `code_complexity(source)` — analyze a string of code.
- `file_complexity(path)` — analyze a file.
- Per-function complexity, line ranges, and **per-line complexity**.
- A `check_script=True` flag to include module-level (script) complexity.
- Optional `refactor_plans` / thresholds for suggested fixes.
- A CLI: `complexipy <path> --max-complexity-allowed 10`.
- Honors ignore comments (can be disabled with `no_ignore=True`).

## Install

```bash
pip install complexipy
```

## Use cases

- CI quality gates: fail builds when a function gets too complex.
- Code review: point reviewers at the exact lines causing complexity.
- Refactoring: identify the top-N most complex functions in a project.
- Education: teach what "readable code" means with concrete numbers.

## Things you can achieve

- A complexity score for a whole file plus a breakdown per function.
- See exactly which nested line adds the most complexity.
- A threshold (default 15) that flags functions needing attention.

## References

- Docs: https://rohaquinlop.github.io/complexipy/
- PyPI: https://pypi.org/project/complexipy/
- GitHub: https://github.com/rohaquinlop/complexipy
- Background: SonarSource "Cognitive Complexity" by G. Ann Campbell
