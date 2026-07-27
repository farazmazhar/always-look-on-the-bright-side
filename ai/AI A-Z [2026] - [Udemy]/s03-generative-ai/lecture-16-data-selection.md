# Lecture 16 — Data Selection

## Structured vs. Unstructured Data

| Type | Description | Examples |
|---|---|---|
| **Structured** | Organized in predefined format — rows, columns, key-value pairs | SQL tables, CSV files, JSON, Excel sheets |
| **Unstructured** | No predefined schema or format | Videos, images, PDFs, audio files, emails, social media posts, raw text |

> Note: JSON is technically semi-structured, but the course groups it under structured for simplicity.

### Examples

```
Structured:
  - Customer database: id, name, age, purchase_history
  - JSON API response: {"user": "alice", "score": 95}

Unstructured:
  - A folder of 10,000 product review images
  - Raw podcast audio files
  - PDF research papers
```

---

## Labeled vs. Unlabeled Data

| Type | Description | Use Case | Example |
|---|---|---|---|
| **Labeled** | Data with target/answer attached | Supervised learning, fine-tuning | Email → "spam" or "not spam"; Image → "cat" |
| **Unlabeled** | Raw data, no annotations | Unsupervised learning, clustering, pretraining | Raw customer reviews, unannotated images |

### Examples

```
Labeled:
  - Medical images with doctor diagnoses ("tumor" / "no tumor")
  - Movie reviews with star ratings (1-5)
  - Chat transcripts with "satisfied" / "unsatisfied" labels

Unlabeled:
  - Scraped web pages (no categories assigned)
  - User behavior logs (no intent labels)
  - Photos from a camera roll (no tags)
```

---

## Data Selection for Foundation Models

| Consideration | Why it matters |
|---|---|
| **Quality** | Garbage in → garbage out. Noisy data hurts model performance. |
| **Diversity** | Narrow data → biased model. Need broad representation. |
| **Volume** | Foundation models need massive scale (trillions of tokens). |
| **Licensing** | Some data can't be used commercially (copyrighted, personal). |
| **Language/Task coverage** | If building a multilingual model, need data in all target languages. |

### Example

```
Building a medical foundation model:

✓ Labeled: 100K doctor-annotated X-rays with diagnoses
✓ Unlabeled: 500K medical journal articles (for pretraining)
✓ Structured: Patient records as tables (symptoms, lab results, outcomes)
✓ Unstructured: Radiology reports as PDFs, surgical videos
✗ Web-scraped Reddit comments (low quality, irrelevant to medicine)
```
