# Slack Notification System Design Prompt

## 簡介

The Slack Notification System Design Prompt is a free AI prompt that builds structured notification strategies for teams managing alerts, workflows, and team communication through Slack. This Slack notification design prompt for ChatGPT, Claude, Gemini, and Grok produces a full integration architecture including message format standards, urgency classification systems with 3-4 tiers, batching rules for non-critical updates, and webhook-ready JSON templates. Integration architects, DevOps teams, and workflow specialists use it to reduce alert fatigue while ensuring critical information reaches the right people at the right time. The prompt analyzes your requirements - critical events, batching needs, team focus hours, and communication norms - and outputs a deployment-ready system with testing protocols and rollout phases. ● Produces urgency classification systems with explicit criteria mapped to Slack mechanisms like @mentions, channel routing, and emoji indicators ● Generates batching rules for non-critical updates, including digest windows, maximum batch sizes, and override conditions ● Provides webhook-ready JSON message templates with dynamic placeholders, actionable links, and consistent formatting standards ● Delivers sequenced implementation plans covering webhook configuration, testing protocols, phased rollout, and team onboarding guidelines ## Prompt

```
## Role

Integration architect and workflow optimization specialist with expertise in notification system design, team communication patterns, and Slack automation.

## Task

Design a comprehensive Slack notification system that reduces cognitive load and enhances team communication through contextual, timely alerts. Balance information delivery with attention management using urgency levels, batching strategies, and team norms to improve productivity without adding noise.

## Context

{{notification-requirements}}

Describe your requirements including: critical events requiring immediate notification, non-critical events suitable for batching, current notification pain points you're solving, team communication preferences and focus hours, and your Slack webhook URL.

## Output

Provide a complete integration strategy structured as:

### Message Format Standards
Design consistent templates that include relevant context without overwhelming recipients. Specify formatting conventions, required fields, and visual hierarchy.

### Urgency Classification System
Define 3-4 urgency tiers with explicit criteria. Map each tier to appropriate Slack mechanisms: mentions (@here, @channel, individual), formatting (emoji indicators, bold/color), and channel routing.

### Batching Rules
Establish rules for grouping non-critical updates, including batching windows (e.g., digest every 2 hours), maximum batch size, and exceptions that bypass batching.

### Message Templates
Provide ready-to-use JSON templates for each event category, including webhook payload structure, dynamic field placeholders, actionable links and CTAs, and contextual information blocks.

### Implementation Steps
Sequenced deployment plan covering webhook configuration, testing protocols, rollout phases, and team onboarding.

### Alignment Guidelines
Recommendations for respecting team boundaries, integrating with existing communication patterns, and maintaining the system over time.

Format all code blocks clearly and ensure templates are immediately usable.
```

## 用法 / Usage
- 必填變數 / Variables: {{notification-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Slack Notification System Design Prompt is a free AI prompt that builds structured notification strategies…
