# heapq

**heapq** implements the **heap queue algorithm**, also known as a *priority
queue*. A heap is a binary tree stored in a plain list where the smallest
element is always at index 0. Because the tree is always kept "heap-ordered",
pushing a value or popping the smallest one costs **O(log n)**, which is
ideal when you repeatedly need the smallest (or largest) item from a stream.

## Why use it?

- Python's built-in `list` with `.sort()` re-sorts the whole list every time —
  expensive if you add items incrementally. A heap keeps insertion and
  extraction cheap.
- You almost never write the data structure yourself; `heapq` is in the
  standard library and battle-tested.
- It underpins priority queues, task schedulers, and Dijkstra / A* shortest
  path algorithms.
- It is a **min-heap** (smallest first); flip signs or use negative values for
  max-heap behavior.

## Key features

- `heappush(heap, item)` — add an item in O(log n).
- `heappop(heap)` — remove and return the smallest item in O(log n).
- `heappushpop(heap, item)` / `heapreplace(heap, item)` — push+pop atomically.
- `heapify(x)` — turn an arbitrary list into a heap **in place** in O(n).
- `nsmallest(n, iterable)` / `nlargest(n, iterable)` — convenience helpers.
- `merge(*iterables)` — merge sorted inputs into one sorted iterator.
- Works on tuples / objects with rich comparisons, so you can store
  `(priority, item)` pairs.

## Install

`heapq` is part of the Python **standard library** — no installation needed.

## Use cases

- Scheduling tasks by priority (process the most important/soonest first).
- Merging several sorted logs or streams in sorted order.
- Streaming "top-N" of a huge dataset without loading it all.
- Dijkstra's shortest path and A* search (the open-set is a priority queue).
- Event simulation where events fire by timestamp.

## Things you can achieve

- A priority queue of `(priority, name)` tuples where `heappop` always returns
  the smallest priority.
- A max-heap by pushing negated values, e.g. `heappush(h, -score)`.
- The top-3 largest elements of a big list with `nlargest`.
- Lazily merged, sorted iteration over multiple sorted lists with `merge`.

## References

- Docs: https://docs.python.org/3/library/heapq.html
