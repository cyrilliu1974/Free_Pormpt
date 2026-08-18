# Goal Achievement Post-Mortem Analysis Prompt

## 簡介

The Goal Achievement Post-Mortem Analysis Prompt is a free AI prompt that conducts systematic reviews of completed goals to extract actionable insights for strategic planning and execution. This goal achievement analysis prompt for ChatGPT walks through a seven-part framework: restating the goal, determining achievement status (achieved, partial, or not achieved), listing the top three success factors and failure factors, conducting root cause analysis with detailed explanations, documenting lessons learned, generating actionable recommendations, and outlining considerations for future goal-setting. It works with ChatGPT, Claude, Gemini, and Grok by prompting the model to act as a strategic analyst and evaluate any business, project, or personal objective you describe. Use it after completing a product launch, finishing a quarter, ending a project sprint, or whenever you need evidence-based insights on what drove outcomes. ● Determines achievement status and isolates the top three success and failure factors for clarity ● Performs root cause analysis with detailed explanations grounded in evidence, not speculation ● Delivers practical lessons learned and actionable recommendations specific to the goal context ● Provides future goal-setting considerations to refine planning and execution strategies ## Prompt

```
## Role
You are a strategic goal achievement analyst conducting a post-mortem analysis to identify success factors, failure points, and actionable lessons learned.

## Task
Analyze the goal described below. Determine whether it was achieved, identify the critical factors that influenced the outcome, conduct root cause analysis, and provide recommendations to improve future goal-setting and execution.

## Context
Goal to analyze: {{goal-description}}

## Output
Deliver your analysis in the following structure:

**Goal Description:**
[Restate the goal clearly and concisely]

**Achievement Status:**
[State whether the goal was achieved, partially achieved, or not achieved]

**Success Factors:**
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

**Failure Factors:**
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

**Root Cause Analysis:**
[Root cause 1]: [Detailed explanation]
[Root cause 2]: [Detailed explanation]
[Root cause 3]: [Detailed explanation]

**Lessons Learned:**
1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

**Recommendations:**
1. [Actionable recommendation 1]
2. [Actionable recommendation 2]
3. [Actionable recommendation 3]

**Future Goal Setting Considerations:**
[Key insights and considerations for setting future goals based on this analysis]

---

**Analysis Criteria:**
- Focus on the most critical factors that directly impacted the outcome
- Base root cause analysis on evidence and data, not speculation
- Ensure lessons learned and recommendations are practical and actionable
- Identify top three items for each category to maintain focus and clarity
```

## 用法 / Usage
- 必填變數 / Variables: {{goal-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Goal Achievement Post-Mortem Analysis Prompt is a free AI prompt that conducts systematic reviews of compl…
