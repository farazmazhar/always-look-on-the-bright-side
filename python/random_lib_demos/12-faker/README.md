# faker

**Faker** generates realistic-looking **fake data**: names, addresses, emails,
text, dates, company names, credit card numbers, and hundreds of other fields.
It is the standard tool for seeding databases, filling in test fixtures, and
building demos that need plausible data.

## Why use it?

- Writing realistic test data by hand is tedious and error-prone.
- Real personal data should *never* be used in tests/demos (privacy/GDPR).
- Faker is deterministic when you set a seed, so tests stay reproducible.

## Key features

- One `Faker()` object exposes hundreds of providers: `name()`, `address()`,
  `email()`, `text()`, `date_time()`, `company()`, `iban()`, `uuid4()`…
- Locale support: `Faker("it_IT")`, `Faker("ja_JP")`, etc. produce localized data.
- `fake.seed_instance(1234)` makes output repeatable.
- Composite generators: `profile()`, `simple_profile()`, `json()`, `pydict()`.
- Custom/community providers can be added (`faker_microservice`, etc.).

## Install

```bash
pip install faker
```

## Use cases

- Populate a database with sample rows for development.
- Generate test fixtures and mock API responses.
- Prototype UIs with realistic-looking content.
- Performance/load testing with varied input data.
- Demo notebooks and sample datasets.

## Things you can achieve

- 100 fake users with unique emails and addresses in a few lines.
- Reproducible test data by seeding the generator.
- Localized names/addresses for different regions.
- Nested JSON structures (`fake.json()`) for API testing.

## References

- Docs: https://faker.readthedocs.io/
- PyPI: https://pypi.org/project/faker/
- GitHub: https://github.com/joke2k/faker
