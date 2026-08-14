# What is LangChain? (LangChain Under 6 Minutes)

## What is LangChain?

LangChain is an open-source framework for building applications powered by Large Language Models (LLMs). It provides composable modules and abstractions that let developers chain together LLMs with other components (tools, data sources, APIs) without boilerplate vendor-specific code.

## Core Modules

### Chat Models
Standardized interface to interact with LLMs from different providers (OpenAI, Anthropic, Google, Ollama, etc.). Abstracts away provider-specific APIs so you can switch models with minimal code changes.

### Prompts / Prompt Templates
Templates with dynamic placeholders for building reusable, parameterized prompts. Also includes Few-Shot prompt templates for in-context learning examples.

### Document Loaders
Load data from diverse sources into a unified Document format: PDFs, CSVs, JSON, web pages, YouTube, Notion, databases, etc. Each loader returns LangChain `Document` objects.

### Text Splitters
Chunk documents into smaller pieces suitable for LLM context windows. Includes: RecursiveCharacterTextSplitter, TokenTextSplitter, semantic chunkers, Markdown-aware splitters.

### Output Parsers
Parse raw LLM text output into structured formats: JSON, Pydantic objects, comma-separated lists, etc. Enables downstream programmatic consumption of LLM responses.

### Memory / History
Persist conversation context across interactions. Types include: ConversationBufferMemory, SummaryMemory, Knowledge Graph Memory, etc.

### Embeddings
Convert text into vector representations for semantic search. Supports OpenAI embeddings, HuggingFace, and other providers.

### Vector Stores
Store and query embeddings for similarity search. Integrations: Pinecone, FAISS, Chroma, Weaviate, etc.

### Retrieval (RAG)
Combine document retrieval with LLM generation. Retrievers fetch relevant documents, which are then fed into the LLM's context to ground responses in external data.

### Tools & Toolkits
Define callable functions the LLM can invoke (API calls, database queries, code execution). The `@tool` decorator converts Python functions into LLM-callable tools. Toolkits bundle related tools (e.g., SQL toolkit, GitHub toolkit).

### Agents
LLM-powered systems that dynamically decide which actions to take and in what order. Unlike chains (hard-coded control flow), agents use an LLM as a reasoning engine to select tools and iterate until a goal is achieved.

### Chains
Composable sequences of components linked via LCEL (LangChain Expression Language). Output of one step feeds into the next. Example: PromptTemplate → LLM → OutputParser.

## Ecosystem

- **LangSmith** — Observability, debugging, testing, and evaluation platform for LLM applications
- **LangGraph** — Low-level orchestration framework for stateful, multi-actor agent workflows with conditional logic, persistence, and streaming
- **LangServe** — Deploy LangChain runnables as REST APIs (FastAPI-based)

## Key Principle

LangChain is model-agnostic and provider-agnostic. Write your application logic once and swap LLMs or tools as needed without rewriting the pipeline.
