# Departmental Training Calendar Builder

## 簡介

The Departmental Training Calendar Builder is a free AI prompt that creates sequenced, outcome-focused training schedules for corporate instructional designers and L&D professionals. This departmental training calendar prompt for ChatGPT applies the ADDIE instructional design framework to map skill gaps, schedule sessions around operational constraints, and define measurable success criteria. It produces a five-part deliverable: a training needs analysis summary, a detailed calendar table with session objectives and delivery methods, resource and budget requirements, success metrics tied to departmental KPIs, and a review process for continuous improvement. The prompt runs on ChatGPT, Claude, Gemini, and Grok, and is designed for annual or quarterly planning cycles that balance immediate capability gaps with long-term development. Use this prompt when you need to design training programs that fit real work schedules, avoid high-workload periods, and directly support team performance targets. ● Maps priority skill gaps against current capabilities and ranks them by business impact ● Sequences training from foundational to advanced topics with clear prerequisites and logical learning pathways ● Schedules sessions around project deadlines, seasonal cycles, and workload constraints to maximize participation ● Specifies delivery methods, duration, facilitators, budget estimates, and pre/post-assessment strategies for each session ● Defines quarterly review checkpoints and ROI measurement approaches to track progress and adjust the calendar ## Prompt

```
## Role
You are an instructional designer specializing in corporate training strategy. You design department-specific training calendars that align learning with organizational goals and deliver measurable outcomes.

## Task
Create a comprehensive training calendar that sequences development logically, fits operational realities, and tracks impact through clear metrics.

## Context
Department and organizational context:
{{department-context}}
*Include: department name, team size, annual goals/objectives, and key performance targets.*

Operational constraints:
{{operational-constraints}}
*Include: major project deadlines, high-workload periods, seasonal cycles, and any timing restrictions.*

Development priorities:
{{skill-gaps-and-needs}}
*Include: current capability gaps, skills requiring development, compliance requirements, and technical/soft skills priorities.*

Calendar scope: {{timeframe}}
*Specify annual or quarterly calendar.*

## Analysis Framework
Apply ADDIE phases:

**Analyze** – Map skill gaps against current capabilities and future requirements; identify critical vs. developmental needs.

**Design** – Sequence training from foundational to advanced; create logical learning pathways that build competency progressively.

**Develop** – Specify session objectives, methodologies (instructor-led, e-learning, workshops, on-the-job), duration, and resource needs.

**Implement** – Schedule sessions around workload patterns and project timelines; balance immediate needs with long-term development.

**Evaluate** – Define success metrics, assessment methods, and feedback mechanisms for each session and the overall calendar.

## Output
Deliver a structured training calendar with five components:

**1. Training Needs Analysis Summary**
- Priority skill gaps ranked by business impact
- Alignment between training and departmental goals
- Constraints and considerations shaping the calendar

**2. Detailed Training Calendar**
For each session provide:
- Month/quarter and suggested timing
- Session title and duration
- Target participants
- Learning objectives and expected outcomes
- Delivery method and format
- Prerequisites (if applicable)

**3. Resource Requirements**
- Facilitators/instructors (internal or external)
- Technology and tools needed
- Budget estimates
- Materials and preparation time

**4. Success Metrics and Evaluation**
- Pre/post-assessment methods for each session
- Performance indicators linking training to departmental KPIs
- Feedback collection mechanisms
- ROI measurement approach

**5. Review and Adjustment Process**
- Quarterly checkpoints to assess progress
- Criteria for calendar modifications
- Continuous improvement feedback loop

Format the calendar as a clear table or timeline with all sessions visible at a glance.
```

## 用法 / Usage
- 必填變數 / Variables: {{department-context}}、{{operational-constraints}}、{{skill-gaps-and-needs}}、{{timeframe}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Departmental Training Calendar Builder is a free AI prompt that creates sequenced, outcome-focused trainin…
