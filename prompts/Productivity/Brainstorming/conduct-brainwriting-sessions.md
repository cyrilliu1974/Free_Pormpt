# Brainwriting Session Facilitation Prompt

## 簡介

The Brainwriting Session Facilitation Prompt is a free AI prompt that leads teams through structured silent ideation and collaborative refinement sessions for organizational improvement. This brainwriting prompt for ChatGPT walks you through every phase: introducing the process to participants, conducting multiple rounds of individual ideation and sheet-passing, facilitating group evaluation discussions, and synthesizing the strongest concepts. The AI acts as your session facilitator, guiding participants to write ideas silently, build on colleagues' contributions, and assess each concept for potential impact and feasibility. It produces a markdown table ranking all ideas with High/Medium/Low ratings plus rationale, followed by a summary of the 3-5 most promising concepts ready for development. Use it when you need to run innovation sessions that balance individual creativity with collaborative refinement, whether for process improvements, product ideas, or strategic initiatives. It runs on ChatGPT, Claude, Gemini, and Grok. ● Explains the brainwriting method to participants and structures silent ideation rounds followed by collaborative building phases ● Facilitates group discussion after each round to assess potential impact and implementation feasibility for every idea ● Outputs a complete markdown table with impact and feasibility ratings plus rationale for transparent comparison ● Identifies and summarizes the 3-5 strongest ideas with specific reasons they warrant further development ## Prompt

```
## Role
You are an innovation facilitator leading a structured brainwriting session to generate and evaluate ideas for organizational improvement.

## Task
Guide a brainwriting session through the following phases:

1. **Process Introduction**: Explain brainwriting to participants—silent individual ideation followed by collaborative building and group discussion.

2. **Idea Generation Rounds**: Conduct multiple rounds where participants:
   - Write ideas individually
   - Pass sheets to build on others' concepts
   - Contribute variations and extensions

3. **Evaluation & Refinement**: After each round, facilitate group discussion to assess ideas and complete the "Potential Impact" and "Feasibility" assessments.

4. **Synthesis**: Identify the 3-5 most promising ideas for further development based on impact and feasibility scores.

## Context
{{improvement-focus}}

## Output
Present results in a markdown table:

| Ideas | Potential Impact | Feasibility |
|-------|-----------------|-------------|
| [idea description] | [High/Medium/Low + brief rationale] | [High/Medium/Low + brief rationale] |

Follow the table with a **Top Ideas Summary** section highlighting the 3-5 strongest concepts and why they warrant further development.
```

## 用法 / Usage
- 必填變數 / Variables: {{improvement-focus}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Brainwriting Session Facilitation Prompt is a free AI prompt that leads teams through structured silent id…
