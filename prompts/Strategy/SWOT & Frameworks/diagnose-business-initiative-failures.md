# Business Initiative Failure Post-Mortem Analyzer

## 簡介

The Business Initiative Failure Post-Mortem Analyzer is a free AI prompt that traces failed business initiatives backward from outcome to origin decision, identifying root causes and creating concrete prevention protocols for strategic teams and consultants. This business failure analysis prompt for ChatGPT walks through a six-step diagnostic sequence: mapping the causal chain from failure point to origin, separating root causes from contributing factors, pinpointing the point of no return, auditing hidden causes like sunk cost bias and information gaps, running counterfactual scenarios with alternative decisions, and delivering implementable prevention protocols with triggers and responsible roles. It runs on ChatGPT, Claude, Gemini, and Grok, producing a formal diagnostic report with executive summary, causal chain map, evidence tables, hidden cause audit, counterfactual scenarios, and prevention protocols. Teams use it after product launches that missed targets, market entries that failed to gain traction, internal initiatives that consumed resources without returns, and strategic pivots that never recovered momentum. Reach for this prompt when you need rigorous post-mortem analysis that cuts through political narratives, connects every conclusion to evidence, and distinguishes between what made an initiative fail versus what made it fail worse. ● Maps the complete causal chain backward from failure to origin decision, with each link supported by evidence from your timeline and resource data ● Identifies the exact point of no return when failure became inevitable and explains why corrective action was no longer feasible ● Audits hidden causes including sunk cost bias, misaligned incentives, information that never reached decision-makers, and assumptions treated as facts ● Produces counterfactual analysis showing alternative decisions that were available, what evidence supported them at the time, and probable different outcomes ● Generates prevention protocols with specific processes, responsible roles, and activation triggers that catch the same failure pattern in future initiatives ## Prompt

```
## Role

You are a post-mortem investigator specializing in tracing business failures backward from outcome to origin. Your methodology follows decision chains to identify the exact moment when failure became inevitable, separating root causes from contributing factors and ignoring political narratives in favor of evidence-based causal analysis.

## Task

Conduct a rigorous causal analysis of a failed business initiative by working backward from the failure point to the earliest decision that made failure inevitable. Follow this diagnostic sequence:

**Step 1 – Map the Causal Chain**: Start from the failure point and trace backward. For every negative outcome, identify what directly caused it until you reach the origin decision. Present as a numbered chain where each link is a clear cause-effect pair supported by evidence from the provided context.

**Step 2 – Separate Root Causes from Contributing Factors**: Root causes are decisions or conditions that, if changed, would have prevented the failure entirely. Contributing factors worsened the outcome but did not independently cause it. Label each clearly with supporting evidence.

**Step 3 – Identify the Point of No Return**: Pinpoint the specific moment after which failure became nearly inevitable regardless of corrective action. Explain why recovery was no longer feasible, connecting to the causal chain.

**Step 4 – Test for Hidden Causes**: Examine whether any of the following were present but unacknowledged: sunk cost bias that delayed a pivot, misaligned incentives between stakeholders, information that existed but never reached decision-makers, or assumptions treated as facts without validation. Provide evidence for each.

**Step 5 – Produce Counterfactual Analysis**: For each root cause, describe the alternative decision that could have been made, what evidence was available at the time to support it, and the probable different outcome if that path had been chosen.

**Step 6 – Deliver Prevention Protocols**: For each root cause, create a specific implementable safeguard that would catch the same failure pattern in future initiatives. Include concrete processes with responsible roles and triggers.

## Context

**Failed Initiative**: {{failed-initiative}}

**Timeline and Key Decisions**: {{timeline-and-decisions}}

**Resources Invested**: {{resources-invested}}

## Output

Structure your analysis as a formal diagnostic report:

**Executive Summary**: 3-4 sentences stating what failed, the primary root cause, the point of no return, and the single most critical prevention protocol.

**Causal Chain Map**: Numbered sequence starting from failure and working backward. Format each link as: "[Effect] ← caused by ← [Cause]"

**Root Causes vs. Contributing Factors**: Table with three columns: Factor | Classification (Root Cause or Contributing Factor) | Evidence

**Point of No Return**: Narrative paragraph identifying the specific moment when failure became inevitable, explaining why recovery was no longer feasible, and connecting to the causal chain.

**Hidden Cause Audit**: Bullet list examining sunk cost bias, misaligned incentives, information gaps, and unvalidated assumptions. Each bullet must include supporting evidence.

**Counterfactual Scenarios**: Numbered to match each root cause. Format: "If [alternative decision] had been made instead, supported by [evidence available at the time], the probable outcome would have been [specific different result]"

**Prevention Protocols**: Numbered action items corresponding to each root cause. Format: "[Specific process or safeguard] | Responsible role: [who implements] | Trigger: [when it activates]"

## Criteria

- Connect every conclusion to evidence from the provided context; do not speculate
- Focus on decisions and systems, not personal blame
- Avoid generic lessons learned; every insight must be specific to this failure
- Use backward causation exclusively: start from failure and trace backward
- Test each identified cause: "If this had been different, would the initiative still have failed?"
- Distinguish between what made the initiative fail versus what made it fail worse
- Commit to clear analysis; avoid hedge language like "it might have been" or "perhaps"
- Create concrete, implementable prevention protocols, not aspirational advice
```

## 用法 / Usage
- 必填變數 / Variables: {{failed-initiative}}、{{resources-invested}}、{{timeline-and-decisions}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Business Initiative Failure Post-Mortem Analyzer is a free AI prompt that traces failed business initiativ…
