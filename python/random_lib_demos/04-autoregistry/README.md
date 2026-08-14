# autoregistry

**autoregistry** implements the *registry* design pattern automatically: it
maps **string names to code** (classes or functions) so you can look up and
instantiate things by name at runtime.

It is a tiny, dependency-free library built around one class, `Registry`.

## Why use it?

- Decouple "what to run" from the code that runs it — pick an implementation
  from a config file, CLI flag, or database value by its name.
- Kill long `if name == "foo": ... elif name == "bar": ...` chains.
- Auto-discover every subclass/function in a namespace instead of maintaining
  a hand-written mapping that you forget to update.

## Key features

- Inherit `Registry` to auto-register **subclasses** by class name.
- Create a `Registry()` object and decorate **functions/classes** with it.
- Case-insensitive lookups by default.
- `len`, iteration, `in`, `[...]`, and `.get(...)` — behaves like a dict.
- Build a registry straight from an **existing module** (e.g. `torch.optim`).
- Works with `@abstractmethod` (the base `Registry` is an `ABCMeta`).
- Configurable naming rules (see the docs).

## Install

```bash
pip install autoregistry
```

## Use cases

- Plugin systems: register "handlers", "parsers", "exporters" by name.
- Command dispatch: map a CLI subcommand to its implementation.
- Configuration-driven behavior: a YAML field chooses which class to use.
- Auto-discovery of strategy/algorithm implementations.
- Game/content pipelines with many named entity types.

## Things you can achieve

- `Pokemon["pikachu"]()` — instantiate the right subclass from a string.
- Add a new subclass in another module and it appears in the registry
  automatically (no manual registration line).
- A single decorator turns any function into an addressable command.

## References

- Docs: https://autoregistry.readthedocs.io/
- PyPI: https://pypi.org/project/autoregistry/
- GitHub: https://github.com/BrianPugh/autoregistry
