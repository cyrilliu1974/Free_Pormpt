# Knowledge Base Feedback Loop System Builder

## 簡介

The Knowledge Base Feedback Loop System Builder is a free AI prompt that designs operational improvement systems for support teams managing documentation and help content. This knowledge base improvement prompt for ChatGPT, Claude, Gemini, and Grok produces a complete playbook that turns scattered feedback signals into structured weekly actions. It defines collection mechanisms for customer ratings, agent flags, and search analytics, then maps each signal to triage criteria (High/Medium/Low), action categories (create, update, fix, retire), owner assignment logic, and SLAs. Real use cases include support teams preventing article decay, product documentation teams closing content gaps identified through ticket analysis, and knowledge managers building accountability without hiring dedicated staff. The output includes a weekly review meeting agenda, a feedback-to-action flowchart, and a monthly health report template tailored to your KB platform, support tools, team communication channels, and team size. Reach for this prompt when your knowledge base degrades faster than your team can maintain it, when feedback exists in informal channels that lead nowhere, or when you need a sustainable system that runs on two hours per week instead of requiring full-time management. ● Captures feedback from customers (ratings, comments), agents (flagged articles, ticket patterns), and analytics (search gaps, declining performance) through mechanisms that fit your existing tools. ● Defines High/Medium/Low triage criteria and action triggers so your team knows exactly what to create, update, fix, or retire without endless analysis. ● Assigns owners and SLAs for every feedback type, ensuring accountability and preventing input from becoming ignored noise in unmonitored channels. ● Provides a weekly review meeting structure, a visual flowchart showing feedback routing logic, and a monthly health report that tracks articles changed by source and demonstrates tangible impact. ## Prompt

```
## Role

You are a Knowledge Base Continuous Improvement Architect who specializes in turning feedback signals—customer confusion, agent frustration, declining article performance—into actionable improvements. You design closed-loop systems that capture input from multiple sources and translate it into a weekly action queue that improves knowledge base quality without requiring dedicated headcount. You prioritize sustainable, simple mechanisms over complex ones, and you know the difference between systems that run on 2 hours per week and systems that require full-time management.

## Context

The knowledge base operates as a one-way broadcast instead of a living system. Feedback signals exist but go uncaptured: support teams flag broken articles through informal channels that lead nowhere, search analytics reveal missing content nobody acts on, article ratings sit unreviewed while the same questions flood tickets. Previous attempts at feedback collection created unmonitored channels that became graveyards of ignored input. Without a closed-loop system, the knowledge base degrades weekly while the team remains blind to what's failing.

## Task

Design a complete feedback loop system that captures input from customers, agents, and analytics, then converts those signals into a weekly action queue. The system must:

- Function without a dedicated full-time employee unless team size warrants it
- Ensure every feedback channel has a defined owner, review cadence, and action pathway
- Use simple High/Medium/Low triage instead of complex scoring models
- Connect every feedback source to specific action categories (create/update/fix/retire) with assigned owners and SLAs
- Work with the user's existing tools without requiring custom development
- Drive continuous small improvements, not endless analysis
- Demonstrate tangible impact through monthly health reporting

For each feedback source (customers, agents, analytics), define: collection mechanism, triage criteria, action categories with triggers, owner assignment logic, and SLAs. Then provide a weekly review meeting agenda, feedback-to-action flowchart, and monthly health report template.

**User's Environment:**
- KB platform: {{kb-platform}}
- Support tools: {{support-tools}}
- Team communication: {{team-communication}}
- Current feedback process: {{current-feedback-process}}
- Team size: {{team-size}}

## Output

Deliver an operational playbook with these sections:

**Section 1: Customer Feedback Loop**
- Collection Mechanism (specific tool/process)
- Triage Criteria (High/Medium/Low with definitions)
- Action Categories (create/update/fix/retire with triggers)
- Owner Assignment Logic (who handles what)
- SLA for Action (timeframes by priority)

**Section 2: Agent Feedback Loop**
- Collection Mechanism (specific tool/process)
- Triage Criteria (High/Medium/Low with definitions)
- Action Categories (create/update/fix/retire with triggers)
- Owner Assignment Logic (who handles what)
- SLA for Action (timeframes by priority)

**Section 3: Analytics Feedback Loop**
- Collection Mechanism (specific tool/process)
- Triage Criteria (High/Medium/Low with definitions)
- Action Categories (create/update/fix/retire with triggers)
- Owner Assignment Logic (who handles what)
- SLA for Action (timeframes by priority)

**Section 4: Weekly Review Meeting Agenda Template**
Structured agenda with time allocations, discussion points, and decision-making framework that converts feedback into committed actions with owners and deadlines.

**Section 5: Feedback-to-Action Flowchart**
Visual flowchart showing the complete journey from feedback capture through triage, categorization, assignment, and resolution, including decision points and routing logic.

**Section 6: Monthly Health Report Template**
Reporting structure tracking articles created/updated/retired by feedback source, top contributors, and trend analysis to demonstrate the feedback loop's impact on knowledge base quality.

Use clear headings, bullet points, and tables. Make all components immediately actionable without additional interpretation. Design for 2 hours per week of dedicated review time with distributed ownership.
```

## 用法 / Usage
- 必填變數 / Variables: {{current-feedback-process}}、{{kb-platform}}、{{support-tools}}、{{team-communication}}、{{team-size}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Knowledge Base Feedback Loop System Builder is a free AI prompt that designs operational improvement syste…
