"""
python-statemachine demo — explicit, safe state transitions.

Run with:  .venv/bin/python 05-python-statemachine/demo.py

You define states and the transitions between them; calling a transition
method is the *only* way to change state, so illegal moves are impossible.
"""

from statemachine import State, StateMachine, TransitionNotAllowed


def state_of(machine: StateMachine) -> str:
    """Return a friendly name of the machine's current state(s)."""
    return ",".join(sorted(machine.configuration_values))


# ---------------------------------------------------------------------------
# 1. A basic traffic light (a simple cycle)
# ---------------------------------------------------------------------------
class TrafficLight(StateMachine):
    # Three states; `green` is where the machine starts.
    green = State(initial=True)
    yellow = State()
    red = State()

    # One event `cycle` moves green->yellow->red->green (via the `|` chain).
    cycle = green.to(yellow) | yellow.to(red) | red.to(green)


print("1. Traffic light cycle:")
light = TrafficLight()
for step in range(4):
    print(f"   {step}: {state_of(light)}  -> cycle() -> ", end="")
    light.cycle()
    print(state_of(light))


# ---------------------------------------------------------------------------
# 2. Guards: a transition only fires when its condition is true
# ---------------------------------------------------------------------------
class Order(StateMachine):
    pending = State(initial=True)
    paid = State()
    shipped = State(final=True)     # a final state ends the machine
    cancelled = State(final=True)

    # `pay` moves to `paid` only if has_funds is True, otherwise to cancelled.
    pay = pending.to(paid, cond="has_funds") | pending.to(cancelled)
    ship = paid.to(shipped)
    cancel = pending.to(cancelled) | paid.to(cancelled)

    # The value is injected when we create the instance (see below).
    has_funds = False


print("\n2. Order with a guard (no funds):")
poor_order = Order(has_funds=False)
print(f"   state={state_of(poor_order)}  allowed={[e.name for e in poor_order.allowed_events]}")
poor_order.pay()  # has_funds is False -> moves to cancelled instead of paid
print(f"   after pay(): {state_of(poor_order)}  (terminated={poor_order.is_terminated})")

print("\n3. Order with a guard (has funds):")
rich_order = Order(has_funds=True)
rich_order.pay()
print(f"   after pay(): {state_of(rich_order)}  allowed={[e.name for e in rich_order.allowed_events]}")

# Trying an illegal move raises TransitionNotAllowed instead of corrupting state.
try:
    rich_order.pay()  # already paid -> `pay` is no longer allowed
except TransitionNotAllowed:
    print("   blocked: cannot pay() twice (TransitionNotAllowed)")

rich_order.ship()
print(f"   after ship(): {state_of(rich_order)}  (terminated={rich_order.is_terminated})")


# ---------------------------------------------------------------------------
# 4. Callbacks: run code on entry/exit and around events
# ---------------------------------------------------------------------------
class VendingMachine(StateMachine):
    idle = State(initial=True)
    has_coin = State()

    insert_coin = idle.to(has_coin)
    vend = has_coin.to(idle)

    def on_enter_has_coin(self):
        print("   [on_enter_has_coin] coin accepted, awaiting selection")

    def before_vend(self):
        print("   [before_vend] dispensing item...")


print("\n4. Vending machine callbacks:")
vm = VendingMachine()
vm.insert_coin()
vm.vend()


# ---------------------------------------------------------------------------
# 5. Imperative control: send() and goto()
# ---------------------------------------------------------------------------
print("\n5. send() and goto():")
vm2 = VendingMachine()
vm2.send("insert_coin")   # trigger an event by name
print(f"   after send('insert_coin'): {state_of(vm2)}")
vm2.goto("idle")          # jump straight to a state
print(f"   after goto('idle'): {state_of(vm2)}")


print("\nDone — the state machine enforced the workflow for us.")
