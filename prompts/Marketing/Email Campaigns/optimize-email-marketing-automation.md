# Behavioral Email Automation Strategy Builder

## 簡介

The Behavioral Email Automation Strategy Builder is a free AI prompt that creates a full implementation plan for triggering personalized email sequences based on how visitors interact with your website. This behavioral email automation prompt for ChatGPT guides you through identifying trackable user actions - page visits, downloads, cart activity, feature interactions - and grouping them into 3–5 distinct segments (first-time browsers, cart abandoners, feature explorers). For each segment, the prompt designs a multi-email series with explicit triggers, content themes, and conversion goals, then specifies the tracking infrastructure (analytics events, pixels, webhooks, UTM parameters) and automation platform configuration needed to connect website behavior to your email tool. It runs on ChatGPT, Claude, Gemini, and Grok. Use this prompt when you need to move beyond batch-and-blast campaigns and deliver timely, relevant messages that respond dynamically to individual user journeys. ● Maps user actions to behavioral segments and designs multi-touch email sequences for each group ● Specifies how to capture on-site behaviors and pass them to your email platform ● Defines automation workflows with trigger conditions, personalization tokens, and segment routing ● Includes an optimization framework with core metrics, A/B test plans, and refinement schedules ## Prompt

```
## Role
You are an expert email marketer specializing in behavioral automation, user segmentation, and personalized campaign design.

## Task
Create a complete behavioral email automation strategy for {{website-url}} that triggers personalized email sequences based on how visitors interact with the site.

## Process

**1. Identify Key User Actions to Track**
List the critical on-site behaviors that signal intent or engagement (e.g., page visits, downloads, cart additions, time on site, feature interactions).

**2. Define Behavioral Segments**
Group users by their action patterns. Create 3-5 segments that represent distinct user journeys or intent levels (e.g., first-time browsers, repeat visitors who haven't converted, cart abandoners, feature explorers).

**3. Map Email Series for Each Segment**
For each segment, design an email sequence that includes:
- Trigger: the specific user action that starts the series
- Content overview: what each email communicates
- Goal: the desired outcome (engagement, conversion, retention)

Format as: Segment name → Email 1 [trigger/content/goal] → Email 2 [trigger/content/goal] → etc.

**4. Specify Tracking Implementation**
Describe how each identified action will be captured (analytics events, pixel tracking, platform-native tracking, UTM parameters, webhooks).

**5. Automation Configuration Blueprint**
Outline the technical setup:
- How website tracking connects to the email platform
- How each email series maps to its segment
- How triggers fire based on tracked actions
- What user data personalizes email content (name, browsing history, purchase behavior, preferences)

**6. Optimization Framework**
Establish monitoring and improvement practices:
- Core metrics to track: open rate, click-through rate, conversion rate, unsubscribe rate
- A/B test plan for subject lines, content blocks, and calls-to-action
- Schedule for segment and series refinement based on performance data
- Method for collecting and integrating user feedback

## Output
Provide a structured automation plan ready for implementation, with each section completed in actionable detail.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Behavioral Email Automation Strategy Builder is a free AI prompt that creates a full implementation plan f…
