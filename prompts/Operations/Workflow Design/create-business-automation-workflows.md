# Business Automation Workflow Designer

## 簡介

The Business Automation Workflow Designer is a free AI prompt that analyzes business operations and creates detailed automation strategies for teams looking to reduce manual work and improve efficiency. This business automation prompt for ChatGPT walks through your operations, identifies the most time-consuming repetitive tasks, and builds complete workflows for each opportunity. For every automation candidate, it recommends practical tools like Zapier, Make.com, n8n, or custom scripts, then lays out step-by-step implementation instructions, estimates efficiency gains, and flags potential challenges with recommended solutions. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering a structured text report that covers current-state analysis, prioritized automation workflows, a phased rollout plan, and change-management strategies. Use it when you need to turn vague efficiency goals into concrete, executable automation projects. ● Identifies repetitive, high-impact tasks that are strong candidates for automation based on time savings and implementation effort. ● Recommends cost-effective, user-friendly tools and provides step-by-step configuration and deployment instructions for each workflow. ● Delivers a phased implementation strategy that balances quick wins with longer-term, multi-system integrations. ● Anticipates rollout challenges such as team adoption, integration compatibility, and data quality, then provides practical solutions for each. ## Prompt

```
## Role

You analyze business operations, identify automation opportunities, and design detailed workflow solutions that reduce manual effort and improve efficiency.

## Context

{{business-operations}}

## Task

1. Write a brief overview of the operations described above.
2. Identify the most repetitive and time-consuming tasks that are strong candidates for automation.
3. For each identified task, build a complete automation workflow covering:
   - The specific task being automated
   - The recommended tool (e.g., Zapier, Make.com, n8n, or custom scripts)
   - Step-by-step process for the automation
   - Estimated efficiency gains from implementing it
4. Outline a phased implementation strategy that is realistic and achievable.
5. List potential challenges that may arise during rollout.
6. Provide a practical solution for each challenge.

Prioritize tools that are user-friendly and cost-effective. Focus on automations that deliver the highest time savings relative to implementation effort.

## Output

**Current Business Operations Overview:**
[Overview of current business operations]

**Identified Repetitive Tasks:**
1. [First repetitive task]
2. [Second repetitive task]
3. [Third repetitive task]

---

**Automation Workflow 1:**
Task: [First repetitive task]
Tool: [Recommended automation tool]
Steps:
1. [Initial setup step]
2. [Configuration step]
3. [Testing and deployment step]
Expected Efficiency Gains: [Time/cost savings estimate]

**Automation Workflow 2:**
Task: [Second repetitive task]
Tool: [Recommended automation tool]
Steps:
1. [Initial setup step]
2. [Configuration step]
3. [Testing and deployment step]
Expected Efficiency Gains: [Time/cost savings estimate]

**Automation Workflow 3:**
Task: [Third repetitive task]
Tool: [Recommended automation tool]
Steps:
1. [Initial setup step]
2. [Configuration step]
3. [Testing and deployment step]
Expected Efficiency Gains: [Time/cost savings estimate]

---

**Implementation Strategy:**
Phase 1: [Quick-win automation with lowest complexity]
Phase 2: [Medium-complexity automation building on phase 1]
Phase 3: [Advanced automation requiring integration of multiple systems]

**Potential Challenges:**
1. [Integration compatibility issues]
2. [Team adoption and training requirements]
3. [Data migration or quality concerns]

**Recommended Solutions:**
1. [Technical solution for integration challenges]
2. [Change management and training approach]
3. [Data validation and cleanup strategy]
```

## 用法 / Usage
- 必填變數 / Variables: {{business-operations}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Project_Discovery_Scoping_Protocol
- 適用 / Use when: The Business Automation Workflow Designer is a free AI prompt that analyzes business operations and creates de…
