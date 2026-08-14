"""
schedium demo — a composable, in-process job scheduler.

Run with:  .venv/bin/python 07-schedium/demo.py

Key idea: you register a function + a *trigger*, then call run_pending() in a
loop. We pass an explicit `now` to run_pending() so the demo is instant and
deterministic (no real waiting). Jobs are zero-argument callables; `now` only
tells the scheduler what the current time is.
"""

from datetime import datetime

from schedium import (
    AtDateTime,
    Between,
    CancelJob,
    Every,
    Job,
    JobDidNotRun,
    On,
    Scheduler,
)


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. A basic job with a repeating cadence
# ---------------------------------------------------------------------------
show("1. Repeating job (every 5 minutes)")
log: list[str] = []


def heartbeat() -> str:
    log.append("beat")
    return "heartbeat-sent"


sched = Scheduler()
sched.append(Job(heartbeat, Every(unit="minute", interval=5), name="heartbeat"))

# Simulate the clock advancing; the job is due only at 5-minute boundaries.
for now in [
    datetime(2026, 2, 4, 10, 0, 30),  # 10:00:30 -> due (first matching bucket)
    datetime(2026, 2, 4, 10, 1, 0),   # same 5-min bucket -> NOT due
    datetime(2026, 2, 4, 10, 5, 0),   # 10:05:00 -> due again
]:
    result = sched.run_pending(now=now)
    label = "ran" if result != [JobDidNotRun] else "skipped (dedup)"
    print(f"   {now:%H:%M:%S} -> {label}: {result!r}")

print(f"   heartbeat ran {len(log)} time(s)")


# ---------------------------------------------------------------------------
# 2. Composing triggers with & (AND) and | (OR)
# ---------------------------------------------------------------------------
show("2. 'Every 10 min, but only 09:00-17:00' (Every & Between)")

calls: list[datetime] = []


def business_hours() -> None:
    calls.append(datetime.now())  # just a marker; the mapping is shown below


# Every 10 minutes, narrowed to the working-hours range (inclusive 9..17).
work_trigger = Every(unit="minute", interval=10) & Between(
    unit="hour_of_day", start=9, end=17
)
sched2 = Scheduler()
sched2.append(Job(business_hours, work_trigger, name="work-hours"))

for now in [
    datetime(2026, 2, 4, 8, 50, 0),   # before hours -> skip
    datetime(2026, 2, 4, 9, 0, 0),    # 09:00 -> run
    datetime(2026, 2, 4, 17, 30, 0),  # 17:30 -> within hour 17 -> run
    datetime(2026, 2, 4, 18, 0, 0),   # after hours -> skip
]:
    result = sched2.run_pending(now=now)
    print(f"   {now:%H:%M} -> {'ran' if result != [JobDidNotRun] else 'skipped'}")

print("   (job ran", len(calls), "times total)")


show("3. 'Weekdays at 08:00' (Every & On & On & On)")


def morning_report() -> None:
    pass  # side effect not needed; the run/skip output is the point


# Every day + is a weekday + hour==8 + minute==0.
morning_trigger = (
    Every(unit="day", interval=1)
    & On(unit="weekdays")
    & On(unit="hour_of_day", value=8)
    & On(unit="minute_of_hour", value=0)
)
sched3 = Scheduler()
sched3.append(Job(morning_report, morning_trigger, name="morning-report"))

for now in [
    datetime(2026, 2, 7, 8, 0, 0),    # Saturday -> skip
    datetime(2026, 2, 9, 8, 0, 0),    # Monday 08:00 -> run
    datetime(2026, 2, 9, 8, 5, 0),    # Monday 08:05 -> skip (minute != 0)
]:
    result = sched3.run_pending(now=now)
    print(f"   {now:%a %H:%M} -> {'ran' if result != [JobDidNotRun] else 'skipped'}")


# ---------------------------------------------------------------------------
# 3. One-shot job (AtDateTime) — fires once, even if started late
# ---------------------------------------------------------------------------
show("4. One-shot job (AtDateTime)")

fired: list[str] = []


def one_time() -> str:
    fired.append("boom")
    return "fired"


sched4 = Scheduler()
target = datetime(2026, 2, 4, 12, 0, 0)
sched4.append(Job(one_time, AtDateTime(target), name="one-shot"))

# We "start late" at 12:05, but AtDateTime still fires exactly once.
print("   run at 12:05:", sched4.run_pending(now=datetime(2026, 2, 4, 12, 5, 0)))
print("   run again 12:06:", sched4.run_pending(now=datetime(2026, 2, 4, 12, 6, 0)))


# ---------------------------------------------------------------------------
# 4. Self-cancelling jobs via CancelJob
# ---------------------------------------------------------------------------
show("5. Self-cancelling job (returns CancelJob)")

runs = 0


def migrate():
    global runs
    runs += 1
    print("   migrating...")
    return CancelJob("migration complete")


sched5 = Scheduler()
sched5.append(Job(migrate, Every(unit="minute", interval=1), name="migration"))

print("   jobs before:", len(sched5.jobs))
sched5.run_pending(now=datetime(2026, 2, 4, 10, 0, 0))
print("   jobs after first run:", len(sched5.jobs), "(job removed itself)")
sched5.run_pending(now=datetime(2026, 2, 4, 10, 1, 0))
print("   nothing left to run:", sched5.run_pending(now=datetime(2026, 2, 4, 10, 2, 0)))


print("\nDone — schedules were driven by simulated time via run_pending(now=...).")
