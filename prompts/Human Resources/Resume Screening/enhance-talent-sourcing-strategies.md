# Talent Sourcing Strategy Optimization Prompt

## 簡介

The Talent Sourcing Strategy Optimization Prompt is a free AI prompt that analyzes hiring data to identify which talent channels produce the best hires relative to investment, then recommends a rebalanced portfolio concentrating resources on high-ROI sources. This talent sourcing prompt for ChatGPT walks you through seven sequential phases: assessing your data landscape, evaluating source performance by quality metrics, calculating true cost per quality hire, applying Pareto analysis to find the vital 20% of channels delivering 80% of top talent, researching emerging platforms, designing an optimized budget allocation (80% proven, 15% high-potential, 5% experimental), and building a measurement system with tracking automation. It runs on ChatGPT, Claude, Gemini, and Grok, adapting to your available data sources, budget constraints, team size, and talent acquisition maturity. Use it when you need to move beyond vanity metrics and redirect hiring resources toward channels that consistently deliver high-performing, long-tenured employees. ● Ranks every talent source by a composite Quality Score (performance rating, retention at 6/12/24 months, and time-to-productivity) to surface which channels deliver exceptional hires. ● Calculates true cost of acquisition per source, including direct fees, time investment, opportunity costs, and turnover expenses, so you understand real ROI. ● Identifies the vital few channels using Pareto analysis, then designs a rebalanced budget allocation with quarterly review triggers and risk mitigation steps. ● Evaluates emerging channels (niche communities, skills platforms, AI matching tools) and recommends pilot programs with scalability and competitive-advantage assessments. ## Prompt

```
## Role

You are a talent acquisition analyst specializing in data-driven sourcing optimization using the Pareto Principle to identify high-ROI hiring channels.

## Task

Analyze hiring data to build a multi-phase sourcing optimization strategy. Identify which talent channels produce the best hires relative to investment, then recommend a rebalanced portfolio concentrating resources on high-ROI sources.

## Context

{{hiring-data}}

Include: available data sources (performance ratings, retention records, cost tracking, source attribution), number of hires in past 12–24 months, roles hired for, current pain points, and any data quality gaps.

{{business-constraints}}

Include: budget limits, team size, talent acquisition maturity level, industry-specific dynamics, and implementation timeline.

## Process

Work through phases sequentially. Pause after each phase and wait for "continue" before proceeding.

**Phase 1: Data Landscape Assessment**  
Review available hiring data. Identify what can be measured, flag gaps, and design a custom analysis framework suited to data quality and organizational maturity.

**Phase 2: Source Performance Analysis**  
Evaluate each talent source (job boards, referrals, agencies, social media, etc.) using:
- Performance rating distribution by source
- Retention at 6, 12, and 24 months
- Time-to-productivity
- Quality Score = (Performance Rating × Retention Rate) / Time-to-Productivity

Output a Source Performance Matrix ranking channels by quality of hire.

**Phase 3: True Cost Calculation**  
Calculate total cost of acquisition for each source, including:
- Direct costs (fees, commissions, subscriptions)
- Time investment (sourcing, screening, interviewing)
- Opportunity costs (unfilled roles, productivity loss)
- Failure costs (turnover, re-hiring)

Output True Cost per Quality Hire for each channel.

**Phase 4: Vital Few Identification**  
Apply Pareto analysis to identify the 20% of sources delivering 80% of top talent. Rank by Quality Score and cost efficiency. Highlight breakthrough performers and consistent winners across roles.

**Phase 5: Emerging Channel Evaluation**  
Research next-generation sources (niche communities, skills platforms, AI matching tools). Assess scalability, competitive advantage, integration complexity, and risk-adjusted returns. Recommend pilot programs.

**Phase 6: Portfolio Optimization**  
Design a rebalanced sourcing portfolio:
- 80% of budget to proven vital sources
- 15% to high-potential emerging channels
- 5% to experimental plays

Provide resource reallocation roadmap, quick wins, risk mitigation, and quarterly review triggers.

**Phase 7: Implementation & Measurement**  
Build tracking automation, quality measurement protocols, cost capture, and a real-time ROI dashboard. Deliver an implementation guide with monitoring tools and continuous improvement cycles.

## Output

For each phase, deliver:
- Clear findings in bullet or table format
- Actionable insights tied to business constraints
- Specific next steps or recommendations
- A prompt to type "continue" before moving to the next phase

Final deliverable: an optimized talent sourcing portfolio with implementation timeline and measurement system.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-constraints}}、{{hiring-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Talent Sourcing Strategy Optimization Prompt is a free AI prompt that analyzes hiring data to identify whi…
