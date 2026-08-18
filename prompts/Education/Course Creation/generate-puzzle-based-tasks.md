# Puzzle-Based Learning Tasks Generator

## 簡介

The Puzzle-Based Learning Tasks Generator is a free AI prompt that produces structured sets of interactive educational puzzles tailored to any subject and learner demographic. This puzzle-based learning prompt for ChatGPT takes your subject matter and target audience, then outputs 5–8 distinct puzzle tasks in a customizable markdown table. Each task pairs a specific puzzle type (logic grids, riddles, pattern recognition, spatial challenges, word problems) with a learning objective, difficulty level, and optional columns for estimated time or success criteria. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for course designers, educators, and instructional designers who need structured, cognitively engaging activities that reinforce concepts through problem-solving rather than passive review. Reach for this prompt when you want to map learning goals to proven puzzle mechanics quickly, ensuring every task challenges learners without overwhelming them and promotes active critical thinking. ● Analyzes subject matter to identify core learning objectives and selects puzzle types that naturally reinforce those concepts. ● Outputs a markdown table with configurable columns (puzzle type, learning objective, difficulty level, estimated time, success criteria). ● Scales difficulty to match audience capabilities, from elementary learners to adult professionals. ● Produces 5–8 distinct, implementable puzzle tasks per generation, ready for immediate classroom or course use. ## Prompt

```
## Role
You are an expert educational game designer specializing in puzzle-based learning experiences.

## Task
Generate a structured set of interactive puzzle tasks that combine entertainment and education. Each task should:
- Challenge learners appropriately while remaining achievable
- Promote critical thinking and problem-solving
- Reinforce key concepts through active engagement

## Context
Subject matter: {{subject}}
Target audience: {{target-audience}}

Analyze the subject to identify core learning objectives, then select puzzle types (riddles, logic grids, pattern recognition, word problems, spatial challenges, etc.) that naturally reinforce those objectives. Match difficulty levels to your audience's capabilities.

## Output
Provide a markdown table with {{number-of-columns}} columns. Include at minimum:
- **Puzzle Type** (the format or mechanic)
- **Learning Objective** (the specific skill or concept reinforced)
- **Difficulty Level** (beginner / intermediate / advanced, or scaled to your audience)

Add any additional columns the count permits (e.g., estimated time, materials needed, success criteria).

Present 5–8 distinct puzzle tasks in the table.
```

## 用法 / Usage
- 必填變數 / Variables: {{number-of-columns}}、{{subject}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Puzzle-Based Learning Tasks Generator is a free AI prompt that produces structured sets of interactive edu…
