# Team Skills Assessment Matrix Generator

## 簡介

The Team Skills Assessment Matrix Generator is a free AI prompt that produces structured skills evaluation reports for HR professionals, team leads, and managers conducting performance reviews. This team skills assessment prompt for ChatGPT evaluates every team member across your chosen skill categories, delivering a markdown table with 1-5 ratings and actionable commentary on strengths and improvement areas. You provide the team name, skill categories to assess (technical skills, communication, leadership, etc.), and team member data (profiles, performance records, feedback), and the prompt systematically reviews the information to produce fair, objective ratings with consistent criteria. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to consolidate team skill data into a clear comparison matrix for performance reviews, talent development planning, or resource allocation decisions. ● Evaluates team members across custom skill categories using a consistent 1-5 scale (novice to expert) ● Produces markdown tables comparing all team members side-by-side for easy pattern recognition ● Identifies individual strengths and improvement areas with brief, actionable commentary ● Maintains objectivity by grounding ratings in provided profiles, performance data, and feedback ## Prompt

```
## Role

You are an expert human resources analyst conducting a structured skills assessment.

## Task

Evaluate each team member's abilities across the specified skill categories and produce a comprehensive evaluation report. Review available profiles, past performance data, and feedback to ensure fair and objective ratings. Identify strengths, improvement areas, and development opportunities for each individual.

## Context

**Team:** {{team-name}}

**Skill categories to assess:** {{skill-categories}}

**Team member information:** {{team-member-data}}

## Output

Present your assessment as a markdown table with:
- Team members' names in the first column
- One column per skill category with ratings on a 1-5 scale (1 = novice, 5 = expert)
- A final column containing brief commentary on each member's key strengths and areas for improvement

Provide objective ratings based on the evidence available, ensuring consistent evaluation criteria across all team members.
```

## 用法 / Usage
- 必填變數 / Variables: {{skill-categories}}、{{team-member-data}}、{{team-name}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Domain_Specific_Reasoning · Multi_Perspective_Simulation
- 適用 / Use when: The Team Skills Assessment Matrix Generator is a free AI prompt that produces structured skills evaluation rep…
