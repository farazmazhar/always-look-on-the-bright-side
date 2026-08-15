# Building a LangChain Chain to Summarize Text

## What We Did

Summarized a block of Wikipedia text about Elon Musk using our first LangChain chain.

## Steps

### 1. Gather Information
Copied a Wikipedia article about Elon Musk into a Python variable:
```python
information = """...elon musk text from wikipedia..."""
```

### 2. Define a Summary Prompt Template
```python
from langchain_core.prompts import PromptTemplate

summary_template = """
Given the information {information} about a person, I want you to create:
1. A short summary
2. Two interesting facts about the person
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template,
)
```
Template incorporates the Wikipedia info and specifies the expected output format.

### 3. Create the ChatOpenAI Model
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5", temperature=0)
```
`temperature=0` → deterministic, factual responses.

### 4. Build the Chain with LCEL
```python
chain = summary_prompt_template | llm
```
The pipe operator `|` is **LCEL (LangChain Expression Language)** — creates a Runnable where the output of one component becomes the input of the next.

### 5. Invoke the Chain
```python
result = chain.invoke(input={"information": information})
```
- Input type: dict with `information` key → PromptTemplate formats it into a string
- → ChatOpenAI (input: string, output: AIMessage)
- Result: structured summary + two interesting facts

### 6. Display the Result
```python
print(result.content)
```
`.content` holds the actual generated text; the LLM output is wrapped in an `AIMessage` object, not a plain string.
