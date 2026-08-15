# Coding Exercise 1: LangChain Model Switching: Groq API Integration

Switching between different LLM models via the Groq API (simulated with mock objects).

## Key Points
- Model names must match exactly what's available on [console.groq.com](https://console.groq.com)
- Groq API key set via the `GROQ_API_KEY` environment variable
- `temperature=0` → consistent/deterministic; higher temperature → more creative responses
- Exercise uses mock classes to simulate `langchain-groq` behavior

## Implementations

### Set API Key
```python
import os

def implement_set_api_key(api_key):
    os.environ["GROQ_API_KEY"] = api_key
```

### Llama 4 Model (temperature=0, consistent)
```python
def implement_llama_4_model():
    return ChatGroq(model="llama-4-8b-instant")
```

### Llama 3.3 Model (more creative)
```python
def implement_llama_3_3_model():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
```

### Query a Model
```python
def implement_query_model(model, prompt):
    response = model.invoke([("human", prompt)])
    return response.content
```

### Compare Both Models
```python
def implement_compare_models(prompt):
    models = {
        "llama-4-8b-instant": implement_llama_4_model,
        "llama-3.3-70b-versatile": implement_llama_3_3_model,
    }
    response = {}
    for model in models:
        llm = models[model]()
        response[model] = llm.invoke(prompt).content
    return response
```

## Mock Setup (provided by exercise)

```python
class ChatGroq:
    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
        ]
        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")

    def invoke(self, messages):
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Messages must be a non-empty list")
        if self.model == "llama-4-8b-instant":
            content = "[Llama 4 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
        elif self.model == "llama-3.3-70b-versatile":
            if self.temperature > 0.2:
                content = "[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            else:
                content = "[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"
        return MockAIMessage(content)


class MockAIMessage:
    def __init__(self, content):
        self.content = content
```

## Learning Objectives
- LangChain-Groq integration patterns
- Switching between LLM models with full, exact model names
- Class instantiation and method calls (`ChatGroq` → `.invoke()`)
- Function composition and data structures (dict of model factories)
- Reading API keys from environment variables instead of hardcoding
