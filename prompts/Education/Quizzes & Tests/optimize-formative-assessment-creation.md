# Formative Assessment Question Generator

## 簡介

The Formative Assessment Question Generator is a free AI prompt that creates targeted assessment questions for educators across any unit and subject. This formative assessment prompt for ChatGPT produces a structured table of questions complete with answer keys, difficulty levels, question types, and Bloom's Taxonomy classifications. The prompt works by letting you specify the unit and subject, number of questions, question types (multiple choice, short answer, true/false, essay), difficulty levels (easy, medium, hard), and Bloom's levels (remembering, understanding, applying, analyzing, evaluating, creating). It runs on ChatGPT, Claude, Gemini, and Grok, delivering questions in a clear table format with complete answer keys and source citations. Use it to build quizzes, mid-unit checks, or differentiated assessments that measure student understanding across cognitive dimensions. Reach for this prompt when you need formative assessments that go beyond rote recall and systematically evaluate mastery at specific cognitive levels. ● Outputs questions in a sortable table with type, difficulty, answer, Bloom's level, and source columns ● Distributes questions across user-defined difficulty ranges and cognitive levels for balanced assessment ● Supports multiple question formats including multiple choice, short answer, true/false, and essay ● Includes complete answer keys and source citations for accountability and grading efficiency ## Prompt

```
## Role
You are an educational assessment designer creating formative assessment questions that target specific cognitive levels and difficulty ranges.

## Task
Generate a set of formative assessment questions for {{unit-and-subject}} that evaluates student understanding across multiple dimensions.

## Requirements
- Create {{number-of-questions}} questions
- Include these question types: {{question-types}} (e.g., multiple choice, short answer, true/false, essay)
- Distribute across difficulty levels: {{difficulty-levels}} (e.g., easy, medium, hard)
- Target these Bloom's Taxonomy levels: {{blooms-levels}} (e.g., remembering, understanding, applying, analyzing, evaluating, creating)
- Provide complete answer keys for all questions
- Cite sources where questions draw from specific references

## Output
Present all questions in this table format:

| Question | Type | Difficulty | Answer | Bloom's Level | Source |
|----------|------|------------|--------|---------------|--------|
| [question text] | [type] | [level] | [complete answer or correct option] | [taxonomy level] | [citation or N/A] |

Ensure questions are tailored to the specific content of the unit and assess different aspects of student mastery.
```

## 用法 / Usage
- 必填變數 / Variables: {{blooms-levels}}、{{difficulty-levels}}、{{number-of-questions}}、{{question-types}}、{{unit-and-subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Formative Assessment Question Generator is a free AI prompt that creates targeted assessment questions for…
