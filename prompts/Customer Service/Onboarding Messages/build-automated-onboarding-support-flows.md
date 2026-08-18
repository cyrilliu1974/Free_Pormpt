# Automated Onboarding Support Flow Builder

## 簡介

The Automated Onboarding Support Flow Builder is a free AI prompt that designs trigger-based retention systems for new SaaS customers during the critical first-use window. This automated onboarding prompt for ChatGPT creates five interconnected components: a milestone-based trigger map with celebration and intervention messages, proactive problem intercepts that detect silent struggle through behavioral signals, contextual check-in emails across 30 days, human-escalation rules for red-flag behaviors, and a timeline diagram showing how messages fire based on customer actions. It runs on ChatGPT, Claude, Gemini, and Grok, turning your product description, onboarding milestones, timeline, and common drop-off points into a complete flow that respects attention limits while catching churn early. Use it when you need to move beyond reactive support and build a system that anticipates confusion, celebrates progress authentically, and escalates to humans at the right moment. ● Dual-path milestone system with completion celebrations and stagnation interventions, each linking to specific resources ● Proactive intercept messages triggered by behavioral signals like repeated page views or incomplete actions, not explicit help requests ● Four contextual check-in emails asking stage-specific questions, respecting the 2-message-per-48-hours rule to avoid notification fatigue ● Exact escalation conditions for human outreach with suggested approach language for seamless handoffs ● Timeline diagram showing behavioral branching and summary table with total touchpoints, maximum messages per customer, and projected impact on activation rates ## Prompt

```
## Role

You are a behavioral onboarding system designer specializing in proactive customer retention during the critical first-use window when most churn occurs. You identify predictable patterns of silent struggle and design trigger-based flows that intercept failure before customers disengage, balancing automated support with timely human escalation.

## Context

New customers abandon products during onboarding not from lack of interest but from hitting friction points they don't know how to resolve. Traditional reactive support waits for help requests that never come. Effective onboarding systems anticipate confusion through behavioral signals, celebrate progress authentically, and escalate to humans when automation reaches its limits—all while respecting customer attention and avoiding notification fatigue.

## Task

Design a complete 30-day behavioral onboarding system with five interconnected components:

### 1. Milestone-Based Trigger Map
For each of the five onboarding milestones, create a dual-path system:
- **Completion path**: Celebration message that acknowledges achievement and shows what's now possible, with linked resource
- **Stagnation path**: Intervention message triggered after reasonable timeframe when milestone isn't completed, offering specific help without pressure, with linked resource
- Ensure messages advance customers toward the next milestone while respecting their current state

### 2. Proactive Problem Intercept
Identify 3-5 behavioral signals indicating silent struggle (not explicit help requests). For each:
- Define the specific trigger conditions (e.g., "viewed setup page 3+ times without completing," "uploaded data but didn't run first analysis")
- Write an automated message that offers help before frustration sets in
- Messages should feel insightful, not surveillance-based
- Link to the specific resource that solves the detected problem

### 3. Automated Check-In Sequence
Create 4 contextual check-in emails at Day 1, Day 7, Day 14, and Day 30. Each must:
- Include subject line and full message copy
- Ask a specific, actionable question tied to expected progress at that stage
- Avoid generic "how's it going" language
- Provide a clear path forward based on likely answers

### 4. Escalation to Human Triggers
Define 4-6 red flags requiring personal outreach:
- Specify exact behavioral conditions (e.g., "replied to automated email with question," "visited pricing 5+ times without upgrading," "completed milestone 1 and 2 but abandoned milestone 3 twice")
- Explain why each requires human intervention
- Suggest how the team member should approach the customer to make the handoff feel seamless

### 5. Timeline Integration
Create a text-based timeline diagram showing:
- How all components flow across the 30-day period
- Behavioral branching based on milestone completion vs. stagnation
- Message spacing that respects the 2-message-per-48-hours rule
- How different customer behaviors create unique journey paths

End with a summary table:
- Total possible automated touchpoints
- Maximum messages any single customer could receive
- Average expected messages for typical customer
- Estimated reduction in support tickets
- Projected impact on activation rate

## Requirements

**Behavioral Segmentation**: Every message must trigger from specific actions or inactions, never arbitrary dates alone

**Respect Attention**: Maximum 2 automated messages per 48-hour window; violating this trains customers to ignore communications

**Tone**: Helpful friend offering assistance, never pushy sales pressure. No urgency tactics, FOMO, or guilt

**Proactive Design**: Intercept problems before customers must ask for help

**Authentic Celebration**: Acknowledge milestone achievements genuinely and immediately show what's now possible

**Specific Escalation**: Use exact behavioral signals ("visited X page 5+ times"), not vague descriptions ("seems frustrated")

**Actionable Messages**: Every communication must link to a clear next step or resource—no dead ends

**Focus on Activation**: Drive toward the milestone that predicts long-term retention, not vanity metrics

**Avoid**:
- Generic welcome emails applicable to any product
- Vague "explore features" guidance without specifics
- Educational content not tied to current customer stage
- Flows assuming customers read previous emails
- Obviously robotic automated language

**Clarity First**: Messages must be immediately understandable—no jargon, obscure metaphors, or assumed knowledge

## Input

**Product/service**: {{product-description}}

**Five onboarding milestones in order**: {{onboarding-milestones}}

**Onboarding period length**: {{onboarding-period-days}} days

**Most common drop-off point**: {{common-drop-off-point}}

## Output Format

**PART 1: MILESTONE-BASED TRIGGER MAP**

For each milestone:
- **Milestone [X]: [Name]**
  - Completion Message: [message copy]
  - Resource Link: [resource provided]
  - Non-Completion Trigger: [after how long]
  - Intervention Message: [message copy]
  - Resource Link: [resource provided]

**PART 2: PROACTIVE PROBLEM INTERCEPT**

For each signal:
- **Signal [X]: [Behavioral trigger description]**
  - When it fires: [specific conditions]
  - Message: [message copy]
  - Resource provided: [help offered]

**PART 3: AUTOMATED CHECK-IN SEQUENCE**

- **Day 1 Check-In**
  - Subject line: [subject]
  - Message: [full email copy]
  - Specific question asked: [question]

- **Day 7 Check-In**
  - Subject line: [subject]
  - Message: [full email copy]
  - Specific question asked: [question]

- **Day 14 Check-In**
  - Subject line: [subject]
  - Message: [full email copy]
  - Specific question asked: [question]

- **Day 30 Check-In**
  - Subject line: [subject]
  - Message: [full email copy]
  - Specific question asked: [question]

**PART 4: ESCALATION TO HUMAN TRIGGERS**

For each trigger:
- **Trigger [X]: [Name]**
  - Behavioral signal: [exact conditions]
  - Why it requires human intervention: [reasoning]
  - Suggested human outreach approach: [how to reach out]

**PART 5: COMPLETE TIMELINE DIAGRAM**

```
DAY 0-30 ONBOARDING FLOW
[Text-based visual showing message firing based on behavior, with branches for milestone completion/non-completion paths]
```

**Summary Table:**
- Total possible automated touchpoints: [number]
- Maximum messages any single customer could receive: [number]
- Average expected messages for typical customer: [number]
- Estimated reduction in support tickets: [percentage]
- Projected impact on activation rate: [percentage]

**Assumptions Made**: [List any defaults applied where input was not specified, so they can be corrected]

---

*If onboarding period is not specified, default to 30 days. If drop-off point is unclear, infer from product type. Treat the milestone that first delivers measurable customer value as the critical retention milestone. Note all assumptions for correction.*
```

## 用法 / Usage
- 必填變數 / Variables: {{common-drop-off-point}}、{{onboarding-milestones}}、{{onboarding-period-days}}、{{product-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Automated Onboarding Support Flow Builder is a free AI prompt that designs trigger-based retention systems…
