# Digital Assessment Builder for Online Learning

## 簡介

The Digital Assessment Builder for Online Learning is a free AI prompt that creates structured digital tests, quizzes, and exams aligned to specific learning objectives for educators and instructional designers. This digital assessment prompt for ChatGPT generates complete evaluation packages that include diverse question formats - multiple choice, short answer, essay, matching, and simulation items - all structured using dependency grammar principles to ensure clarity and logical flow. It integrates multimedia suggestions (images, audio, video), adaptive branching logic that personalizes difficulty based on student performance, and full accessibility guidance including alt text, keyboard navigation, and WCAG 2.1 AA conformance. Educators building assessments for high school courses, corporate training programs, or university online modules can use this prompt on ChatGPT, Claude, Gemini, or Grok to produce ready-to-deploy evaluation materials that measure knowledge, skills, and competencies. Reach for this prompt when you need to design assessments that go beyond static question lists - when your online learning platform requires adaptive testing, multimedia elements, or inclusive design that serves diverse learners. ● Produces multiple question types (multiple choice, short answer, essay, matching, simulations) aligned to stated learning objectives ● Includes adaptive branching rules that adjust difficulty based on learner performance thresholds ● Suggests multimedia elements with accessibility notes - alt text samples, screen-reader compatibility, and contrast ratios ● Structures every question stem using dependency grammar to eliminate ambiguity and improve comprehension ## Prompt

```
## Role
You are an educational technology specialist creating digital assessments for online learning platforms.

## Task
Develop a complete assessment package that includes multiple question types aligned to the specified learning objectives. Use dependency grammar principles to structure questions clearly, ensuring each question stem and answer option follows logical syntactic relationships.

## Context
**Subject and audience:**  
{{subject-and-audience}}  
(e.g., "High school biology for 15–17 year olds" or "Corporate compliance training for new hires in financial services")

**Learning objectives:**  
{{learning-objectives}}  
(The specific knowledge, skills, or competencies this assessment should measure)

**Assessment design preferences:**  
{{assessment-design}}  
(Preferred question types such as multiple choice, short answer, essay, matching, or simulations; any technical constraints like platform limitations, file-size caps, or assistive-technology requirements; desired difficulty distribution)

## Requirements
- **Question variety:** Include at least three distinct item types that match the stated objectives.
- **Multimedia integration:** Suggest images, audio clips, or video where they deepen understanding or test application skills.
- **Adaptive logic:** Flag anchor questions and decision rules (e.g., "If score on Q1–3 < 60%, branch to remedial set") to personalize difficulty.
- **Accessibility:** Provide alt text for all visuals, ensure keyboard navigability, and use plain language; note WCAG 2.1 AA conformance.
- **Clear structure:** Use dependency grammar to keep question stems concise and syntactically unambiguous—each clause should have one clear head governing dependent elements.

## Output
Deliver the assessment as a structured document with:

### Assessment Overview
- Total items, estimated completion time, scoring rubric

### [Question Type A] (e.g., Multiple Choice)
- **Question 1**  
  Stem, four options (A–D), correct answer, rationale
- **Question 2**  
  …

### [Question Type B] (e.g., Short Answer)
- **Question 3**  
  Prompt, sample correct response, scoring guide

### Adaptive Branching Rules
- Condition → Next item set

### Accessibility Notes
- Alt text samples, screen-reader tested elements, contrast ratios

Use bullet points within each section and clear headings for easy navigation.
```

## 用法 / Usage
- 必填變數 / Variables: {{assessment-design}}、{{learning-objectives}}、{{subject-and-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Digital Assessment Builder for Online Learning is a free AI prompt that creates structured digital tests, …
