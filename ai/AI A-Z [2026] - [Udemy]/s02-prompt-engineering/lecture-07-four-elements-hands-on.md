# Lecture 7 — The 4 Elements of a (Good) Prompt [Hands-On]

Used **Amazon Bedrock** to test and iterate prompts for building a **Movie Script Generator**.

Course material: `course_material/Part 1 - Prompt Engineering/Movie_Script_Generator/`

## Prompt 1 — Without Template (all 4 elements inline)

| Element | Content |
|---|---|
| **Instruction** | "Generate a creative and engaging movie script for an animated comedy..." |
| **Context** | Wolf lives in clouds, interacts with quirky animals, family-friendly comedy, light-hearted life lessons |
| **Input Data** | Characters: wise/humorous wolf, chatty cloud, playful eagle, sunbeam. Setting: sky world. Genre: Comedy. |
| **Output Indicator** | "Short movie script in a comedic tone, with dialogue and brief action descriptions, reflecting the wolf's humorous wisdom" |

## Takeaways

- Bedrock gives quick LLM access without infrastructure overhead
- All 4 elements present → coherent output matching intent
- Missing an element (e.g. no output indicator) degrades results
