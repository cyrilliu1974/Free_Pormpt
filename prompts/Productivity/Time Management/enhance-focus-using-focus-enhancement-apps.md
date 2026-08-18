# Focus Enhancement App Recommendation Prompt

## 簡介

The Focus Enhancement App Recommendation Prompt is a free AI prompt that analyzes your work situation and recommends the best focus-enhancing applications tailored to your productivity challenges. This focus app recommendation prompt for ChatGPT takes your work context - including your tasks, environment, current distractions, device preferences, and experience level - and delivers 3-5 curated app suggestions in a structured table format. Each recommendation includes detailed features, measurable benefits, and concrete use cases so you can quickly identify which tools fit your workflow. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across all major text-generation models. Use it when you're struggling with distractions, transitioning to remote work, or looking to upgrade your productivity stack with apps that match your specific needs rather than generic lists. ● Analyzes your unique work context, challenges, and device preferences before recommending apps ● Delivers results in a comparison table with App Name, Features, Benefits, and Use Cases columns ● Covers 3-5 curated apps per request, filtering out noise and generic productivity advice ● Includes an introductory explanation of why focus tools matter for your specific situation ## Prompt

```
## Role
You are a productivity expert specializing in focus enhancement tools and distraction management.

## Task
Analyze the user's work context and recommend focus enhancement applications that match their specific needs. For each recommended app, provide a comprehensive overview covering key features, benefits, and use cases.

## Context
{{work-context}}

Include: the task or project you're working on, your work environment, current productivity challenges, preferred devices, and your experience level with productivity apps.

## Output
Begin with a brief introduction (2-3 sentences) explaining why focus enhancement apps are important for productivity in the user's specific situation.

Then present 3-5 recommended apps in a markdown table with these columns:

| App Name | Features | Benefits | Use Cases |
|----------|----------|----------|-----------|
```

## 用法 / Usage
- 必填變數 / Variables: {{work-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Focus Enhancement App Recommendation Prompt is a free AI prompt that analyzes your work situation and reco…
