# Lecture 20 — Tokens and Embeddings

## Tokens

A **token** is the smallest unit of text an LLM processes — not quite a word, not quite a character.

### How Tokenization Works

```
Text: "Hello, world!"

Tokens: ["Hello", ",", " world", "!"]   ← 4 tokens
```

Tokenizers break text into subword units. Common words get their own token; rare words get split.

### Examples

| Text | Tokens | Count |
|---|---|---|
| `"cat"` | `["cat"]` | 1 |
| `"cats"` | `["cats"]` | 1 |
| `"unbelievable"` | `["un", "bel", "ievable"]` | 3 |
| `"I love AI"` | `["I", " love", " AI"]` | 3 |
| `"The quick brown fox jumps over the lazy dog."` | `["The", " quick", " brown", " fox", " jumps", " over", " the", " lazy", " dog", "."]` | 10 |

> See it live: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

### Token ≠ Word ≈ Character

| Rule of thumb | Approx |
|---|---|
| 1 token | ~4 characters in English |
| 1 token | ~0.75 words |
| 100 tokens | ~75 words |
| 1,000 tokens | ~750 words |

### Why Tokens Matter

- **Cost** — APIs charge per token (input + output)
- **Context window** — token count determines how much fits
- **Encoding** — everything (text, code, numbers) becomes tokens before the model sees it

---

## Embeddings

An **embedding** is a numerical vector (list of numbers) that represents the **meaning** of a token, word, sentence, or document in a high-dimensional space.

### What They Look Like

```
Word: "king"
Embedding: [0.23, -0.54, 0.18, 0.91, -0.33, ..., 0.05]
           └──────── 768 to 4096 dimensions ──────────┘
```

Each number captures some aspect of meaning — the model learns these during training.

### How Words Relate in Embedding Space

Semantically similar words are **close together** in vector space. Distance = difference in meaning.

```
              cat ──┐
                    ├─── close (both are pets)
              dog ──┘

              dog ───────────────────── airplane
                    ↑                          ↑
               near each other            far apart
              (both animals)          (unrelated concepts)
```

### Distance Between Embeddings

Two common ways to measure:

| Method | What it means | Example |
|---|---|---|
| **Cosine Similarity** | Angle between vectors. Range: -1 to 1. 1 = identical direction. | "cat" vs "dog" → 0.85 (similar). "cat" vs "airplane" → 0.12 (different) |
| **Euclidean Distance** | Straight-line distance. Smaller = more similar. | "happy" vs "joyful" → 0.3. "happy" vs "sad" → 2.1 |

### Famous Example: Word Analogies

```
Embedding("king") - Embedding("man") + Embedding("woman") ≈ Embedding("queen")

In vector space:
  king ──→ queen
   │         │
  man ────→ woman

The vectors capture the gender relationship.
```

### Sentence-Level Embeddings

Not just words — entire sentences or paragraphs get a single embedding vector.

```
"My favourite fruit is an apple."  →  [0.12, 0.87, -0.44, ...]
"I enjoy eating apples."           →  [0.15, 0.82, -0.41, ...]   ← close (similar meaning)
"The stock market crashed today."  →  [-0.72, 0.03, 0.91, ...]   ← far (different topic)
```

### Why Embeddings Matter

| Use Case | How embeddings help |
|---|---|
| **Semantic search** | Find documents by meaning, not keywords |
| **RAG** | Retrieve relevant chunks by embedding similarity |
| **Clustering** | Group similar documents, reviews, or images |
| **Classification** | Use embeddings as features for downstream models |
| **Recommendations** | "Users who liked X also liked Y" via embedding distance |

### Visualizing Embedding Space

Even though embeddings have hundreds of dimensions, you can reduce them to 2D/3D for visualization (using PCA or t-SNE):

```
       animals                 technology
    ┌──────────┐            ┌──────────┐
    │ dog  cat │            │ python AI │
    │  horse   │            │  code ML  │
    └──────────┘            └──────────┘
         │                       │
         └───────────┬───────────┘
                     │
             ┌───────┴────────┐
             │  apple banana  │
             │  orange grape  │
             └────────────────┘
                  food
```

Similar concepts cluster together in space.
