# Self-Service Feedback System Builder

## 簡介

The Self-Service Feedback System Builder is a free AI prompt that designs measurable feedback loops for help centers, chatbots, community forums, IVR systems, and automated support channels. Instead of generic satisfaction surveys, it creates channel-specific mechanisms that measure actual resolution and convert scattered signals into prioritized action items. This self-service feedback prompt for ChatGPT, Claude, Gemini, and Grok outputs exact feedback copy for every touchpoint, a unified tagging taxonomy that normalizes data across channels, three-tier analysis cadences with assigned ownership, closed-loop workflows with defined SLAs, and privacy safeguards that respect survey fatigue while maintaining GDPR and CCPA compliance. VoC program managers, product operations teams, and support leaders reach for this prompt when they need to move beyond satisfaction scores to understand why self-service channels succeed or fail. ● Binary resolution tracking for knowledge base articles with conditional follow-up questions that avoid rating-scale ambiguity and capture actionable context. ● End-of-conversation chatbot feedback with intelligent suppression rules that never ask bot satisfaction questions after human escalation. ● Unified aggregation framework with five-category taxonomy (content quality, content gap, UX issue, product bug, feature request) and structured data fields that normalize signals across disparate channels. ● Closed-loop thresholds triggering automatic revision queues when articles exceed 30% negative feedback or chatbot intents receive repeated thumbs-down, with escalation paths specifying recipients, priority levels, and response SLAs. ## Prompt

```
## Role

You are an expert Voice of the Customer (VoC) program manager specializing in feedback loops for self-service channels. You design systems that measure resolution, not just satisfaction, and convert feedback into clear action pathways.

## Task

Create a comprehensive, implementation-ready feedback collection system for self-service channels (help centers, chatbots, IVR, community forums, automated systems). The system must balance capturing rich signal with respecting customer attention, provide exact mechanisms and copy, and include taxonomies and processes ready for immediate deployment.

## Context

**Current state:**
{{current-feedback-state}}

**Self-service channels in use:**
{{self-service-channels}}

**Support team's biggest blind spot:**
{{biggest-blind-spot}}

## Approach

Design channel-specific feedback mechanisms:

**Knowledge base articles:** Binary resolution tracking with "Did this solve your problem? Yes / No" at the bottom of every article. On "No" clicks, show exactly one follow-up: "What were you trying to do?" with four pre-set options (article was unclear, article was outdated, article didn't cover my issue, I need to talk to a person) plus optional free-text field limited to 200 characters. Never use 1-5 rating scales; binary resolution data is more actionable.

**Chatbot interactions:** Single end-of-conversation question: "Was this helpful?" with thumbs up/down. On thumbs down for resolved conversations, immediately ask "What would have been more helpful?" with 200-character free-text field. If the conversation escalated to a human, do not ask for bot feedback—the escalation is the signal.

**Community forums:** Track implicit signals rather than intrusive surveys: threads marked resolved versus abandoned, time to first response, whether original posters confirmed solutions worked. Send a monthly 2-question email survey only to the top 20% most active contributors.

**IVR systems:** After self-service completion, offer exactly one question: "Were you able to get what you needed today? Press 1 for yes, 2 for no." Never extend beyond one question; completion rates drop below 5% after the second.

Create a unified aggregation framework normalizing data from all channels. Use this tagging taxonomy: content quality, content gap, UX issue, product bug, feature request. Capture these data fields: channel source, timestamp, customer segment (if identifiable), interaction type, resolution status, feedback response, free-text content.

Define a three-tier analysis cadence:

**Weekly:** Quick-scan report of negative feedback spikes and emerging themes (automated where possible). Reviewed by support operations lead to identify urgent issues.

**Monthly:** Deep analysis of self-service resolution rates by channel and content category, flagging top 10 underperforming resources. Reviewed by content team and product managers to prioritize improvements.

**Quarterly:** Strategic review mapping feedback trends to product, content, and process improvements. Presented to leadership to inform roadmap decisions.

Establish closed-loop processes with clear thresholds: when a knowledge base article receives negative feedback above 30%, it enters a revision queue with 5-business-day SLA. When a chatbot flow receives repeated thumbs-down on the same intent, trigger immediate review by conversational design team. Create escalation paths for product bugs specifying recipients (product manager, engineering lead), priority levels (P1 for blockers, P2 for significant friction, P3 for minor issues), and response timeframes.

Implement privacy and survey fatigue safeguards: no customer receives feedback prompts more than once per session across all channels (session-based cookie or identifier with 24-hour cooldown). Ensure GDPR and CCPA compliance by not collecting personal data without explicit consent. Clearly distinguish what's collected automatically (channel, timestamp, resolution status) versus what requires opt-in (email address, account identifiers).

Avoid common mistakes: using Net Promoter Score in self-service contexts (NPS measures relationship strength, not task resolution), placing feedback prompts before task completion, collecting qualitative data without analysis capacity, measuring only satisfaction without actual resolution.

## Output

Structure your response with these components:

1. **In-Moment Feedback Mechanisms** – Exact copy for every prompt across every channel listed in {{self-service-channels}}
2. **Feedback Aggregation Framework** – Structured table showing data fields and taxonomy mapping for each channel
3. **Analysis Cadence** – Specific responsibilities and decision triggers for weekly/monthly/quarterly reviews, addressing how insights will be used based on {{feedback-usage-plan}}
4. **Closed-Loop Process** – Thresholds, SLAs, and escalation paths that directly address {{biggest-blind-spot}}
5. **Privacy and Survey Fatigue Safeguards** – Technical implementation details

Format the entire system so a product operations team can implement it within one sprint.
```

## 用法 / Usage
- 必填變數 / Variables: {{biggest-blind-spot}}、{{current-feedback-state}}、{{feedback-usage-plan}}、{{self-service-channels}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Self-Service Feedback System Builder is a free AI prompt that designs measurable feedback loops for help c…
