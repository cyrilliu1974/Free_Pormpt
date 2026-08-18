# Licensing Proposal Comparison & Analysis Prompt

## 簡介

The Licensing Proposal Comparison & Analysis Prompt is a free AI prompt that evaluates multiple intellectual property licensing offers across five critical deal dimensions for businesses, legal teams, and IP managers. This licensing proposal analysis prompt for ChatGPT systematically compares royalty rates, advance payments, territorial coverage, exclusivity provisions, performance requirements, term length, indemnification clauses, and liability limitations. It produces structured markdown comparison tables, calculates financial outcomes under low, medium, and high revenue scenarios, and delivers ranked recommendations based on strategic value and risk-adjusted returns. Built to run on ChatGPT, Claude, Gemini, and Grok, the prompt turns complex multi-party licensing negotiations into clear, decision-ready analysis. Use it when evaluating trademark licenses, patent licensing deals, technology transfers, or content licensing agreements where side-by-side comparison of material terms is essential. ● Creates side-by-side markdown tables comparing financial terms, scope of rights, restrictions, duration, and risk allocation across all proposals ● Calculates total cost and net revenue projections under three performance scenarios to model financial impact ● Assesses competitive positioning, strategic alignment, and risk-reward trade-offs for each deal structure ● Delivers numbered, ranked recommendations ordered by strategic value with specific rationale for each option ## Prompt

```
## Role

You are an expert licensing attorney specializing in intellectual property transactions, with deep experience analyzing licensing agreements across multiple industries.

## Task

Conduct a comprehensive comparative analysis of the licensing proposals provided. Systematically evaluate each proposal across five critical dimensions:

1. **Financial terms** – royalty rates, advance payments, minimum guarantees, payment structures
2. **Scope of rights** – territorial coverage, field of use limitations, exclusivity provisions
3. **Restrictions and obligations** – performance requirements, reporting obligations, operational constraints
4. **Duration and termination** – term length, renewal options, exit clauses
5. **Risk allocation** – indemnification, insurance requirements, liability limitations

For each dimension, create side-by-side comparison tables highlighting material differences. Calculate financial implications of different royalty structures under low, medium, and high revenue scenarios. Assess competitive advantages and disadvantages of each deal's scope. Evaluate risk exposure and mitigation strategies.

## Context

{{proposals-and-context}}

## Output

Structure your analysis as follows:

1. **Comparison tables** (markdown format) – one table per dimension, showing all proposals side-by-side
2. **Financial impact analysis** – detailed calculations showing total cost and net revenue under low, medium, and high performance scenarios
3. **Strategic assessment** – competitive positioning, risk-reward trade-offs, alignment with stated business priorities
4. **Ranked recommendations** – numbered list ordered by strategic value and risk-adjusted returns, with specific rationale for each ranking

Highlight the most favorable deal structure based on the business priorities and risk tolerance described in the context.
```

## 用法 / Usage
- 必填變數 / Variables: {{proposals-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Licensing Proposal Comparison & Analysis Prompt is a free AI prompt that evaluates multiple intellectual p…
