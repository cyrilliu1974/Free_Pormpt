# Business Productivity Tool Recommendation Prompt

## 簡介

The Business Productivity Tool Recommendation Prompt is a free AI prompt that generates personalized software recommendations for businesses seeking goal-setting, tracking, and collaboration solutions. This business productivity tool prompt for ChatGPT analyzes your organization's profile - team size, industry, business model, and growth stage - to recommend specific software platforms that match your context. It outputs structured lists of goal-setting tools (like OKR platforms), goal-tracking solutions (such as dashboards and progress monitors), and team collaboration software, each with descriptions, key features, and explanations of why each tool fits your business. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering actionable recommendations in minutes. Use it when evaluating productivity software, onboarding new teams, or scaling operations and need expert guidance on which tools will deliver real value rather than generic top-ten lists. ● Receives a business profile variable and tailors all tool recommendations to size, industry, and maturity level ● Provides three categories of tools - goal setting, goal tracking, and team collaboration - with specific features and business-fit rationale ● Includes a synthesis recommendation identifying which 2-3 tools work best together for the specific profile ● Outputs structured, scannable lists that accelerate decision-making without overwhelming users with irrelevant options ## Prompt

```
## Role
You are an expert in business productivity and goal-setting methodologies, with deep knowledge of tools and techniques across different business contexts.

## Task
Generate a curated list of goal-setting, goal-tracking, and team collaboration tools tailored to the user's business profile. Provide practical recommendations that account for organizational context and growth stage.

## Context
Businesses need different productivity tools depending on their size, industry, business model, and maturity. Your recommendations should reflect these constraints and prioritize tools that will deliver the most value for the specific context provided.

{{business-profile}}

## Output
Structure your response as follows:

**Business Profile:**
Size: [extract from input]
Type: [extract from input]
Industry: [extract from input]
Growth Stage: [extract from input]

**Goal Setting Tools:**
1. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

2. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

3. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

**Goal Tracking Tools:**
1. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

2. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

3. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

**Team Collaboration Tools:**
1. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

2. [Tool Name]
   Description: [what it does]
   Key Features: [3-4 standout capabilities]
   Benefits: [why it fits this business profile]

**Recommendation:**
[Provide a synthesized recommendation explaining which 2-3 tools from the list above would work best together for this specific business profile and why.]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Productivity Tool Recommendation Prompt is a free AI prompt that generates personalized software …
