# graphlib

**graphlib** (Python 3.9+) provides **topological sorting** for directed
graphs. Its star feature, `TopologicalSorter`, orders nodes so that every
dependency comes before the things that depend on it — and it detects
circular dependencies (cycles), which would otherwise be an infinite loop or a
silent bug.

## Why use it?

- Hand-rolling topological sorts is easy to get subtly wrong; this is the
  standard-library, tested implementation.
- Built-in **cycle detection** — you get a clear `CycleError` naming the
  offending nodes instead of infinite recursion or a hung process.
- Simple API — pass a `dict` of node → predecessors, or call `add()` repeatedly.
- Efficient — uses Kahn's algorithm with an internal ready-queue.

## Key features

- `TopologicalSorter(graph=None)` — sort a graph of hashable nodes.
- `.add(node, *predecessors)` — declare that a node depends on the others.
- `.prepare()` then `.get_ready()` / `.is_active()` — the **incremental**
  / streaming API, great for parallel scheduling of ready nodes.
- `.static_order()` — the simple one-shot ordering.
- `CycleError` — raised when the graph has a cycle (includes the cycle path).

## Install

`graphlib` is part of the Python **standard library** (3.9+) — no installation
needed. A backport exists on PyPI as `graphlib-backport` for older versions.

## Use cases

- Build systems: compile packages/tasks in the correct order.
- Dependency resolution: pip/npm-style "install prerequisites first".
- Database schema migration ordering.
- Spreadsheet / formula recalculation order.
- Task schedulers that want to run all "ready" (dependency-free) tasks in parallel.

## Things you can achieve

- Topologically sort a build pipeline so every dependency builds first.
- Run ready tasks concurrently with the incremental `get_ready()` API.
- Catch a circular dependency and see exactly which nodes are in the cycle.
- Feed an entire graph at once as a `dict` of node → predecessors.

## References

- Docs: https://docs.python.org/3/library/graphlib.html
