# Assessment Criteria Generator for Educators

## 簡介

The Assessment Criteria Generator for Educators is a free AI prompt that creates structured, standards-aligned evaluation rubrics for teachers, instructional designers, and curriculum developers. This assessment criteria prompt for ChatGPT takes your subject, grade level, curriculum standards, learning objectives, and assessment type - then outputs a markdown table with criterion names, detailed descriptions for consistent scoring, and weightage percentages that total 100%. It works on ChatGPT, Claude, Gemini, and Grok, making it practical for formative quizzes, summative projects, performance tasks, written exams, and professional certifications. Teachers use it to ensure fair grading, align assessments with state or national standards, and communicate expectations clearly to students and peer evaluators. Reach for this prompt when you need to design a rubric quickly, maintain consistency across multiple graders, or verify that your assessment priorities match your instructional goals. ● Produces a markdown table with criteria, descriptions, and weightage columns that sum to exactly 100%. ● Aligns every criterion with the curriculum standards and learning objectives you specify. ● Adjusts grain-size and number of criteria to suit formative quizzes, summative projects, or performance tasks. ● Provides evaluator-friendly descriptions that support consistent, equitable scoring across raters. ## Prompt

```
## Role
You are an expert educational assessor specializing in the design of rigorous, fair, and standards-aligned evaluation metrics.

## Task
Create a comprehensive set of assessment criteria for the given subject and educational context. Ensure each criterion:
- Aligns directly with the provided curriculum standards and learning objectives
- Reflects appropriate emphasis through its assigned weightage
- Is clearly described so evaluators can apply it consistently

## Context
{{assessment-context}}

Include: subject, educational level (e.g., Grade 5, undergraduate, professional certification), curriculum standards or frameworks being addressed, specific learning objectives the assessment must measure, and the type of assessment (formative quiz, summative project, performance task, written exam, etc.).

## Output
Deliver your assessment criteria as a markdown table with exactly three columns:

| Criteria | Description | Weightage |
|----------|-------------|----------|
| [Criterion name] | [Clear explanation of what is being evaluated and how] | [%] |

Ensure:
- Weightage percentages sum to exactly 100%
- Higher weightages reflect the most critical learning outcomes
- Descriptions provide sufficient detail for consistent scoring
- The number and grain-size of criteria suit the assessment type
```

## 用法 / Usage
- 必填變數 / Variables: {{assessment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Assessment Criteria Generator for Educators is a free AI prompt that creates structured, standards-aligned…
