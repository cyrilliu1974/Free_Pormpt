# Innovation Project Evaluation Framework Generator

## 簡介

The Innovation Project Evaluation Framework Generator is a free AI prompt that builds a structured scoring system to assess and rank innovation projects for businesses managing multiple initiatives. This innovation evaluation prompt for ChatGPT produces a four-dimension weighted framework that scores each project on strategic alignment (30%), market potential (30%), technical feasibility (20%), and resource requirements (20%). It delivers project-by-project assessments with justified scores, a ranked prioritization list, and tier-based implementation recommendations. The prompt works on ChatGPT, Claude, Gemini, and Grok, requiring only your innovation-portfolio-context to generate a complete evaluation system with scoring methodology, individual project analyses, and sequenced resource allocation guidance. Use it when you need to compare multiple innovation projects objectively, allocate budgets to high-impact initiatives, or present a data-driven case for which projects to greenlight. ● Produces a four-dimension weighted scoring model with clear 1-5 scale definitions and calculation formulas ● Generates individual project evaluations with justified scores for strategic fit, market opportunity, technical risk, and resource needs ● Ranks all projects by final weighted score and assigns priority tiers with implementation sequencing logic ● Outputs clean markdown tables for side-by-side project comparison and resource allocation planning ## Prompt

```
## Role
You are an innovation strategist specializing in technology evaluation, business strategy, and portfolio prioritization.

## Task
Create a comprehensive framework to evaluate and prioritize innovation projects. Use a weighted scoring system across four dimensions: strategic alignment, market potential, technical feasibility, and resource requirements.

## Context
{{innovation-portfolio-context}}

## Output
Deliver a structured evaluation framework containing:

### 1. Scoring Framework
Define how to assess each dimension on a 1-5 scale:

**Strategic Alignment (30% weight)**
- Business objective alignment
- Strategic value contribution
- Score rationale

**Market Potential (30% weight)**
- Target market definition
- Market size and growth trajectory
- Competitive positioning
- Score rationale

**Technical Feasibility (20% weight)**
- Technology readiness level
- Development complexity
- Key technical risks
- Score rationale

**Resource Requirements (20% weight)**
- Financial investment needed
- Team and talent requirements
- Implementation timeline
- Score rationale

### 2. Scoring Methodology
Explain the weighted calculation:
- Final Score = (Strategic × 0.30) + (Market × 0.30) + (Technical × 0.20) + (Resource × 0.20)
- Interpretation guidelines for score ranges

### 3. Project Evaluations
For each project in the portfolio, provide:
- Project name and brief description
- Strategic alignment score with justification
- Market potential score with justification
- Technical feasibility score with justification
- Resource requirements score with justification
- **Weighted average score**

### 4. Prioritization Recommendation
Rank all projects by weighted score from highest to lowest, with:
- Priority tier assignment (Tier 1: Implement now, Tier 2: Queue for next cycle, Tier 3: Reconsider or shelve)
- Resource allocation recommendations
- Implementation sequencing rationale

Format all output in clean markdown with tables for project comparisons where helpful.
```

## 用法 / Usage
- 必填變數 / Variables: {{innovation-portfolio-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Innovation Project Evaluation Framework Generator is a free AI prompt that builds a structured scoring sys…
