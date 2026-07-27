# Lecture 18 — Training vs. Inference

## Training: How the Model Learns

### The Process

```
Raw text corpus → Tokenize → Model predicts next token → Compare with actual → Update weights
                       ↑                                                              |
                       └──────────────────── Loop billions of times ──────────────────┘
```

### Step by Step

1. **Feed a sequence of tokens** from the training data
   ```
   Input:  ["The", "cat", "sat", "on"]
   Target:  "the"
   ```

2. **Model predicts the next token** — it outputs a probability distribution over the entire vocabulary
   ```
   Model output:
     "the"   → 0.42
     "a"     → 0.18
     "mat"   → 0.11
     "floor" → 0.06
     ... (50,000+ other tokens)
   ```

3. **Compare prediction with the actual next token** using a loss function (cross-entropy)
   ```
   Actual: "the" (index 5)
   Predicted probability for "the": 0.42
   Loss = -log(0.42) = 0.868
   ```

4. **Backpropagation** — compute gradients of loss w.r.t. every weight

5. **Update weights** — push probabilities up for correct tokens, down for wrong ones
   ```
   Before update: P("the") = 0.42
   After update:  P("the") = 0.44  (moves up slightly)
   ```

6. **Repeat** over the entire training corpus, billions of times

### Self-Supervised Learning

No human labels needed. The data labels itself — the next word in the original text IS the label.

```
Input:  "Paris is the capital of"
Label:  "France"   ← just the next word from the original document

Input:  "def fibonacci(n):"
Label:  "    if"   ← the model learns to predict code

Input:  "The mitochondria is the powerhouse of"
Label:  "the"      ← learns common phrases and knowledge
```

### Analogy

> Like a child learning to read by guessing the next word in millions of sentences — getting feedback each time, gradually improving prediction accuracy.

---

## Inference: How the Model Generates

### The Process

```
User prompt → Tokenize → Feed to model → Predict next token → Append to sequence → Repeat
                ↑                                                       |
                └─────────────── Autoregressive loop ───────────────────┘
```

### Step by Step

1. **User provides input**
   ```
   Prompt: "Once upon a"
   Tokenized: ["Once", "upon", "a"]  (3 tokens)
   ```

2. **Model processes the entire sequence so far** and predicts the next token
   ```
   Predictions for token 4:
     "time"  → 0.35
     "day"   → 0.12
     "story" → 0.08
     ...
   ```

3. **Select a token** (greedy, or sampling based on temperature/top-p/top-k)
   ```
   Selected: "time"
   ```

4. **Append it to the sequence**
   ```
   Sequence: ["Once", "upon", "a", "time"]
   ```

5. **Feed the extended sequence back** to predict the NEXT token
   ```
   Input:  ["Once", "upon", "a", "time"]
   Output: "there"  (0.62 probability)
   ```

6. **Repeat** until max length, stop sequence, or EOS token

### Example: Full Generation

```
Prompt:    "The future of AI is"

Step 1:    "The future of AI is"  →  "bright"
Step 2:    "The future of AI is bright"  →  "and"
Step 3:    "The future of AI is bright and"  →  "full"
Step 4:    "The future of AI is bright and full"  →  "of"
Step 5:    "..."  →  "possibilities"
Step 6:    "..."  →  "."
Step 7:    "..."  →  <EOS>  (stop)

Result:    "The future of AI is bright and full of possibilities."
```

---

## Context Window: How Much History?

The model sees **all previous tokens** in the current conversation — up to the **context window** limit.

### Context Window Size by Model

| Model | Context Window | Equivalent to |
|---|---|---|
| GPT-3 | 2,048 tokens | ~1,500 words / ~6 pages |
| GPT-3.5 Turbo | 4,096 – 16,385 tokens | ~12,000 words / ~50 pages |
| GPT-4 Turbo | 128,000 tokens | ~96,000 words / ~300 pages |
| Claude 3 | 200,000 tokens | ~150,000 words |
| Gemini 1.5 Pro | 1,000,000+ tokens | ~750,000 words / full books |
| Llama 3 | 8,192 tokens | ~6,000 words |

### What Happens at the Limit

```
Context window = 4,096 tokens

Prompt (500 tokens) + Generated so far (3,700 tokens) = 4,200 tokens
                                                          ↑
                                                    EXCEEDS WINDOW

→ Oldest tokens are dropped (truncation)
→ Model "forgets" early parts of the conversation
→ Quality degrades — inconsistent, circular, or contradictory output
```

### Key Insight

> The model does NOT "remember" anything between separate API calls. Each inference call processes the full input sequence from scratch. The illusion of memory comes from sending back the entire conversation history each time.

### Example: Why Context Window Matters

```
User: "My name is Alice and I'm a software engineer."
Assistant: "Hi Alice! How can I help with your engineering work?"
User: "Write a function to sort a list."
Assistant: [writes sort function]
User: "Now add error handling."
Assistant: [adds error handling — still knows Alice wants Python code]
...
(after 20+ turns, conversation exceeds context window)
...
User: "What did I say my name was?"
Assistant: "I don't recall. Could you tell me again?"  ← early info truncated
```
