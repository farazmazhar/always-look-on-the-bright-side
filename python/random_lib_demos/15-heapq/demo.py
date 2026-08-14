"""
heapq demo — a heap / priority queue from the standard library.

Run with:  .venv/bin/python 15-heapq/demo.py

A heap is a list that is kept "heap-ordered": the smallest item sits at index 0,
and push/pop both cost O(log n). This is the workhorse behind priority queues,
task schedulers, and Dijkstra's algorithm.
"""

import heapq


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. heappush / heappop — the core priority-queue operations
# ---------------------------------------------------------------------------
show("1. Push & pop (a min-heap, so the SMALLEST comes out first)")

heap: list[int] = []
for value in [5, 1, 9, 3, 7]:
    heapq.heappush(heap, value)

print(f"   heap after pushes: {heap}   (smallest is at index 0)")
order = []
while heap:
    order.append(heapq.heappop(heap))
print(f"   pop order: {order}  -> sorted ascending")


# ---------------------------------------------------------------------------
# 2. Storing (priority, item) tuples — a true priority queue
# ---------------------------------------------------------------------------
show("2. Priority queue with (priority, item) tuples")

tasks = []
# Lower number = higher priority.
heapq.heappush(tasks, (1, "write docs"))
heapq.heappush(tasks, (3, "water plants"))
heapq.heappush(tasks, (2, "fix bug"))

while tasks:
    priority, name = heapq.heappop(tasks)
    print(f"   priority {priority}: {name}")


# ---------------------------------------------------------------------------
# 3. heapify — turn an existing list into a heap in place
# ---------------------------------------------------------------------------
show("3. heapify() an existing list (in place, O(n))")

data = [9, 3, 7, 1, 5]
print(f"   before: {data}")
heapq.heapify(data)
print(f"   after : {data}  (index 0 is now the minimum)")
print(f"   heappop -> {heapq.heappop(data)}")


# ---------------------------------------------------------------------------
# 4. Max-heap by negating values
# ---------------------------------------------------------------------------
show("4. Max-heap: store negated values")

scores = [42, 7, 99, 18, 55]
max_heap = []
for s in scores:
    heapq.heappush(max_heap, -s)  # negate so the largest becomes the "smallest"

top = -heapq.heappop(max_heap)  # negate back on the way out
print(f"   highest score: {top}")

# Or the simplest route when you just need the top-N of an existing collection:
print(f"   top 3 via nlargest: {heapq.nlargest(3, scores)}")


# ---------------------------------------------------------------------------
# 5. heappushpop / heapreplace — push and pop in one operation
# ---------------------------------------------------------------------------
show("5. heappushpop vs heapreplace")

h = [3, 7, 9, 20]
heapq.heapify(h)
print(f"   heap: {h}")

# heappushpop pushes the new item, then pops the SMALLEST of the old+new.
print(f"   heappushpop(..., 1) -> {heapq.heappushpop(h, 1)}  (pushed 1, pops min)")
print(f"   heap now: {h}")

print(f"   heapreplace(..., 0) -> {heapq.heapreplace(h, 0)}  (pops min, pushes 0)")
print(f"   heap now: {h}   (heapreplace does NOT add 0 to the candidate set)")


# ---------------------------------------------------------------------------
# 6. merge — combine sorted iterables in sorted order
# ---------------------------------------------------------------------------
show("6. merge() several sorted streams")

a = [1, 4, 7, 10]
b = [2, 5, 8]
c = [3, 6, 9]
merged = list(heapq.merge(a, b, c))
print(f"   merged: {merged}")


print("\nDone — see how push/pop stays O(log n) even as the heap grows.")
