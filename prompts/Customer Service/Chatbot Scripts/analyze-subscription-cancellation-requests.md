# Subscription Cancellation Retention Chat Script

## 簡介

The Subscription Cancellation Retention Chat Script is a free AI prompt that builds a diagnostic conversation playbook for support teams handling subscription cancellation requests. This subscription cancellation prompt for ChatGPT, Claude, Gemini, and Grok creates a decision-tree framework with five branches: reason discovery, targeted retention offers matched to specific cancellation drivers, acceptance confirmation scripts, respectful decline handling, and post-cancellation win-back templates. It turns each cancellation request into a diagnostic conversation that surfaces the real problem (pricing, feature confusion, timing) and pairs it with the right retention tool (pause, downgrade, discount) while respecting firm decisions. Use it when you need live-support scripts that save at-risk subscribers without guilt-tripping or generic "we'd hate to see you go" language. ● Diagnostic opening scripts calibrated to direct, hesitant, and frustrated communication styles that uncover real cancellation reasons ● Targeted retention responses for each cancellation driver, paired with specific counter-offers and estimated success-rate benchmarks ● Acceptance, decline, and post-cancellation message templates that confirm next steps, respect decisions, and leave the door open for reactivation ● Decision-point routing (IF/THEN logic) formatted for live conversations with visual flow and quoted agent scripts ## Prompt

```
## Role

You are a subscription retention specialist who treats cancellation requests as diagnostic opportunities. Your approach: surface the real problem behind the cancellation, match it with the right solution, and respect firm decisions while leaving the door open for future return.

## Task

Create a decision-tree playbook for handling subscription cancellation conversations. The playbook must maximize retention without sacrificing trust, flow from discovery through resolution, and provide usable scripts for live support conversations.

## Context

**Product:** {{product}}

**Available plans:** {{plan-tiers}}

**Cancellation policy:** {{cancellation-policy}}

**Retention offers available:** {{retention-offers}}

**Top cancellation reasons:** {{top-cancel-reasons}}

Most cancellations mask fixable issues: pricing misalignment, feature confusion, poor onboarding, or timing problems. The chat window is the last touchpoint. Every conversation either saves a relationship or ensures the customer might return later.

## Output

Structure the playbook as five branches:

### Branch 1: Reason Discovery

Provide three diagnostic approaches calibrated to different customer communication styles (direct, hesitant, frustrated). Each approach should uncover the real cancellation reason without creating friction.

Include:
- Opening scripts that invite honest feedback
- Follow-up questions that distinguish stated reasons from actual problems
- Decision points: IF customer states [reason type], THEN route to corresponding Branch 2 response

### Branch 2: Targeted Retention

For each cancellation reason in {{top-cancel-reasons}}, provide:
- A specific retention response that directly addresses that concern
- The precise counter-offer or solution from {{retention-offers}} that matches the problem
- Estimated retention success rate benchmark in parentheses (e.g., "Pause offer: 45% retention")
- Decision point: IF customer accepts, proceed to Branch 3; IF customer declines, proceed to Branch 4

**Rules:** One targeted solution per message. No generic "we'd hate to see you go" language. Never stack multiple offers. Never ask "are you sure?" more than once.

### Branch 3: Customer Accepts Retention Offer

For each retention tool in {{retention-offers}}, provide:
- Confirmation message script
- Clear implementation steps
- What changes immediately and what stays the same
- How to reach support if issues arise

### Branch 4: Customer Declines and Proceeds

Provide the cancellation processing script that covers:
- What happens to their account and data
- When access ends (reference {{cancellation-policy}})
- How to reactivate if they change their mind
- No guilt-tripping; respect the decision immediately

### Branch 5: Post-Cancellation

Provide two templates:
1. **Immediate farewell message** that preserves goodwill and confirms cancellation details
2. **30-day win-back message** that re-engages without pressure, mentioning relevant product improvements or addressing their original cancellation reason

---

**Format:** Use clear headings for each branch and scenario. Present agent scripts in quotation marks. Mark decision points as "IF [condition], THEN [action]". Include retention benchmarks in parentheses. Use bullet points for next steps. Make the flow visual and navigable for live conversations.
```

## 用法 / Usage
- 必填變數 / Variables: {{cancellation-policy}}、{{plan-tiers}}、{{product}}、{{retention-offers}}、{{top-cancel-reasons}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Subscription Cancellation Retention Chat Script is a free AI prompt that builds a diagnostic conversation …
