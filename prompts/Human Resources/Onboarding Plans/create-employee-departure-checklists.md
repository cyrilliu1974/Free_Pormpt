# Employee Offboarding Checklist Generator

## 簡介

The Employee Offboarding Checklist Generator is a free AI prompt that creates prioritized departure checklists for HR teams managing employee exits across organizations of all sizes. This employee offboarding prompt for ChatGPT, Claude, Gemini, and Grok produces a numbered list of 10 critical tasks that must be completed within the first week of an employee's departure, each with a specific timeframe (within 2 hours, by end of day 1, by day 3), assigned owner, and documented business risk if delayed. You provide details about your offboarding scenario - voluntary resignation, termination, role type, access levels - and the prompt prioritizes tasks around legal compliance, security vulnerabilities, operational continuity, and team morale. HR operations specialists use it to prevent data breaches, protect intellectual property, maintain regulatory compliance, and ensure smooth knowledge transfer during transitions at Fortune 500 companies, high-growth startups, and mid-sized organizations. ● Prioritizes tasks by urgency and impact, focusing on immediate security access revocation, legal documentation, and operational handoffs. ● Identifies the specific responsible party (IT, legal, manager, payroll) for each task to eliminate ambiguity during transitions. ● Documents concrete business risks - data breach exposure, compliance penalties, knowledge loss - tied to delayed action. ● Adapts to different departure scenarios including voluntary resignations, terminations, layoffs, retirements, and role-specific considerations. ## Prompt

```
## Role
You are an HR operations specialist with deep expertise in employee offboarding across organizations of all sizes.

## Task
Create a prioritized checklist of 10 critical tasks HR must complete within the first week of an employee's departure. Each task must include:
- Specific timeframe within the first week (e.g., "within 2 hours," "by end of day 1," "by day 3")
- Responsible party
- Business risk if delayed

## Context
Employee departures create immediate operational, legal, and security risks that compound rapidly without systematic action. The first week is crucial for protecting company assets, maintaining compliance, preserving relationships, and ensuring knowledge transfer.

**Scenario details:**
{{offboarding-scenario}}

Focus on tasks with immediate time-sensitive implications: legal compliance, security vulnerabilities (data breaches, intellectual property protection), operational continuity, and team morale. Address tasks applicable to both voluntary and involuntary departures.

## Output
Deliver a numbered list (1-10) in priority order. For each task, state:
1. **Task name and description**
2. **Timeframe:** When within the first week it must be completed
3. **Owner:** Role/department responsible
4. **Risk if delayed:** Specific compliance, security, operational, or relationship consequences
```

## 用法 / Usage
- 必填變數 / Variables: {{offboarding-scenario}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Manifest_Heuristic_Consistency_Scanner
- 適用 / Use when: The Employee Offboarding Checklist Generator is a free AI prompt that creates prioritized departure checklists…
