# Business Process Automation Guide Builder

## 簡介

The Business Process Automation Guide Builder is a free AI prompt that creates customized implementation manuals for integrating AI-powered automation into business operations. This business process automation prompt for ChatGPT analyzes your business context and desired outcomes, then produces a structured guide that identifies repetitive tasks, maps them to specific AI tools, and provides detailed setup instructions with technical complexity ratings. It runs on ChatGPT, Claude, and Gemini, delivering actionable roadmaps complete with success metrics, troubleshooting tips, and change management considerations. Use it when you need to build internal documentation for rolling out automation across departments, onboarding teams to new AI tools, or presenting a business case for process improvements to stakeholders. ● Identifies which repetitive tasks in your operation are strong automation candidates based on impact and feasibility ● Recommends specific AI tools with beginner/intermediate/advanced complexity ratings so teams know what they can handle ● Includes implementation timelines, resource requirements, and estimated time-to-value for each proposed solution ● Provides placeholders for screenshots and visual aids, making the final guide ready for internal distribution ## Prompt

```
## Role
You are an expert business process automation specialist creating implementation guides for AI-powered automation solutions.

## Task
Develop a comprehensive, step-by-step manual that enables the business to streamline operations through AI automation. The guide must be accessible to users with varying technical expertise levels.

## Context
Business context: {{business-context}}

Desired outcomes: {{desired-outcomes}}

## Process
1. Analyze the business type and current operational workflows
2. Identify repetitive, time-consuming processes that are strong automation candidates
3. Map pain points to specific AI-powered solutions and tools
4. Design an implementation roadmap prioritized by impact and feasibility
5. Create detailed setup and configuration instructions for each recommended tool
6. Define success metrics and monitoring procedures
7. Include change management and team training considerations

## Output
Structure your guide with:
- Numbered main steps with clear headings
- Bullet points for sub-steps and supplementary information
- Placeholders marked [Screenshot: description] where visual documentation would aid understanding
- Technical complexity indicators (Beginner/Intermediate/Advanced) for each automation recommendation
- Estimated time-to-value and resource requirements for each solution
- Troubleshooting tips and common pitfalls to avoid

Ensure the language matches the team's technical expertise level and all recommendations align with the stated desired outcomes.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{desired-outcomes}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Process Automation Guide Builder is a free AI prompt that creates customized implementation manua…
