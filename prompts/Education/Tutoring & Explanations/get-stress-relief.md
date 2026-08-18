# Student Stress Management Guide Builder

## 簡介

The Student Stress Management Guide Builder is a free AI prompt that creates tailored stress management tables for students facing academic pressures. This student stress management prompt for ChatGPT takes a student's educational level, main stressors, learning preferences, and available resources, then outputs a structured markdown table pairing 8-12 common academic challenges - exam anxiety, workload overload, time management, social pressures, performance expectations - with actionable coping techniques and specific support resources. Developed for educational psychologists, academic advisors, school counselors, and student success coordinators, it runs on ChatGPT, Claude, and Gemini to deliver vocabulary and examples matched to each learner's context. The prompt ensures every strategy is practical, evidence-based, and immediately implementable, whether the student is in high school, college, or graduate study. ● Maps each academic stressor to 2-3 concrete, evidence-based coping techniques the student can try immediately. ● Suggests specific resources - campus counseling, mental health apps, study technique guides, peer support networks - tailored to the student's environment. ● Adapts language, examples, and strategies to match educational level and learning preferences. ● Covers workload management, exam anxiety, time constraints, social challenges, performance pressure, and resource limitations in a single table. ## Prompt

```
## Role
You are an educational psychologist specializing in student well-being and academic performance.

## Task
Create a comprehensive stress management guide tailored to the student's academic context. Identify key academic stressors, provide evidence-based coping strategies, and recommend practical support resources.

## Context
Student profile:
- Educational level and main stressors: {{student-profile}}
- Learning preferences and available resources: {{support-context}}

Address common academic pressures including workload management, exam anxiety, time constraints, social challenges, performance expectations, and resource limitations. Ensure strategies are practical and accessible across different academic settings.

## Output
Deliver your guide as a markdown table with three columns:

| Stressor | Coping Strategy | Resources |
|----------|----------------|------------|

Include 8-12 rows covering both the student's specific stressors and other common academic pressures. For each:
- **Stressor**: Name the challenge clearly
- **Coping Strategy**: Provide 2-3 actionable, evidence-based techniques the student can implement immediately
- **Resources**: List specific tools, services, or references (campus counseling, apps, techniques, websites)

Tailor vocabulary and examples to the student's educational level. Prioritize strategies compatible with their learning style and available resources.
```

## 用法 / Usage
- 必填變數 / Variables: {{student-profile}}、{{support-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Student Stress Management Guide Builder is a free AI prompt that creates tailored stress management tables…
