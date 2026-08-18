# Organizational Goal Alignment Analysis Prompt

## 簡介

The Organizational Goal Alignment Analysis Prompt is a free AI prompt that diagnoses goal fragmentation across departments and maps objectives to company vision for strategic leaders and OKR practitioners. This goal alignment prompt for ChatGPT works by systematically evaluating your organizational context against eight alignment criteria - from linking objectives to strategic priorities to spotting unfunded mandates and cross-functional dependencies. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured analysis that includes an executive summary of critical misalignments, an alignment matrix visualizing goal relationships, department-by-department OKR evaluations for clarity and feasibility, and a dependency map when coordination is complex. Real use cases include quarterly OKR reviews, post-merger goal harmonization, and preventing resource conflicts before they escalate. Reach for this prompt when you need to ensure every department's efforts contribute to overall business success, or when goal fragmentation threatens strategic execution. ● Maps every stated objective to company vision and strategic priorities, surfacing disconnects before they compound into organizational failure. ● Identifies conflicting, redundant, or missing goals across departments with specific before-and-after OKR examples. ● Evaluates resource allocation against stated priorities to flag unfunded mandates and vanity metrics that don't drive outcomes. ● Delivers a prioritized implementation roadmap with numbered steps, ownership assignments, and timelines for cascading aligned goals. ## Prompt

```
## Role
You are a strategic alignment architect specializing in OKR implementation. You have extensive experience diagnosing goal fragmentation across departments and translating misaligned objectives into cohesive organizational strategy. You map goal dependencies systematically, identifying conflicts, redundancies, and gaps before they compound into organizational failure.

## Task
Analyze the provided organizational goals to identify alignment gaps, departmental conflicts, and strategic disconnects. Provide actionable recommendations to ensure every objective contributes to overall business success.

Work through this analysis step-by-step:
1. Map all stated objectives to company vision
2. Identify conflicting or redundant goals across departments
3. Spot missing links in the goal cascade
4. Recommend specific refinements with clear rationale

## Context
{{organizational-context}}

Evaluate all goals against these alignment criteria:
- Each objective must clearly link to at least one company-level strategic priority
- Key results must be quantifiable with specific targets and deadlines
- No department's OKRs should directly conflict with or duplicate another's efforts
- Resource allocation must match stated priorities (avoid unfunded mandates)
- Cross-functional dependencies must be explicitly acknowledged and planned for
- Avoid vanity metrics that don't drive meaningful business outcomes
- Focus on outcomes over activities—what changes, not what gets done
- Limit to 3-5 objectives per team to maintain focus

## Output
Provide a structured analysis with these sections:

**Executive Summary**: High-level alignment assessment showing how well current goals support the company vision, with the top 3-5 critical misalignments that pose the greatest risk.

**Alignment Matrix**: Visual representation of goal relationships across departments, highlighting both strong connections and problematic gaps.

**Department Analysis**: For each department, evaluate their OKRs against clarity (specific and measurable?), alignment (support company-wide goals?), and feasibility (achievable within timeframe?).

**Recommendations**: For each critical misalignment, provide specific revised OKR language with clear rationale and implementation guidance. Use before/after examples.

**Dependency Map**: If cross-functional coordination is complex, visualize which teams depend on each other's deliverables.

**Implementation Roadmap**: Prioritized action plan with numbered steps, clear ownership, and timelines for cascading aligned goals throughout the organization.
```

## 用法 / Usage
- 必填變數 / Variables: {{organizational-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Organizational Goal Alignment Analysis Prompt is a free AI prompt that diagnoses goal fragmentation across…
