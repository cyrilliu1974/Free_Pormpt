# Personal Study Plan Generator for Any Subject

## 簡介

The Personal Study Plan Generator is a free AI prompt that creates customized, topic-by-topic study plans for any subject and learner profile. This study plan prompt for ChatGPT takes two inputs - the subject you want to learn and a description of the learner (age, skill level, learning style, goals) - and returns a full roadmap organized as a markdown table with study resources, practice activities, and assessment methods for each topic. The prompt works by analyzing the learner profile to match the plan to their needs, breaking the subject into logically sequenced topics that build from foundational to advanced concepts, and recommending diverse materials to keep engagement high. Educators use it to design semester plans, tutors use it for one-on-one clients, and self-directed learners use it to structure independent study. It runs on ChatGPT, Claude, and Gemini, delivering output in markdown table format with an introductory rationale. Reach for this prompt whenever you need a structured learning path but want it personalized rather than generic - whether you're planning for a student, a team training program, or your own skill development. ● Analyzes learner profile (age, skill level, learning preferences) to tailor topic selection and resource types ● Sequences topics from foundational to advanced, ensuring each builds on prior knowledge ● Suggests specific study resources, hands-on practice activities, and assessment methods for every topic ● Outputs a clean markdown table format with an introductory rationale explaining the plan's structure and approach ## Prompt

```
## Role
You are an expert educational consultant specializing in personalized study plans.

## Task
Design a comprehensive, tailored study plan that optimizes learning efficiency and effectiveness for the given subject and learner profile.

## Context
Subject: {{subject}}
Learner profile: {{learner-profile}}

Analyze the learning style and skill level to customize your approach. Break down the subject into manageable topics that build progressively on prior knowledge. Select appropriate study resources, practice activities, and assessment methods for each topic. Incorporate diverse learning materials to maintain engagement and address different aspects of the subject.

## Output
Provide a brief introduction (2-3 paragraphs) explaining the overall structure, approach, and rationale of the study plan.

Then present the plan as a markdown table:

| Topic | Study Resources | Practice Activities | Assessment Methods |
|-------|----------------|-------------------|-------------------|

Ensure the topics progress logically from foundational to advanced concepts.
```

## 用法 / Usage
- 必填變數 / Variables: {{learner-profile}}、{{subject}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personal Study Plan Generator is a free AI prompt that creates customized, topic-by-topic study plans for …
