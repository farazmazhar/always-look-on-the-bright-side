# Project Setup

Instructor sets up the working environment for the course's Hello World project.

## Steps

### 1. Clone the Course Repository
```bash
git clone https://github.com/emarco177/langchain-course
```

### 2. Create an Orphan Branch
Clean start with no parent/commit history — isolates the project from course material.
```bash
git checkout --orphan project/hello-world
git rm -rf .
```

### 3. Initialize the Project with uv (Python 3.12)
```bash
uv init
```
Generates `pyproject.toml` and a boilerplate `main.py`.

### 4. Install Dependencies
```bash
uv add langchain langchain-openai
```
LangChain has modularized integrations — install only the provider packages you use (`langchain-openai`).

### 5. Other Libraries
- `python-dotenv` — load secrets from `.env`
- `black` / `isort` — formatting + import sorting (instructor)

> **Note:** `ruff` covers both formatting and linting — can replace black + isort.

### 6. Create `.gitignore`
Copy the standard Python `.gitignore` template from GitHub so `.env` and `.venv` are never tracked.

### 7. Configure `.env`
```env
OPENAI_API_KEY=sk-...
```
`langchain-openai` looks for `OPENAI_API_KEY` by default. Treat API keys like passwords — never commit them.

### 8. Test the Environment Variable
```python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))
```
Verifies venv is active, packages installed, and `.env` is loading properly.

### 9. Commit and Push
Clean up test code, format, then:
```bash
git commit -m "environment setup"
git push
```

## Notes
- The `project/hello-world` branch should still be accessible in the course repo.
- LangChain course is compatible with V0.3.0.
