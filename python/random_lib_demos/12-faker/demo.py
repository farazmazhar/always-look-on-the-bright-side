"""
faker demo — generate realistic fake data.

Run with:  .venv/bin/python 12-faker/demo.py

One Faker() object exposes hundreds of provider methods (name, address, ...).
A seed makes the output reproducible — handy for tests and demos.
"""

from faker import Faker


def show(title: str) -> None:
    print(f"\n{title}")


# ---------------------------------------------------------------------------
# 1. The basic object and a few providers
# ---------------------------------------------------------------------------
show("1. Basic providers")

fake = Faker()
print("   name:        ", fake.name())
print("   address:     ", fake.address().replace("\n", ", "))
print("   email:       ", fake.email())
print("   phone:       ", fake.phone_number())
print("   company:     ", fake.company())
print("   job:         ", fake.job())
print("   text:        ", fake.text(max_nb_chars=60).replace("\n", " "))


# ---------------------------------------------------------------------------
# 2. Specialized data types
# ---------------------------------------------------------------------------
show("2. Specialized data")

print("   date_of_birth:", fake.date_of_birth(minimum_age=18, maximum_age=90))
print("   uuid4:        ", fake.uuid4())
print("   ipv4:         ", fake.ipv4())
print("   credit card:  ", fake.credit_card_number())
print("   iban:         ", fake.iban())
print("   hex color:    ", fake.hex_color())
print("   url:          ", fake.url())


# ---------------------------------------------------------------------------
# 3. Locales — data shaped for a specific country/language
# ---------------------------------------------------------------------------
show("3. Locales")

it = Faker("it_IT")
ja = Faker("ja_JP")
print("   Italian name:  ", it.name())
print("   Italian city:  ", it.city())
print("   Japanese name: ", ja.name())
print("   Japanese city: ", ja.city())


# ---------------------------------------------------------------------------
# 4. Seeding for reproducibility
# ---------------------------------------------------------------------------
show("4. Seeding")

a = Faker()
a.seed_instance(1234)
b = Faker()
b.seed_instance(1234)

print("   seeded name A:", a.name())
print("   seeded name B:", b.name())
print("   same sequence? ", [a.name() for _ in range(3)] == [b.name() for _ in range(3)])


# ---------------------------------------------------------------------------
# 5. Composite profiles and nested structures
# ---------------------------------------------------------------------------
show("5. Composite generators")

profile = fake.profile(fields=["name", "mail", "job", "birthdate"])
print("   profile:", profile)

doc = fake.pydict(10, value_types=["str", "int", "email"])
print("   pydict keys:", list(doc.keys())[:5], "... (10 fields total)")


# ---------------------------------------------------------------------------
# 6. Generate a batch of fake users (a common real-world task)
# ---------------------------------------------------------------------------
show("6. Batch of fake users")


def make_user(f: Faker) -> dict:
    return {
        "id": f.uuid4(),
        "name": f.name(),
        "email": f.email(),
        "city": f.city(),
        "age": f.random_int(18, 70),
    }


users = [make_user(fake) for _ in range(3)]
for u in users:
    print("   ", u)

print("\nDone — never hand-write fake data again (and never test with real data).")
