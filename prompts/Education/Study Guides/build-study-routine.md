# Study Schedule Builder Prompt for ChatGPT

## 簡介

The Study Schedule Builder Prompt for ChatGPT is a free AI prompt that creates tailored study routines for students and educators seeking optimized learning plans. This study schedule prompt for ChatGPT analyzes five key inputs (subject, student profile, learning style, available study time, and academic goals) and outputs a structured markdown table with time blocks, activities, and durations. Each activity includes a justification explaining how it supports the student's learning style and goals. The prompt incorporates evidence-based study techniques, strategic breaks for retention, and time management principles. It runs on ChatGPT, Claude, Gemini, and Grok. Real use cases include educators designing routines for tutoring clients, students building exam prep plans, and parents creating homework schedules for children with different learning preferences. Use this prompt when you need a study plan that balances focused work periods with rest, addresses subject-specific requirements, and fits within real-world time constraints. ● Outputs a markdown table with time, activity, and duration columns for easy readability and scheduling. ● Includes written justifications below each activity explaining alignment with learning style and academic goals. ● Incorporates strategic break intervals and evidence-based study techniques like spaced repetition and active recall. ● Adapts to varied student profiles, subjects, and time constraints, from 30-minute daily sessions to multi-hour exam prep blocks. ## Prompt

```
## Role
You are an educational consultant specializing in personalized study design and learning optimization.

## Task
Create a tailored study schedule that maximizes learning efficiency and academic performance. Analyze learning preferences, balance focused work with rest periods, and apply evidence-based study techniques and time management principles.

## Context
**Subject:** {{subject}}
**Student profile:** {{student-profile}}
**Learning style:** {{learning-style}}
**Available study time:** {{available-study-time}}
**Academic goals:** {{goals}}

## Output
Deliver the study routine as a markdown table with three columns: **Time**, **Activity**, and **Duration**. Below each activity row, add a brief explanation justifying why that activity is included and how it supports the student's learning style and goals.

Ensure the schedule:
- Aligns with the stated learning style
- Addresses subject-specific requirements
- Incorporates strategic breaks for retention
- Fits within the available study time
- Progresses toward the academic goals
```

## 用法 / Usage
- 必填變數 / Variables: {{available-study-time}}、{{goals}}、{{learning-style}}、{{student-profile}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Study Schedule Builder Prompt for ChatGPT is a free AI prompt that creates tailored study routines for stu…
