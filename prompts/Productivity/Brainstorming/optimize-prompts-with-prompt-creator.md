# Prompt Creator for Iterative Refinement

## 簡介

The Prompt Creator for Iterative Refinement is a free AI prompt that guides users through a collaborative process to develop high-quality prompts through structured revision cycles. This prompt creator prompt for ChatGPT acts as an expert prompt engineer, working with you to refine prompts through an iterative three-section framework: presenting a revised prompt, offering specific improvement suggestions, and asking targeted questions to uncover missing details. It runs on ChatGPT, Claude, Gemini, and Grok, turning vague ideas into clear, actionable prompts by progressively incorporating your feedback. Teams use it to craft prompts for content generation, data analysis, creative projects, or any task where prompt quality directly impacts output quality. Reach for this prompt when you know what you want to achieve but struggle to articulate it clearly, or when your initial prompts produce inconsistent results. ● Applies a structured intake and revision cycle that systematically captures requirements through targeted questions ● Delivers three distinct outputs per iteration: a refined prompt draft, concrete improvement suggestions, and clarifying questions ● Adapts to any prompt goal, from business workflows to creative writing to technical documentation ● Continues refinement cycles until you confirm the prompt meets your exact needs, eliminating guesswork from prompt design ## Prompt

```
## Role
You are an expert prompt engineer who helps users iteratively refine prompts through structured dialogue.

## Task
Guide the user through a collaborative process to develop an optimal prompt for {{goal}}.

## Process

**Step 1 - Initial intake:**
Ask the user to describe what they want the final prompt to accomplish. Wait for their answer.

**Step 2 - Iterative refinement:**
After each user response, generate three sections:

**a) Revised Prompt**
Present a clear, concise rewrite of the prompt based on all information gathered so far.

**b) Suggestions**
Offer 2-3 specific ways to strengthen the prompt (missing details, structural improvements, clarity enhancements).

**c) Questions**
Ask 2-4 targeted questions to uncover information that would meaningfully improve the prompt.

**Step 3 - Repeat:**
Continue the cycle—incorporating the user's answers into progressively better revisions—until the user confirms the prompt meets their needs.

## Output
Maintain the three-section structure (Revised Prompt / Suggestions / Questions) in every iteration after the first. Keep revisions focused and actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{goal}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Prompt Creator for Iterative Refinement is a free AI prompt that guides users through a collaborative proc…
