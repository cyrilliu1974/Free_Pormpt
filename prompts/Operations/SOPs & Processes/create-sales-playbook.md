# Sales Playbook Creator for Revenue Teams

## 簡介

The Sales Playbook Creator is a free AI prompt that builds structured, actionable sales playbooks for revenue teams, sales operations leaders, and go-to-market strategists. This sales playbook prompt for ChatGPT guides the model to produce a multi-section playbook: sales process stages mapped to activities and success metrics, role definitions with KPIs and skill requirements, best-practice scripts with dos and don'ts, a tools and technology stack with integration points, performance metrics with targets and measurement cadence, and training modules with evaluation criteria and real-world scenarios. It runs on ChatGPT, Claude, and Gemini; you supply a single {{sales-context}} variable describing your sales motion, team structure, deal size, and cycle length, and the model returns a formatted, table-driven playbook ready to share with your team. Use it when onboarding new sellers, standardizing a distributed sales org, launching a new product line, or auditing your existing process for gaps. ● Maps every stage of your sales funnel to key activities, success criteria, tools, and expected duration ● Defines roles and responsibilities with measurable KPIs and required skill sets for accountability ● Provides best-practice guidance, anti-patterns to avoid, and sample dialogue for common scenarios ● Includes a prioritized technology stack table and a training curriculum with evaluation checkpoints ## Prompt

```
## Role

You are an expert sales operations strategist creating a comprehensive Sales Playbook to optimize sales performance and drive consistent execution.

## Task

Build a complete Sales Playbook covering:

1. **Sales Process Stages** – mapped with key activities, success metrics, tools/resources, and duration
2. **Key Roles & Responsibilities** – with KPIs and required skills for each role
3. **Best Practices & Scripts** – dos, don'ts, and sample dialogue
4. **Sales Tools & Technologies** – with purpose, integration points, and priority
5. **Performance Metrics** – targets, measurement frequency, and impact scores
6. **Training & Onboarding** – modules, timelines, resources, evaluation criteria, and a real-world scenario

## Context

{{sales-context}}

Include: sales process stages, team roles, key tools, and any unique aspects of the sales motion (deal size, sales cycle length, customer segments, etc.).

## Output

Deliver the playbook in this structure:

### 1. Sales Process Stages

| Stage Name | Key Activities | Success Metrics | Tools/Resources | Duration |
|------------|----------------|-----------------|-----------------|----------|
| [stage]    | [activities]   | [metrics]       | [tools]         | [time]   |

### 2. Key Roles & Responsibilities

**[Role Title]**
- Responsibilities: [list]
- KPIs: [metrics]
- Required Skills: [skills]

### 3. Best Practices & Scripts

✅ **Do:**
- [practice]

❌ **Don't:**
- [anti-pattern]

📝 **Sample Script:**
"[dialogue example]"

### 4. Sales Tools & Technologies

| Tool Name | Purpose | Integration Points | Priority |
|-----------|---------|-------------------|----------|
| [tool]    | [use]   | [integrations]    | [level]  |

### 5. Performance Metrics

| Metric Name | Target | Measurement Frequency | Impact Score |
|-------------|--------|----------------------|-------------|
| [metric]    | [goal] | [cadence]            | [1-10]      |

### 6. Training & Onboarding

**Module [N]: [Title]**
- Timeline: [duration]
- Resources: [materials]
- Evaluation: [criteria]

**Real-World Scenario:**
[Example walkthrough of applying the playbook to a typical deal]

Use tables, bullet points, and concrete examples throughout. Make every section immediately actionable.
```

## 用法 / Usage
- 必填變數 / Variables: {{sales-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Sales Playbook Creator is a free AI prompt that builds structured, actionable sales playbooks for revenue …
