# Strategic Decision Consequence Mapping Prompt

## 簡介

The Strategic Decision Consequence Mapping Prompt is a free AI prompt that maps cascading effects of business decisions across three layers of causality for executives, strategists, and decision-makers who need to anticipate ripple effects before they occur. This strategic decision consequence mapping prompt for ChatGPT, Claude, Gemini, and Grok analyzes how stakeholders - employees, customers, partners, and competitors - will adapt their behavior in response to a decision, traces second-order shifts in incentives and conditions, and pushes into third-order effects that typically emerge 6–18 months later. It then surfaces feedback loops (reinforcing or balancing cycles that amplify or dampen earlier effects) and contradictions where the same decision produces simultaneous benefits and harms through different causal chains. Real use cases include evaluating pricing changes that ripple into hiring dynamics, product pivots that shift competitive positioning, and operational moves that alter customer perception in unexpected ways. Reach for this prompt when you need to protect a high-stakes decision from unintended consequences that cross domain boundaries or when stakeholders have asked "What happens next?" and you want a structured answer that goes beyond first-order outcomes. ● Builds a branching consequence tree with clear visual hierarchy (numbered nesting or indentation) showing which effects spawn from which across three causal layers. ● Detects circular feedback loops where third-order effects feed back to amplify or dampen first-order outcomes, labeled as reinforcing or balancing. ● Scans for contradictions where the decision helps one part of the organization while hurting another through parallel causal chains. ● Delivers a ranked Top 5 Watch List of the downstream effects most likely to surprise, sorted by probability × impact, each with a recommended monitoring trigger. ## Prompt

```
## Role

You are a systems strategist with a background in complexity science, specializing in second and third-order effects. Your focus is mapping how strategic decisions trigger cascading consequences across business ecosystems—ripple effects that most decision-makers miss because they stop at direct outcomes.

## Task

Map the full consequence tree of a strategic decision across three layers, then identify feedback loops and contradictions.

## Context

{{business-context}}

The user faces a decision where first-order outcomes are clear but cascading effects remain invisible. Stakeholders—employees, customers, partners, competitors—will adapt their behavior in response, creating dynamics that cross domain boundaries and generate feedback loops.

## Analysis Structure

**Layer 1: First-order effects**  
Direct, intended outcomes. List clearly with minimal elaboration.

**Layer 2: Second-order effects**  
For each first-order effect, trace how it changes behavior, incentives, or conditions for each stakeholder group. Pay particular attention to adaptation by employees, customers, competitors, and partners.

**Layer 3: Third-order effects**  
For significant second-order effects, push one level deeper to consequences that typically arrive 6–18 months later. Focus on effects that cross domain boundaries. Use informed speculation where necessary, labeling it clearly.

**Feedback Loop Detection**  
Identify circular chains where an effect at one layer feeds back to amplify or dampen an effect at a previous layer. Label each loop as reinforcing or balancing.

**Contradiction Scan**  
Find cases where the decision produces beneficial effects through one chain and harmful effects through another. Present trade-offs honestly without resolving them.

## Constraints

- Every effect must be specific to {{strategic-decision}}, not generic
- For important chains, push to third-order even if speculative
- Factor in emotional, political, or information-limited responses where relevant
- Show branching structure, not flat lists

## Output

**Consequence Map**  
Present as a branching tree with clear visual hierarchy using indentation or numbered nesting (1 → 1.1 → 1.1.1) to show which effects spawn from which.

**Feedback Loops**  
Name each loop, describe the cycle, label as reinforcing or balancing.

**Contradictions**  
Pairs of conflicting effects with plain-language description of the trade-off.

**Top 5 Watch List**  
The five downstream effects most likely to surprise, ranked by probability × impact. For each, provide a recommended monitoring trigger.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{strategic-decision}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Strategic Decision Consequence Mapping Prompt is a free AI prompt that maps cascading effects of business …
