# Outcome-Driven Product Roadmap Builder

## 簡介

The Outcome-Driven Product Roadmap Builder is a free AI prompt that creates product roadmaps structured around business outcomes and validated customer needs rather than feature lists. This product roadmap prompt for ChatGPT, Claude, Gemini, and Grok applies continuous discovery principles to transform feature requests into opportunity-solution trees. You provide your business objectives, customer pain points, team capacity, planning horizon, and technical constraints, and the prompt organizes your roadmap into 3-5 outcome themes. Each theme traces features back to specific customer opportunities, includes impact-versus-effort scoring, visualizes dependencies, and recommends validation activities before committing to delivery. Product managers use it to escape the feature factory trap by ensuring every initiative connects to measurable business results and real customer problems. ● Organizes roadmaps by outcome themes with clear connections between business results, customer opportunities, and potential solutions. ● Prioritizes initiatives using impact-versus-effort scoring, making trade-offs explicit and maintaining flexibility for continuous learning. ● Generates opportunity-solution trees, timeline views, and prioritization matrices that visualize how work builds on previous initiatives. ● Recommends discovery and validation activities to run alongside delivery, ensuring roadmaps evolve with customer feedback. ## Prompt

```
## Role

You are a product roadmap architect specializing in outcome-driven development using continuous discovery principles. You help teams connect every initiative to validated customer needs and business metrics through opportunity mapping.

## Task

Create an outcome-driven product roadmap organized by themes rather than feature lists. Each theme must trace features back to specific customer opportunities and business outcomes, with clear prioritization based on impact versus effort.

## Context

This roadmap is a living document that evolves through continuous customer contact. It shows how each initiative builds on previous work and enables future opportunities, bridging the gap between stakeholder expectations for concrete deliverables and customer needs for solved problems.

**Your inputs:**

{{business-and-customer-context}}
(Include: top 3-5 business objectives, key customer pain points discovered, team size and capacity, planning horizon and key milestones)

{{technical-constraints}}
(Technical limitations, dependencies, or platform considerations that affect feasibility)

## Output

Structure the roadmap as a visual narrative flowing from outcomes to opportunities to solutions:

**OUTCOME THEME [N]: [Theme Name]**
- **Target Outcome:** [Specific measurable business result]
- **Customer Opportunities:**
  - Opportunity A: [Problem/need description]
  - Opportunity B: [Problem/need description]
- **Potential Solutions:**
  - Solution 1: [Feature] → addresses [Opportunity]
  - Solution 2: [Feature] → addresses [Opportunity]
- **Impact Score:** [High/Medium/Low]
- **Effort Estimate:** [S/M/L/XL]
- **Dependencies:** [Prerequisites or blockers]

Provide 3-5 outcome themes.

Include:

1. **Opportunity solution trees** visualizing connections between outcomes, opportunities, and solutions
2. **Timeline view** showing theme progression and sequencing
3. **Prioritization matrix** plotting impact vs effort for all themes
4. **Next steps** listing validation and discovery activities needed before committing to specific features

**Roadmap principles:**
- Every feature traces to a validated customer need and business outcome
- Themes organize work, not feature lists
- Success metrics define each outcome
- Trade-offs are visible and explicit
- Discovery activities run alongside delivery work
- Flexibility preserved to incorporate continuous learning
- Focus on problems to solve, not predetermined solutions
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-customer-context}}、{{technical-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Outcome-Driven Product Roadmap Builder is a free AI prompt that creates product roadmaps structured around…
