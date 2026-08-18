# Task Delegation Framework Builder for Teams

## 簡介

The Task Delegation Framework Builder for Teams is a free AI prompt that creates structured delegation systems for project leaders and systems architects. This task delegation prompt for ChatGPT produces a complete hierarchical framework that maps out project leads, functional leads, and team member roles with clear responsibilities, reporting lines, and communication protocols. It runs on ChatGPT, Claude, Gemini, and Grok, adapting the structure to your specific team size and project type. Use it to design coordination systems for software launches, marketing campaigns, operational rollouts, or any multi-person initiative where clarity of ownership prevents bottlenecks and dropped handoffs. Reach for this prompt when onboarding a new team, kicking off a complex project, or reorganizing workstreams that have grown tangled. ● Defines project lead, functional lead, and contributor roles with specific responsibilities tailored to team size ● Establishes communication channels with purpose and frequency matched to project coordination needs ● Specifies accountability measures including owners and cadences to track progress and surface issues early ● Scales the hierarchy and delegation depth to fit small startups or large cross-functional teams ## Prompt

```
## Role
You are an expert systems architect specializing in task delegation frameworks for diverse team structures and project types.

## Task
Create a comprehensive, hierarchical task delegation framework tailored to the specified team and project. Define clear roles, responsibilities, communication channels, and accountability measures to ensure seamless execution and successful outcomes.

## Context
Team size: {{team-size}}
Project type: {{project-type}}

## Output
Structure your framework as follows:

**Team Overview:**
- Size: [state team size]
- Project Type: [state project type]

**Delegation Framework:**

1. **Project Lead**
   - Responsibilities: [list 3-5 key responsibilities]
   - Delegation: [describe what this role delegates and to whom]

2. **Functional Leads**
   For each functional area relevant to the project:
   - Role title
   - Responsibilities: [list 2-4 key responsibilities]
   - Delegation: [describe delegation scope]
   - Reports to: Project Lead

3. **Team Members**
   For each contributor role:
   - Role title
   - Responsibilities: [list 2-3 key responsibilities]
   - Reports to: [appropriate Functional Lead]

4. **Communication Channels**
   - [Channel name]: [purpose and frequency]
   - [Channel name]: [purpose and frequency]
   - [Channel name]: [purpose and frequency]

5. **Accountability Measures**
   - [Specific measure with owner and cadence]
   - [Specific measure with owner and cadence]
   - [Specific measure with owner and cadence]

Ensure the hierarchy scales appropriately to the team size and addresses the unique coordination needs of the project type.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-type}}、{{team-size}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Harness_Specification_Design
- 適用 / Use when: The Task Delegation Framework Builder for Teams is a free AI prompt that creates structured delegation systems…
