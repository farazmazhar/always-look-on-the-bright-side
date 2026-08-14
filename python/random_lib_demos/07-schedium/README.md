# schedium

**schedium** is a lightweight, composable, in-process, pure-Python job
scheduler. You register *jobs* (a function + a *trigger* describing when it
should run), then call `run_pending()` in your own loop to execute anything
that is due.

## Why use it?

- **No threads, no processes** — jobs run inline when *you* call `run_pending()`.
- **Composable triggers** — combine simple primitives with `&` (AND) and `|` (OR)
  to express complex schedules.
- **Automatic deduplication** — calling `run_pending()` repeatedly in the same
  time bucket is safe; a job runs at most once per bucket.
- **Zero dependencies** — pure Python, fully typed, mypy-checked.

## Key features

- `Scheduler` + `Job(func, trigger, name=...)` + `sched.append(...)`.
- Deterministic testing via `run_pending(now=some_datetime)`.
- Trigger primitives: `Every`, `Tick`, `On`, `Between`, `AtDateTime`,
  `BetweenDateTime`, and helpers `Daily` / `Weekly`.
- Compose triggers with `&` (narrow) and `|` (alternatives).
- `CancelJob` return value to make a job remove itself.
- `JobDidNotRun` sentinel in `run_pending()` results.
- Optional threaded/queued schedulers for background execution.
- A module-level default scheduler (`add_job`, `run_pending`).

## Install

```bash
pip install schedium
```

## Use cases

- Background housekeeping: cleanups, syncs, cache refreshes, report emails.
- Cron-like jobs inside a long-running process or worker.
- "Every N minutes but only during business hours" style schedules.
- One-shot delayed tasks without a cron daemon.
- Embeddable scheduler for libraries/tools that need a heartbeat loop.

## Things you can achieve

- Run a job every 5 minutes, but only on weekdays between 09:00–17:00.
- A one-shot job that fires at a specific datetime (even if started late).
- Safe re-entry: a job runs at most once per minute no matter how often you poll.
- Self-cancelling jobs that remove themselves after completing a migration.

## References

- Docs: https://schedium.readthedocs.io/
- PyPI: https://pypi.org/project/schedium/
- GitHub: https://github.com/MarcBresson/schedium
