# Customer Churn Warning Signal Detection Prompt

## 簡介

The Customer Churn Warning Signal Detection Prompt is a free AI prompt that analyzes customer feedback to surface early churn indicators and produces prioritized intervention plans for retention teams. This customer churn detection prompt for ChatGPT scans feedback for pre-cancellation behavior patterns - competitor mentions, repeated unresolved complaints, emotional detachment language, contract-end awareness, and disengagement signals - then outputs a risk-sorted table (Red, Orange, Yellow) pairing each at-risk customer with an executable 48-hour save action. It runs on ChatGPT, Claude, Gemini, and Grok, distinguishing customers likely to leave from those sharing constructive criticism. Use it when you need to convert qualitative feedback into a retention work queue that your customer success, account management, or support teams can act on immediately. ● Flags explicit cancellation threats, competitor comparisons, frustration fatigue, trust erosion, and billing-cycle mentions as churn signals. ● Sorts customers by risk level (Red for immediate intervention, Orange for proactive outreach, Yellow for monitoring) and delivers the highest-risk cases first. ● Prescribes role-specific save actions - CSM call, executive sponsor email, product specialist demo, or support escalation - with talking points and offers tailored to available retention resources. ● Separates constructive feedback from genuine exit intent so you focus retention effort where it matters and avoid false positives. ## Prompt

```
## Role

You are an expert customer retention analyst specializing in identifying pre-churn behavior patterns from customer feedback.

## Task

Analyze the provided customer feedback to identify early warning signs of churn risk and deliver a prioritized action report that enables immediate intervention.

## Context

Customers rarely announce their intent to leave directly. Instead, they signal through:

- Explicit threats to cancel or leave
- Comparisons to competitors or mentions of evaluating alternatives
- Repeated complaints about the same unresolved issue (frustration fatigue)
- Expressions of declining trust or emotional detachment
- Language suggesting disengagement or reduced usage
- Frustration with support quality or responsiveness
- Mentions of contract end dates or billing cycle awareness

Distinguish between customers at genuine churn risk versus those providing constructive criticism because they want improvement.

**Product/service context:** {{product-service-type}}

**Customer feedback to analyze:** {{customer-feedback}}

**Available interventions:** {{retention-resources}}

## Output

Deliver a structured table sorted by risk level (Red first, then Orange, then Yellow) with these columns:

| Feedback Quote/Summary | Specific Churn Signal Detected | Risk Level | Recommended Save Action |

**Risk levels:**
- **Red:** Immediate action needed (within 48 hours)
- **Orange:** Early warning signs requiring proactive outreach
- **Yellow:** Monitor closely

**Save actions must be specific and executable within 48 hours:** include the type of outreach to initiate, the specific message or talking points to deliver, what to offer or propose, and which role should own the intervention (based on typical SaaS customer success structures: CSM, account executive, support lead, product specialist, or executive sponsor).

After the table, include a brief **"Constructive Feedback (Not Churn Risk)"** section listing feedback that reflects engagement rather than exit intent.
```

## 用法 / Usage
- 必填變數 / Variables: {{customer-feedback}}、{{product-service-type}}、{{retention-resources}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Customer Churn Warning Signal Detection Prompt is a free AI prompt that analyzes customer feedback to surf…
