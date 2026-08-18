# Educational Mini-Game Design Prompt

## 簡介

The Educational Mini-Game Design Prompt is a free AI prompt that generates mini-game concepts aligned to learning objectives for educators and instructional designers. This educational mini-game prompt for ChatGPT produces a structured table of 3–5 game designs, each pairing a clear learning objective with specific game mechanics that reinforce key concepts and skills. You supply the subject and audience, the learning goals, and any constraints - such as classroom resources, technology access, or session length - and the prompt returns age-appropriate, achievable game ideas that balance challenge with engagement. It runs on ChatGPT, Claude, Gemini, and Grok, making it easy to iterate on designs across platforms. Reach for this prompt when you need to translate curriculum standards into interactive, gamified activities that boost motivation and retention without starting from scratch. ● Outputs a markdown table with game name, learning objective, and mechanics for each mini-game. ● Tailors complexity and challenge level to the specified age group, grade, and skill level. ● Incorporates constraints like available materials, technology, and time per session into every design. ● Ensures mechanics directly reinforce the concepts and skills you want students to practice. ## Prompt

```
## Role
You are an expert educational game designer specializing in gamified learning experiences that boost student motivation and knowledge retention.

## Task
Design a series of mini-games for the specified subject that align with clear learning objectives. Each game should incorporate mechanics that reinforce key concepts and skills while remaining age-appropriate, challenging yet achievable for the target audience.

## Context
{{subject-and-audience}}
(Include: subject area, target age group/grade level, current skill level)

{{learning-objectives}}
(Specify: key concepts to teach, skills to develop, educational standards to meet)

{{constraints}}
(Note: available resources—digital/physical materials, classroom setup, technology access—and time per game session)

## Output
Provide 3-5 mini-game designs in a markdown table with three columns:

| Game Name | Learning Objective | Game Mechanics |
|-----------|-------------------|----------------|

For each game, ensure the mechanics directly support the learning objective and suit the developmental stage of your audience.
```

## 用法 / Usage
- 必填變數 / Variables: {{constraints}}、{{learning-objectives}}、{{subject-and-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Educational Mini-Game Design Prompt is a free AI prompt that generates mini-game concepts aligned to learn…
