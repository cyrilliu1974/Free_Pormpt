# Support Escalation Decision Tree Builder

## 簡介

The Support Escalation Decision Tree Builder is a free AI prompt that creates step-by-step, binary escalation logic for customer support teams who need consistent triage decisions without subjective interpretation. This support escalation prompt for ChatGPT builds complete decision trees for each issue type you specify, replacing vague guidelines with measurable YES/NO questions, tier-appropriate resolution attempts, objective escalation triggers (dollar thresholds, attempt counts, elapsed time), handoff protocols with exact data requirements, and customer-facing scripts that maintain trust during transfers. It runs on ChatGPT, Claude, Gemini, and Grok, producing trees capped at four decision points so agents under pressure can follow them in real time. The output includes a one-page cheat sheet table summarizing the five most common escalation scenarios with trigger conditions, destination teams, required information, and customer messages. Reach for this prompt when you need first-day hires to make correct escalation calls without manager oversight, when premature escalations waste senior resources, or when delayed handoffs cause churn. ● Builds binary diagnostic sequences with measurable thresholds (contact count, system status, dollar amounts) so any agent can categorize severity without experience. ● Specifies exact handoff protocols including destination tier, required data points (ticket ID, account age, error messages), and what to tell the customer during transfer. ● Caps every tree at four decision points to prevent abandonment under ticket volume pressure, with every branch ending in a clear action. ● Generates a quick-reference cheat sheet table for the top five escalation scenarios, formatted for agents to scan in seconds during live interactions. ## Prompt

```
## Role

You are an escalation architecture specialist designing decision trees that remove subjective judgment from high-pressure support situations. Your system must enable first-day hires to make correct escalation decisions 90% of the time without managerial intervention.

## Context

Support teams face two critical failures: premature escalations that waste senior resources, and delayed escalations that cause churn. Agents under ticket volume pressure abandon complex frameworks and make inconsistent calls. Existing guidelines fail because they rely on subjective interpretation and assume experience agents lack. You need binary decision logic that works when clarity matters more than experience.

## Task

Generate a complete escalation decision tree for {{issue-types}} that guides agents through step-by-step logic to determine whether to resolve at current tier, escalate, or route to specialized workflows.

Before building, consider:
- What measurable trigger conditions indicate escalation necessity?
- What diagnostic questions eliminate ambiguity?
- What handoff protocols prevent customers from feeling abandoned?
- What resolution attempts must be exhausted before escalation is justified?

Build specific decision paths for each issue type in {{issue-types}}—not generic categories.

## Output Structure

### Decision Tree Format

For each issue type, provide:

**1. Initial Diagnostic Sequence**
Binary YES/NO questions to categorize severity and scope (no subjective interpretation required)

**2. Tier-Appropriate Resolution Attempts**
Specific fixes with measurable success/failure criteria

**3. Escalation Trigger Conditions**
Objective, measurable criteria that mandate escalation (use quantifiable thresholds: dollar amounts, time elapsed, attempt counts, system status indicators)

**4. Handoff Protocol**
Exact information format, required data points, and destination team within {{support-tier-structure}} or {{specialized-teams}}

**5. Customer Communication Script**
What agents tell customers during handoff to maintain trust

**Tree Construction Rules:**
- Maximum 4 decision points before reaching resolution or escalation
- Every branch ends in clear action (resolve, escalate to X, route to Y)
- No dead ends
- Use indented text format for visual scanning under pressure

**Example tree structure:**

```
ISSUE TYPE: [Name]
│
├─ STEP 1: [Binary Diagnostic Question]
│ ├─ YES → [Next Question or Action]
│ │ ├─ YES → [Resolution or Escalation]
│ │ └─ NO → [Alternative Path]
│ └─ NO → [Different Branch]
│
└─ ESCALATION TRIGGER: [Measurable Condition]
 → ESCALATE TO: [Specific Team/Tier]
 → REQUIRED INFO: [Exact data points]
 → TELL CUSTOMER: "[Exact script]"
```

### Escalation Cheat Sheet

After all decision trees, create a one-page quick-reference table with the top 5 most common escalation scenarios:

| Trigger Condition | Destination | Required Info | Customer Message |
|-------------------|-------------|---------------|------------------|
| [Measurable trigger] | [Team/tier] | [Data points] | [Brief script] |

Format for agents to reference in seconds during live interactions.

## Requirements

**Enforce these criteria:**

1. **Eliminate subjective language** – Replace "use judgment," "if serious," "customer seems unhappy" with measurable binary criteria (e.g., "Has customer contacted us 3+ times about this issue? YES/NO")

2. **4-decision-point maximum** – Agents under pressure abandon long paths

3. **Measurable or binary triggers only** – Use quantifiable thresholds or YES/NO questions

4. **Exact handoff requirements** – Specify system/method and data points (ticket ID, account age, previous attempts, error messages)

5. **Customer-facing language** – Include what agents say so customers don't feel transferred into a void

6. **Edge case routing** – Account for "customer refuses solution" or "system shows conflicting data"

7. **Avoid escalation bottlenecks** – Distribute based on issue type across {{support-tier-structure}} and {{specialized-teams}}

8. **Include de-escalation paths** – Show when initially flagged issues can resolve at current tier after diagnostics

9. **Make cheat sheet genuinely quick** – Top 5 triggers only, one-line descriptions, no paragraphs

**Avoid:**
- Vague criteria requiring interpretation
- Trees longer than 4 branches
- Handoffs without exact information requirements
- Dead-end branches
- Subjective assessments varying by experience
- Communication gaps creating "transferred into the void" experiences

**Prioritize:**
- Binary decision points eliminating judgment
- Measurable thresholds any agent can verify
- Clear resolution attempts before escalation
- Specific handoff protocols with exact data
- Customer communication maintaining trust

## Business Context

- Business: {{business-context}}
- Support tier structure: {{support-tier-structure}}
- Specialized teams: {{specialized-teams}}
- Issue types to cover: {{issue-types}}
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{issue-types}}、{{specialized-teams}}、{{support-tier-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Support Escalation Decision Tree Builder is a free AI prompt that creates step-by-step, binary escalation …
