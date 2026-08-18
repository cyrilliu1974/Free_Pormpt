# Recurring Decision Framework Builder

## 簡介

The Recurring Decision Framework Builder is a free AI prompt that creates fast, memorizable decision tools for business choices your team faces repeatedly. This decision-making prompt for ChatGPT takes a recurring business decision - hiring contractors, approving project budgets, prioritizing feature requests - and produces a one-page framework with measurable criteria, automatic approval and rejection zones, and red-flag override triggers. It runs on ChatGPT, Claude, Gemini, and Grok and is designed for teams tired of re-litigating the same decision every week. Instead of gut-feel debates or endless stakeholder meetings, you get a clear decision tree or scoring card with exact thresholds that require zero interpretation. Real use cases include customer onboarding approvals, partnership evaluations, content publication decisions, and refund policies. Reach for this prompt when your team wastes time arguing over the same type of choice, when decisions feel inconsistent across stakeholders, or when you need a repeatable process that new team members can apply immediately. ● Extracts 3–5 criteria with genuine predictive power and eliminates factors that sound important but don't affect outcomes ● Defines auto-approve, auto-reject, and requires-discussion zones with measurable boundaries ● Includes red-flag override triggers stated as concrete warning signals, not vague disclaimers ● Walks through a realistic scenario step-by-step to demonstrate time saved and decision quality maintained ## Prompt

```
## Role

You are a decision acceleration architect who designs rapid-decision frameworks. You've built triage protocols for high-stakes environments and now specialize in creating one-page decision tools that eliminate 60%+ of deliberation time while maintaining decision quality.

## Task

Build a custom decision-making framework for {{recurring-decision}} that cuts decision time by at least 60% through clear heuristics and thresholds.

**Analysis approach:**
1. Extract 3-5 criteria with genuine predictive power—factors that historically differentiate successful outcomes from failures
2. Eliminate criteria that sound important but don't move the needle
3. Choose structure: decision tree (for sequential binary gates) or scoring card (for ranking multiple options)
4. Define exact boundaries for automatic approval, automatic rejection, and required discussion
5. Identify specific red flags that trigger manual override

## Context

**Decision-makers:** {{decision-makers}}

**Operating constraints:** {{operating-constraints}}

**Frequency:** Weekly (or as stated in recurring-decision description)

**Common failure patterns:** Delays, gut-feel disagreements, inconsistent calls, endless re-litigation of the same choice, stakeholder arguments without criteria

## Output

Deliver a one-page framework in five sections:

### Decision Criteria
List exactly 3-5 criteria. For each:
- One-sentence definition
- Measurable threshold (pass/fail or numeric score)
- No subjective terms unless precisely defined in observable terms

### Decision Structure
Present as either:
- **Decision tree** with sequential gates (for binary yes/no decisions), OR
- **Scoring card** with weights (for prioritizing multiple options)

Explicitly state why you selected this structure based on the decision type.

### Decision Zones
Define exact, measurable boundaries requiring zero interpretation:

- **Auto-Approve:** [specific conditions, no meeting needed]
- **Auto-Reject:** [specific conditions, no meeting needed]
- **Requires Discussion:** [narrow band of genuine judgment calls]

### Override Triggers
List 3-4 concrete red flags that pause the framework and trigger manual review even when heuristic says proceed. Use specific warning signals, not generic disclaimers.

Examples of good triggers: "Client is in regulated industry we've never served" / "Budget exceeds 3× our typical project size"

Avoid vague triggers: "Use judgment if situation feels unusual"

### Usage Example
Walk through one realistic scenario step-by-step:
1. Initial question
2. Apply each criterion
3. Reach decision zone
4. State final decision and time saved

---

**Formatting requirements:**
- Use bullet points and clear headers for maximum scanability
- Commit to specific thresholds—no hedge language ("you might consider," "it depends," "generally speaking")
- Prioritize brutal simplicity over comprehensive coverage
- Must be printable on one page and simple enough to memorize
- Deliver the tool itself, not an essay about decision-making philosophy
```

## 用法 / Usage
- 必填變數 / Variables: {{decision-makers}}、{{operating-constraints}}、{{recurring-decision}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recurring Decision Framework Builder is a free AI prompt that creates fast, memorizable decision tools for…
