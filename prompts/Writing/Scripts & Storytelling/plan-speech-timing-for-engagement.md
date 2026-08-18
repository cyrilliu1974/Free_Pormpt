# Speech Timing and Outline Generator for ChatGPT

## 簡介

The Speech Timing and Outline Generator is a free AI prompt that creates time-constrained, persuasive speech outlines for speakers, presenters, and communicators who need to captivate specific audiences. This speech timing prompt for ChatGPT builds complete outlines organized by opening hooks, hierarchical main points with subpoints, supporting evidence, concrete examples, and powerful conclusions - all structured to fit your exact time limit. It applies dependency grammar principles to ensure logical flow, where each section builds naturally from the previous one and supporting details remain clearly subordinate to central claims. The prompt works across ChatGPT, Claude, and Gemini, adapting tone and content to match your target audience, from boardroom executives to community gatherings. Use it when you need to transform a core message into a persuasive speech framework that balances storytelling with structured argumentation. ● Generates opening hooks - questions, anecdotes, or statements - that immediately capture attention and set the stage for your key message ● Builds hierarchical main points with nested subpoints, evidence, and specific examples that maintain logical dependency relationships ● Embeds relatable stories and concrete details in each section to illustrate abstract concepts and keep audiences engaged ● Creates conclusions that reinforce the central message with memorable closing statements or clear calls to action, all timed to your constraint ## Prompt

```
## Role
You are an expert speechwriter specializing in structured, persuasive outlines.

## Task
Create a compelling speech outline that fits within the specified time constraint and captivates the target audience from opening to close.

## Context
**Topic:** {{topic}}
**Time limit:** {{time-limit}}
**Target audience:** {{target-audience}}
**Desired tone:** {{tone}}
**Key message:** {{key-message}}

Use dependency grammar principles to ensure each section flows logically from the previous one, with supporting points clearly subordinate to main claims.

## Output
Deliver the outline in this format:
- **I. Opening Hook** – An attention-grabbing statement, question, or anecdote that immediately engages the audience.
- **II. Main Point 1** 
  - A. Subpoint with supporting evidence or story 
  - B. Subpoint with supporting evidence or story 
    - 1. Specific detail or example 
    - 2. Specific detail or example
- **III. Main Point 2** (repeat structure)
- **IV. Main Point 3** (as needed for time limit)
- **V. Conclusion** – Reinforce the key message with a memorable closing statement or call to action.

Ensure each main point directly supports the key message, and include at least one relatable story or concrete example per section to illustrate abstract concepts.
```

## 用法 / Usage
- 必填變數 / Variables: {{key-message}}、{{target-audience}}、{{time-limit}}、{{tone}}、{{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Speech Timing and Outline Generator is a free AI prompt that creates time-constrained, persuasive speech o…
