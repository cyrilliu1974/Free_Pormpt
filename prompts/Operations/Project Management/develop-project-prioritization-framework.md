# Project Prioritization Framework Builder

## 簡介

The Project Prioritization Framework Builder is a free AI prompt that designs data-driven scoring systems to help organizations evaluate, rank, and sequence their project portfolios. This project prioritization prompt for ChatGPT, Claude, Gemini, and Grok delivers a complete framework including a three-factor scoring methodology (ROI, resource availability, strategic alignment), customizable weighting controls, dashboard visualization specifications, and an actionable implementation roadmap. Teams use it to move from ad-hoc project selection to systematic, repeatable portfolio decisions that balance financial return, capacity constraints, and strategic objectives. The prompt adapts to your organization's context - whether you're managing software sprints, capital investments, or cross-functional initiatives - and produces decision rules, scoring thresholds, and visual analytics designs ready for immediate deployment. Reach for this prompt when you need to standardize how projects are evaluated, justify resource allocation decisions, or align your portfolio with shifting business priorities. ● Generates three-factor scoring rubrics with clear 1-5 criteria for ROI, resources, and strategic fit ● Provides customizable weighting so organizations can shift priorities without redesigning the entire system ● Specifies dashboard layouts, chart types, and filtering capabilities for decision-support visualization ● Delivers a seven-step implementation roadmap covering stakeholder validation, data collection, piloting, and governance integration ## Prompt

```
## Role
You are an expert decision-making framework designer specializing in project portfolio optimization through data-driven prioritization systems.

## Task
Design a comprehensive project prioritization framework that enables organizations to evaluate and rank projects using multi-factor scoring, visual analytics, and strategic recommendations.

## Context
Organization details:
{{organization-context}}

Apply this context when calibrating scoring thresholds, weighting recommendations, and identifying strategic alignment patterns throughout the framework design.

## Output
Deliver a complete prioritization framework structured as follows:

**1. Multi-Factor Scoring System**
- ROI Score (1-5): Assess financial return potential and payback period
- Resource Score (1-5): Evaluate availability of budget, talent, and capacity
- Strategic Alignment Score (1-5): Measure fit with organizational objectives
- Provide customizable weighting mechanism so organizations can adjust factor importance based on current priorities

**2. Scoring Methodology**
- Define clear criteria and numeric thresholds for each score level (1-5) across all three factors
- Include decision rules for edge cases and ties
- Specify data inputs required for objective scoring

**3. Data Visualization Design**
- Interactive dashboard specifications including:
  - Comparative bar graphs for project scores
  - Resource allocation views (pie charts, stacked bars)
  - Strategic alignment matrix mapping projects against objectives
- Enable filtering, sorting, and drill-down capabilities

**4. Prioritization Recommendations**
- Rank projects by weighted composite scores
- Identify "quick wins" (high ROI, low resource demand)
- Identify "strategic bets" (high alignment, transformational impact)
- Provide guidance on portfolio balance and project sequencing

**5. Implementation Roadmap**
1. Define and validate scoring criteria with stakeholders
2. Gather and normalize project data
3. Build scoring model and visualization tools
4. Pilot framework with project subset
5. Refine based on pilot learnings
6. Integrate into existing governance processes
7. Deploy training and change management support

Ensure all components are actionable and immediately applicable to the organization's portfolio decisions.
```

## 用法 / Usage
- 必填變數 / Variables: {{organization-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Project Prioritization Framework Builder is a free AI prompt that designs data-driven scoring systems to h…
