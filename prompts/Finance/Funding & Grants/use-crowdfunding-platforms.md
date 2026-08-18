# Crowdfunding Platform Comparison Prompt

## 簡介

The Crowdfunding Platform Comparison Prompt is a free AI prompt that researches and compares the three major crowdfunding platforms to help entrepreneurs choose the right funding option for their venture. This crowdfunding platform prompt for ChatGPT analyzes Kickstarter, Indiegogo, and GoFundMe across fee structures, funding models (all-or-nothing versus flexible), audience reach, success rates, and category fit. It produces a structured markdown table comparing key features, costs, and support resources, followed by a tailored recommendation based on your specific business context, funding goals, and target audience. Use it when you need to evaluate which platform offers the best visibility, backer engagement, and terms for your product launch, creative project, or startup campaign. It runs on ChatGPT, Claude, Gemini, and Grok. ● Compares platform fee structures and payment processing costs to identify the most cost-effective option for your budget. ● Evaluates all-or-nothing versus flexible funding models to match your project's risk tolerance and timeline. ● Assesses audience demographics, category strengths, and geographic availability to maximize backer reach. ● Provides a context-specific recommendation that aligns platform strengths with your business type, funding goal, and campaign strategy. ## Prompt

```
## Role
You are an expert crowdfunding analyst specializing in platform comparison and selection strategy.

## Task
Research and compare Kickstarter, Indiegogo, and GoFundMe as funding options for a new business venture. Analyze each platform's key features, fee structures, audience reach, funding models (all-or-nothing vs. flexible), success rates, and suitability for different project types. Synthesize your findings into a clear, actionable comparison.

## Context
Business context: {{business-context}}

Consider how each platform's strengths align with the project's funding goal, timeline, target audience demographics, geographic restrictions, and project category. Evaluate practical factors like payment processing, platform visibility, backer community engagement, and post-campaign fulfillment support.

## Output
Present your analysis as a markdown table with three columns:
- **Platform Name** (Kickstarter, Indiegogo, GoFundMe)
- **Key Features** (funding model, audience type, project categories, geographic availability, support resources)
- **Fees** (platform fees, payment processing fees, any additional costs)

Below the table, provide a brief recommendation (2-3 sentences) on which platform best suits the specified business context and why.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Crowdfunding Platform Comparison Prompt is a free AI prompt that researches and compares the three major c…
