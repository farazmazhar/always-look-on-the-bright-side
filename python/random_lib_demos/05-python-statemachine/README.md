# python-statemachine

**python-statemachine** lets you describe **finite state machines** as plain
Python classes. You declare states, the transitions between them, and the
conditions under which a transition is allowed — then drive the machine by
calling the transition methods.

## Why use it?

- Makes messy "status + lots of ifs" code explicit and safe: invalid state
  changes are *impossible* by construction.
- The state machine *is* the documentation of your workflow.
- Supports conditions/guards, callbacks, entry/exit actions, and even UML
  statecharts (nested/parallel states).

## Key features

- `State` (with `initial=True` / `final=True`) and named transitions via
  `green.to(yellow)`.
- `|` chains: one event can fan out to different target states.
- Guards with `cond=` / `unless=` to gate transitions on runtime conditions.
- Automatic callbacks: `on_enter_<state>`, `on_exit_<state>`,
  `before_<event>`, `after_<event>`.
- `.allowed_events`, `.send("event")`, `.goto("state")`, `.is_terminated`.
- Models: attach domain data to the machine instance via `__init__` kwargs.
- Graph/statechart support (`StateChart`) for nested and parallel regions.

## Install

```bash
pip install python-statemachine
```

## Use cases

- Order/booking lifecycles (pending → paid → shipped → cancelled…).
- Workflow engines, approval pipelines, ticket states.
- Game state (menu → playing → paused → game over).
- Traffic lights, vending machines, IoT device states.
- Protocol/session state handling.

## Things you can achieve

- Guarantee a cancelled order can never be "shipped".
- Attach side effects to state entry (send email on `approved`).
- Guard transitions on business rules (`cond="has_funds"`).
- Export/inspect the machine to list what is allowed right now.

## References

- Docs: https://python-statemachine.readthedocs.io/
- PyPI: https://pypi.org/project/python-statemachine/
- GitHub: https://github.com/fgmacedo/python-statemachine
