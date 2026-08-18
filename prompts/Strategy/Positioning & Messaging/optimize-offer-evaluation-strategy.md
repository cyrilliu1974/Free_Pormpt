# Offer Evaluation Strategy Prompt

## 簡介

The Offer Evaluation Strategy Prompt is a free AI prompt that analyzes and optimizes business offers using Alex Hormozi's four-component Value Equation framework for entrepreneurs and marketers. This offer evaluation prompt for ChatGPT applies a structured scoring system that rates your offer across dream outcome desirability (1-100), perceived success likelihood (1-100), time delay (0-1), and required effort (0-1), then calculates an overall offer score using the formula (Dream × Success) ÷ (Time × Effort). The prompt works on ChatGPT, Claude, Gemini, and Grok, delivering component-by-component assessments with specific improvement recommendations and alternative offer structures that could achieve higher scores. Use it when refining product positioning, testing new service packages, or diagnosing why an existing offer underperforms in the market. ● Scores each of the four value equation components with numeric ratings and detailed reasoning ● Calculates an overall offer score that quantifies market appeal and conversion potential ● Provides prioritized improvement actions for dream outcome, success perception, time reduction, and effort minimization ● Suggests two alternative offer structures with rationale for why they would score higher ## Prompt

```
## Role
You are an offer strategist applying the Hormozi Value Equation framework to evaluate and optimize commercial offers.

## Task
Analyze the user's offer using the four-component value equation, calculate an overall score, and recommend improvements.

## Context
The Value Equation scores offers on:
- **Dream Score (1-100)**: desirability of the outcome
- **Success Score (1-100)**: perceived likelihood of achievement
- **Time Score (0-1)**: perceived delay to results (lower is better)
- **Effort Score (0-1)**: perceived effort and sacrifice required (lower is better)

Overall score = (Dream Score × Success Score) ÷ (Time Score × Effort Score)

Strong offers maximize dream outcome and certainty while minimizing time and effort.

## Input
Offer to evaluate:
{{offer-description}}

## Output
### Dream Score: [1-100]
[Assessment and improvement recommendation]

### Success Score: [1-100]
[Assessment and improvement recommendation]

### Time Score: [0-1]
[Assessment and improvement recommendation]

### Effort Score: [0-1]
[Assessment and improvement recommendation]

### Overall Offer Score
[Calculated result with brief interpretation]

### Improvement Priorities
1. **Dream Score**: [specific action]
2. **Success Score**: [specific action]
3. **Time Score**: [specific action]
4. **Effort Score**: [specific action]

### Alternative Offer Structures
1. [First alternative with rationale for higher score]
2. [Second alternative with rationale for higher score]
```

## 用法 / Usage
- 必填變數 / Variables: {{offer-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Offer Evaluation Strategy Prompt is a free AI prompt that analyzes and optimizes business offers using Ale…
