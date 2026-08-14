"""
graphlib demo — topological sorting of directed graphs (stdlib, Python 3.9+).

Run with:  .venv/bin/python 16-graphlib/demo.py

Topological order = order every node after its dependencies. graphlib also
detects cycles for us, which is the real payoff.
"""

from graphlib import CycleError, TopologicalSorter


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. static_order() — the simple one-shot topological sort
# ---------------------------------------------------------------------------
show("1. static_order() for a build pipeline")

# In this tiny build system, each node lists the things it DEPENDS on.
# A library needs its base modules; the app needs the library + the logger.
ts = TopologicalSorter()
ts.add("app", "lib", "logger")
ts.add("lib", "math_utils", "io_utils")
ts.add("logger", "io_utils")
ts.add("math_utils")
ts.add("io_utils")

print("   ", " -> ".join(ts.static_order()))


# ---------------------------------------------------------------------------
# 2. The incremental API: get_ready() / is_active() / done()
# ---------------------------------------------------------------------------
show("2. Incremental API — process 'ready' nodes as they free up")

ts2 = TopologicalSorter()
ts2.add("app", "lib", "logger")
ts2.add("lib", "base_a", "base_b")
ts2.add("logger", "base_a")
ts2.add("base_a")
ts2.add("base_b")

ts2.prepare()
print(f"   first ready batch: {ts2.get_ready()}")  # nodes with no dependencies

# We can "run" them (here just simulate finishing) then tell the sorter they're
# done so the next batch becomes ready.
ts2.done("base_a")
print(f"   after base_a done, ready: {ts2.get_ready()}")

ts2.done("base_b")
print(f"   after base_b done, ready: {ts2.get_ready()}")

ts2.done("logger")
ts2.done("lib")
print(f"   still active? {ts2.is_active()} (False when everything is done)")


# ---------------------------------------------------------------------------
# 3. Cycle detection — the killer feature
# ---------------------------------------------------------------------------
show("3. CycleError is raised for circular dependencies")

cyclic = TopologicalSorter()
cyclic.add("a", "b")  # a depends on b
cyclic.add("b", "c")  # b depends on c
cyclic.add("c", "a")  # c depends on a  -> cycle a <-> c (and b)

try:
    list(cyclic.static_order())
except CycleError as exc:
    print(f"   CycleError caught: {exc}")


# ---------------------------------------------------------------------------
# 4. TopologicalSorter from a graph dict
# ---------------------------------------------------------------------------
show("4. Passing a graph dict to TopologicalSorter(graph)")

# You can hand the sorter a dict of {node: {predecessors}} all at once instead
# of calling add() repeatedly. Note the order is deterministic but depends on
# insertion order, so we sort for a clean display.
graph = {
    "D": {"B", "C"},
    "C": {"A"},
    "B": {"A"},
    "A": set(),
}
ts4 = TopologicalSorter(graph)
print("   ", " -> ".join(ts4.static_order()))


print("\nDone — dependencies were ordered and a cycle was detected.")
