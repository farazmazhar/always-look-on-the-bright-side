# LangChain Fundamentals: Prompt Templates, ChatModels, and Chains

## 1. Prompt Templates

A prompt is the text input sent to an LLM. A **PromptTemplate** is a reusable, dynamic prompt with placeholders.

```python
from langchain_core.prompts import PromptTemplate

template = "I want you to write a cool, funny jingle for a {product} product."
prompt = PromptTemplate(template=template, input_variables=["product"])

prompt.format(product="cat food")   # "I want you to write a cool, funny jingle for a cat food product."
prompt.format(product="piano")      # "I want you to write a cool, funny jingle for a piano product."
```

## 2. ChatModels

`ChatOpenAI` is a **Chat Model** — the standard LangChain interface for modern conversational LLMs (GPT, Claude, Gemini).

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5", temperature=0)
```

- Modern LLMs are designed around **messages**, not raw strings.
- Message types: **SystemMessage** (instructions), **HumanMessage** (user input), **AIMessage** (model response).
- Chat models take a list of messages in, return a new AIMessage out.

## 3. Chains

A **Chain** is a sequence of components where the **output of one step becomes the input of the next**.

Built with LCEL (LangChain Expression Language) using the pipe operator `|`:

```python
chain = prompt | llm
response = chain.invoke({"product": "cat food"})
```

Advanced workflow example:
1. User query
2. PromptTemplate formats it
3. LLM generates response
4. OutputParser parses raw text → structured format (e.g., JSON)
5. Tool / external API call
6. Final LLM call produces polished output
