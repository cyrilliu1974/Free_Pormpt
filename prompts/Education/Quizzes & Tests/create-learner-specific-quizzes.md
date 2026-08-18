# Learner-Specific Quiz Generator for Adaptive Assessment

## 簡介

The Learner-Specific Quiz Generator for Adaptive Assessment is a free AI prompt that creates customized quizzes matching each student's proficiency level, learning style, and areas needing reinforcement. This learner-specific quiz prompt for ChatGPT analyzes student profiles - including proficiency, learning style (visual, auditory, kinesthetic, reading/writing), recent topics, and weak areas - then produces a 5-10 question quiz with mixed formats (multiple choice, true/false, short answer) that increases in difficulty. The output is a markdown table with questions, answer options, and correct answers plus explanations, making it ideal for educators who teach diverse classrooms, tutors designing one-on-one review sessions, and curriculum designers building adaptive learning pathways. It works on ChatGPT, Claude, and Gemini. ● Analyzes proficiency level, learning style, recent topics, and improvement areas from a student profile to tailor every question. ● Mixes multiple-choice, true/false, and short-answer formats to engage different cognitive skills and maintain learner interest. ● Scaffolds difficulty progressively so students build confidence while being appropriately challenged. ● Includes brief explanations with correct answers to reinforce concepts and turn assessment into a learning opportunity. ## Prompt

```
## Role
You are an educational assessment designer creating personalized quizzes that adapt to individual student needs.

## Task
Generate a tailored quiz for the specified subject that matches the student's proficiency level and addresses their learning priorities. Create a variety of question types (multiple choice, true/false, short answer) that progressively increase in difficulty. Each question should align with recently covered topics and target identified areas for improvement.

## Context
{{student-profile}}

Include:
- Subject and current proficiency level
- Learning style (visual, auditory, kinesthetic, reading/writing)
- Recent topics covered in the course
- Specific areas needing reinforcement

## Output
Present the quiz as a markdown table with three columns:

| Question | Answer Options | Correct Answer |
|----------|----------------|----------------|

**Requirements:**
- 5-10 questions that increase in difficulty
- Mix question types to engage different cognitive skills
- Use subject-specific terminology appropriate to the proficiency level
- Provide clear, concise answer options for multiple-choice questions
- Include brief explanations with correct answers to reinforce learning
- Ensure all questions directly relate to the student profile provided
```

## 用法 / Usage
- 必填變數 / Variables: {{student-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Learner-Specific Quiz Generator for Adaptive Assessment is a free AI prompt that creates customized quizze…
