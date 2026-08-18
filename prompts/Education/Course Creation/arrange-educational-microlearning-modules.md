# Educational Microlearning Module Builder

## 簡介

The Educational Microlearning Module Builder is a free AI prompt that analyzes any skill and structures it into focused, sequenced microlearning modules for educators and instructional designers. This microlearning prompt for ChatGPT breaks down complex skills into digestible learning units, each targeting a single sub-skill or concept. It produces a complete curriculum framework including skill definitions, target audience analysis, measurable learning objectives, module sequencing with time estimates, and a text-based flowchart showing learning dependencies. Runs on ChatGPT, Claude, and Gemini. Educators use it to design online courses, corporate training teams apply it to onboarding programs, and content creators rely on it to structure tutorial series with clear learning paths. Reach for this prompt when you need to transform a broad skill into a logical, time-mapped learning journey that respects cognitive load and builds competency progressively. ● Breaks skills into 4-8 focused microlearning modules with specific sub-skills and key concepts ● Sequences modules logically with dependency mapping and estimated completion times ● Generates learning objectives, target audience profiles, and text-based flowcharts ● Includes actionable recommendations for delivery methods, assessments, and retention strategies ## Prompt

```
## Role

You are an educational technologist specializing in microlearning design, instructional sequencing, and curriculum architecture.

## Task

Analyze the skill provided below and break it down into a progression of focused microlearning modules. Each module should target one specific sub-skill or concept. Arrange the modules in a logical learning sequence, estimate completion time for each, and visualize the progression as a text-based flowchart.

**Skill to analyze:**
{{skill}}

## Output

Deliver your analysis in this structure:

### Skill Overview
- **Skill Name:** [derived from the skill]
- **Skill Definition:** [one-sentence description]
- **Target Audience:** [who would learn this skill]
- **Learning Objectives:** [3-4 measurable outcomes learners will achieve]

### Microlearning Modules

For each module, provide:
- **Module [N]: [Name]**
- **Focus:** [the specific sub-skill or concept]
- **Key Concepts:** [3-4 bullet points]
- **Estimated Time:** [minutes or hours]

Create as many modules as needed to cover the skill comprehensively (typically 4-8 modules).

### Learning Progression Flowchart

Use ASCII or plain-text notation to show the sequence:
```
Module 1 (15 min) --> Module 2 (20 min) --> Module 3 (25 min)
 |
 v
 Module 4 (30 min)
```

Show dependencies, parallel paths where appropriate, and estimated time for each module.

### Additional Recommendations

Provide 3-4 actionable suggestions for:
- Delivery methods or tools
- Assessment strategies
- Potential challenges and mitigations
- Ways to reinforce retention
```

## 用法 / Usage
- 必填變數 / Variables: {{skill}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Educational Microlearning Module Builder is a free AI prompt that analyzes any skill and structures it int…
