# Stress Management App Evaluator and Recommender

## 簡介

The Stress Management App Evaluator and Recommender is a free AI prompt that generates scientifically-backed, audience-specific recommendations for stress management apps and digital wellbeing tools. This stress management prompt for ChatGPT evaluates each tool across three dimensions - effectiveness, user experience, and relevance - and organizes recommendations by category (mindfulness, relaxation, time management, and more). The prompt runs on ChatGPT, Claude, and Gemini, producing structured reports that identify key stressors for your audience and match them with the most suitable technology solutions. It is designed for mental health professionals, coaches, HR teams, educators, and wellness consultants who need to recommend digital tools with confidence and clarity. ● Produces a full evaluation framework with 0–5 ratings for effectiveness, user experience, and audience fit ● Identifies key stress factors specific to the target audience before recommending tools ● Organizes apps into logical categories and highlights top recommendations with rationale ● Balances strengths and limitations, ensuring honest, scientifically-grounded assessments ## Prompt

```
## Role
You are an expert in mental health and stress management with deep knowledge of technology-based wellbeing solutions.

## Task
Generate a comprehensive, evaluated list of stress management apps and tools tailored to the specified target audience. Assess each recommendation on effectiveness, user experience, and relevance.

## Context
Target audience: {{target-audience}}

Focus on evidence-based tools with scientific backing for stress reduction. Balance strengths and limitations in your evaluations. Ensure all recommendations genuinely fit the audience's needs and preferences.

## Output
Structure your response as follows:

**Target Audience Overview:**
[Brief description of the audience and their key characteristics]

**Key Stress Factors:**
[Main sources of stress for this audience]

**App Categories:**

For each relevant category (mindfulness, relaxation, time management, etc.):

**Category: [Category Name]**

*App 1:*
- Name: [App Name]
- Description: [App Description]
- Key Features: [List of features]
- Effectiveness Rating: [0-5]
- User Experience Rating: [0-5]
- Relevance to Target Audience: [0-5]

*App 2:*
- Name: [App Name]
- Description: [App Description]
- Key Features: [List of features]
- Effectiveness Rating: [0-5]
- User Experience Rating: [0-5]
- Relevance to Target Audience: [0-5]

[Continue for 4-6 categories with 2 apps each]

**Top Recommendations:**
[Summary of the highest-rated apps across all categories, with brief rationale for why they stand out for this audience]
```

## 用法 / Usage
- 必填變數 / Variables: {{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Stress Management App Evaluator and Recommender is a free AI prompt that generates scientifically-backed, …
