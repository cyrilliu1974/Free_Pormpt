# Team Training Session Plan Builder

## 簡介

The Team Training Session Plan Builder is a free AI prompt that creates comprehensive, multi-session training curricula for L&D professionals and training coordinators. This team training prompt for ChatGPT produces a markdown table organizing your entire program: session titles, scheduling, and measurable objectives for each meeting. It sequences topics from foundational to advanced, balances cognitive load across sessions, and ensures continuity so later workshops reinforce earlier learning. Real use cases include onboarding programs, skills development initiatives, compliance training series, and technical upskilling tracks. The prompt runs on ChatGPT, Claude, Gemini, and Grok, requiring three variables: your training topic, program parameters (session count, duration, scheduling preferences), and the key improvement areas or competencies your team needs to develop. Reach for this prompt when you need to design a cohesive training series rather than one-off workshops, or when stakeholders require a clear roadmap of learning objectives and timelines. ● Sequences sessions logically from foundational concepts to advanced applications ● Defines measurable learning objectives for each training session ● Distributes topics evenly to prevent cognitive overload and maximize retention ● Builds continuity across the curriculum so each session reinforces prior learning ## Prompt

```
## Role
You are an expert training coordinator designing a multi-session training program.

## Task
Create a comprehensive training plan that enhances team skills and knowledge through a structured curriculum. Balance learning objectives, session pacing, and measurable outcomes across all sessions.

## Context
**Training topic:** {{training-topic}}

**Program parameters:** {{program-parameters}}
(Include: number of sessions, duration per session, scheduling preferences)

**Key areas for improvement:** {{improvement-areas}}
(List the priority skills, knowledge gaps, or competencies the team needs to develop)

## Approach
- Sequence sessions logically from foundational to advanced concepts
- Distribute topics evenly to avoid cognitive overload
- Define clear, measurable objectives for each session
- Build continuity so later sessions reinforce earlier learning

## Output
Deliver the training plan as a markdown table with these columns:

| Session Title | Date | Time | Key Objectives |
|--------------|------|------|----------------|

Each row represents one training session. Populate Date and Time fields with placeholder formats (e.g., "Week 1, Day 1" or "TBD") unless specific scheduling details are provided in the program parameters.
```

## 用法 / Usage
- 必填變數 / Variables: {{improvement-areas}}、{{program-parameters}}、{{training-topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Team Training Session Plan Builder is a free AI prompt that creates comprehensive, multi-session training …
