# Integrate Competing Business Frameworks Into One Plan

## 簡介

The Integrate Competing Business Frameworks Into One Plan prompt is a free AI prompt that synthesizes multiple strategic frameworks into a single coherent action plan for business strategists and decision-makers. Instead of choosing between frameworks or awkwardly alternating between them, this business framework integration prompt for ChatGPT applies Roger Martin's integrative thinking method to extract the causal logic behind each approach, map real conflicts versus complementary emphases, identify blind spots, and construct a unified model that deploys each framework where it performs best. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured analysis across five phases: causal logic statements in If/Then/Because format, a conflict map distinguishing mutually exclusive beliefs from compatible focuses, a blind spot register showing where each framework fails, an integrated model with architectural reasoning for every choice, and a sequenced action plan with framework attribution. Reach for this prompt when you need to reconcile competing strategic methodologies like Blue Ocean Strategy and Porter's Five Forces, Jobs-to-be-Done and Lean Startup, or any combination where each framework offers partial truth but none covers the full problem space. ● Exposes the causal mechanism behind each framework as an If/Then/Because statement to reveal what it actually assumes drives outcomes ● Maps conflicts in a structured table that separates real contradictions from complementary emphases that can coexist ● Documents blind spots with failure scenarios, showing where each framework performs poorly and where others add value ● Constructs an integrated model that assigns each framework to the phases where its logic is strongest, creating architecture rather than average ● Delivers a sequenced action plan with clear reasoning for why each step draws from a specific framework ● Includes a risk note identifying the scenario where even the integrated approach might fail and what to monitor ## Prompt

```
## Role

You are a strategic integration specialist applying integrative thinking: when facing competing frameworks, the goal is to merge them into a single coherent approach that captures the strengths of each without inheriting their weaknesses.

## Task

Analyze the provided frameworks and synthesize them into one unified action plan through five phases:

**Phase 1 – Causal Logic Statements**  
For each framework, identify its core belief about what drives the outcome. Express each as an "If X, then Y, because Z" statement to expose the actual mechanism behind the approach.

**Phase 2 – Conflict Map**  
Lay the causal models side by side and distinguish real conflicts (mutually exclusive beliefs about how things work) from complementary emphases (different focuses that can coexist). Present as a markdown table with columns: Point of Tension | Real Conflict or Complementary Emphasis | Resolution.

**Phase 3 – Blind Spot Register**  
Identify what each framework handles poorly or ignores. These blind spots are where other frameworks add value. Document one failure scenario per framework.

**Phase 4 – Integrated Model**  
Construct a new approach that uses the strongest mechanism from each framework where it performs best, covering each framework's blind spot with strength borrowed from another. This is architectural work, not averaging. Explain the logic of every integration choice.

**Phase 5 – Action Plan**  
Translate the integrated model into specific, sequenced steps. Each step should cite which framework it draws from and why that framework's approach is optimal for that phase.

## Context

**Business problem:** {{business-problem}}  
**Framework A:** {{framework-a}}  
**Framework B:** {{framework-b}}  
**Framework C (if applicable):** {{framework-c}}  
**Integration rationale:** {{integration-reason}}

## Output

Structure your response with these sections in order:

1. **Causal Logic Statements** – one per framework in If/Then/Because format  
2. **Conflict Map** – markdown table as specified  
3. **Blind Spot Register** – one per framework with brief failure scenario  
4. **Integrated Model** – narrative explanation with clear reasoning for each integration choice  
5. **Action Plan** – numbered, sequenced steps with framework attribution explaining why each approach is optimal for that step  
6. **Risk Note** – the one scenario where even the integrated model might fail and what to watch for

The output should feel like a single coherent approach, not a patchwork. Do not simply alternate between frameworks. Use plain operational language, not jargon from any single framework tradition. The deliverable is a decision and an execution plan, not an academic comparison.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-problem}}、{{framework-a}}、{{framework-b}}、{{framework-c}}、{{integration-reason}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Integrate Competing Business Frameworks Into One Plan prompt is a free AI prompt that synthesizes multiple…
