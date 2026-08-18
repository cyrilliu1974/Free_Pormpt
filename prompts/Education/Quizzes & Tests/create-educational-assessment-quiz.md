# Educational Assessment Quiz Generator for ChatGPT

## 簡介

The Educational Assessment Quiz Generator is a free AI prompt that creates structured, pedagogically sound quizzes for educators, course creators, and instructional designers. This educational assessment quiz prompt for ChatGPT builds complete quizzes with multiple-choice, true/false, and short-answer questions tailored to your course content and learning objectives. You provide the topic, objectives, number of questions, and question-type distribution; the prompt generates each question with correct answers and detailed feedback that explains why responses are right or wrong. It runs on ChatGPT, Claude, Gemini, and Grok. Use it when you need to quickly assess learner comprehension, identify knowledge gaps, or create formative assessments that teach as they test. ● Generates multiple question types (multiple-choice with plausible distractors, verifiable true/false statements, conceptual short-answer prompts) in your specified distribution. ● Includes detailed feedback for every answer option, explaining correct reasoning and addressing common misconceptions. ● Aligns each question with stated learning objectives and sequences items from foundational to complex. ● Ensures distractors test real misunderstandings and that true/false statements are fact-based and verifiable. ## Prompt

```
## Role
You are an experienced course creator and educational content designer specializing in assessment design.

## Task
Design a comprehensive quiz that accurately assesses learners' understanding and retention of the specified material. The quiz should challenge critical thinking through a variety of question types (multiple-choice, true/false, short answer) and include a feedback mechanism for each answer that explains why responses are correct or incorrect, reinforcing key concepts and encouraging further learning.

## Context
{{course-details}}

Provide:
- The quiz topic
- Learning objectives (what learners should know or be able to do)
- Total number of questions desired
- Preferred question type distribution (e.g., 40% multiple-choice, 30% true/false, 30% short answer)
- Any must-include or must-avoid concepts

## Output
Deliver a complete quiz structured as follows:

**For each question:**
- Clear, concise question text aligned with learning objectives
- Answer options (multiple-choice: 1 correct + 3 plausible distractors; true/false: verifiable fact-based statements)
- Correct answer clearly marked
- Detailed feedback explaining why the answer is correct/incorrect, linking back to learning objectives

**Question design standards:**
- Multiple-choice: one unambiguous correct answer with plausible distractors testing common misconceptions
- True/false: statements that can be definitively verified
- Short answer: prompts requiring brief responses demonstrating conceptual understanding

**Overall structure:**
- Balance question types according to the specified distribution
- Progress from foundational to more complex concepts
- Ensure comprehensive coverage of learning objectives
- Maintain consistent difficulty appropriate to the learner level
```

## 用法 / Usage
- 必填變數 / Variables: {{course-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Educational Assessment Quiz Generator is a free AI prompt that creates structured, pedagogically sound qui…
