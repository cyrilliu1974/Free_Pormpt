# Design Support Quality Scorecards

## 簡介

The Design Support Quality Scorecards prompt is a free AI prompt that builds evaluation frameworks for customer support teams using observable behaviors, consistent scoring criteria, and development-focused feedback structures. This support quality scorecard prompt for ChatGPT guides you through designing a 5-7 category evaluation framework with behavioral anchors for each score level (1, 3, and 5), weighted percentages that reflect business priorities, a red flags list for automatic disqualifiers, and a coaching template under 150 words that balances recognition with actionable improvement. It runs on ChatGPT, Claude, Gemini, and Grok and delivers scorecards reviewers can complete in under five minutes while maintaining inter-rater reliability within one point. Use it when you need to transform subjective quality assessment into consistent performance data that reveals patterns and drives agent development rather than punitive evaluation. ● Creates 5-7 scoring categories with concrete behavioral anchors at each performance level so two reviewers score the same conversation consistently ● Defines weighted percentages based on business impact and explains why certain categories matter more than others ● Generates a red flags list of 5-8 automatic disqualifiers representing genuine risk like customer harm, reputation damage, or compliance violations ● Includes a fill-in-the-blank coaching template under 150 words with sections for strengths, one focused improvement area, and a specific action for the next conversation ## Prompt

```
## Role
You are a support quality architect building evaluation frameworks that develop agents rather than punish them. You design scorecards that transform subjective judgment into consistent, actionable performance data using observable behaviors and clear scoring anchors.

## Task
Create a Support Quality Scorecard that reveals performance patterns, guides coaching conversations, and takes under 5 minutes per conversation to complete.

Before building the scorecard, analyze:
1. What differentiates excellent support from mediocre support in this specific context
2. Which behaviors capture both technical accuracy and human connection
3. How to define scoring so two reviewers score the same conversation within one point
4. Which categories deserve more weight based on business impact
5. Which failures are catastrophic versus normal variation
6. How scores translate into growth conversations

## Context
{{business-context}}

## Output
Deliver three components:

### 1. Scoring Categories Table
Create 5-7 categories in a table with columns:
- Category Name
- Definition (one sentence, observable behaviors only)
- Score 1 Description (what reviewer sees in conversation)
- Score 3 Description (competent performance)
- Score 5 Description (excellent performance, not perfect)
- Weight (percentage reflecting business priority)

Include final row showing weighted overall score calculation.

**Requirements:**
- Define categories using concrete behaviors, not abstract qualities ("acknowledged customer's frustration before explaining solution" not "showed professionalism")
- Score gaps represent competent vs. excellent, not acceptable vs. perfect
- Weights reflect business priorities; explain why certain categories matter more
- Span both technical execution (accuracy, completeness, efficiency) and human connection (empathy, clarity, tone)

### 2. Red Flags List
5-8 automatic disqualifiers as numbered list. Each red flag:
- One clear sentence specifying what triggers it
- Represents genuine risk: customer harm, reputation damage, compliance violation
- Specific enough for reviewers to identify without ambiguity
- Overrides overall score and demands immediate intervention

Do not include minor issues.

### 3. Coaching Template
Fill-in-the-blank template under 150 words with three sections:
- **What [Agent Name] did well:** [placeholder for specific strengths with conversation examples]
- **One area to develop:** [placeholder for single focused improvement]
- **Specific action for next conversation:** [placeholder for concrete behavior to practice]

Template must balance recognition with development and translate scores into immediately applicable actions.

**System-wide requirements:**
- Two reviewers score same conversation within one point of each other
- Complete scoring in under 5 minutes
- Reveal patterns across multiple conversations
- Generate feedback agents can immediately apply
- Capture strengths so coaching starts with recognition
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Design Support Quality Scorecards prompt is a free AI prompt that builds evaluation frameworks for custome…
