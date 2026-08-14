"""
autoregistry demo — map string names to classes/functions automatically.

Run with:  .venv/bin/python 04-autoregistry/demo.py

Three ways to use Registry are shown below:
  1. inherit it   -> subclasses auto-register by their class name
  2. instantiate   -> decorate functions/classes with a Registry object
  3. wrap a module -> every public name in a module becomes a key
"""

from abc import abstractmethod

from autoregistry import Registry


# ---------------------------------------------------------------------------
# 1. Inheritance: subclasses register themselves
# ---------------------------------------------------------------------------
# Define a base "interface" by inheriting Registry. Abstract methods are
# allowed because Registry's metaclass is ABCMeta.
class PaymentGateway(Registry):
    @abstractmethod
    def charge(self, amount: float) -> str:
        """Charge a customer; returns a confirmation message."""


# Just defining these subclasses is enough — they are registered automatically.
class Stripe(PaymentGateway):
    def charge(self, amount: float) -> str:
        return f"Charged ${amount:.2f} via Stripe"


class PayPal(PaymentGateway):
    def charge(self, amount: float) -> str:
        return f"Charged ${amount:.2f} via PayPal"


class CashApp(PaymentGateway):
    def charge(self, amount: float) -> str:
        return f"Charged ${amount:.2f} via CashApp"


print("1. Inherited registry:")
print("   keys:", list(PaymentGateway))
print("   len:", len(PaymentGateway))

# Look up a class by name (case-insensitive!) and instantiate it.
gateway_name = "stripe"           # imagine this came from a config file
gateway_cls = PaymentGateway[gateway_name]
gateway = gateway_cls()
print(f"   PaymentGateway['stripe'] -> {gateway.charge(19.99)}")

# Missing keys raise KeyError; .get() lets you provide a fallback.
print("   .get() with fallback:", PaymentGateway.get("bitcoin", Stripe).__name__)
print("   'PAYPAL' in registry:", "PAYPAL" in PaymentGateway)


# ---------------------------------------------------------------------------
# 2. Decorator: register functions under a Registry object
# ---------------------------------------------------------------------------
commands = Registry()  # a standalone registry, no inheritance needed


@commands
def hello(name: str) -> str:
    return f"Hello, {name}!"


@commands()  # calling the registry as a decorator also works
def bye(name: str) -> str:
    return f"Bye, {name}!"


def manual(name: str) -> str:
    return f"Manual greeting for {name}!"


# You can also assign entries like a normal dictionary (any string key).
commands["manual"] = manual

print("\n2. Function registry:")
print("   keys:", list(commands))
print("   commands['hello']('Ada'):", commands["hello"]("Ada"))
print("   commands['manual']('Bob'):", commands["manual"]("Bob"))


# ---------------------------------------------------------------------------
# 3. Module registry: discover everything inside a module
# ---------------------------------------------------------------------------
# Pass any module to Registry and its public names become keys. We use a small
# stdlib module here for the demo; real code might use your own plugin module.
import statistics as stats_module

stats = Registry(stats_module)
print("\n3. Module registry (statistics):")
print("   some keys:", [k for k in stats if not k.startswith("_")][:8])
print("   stats['mean']([1,2,3,4]):", stats["mean"]([1, 2, 3, 4]))


# ---------------------------------------------------------------------------
# 4. A realistic dispatch example
# ---------------------------------------------------------------------------
# Combine #1 and a lookup to emulate config-driven behavior end to end.
def process_payment(gateway_name: str, amount: float) -> str:
    # Look up the gateway class by string, instantiate, and use it.
    cls = PaymentGateway.get(gateway_name)
    if cls is None:
        return f"Unknown gateway: {gateway_name!r}"
    return cls().charge(amount)


print("\n4. Config-driven dispatch:")
for name in ("paypal", "cashapp", "stripe", "dogecoin"):
    print(f"   process_payment({name!r}) -> {process_payment(name, 5.00)}")


print("\nDone — a registry turned strings into working code.")
