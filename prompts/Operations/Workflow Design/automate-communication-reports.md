# Automate Communication Reports

## 簡介

The Automate Communication Reports prompt is a free AI prompt that designs proactive email reporting systems for organizations seeking to prevent crises through strategic information flow. It produces a complete implementation plan covering SMTP setup with modern authentication, role-based recipient management, human-readable report generation pipelines, scheduling engines that respect work patterns and time zones, error handling frameworks, and logging architectures. This communication reports prompt for ChatGPT works with Claude, Gemini, and Grok to transform raw automation requirements into actionable technical specifications that balance delivery mechanics with human readability, moving reporting into important-but-not-urgent territory rather than reactive firefighting. Reach for this prompt when you need to build email automation that respects organizational rhythm, prevents notification fatigue, and ensures critical information reaches the right people at the right time without overwhelming inboxes or escalating into emergencies. ● Produces SMTP configuration guidance with OAuth2 and App Password authentication, secure credential storage practices, and connection testing procedures. ● Designs role-based recipient management systems with dynamic list maintenance, unsubscribe mechanisms, and preference handling to ensure reports reach appropriate stakeholders. ● Creates report generation pipelines that prioritize clear visual hierarchy and human readability over raw data dumps, with attachment protocols and size management. ● Builds scheduling engines that align delivery with recipient work patterns, handle multiple time zones, enforce blackout periods, and include subject line templates optimized for inbox filtering. ● Specifies error handling frameworks with graceful failure recovery, administrator notifications, retry logic, and actionable logging architectures for troubleshooting and compliance. ## Prompt

```
## Role

You are an automation architect specializing in proactive email reporting systems.

## Task

Design a comprehensive email automation implementation plan that compiles, formats, and delivers reports proactively. The system must handle SMTP configuration, recipient management, content generation, scheduling, error handling, and logging while prioritizing human readability and organizational rhythm.

## Context

Effective automation balances technical delivery with human communication patterns. Reports must be readable, timely, and aligned with work patterns—not raw data dumps. The goal is to move reporting into "important but not urgent" territory, preventing crises through strategic information flow rather than reactive firefighting.

{{automation-requirements}} should cover: SMTP server details (address, port, security protocol, authentication method), recipient lists with roles, data sources and metrics to include, report format preferences, scheduling frequency and time zones, blackout periods, and your organization's communication culture (reading habits, urgency patterns, preferred report density).

## Output

Provide a step-by-step implementation plan with these sections:

### 1. SMTP Configuration Setup
- Server connection parameters and modern authentication (OAuth2, App Passwords)
- Secure credential storage practices (never plain text)
- Connection testing procedures

### 2. Recipient Management System
- Role-based distribution logic
- Dynamic list maintenance
- Unsubscribe mechanisms and preference handling

### 3. Report Generation Pipeline
- Data source integration workflow
- Human-readable formatting with clear visual hierarchy
- Attachment protocols and size management

### 4. Scheduling Engine
- Time-based triggers aligned with recipient work patterns
- Timezone handling across distributed teams
- Blackout period enforcement

### 5. Subject Line Templates
- Dynamic templates with report type, date range, and urgency indicators
- Filtering-friendly conventions for easy inbox management

### 6. Error Handling Framework
- Graceful failure recovery for bounce-backs, timeouts, and server errors
- Administrator notifications without user spam
- Retry logic and fallback procedures

### 7. Logging Architecture
- Actionable audit trails with context (not just timestamps)
- Troubleshooting metadata
- Compliance and security tracking

### 8. Testing Protocol
- Pre-launch validation checklist
- Pilot group rollout strategy
- Feedback integration loop

### 9. Maintenance Procedures
- Ongoing optimization guidelines
- Performance monitoring
- Report effectiveness metrics (open rates, action taken)

**Format:** Use code blocks for configuration examples, bullet points for features, numbered steps for procedures, and warning callouts for security considerations. Prioritize preventing notification fatigue—focus on report quality and timing over frequency.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Automate Communication Reports prompt is a free AI prompt that designs proactive email reporting systems f…
