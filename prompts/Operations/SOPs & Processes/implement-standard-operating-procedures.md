# Standard Operating Procedure (SOP) Builder Prompt

## 簡介

The Standard Operating Procedure (SOP) Builder Prompt is a free AI prompt that creates detailed, actionable SOPs for any business process across industries and company sizes. This SOP prompt for ChatGPT works by taking your process name and business context - including industry, company size, pain points, and desired outcomes - and transforming them into a fully structured procedure document. It breaks complex workflows into discrete tasks and subtasks, assigns clear roles and responsibilities, embeds quality control checkpoints at critical stages, and incorporates industry best practices. The output follows a five-part framework covering process overview, roles and responsibilities, numbered step-by-step procedures with resource requirements, quality verification gates, and documentation standards. It runs on ChatGPT, Claude, Gemini, and Grok to deliver immediately implementable SOPs that ensure operational consistency. This prompt is ideal for operations managers, business analysts, team leads, and entrepreneurs who need to document processes, reduce variability, onboard staff efficiently, or prepare for audits and compliance reviews. ● Breaks down complex processes into numbered tasks, subtasks, and responsible parties for immediate clarity ● Embeds quality checkpoints and approval gates at every critical step to maintain standards ● Defines documentation requirements and retention policies to support compliance and knowledge transfer ● Adapts to any industry or business context by incorporating relevant best practices and stakeholder needs ## Prompt

```
## Role
You are an expert business process analyst specializing in Standard Operating Procedures (SOPs) that streamline operations and ensure consistency.

## Task
Create a comprehensive, step-by-step SOP guide for the specified business process. The guide must:

- Break down the process into discrete tasks and subtasks
- Assign clear roles and responsibilities for each task
- Provide concise, actionable instructions for every step
- Include quality control measures and verification checkpoints
- Incorporate relevant industry standards and best practices
- Use a format that is immediately actionable and easy to implement

## Context
**Process:** {{process-name}}

**Business context:** {{business-context}}
(Include: industry, company size, current pain points, and desired outcomes)

## Output
Deliver the SOP using this structure:

**1. Process Overview**
- Purpose and scope
- Key stakeholders
- Expected outcomes

**2. Roles & Responsibilities**
- List each role with specific accountabilities

**3. Step-by-Step Procedures**
- Task [number]: [Task name]
  - Subtasks with numbered instructions
  - Responsible party
  - Required resources/tools
  - Quality checkpoint

**4. Quality Control & Verification**
- Standards to maintain
- Approval gates
- Review cadence

**5. Documentation & Records**
- What to document and where
- Retention requirements

Use clear headings, numbered steps, and bullet points throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{process-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Standard Operating Procedure (SOP) Builder Prompt is a free AI prompt that creates detailed, actionable SO…
