# Incident Report Analysis Generator

## 簡介

The Incident Report Analysis Generator is a free AI prompt that transforms raw incident data into professional, comprehensive post-mortem reports for technical teams and operations managers. This incident report prompt for ChatGPT guides the AI to produce structured documentation covering incident timelines, impact assessments, root cause analysis, and corrective action plans. You provide the incident details - issue description, timestamps, affected services, downtime estimates, user impact, immediate fixes, and contributing factors - and the prompt formats everything into a clear, stakeholder-ready report. It runs on ChatGPT, Claude, Gemini, and Grok, making it ideal for DevOps teams, IT operations, quality assurance specialists, and anyone responsible for documenting system outages or technical failures. Reach for this prompt when you need to convert scattered incident data into a professional report that communicates what happened, why it happened, and how recurrence will be prevented. ● Structures reports with dedicated sections for incident summary, timeline, impact assessment, root cause analysis, corrective actions, and follow-up lessons learned ● Guides the AI to use clear, neutral language accessible to both technical and non-technical stakeholders, avoiding blame while focusing on learning and improvement ● Prompts quantitative impact measures including downtime duration, transaction counts, revenue effects, and user scope to convey scale ● Produces actionable recommendations prioritized by impact and feasibility, with specific tasks, owners, and due dates for accountability ## Prompt

```
## Role
You are an expert incident report writer with deep knowledge of root cause analysis, incident management, and technical writing.

## Task
Create a comprehensive incident report that details the provided issue or outage. Analyze the information and craft a clear, actionable report that helps stakeholders understand what happened, why it happened, and what steps are being taken to prevent recurrence.

## Context
Incident details:
{{incident-details}}

*Include: issue description, outage start/end times, services impacted, timeline events with timestamps, systems affected, estimated downtime, transactions/revenue/user impact, proximate cause, underlying factors, immediate fixes applied, and any available follow-up information.*

## Output
Format the report with these sections:

# Incident Summary
- Issue: [concise description]
- Outage Start Time: [timestamp]
- Outage End Time: [timestamp]
- Services Impacted: [list]

# Incident Timeline
1. [time]: [event]
2. [time]: [event]
3. [time]: [event]

# Impact Assessment
- Systems Affected: [systems]
- Estimated Downtime: [duration]
- Transactions Lost: [count]
- Revenue Impact: [amount]
- User Impact: [scope]

# Root Cause Analysis
- Proximate Cause: [immediate trigger]
- Underlying Factors: [contributing conditions]
- Explanation: [clear analysis connecting factors to outcome]

# Corrective Actions
- Immediate Fixes: [actions taken to restore service]
- Process Improvements: [workflow changes]
- Monitoring Enhancements: [observability upgrades]
- Long-term Remediations: [strategic initiatives]

# Incident Follow-Up
- Lessons Learned: [key insights]
- Action Items: [specific tasks with owners and due dates]

**Guidelines:**
- Use clear, concise language accessible to both technical and non-technical stakeholders
- Focus on objective facts and data-driven insights
- Prioritize actionable recommendations based on impact and feasibility
- Maintain a neutral, professional tone focused on learning and improvement rather than blame
- Use quantitative measures where possible to convey scale of impact
```

## 用法 / Usage
- 必填變數 / Variables: {{incident-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Incident Report Analysis Generator is a free AI prompt that transforms raw incident data into professional…
