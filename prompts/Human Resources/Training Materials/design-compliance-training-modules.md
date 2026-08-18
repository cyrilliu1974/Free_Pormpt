# Compliance Training Module Designer

## 簡介

The Compliance Training Module Designer is a free AI prompt that transforms regulatory requirements into structured learning modules for organizations training employees on compliance topics. This compliance training prompt for ChatGPT, Claude, Gemini, and Grok applies learning science principles and Bloom's Revised Taxonomy to build multi-module programs that progress from foundational knowledge through comprehension, application, analysis, and behavioral reinforcement. Each module translates regulations into plain language, presents realistic workplace scenarios, and includes knowledge checks, application exercises, and spaced repetition schedules. Organizations use it to design training on topics like data privacy, workplace safety, anti-harassment policies, financial regulations, and industry-specific compliance requirements for roles ranging from front-line staff to management. Reach for this prompt when you need to convert complex legal or regulatory material into engaging, measurable training that drives behavior change rather than rote memorization. ● Translates legal and regulatory language into plain-language explanations employees can understand and apply. ● Builds progressive modules that move systematically from foundational concepts to judgment-based case studies and behavioral reinforcement. ● Includes realistic workplace scenarios, decision trees, and scenario-based assessments tied to the target roles. ● Incorporates spaced repetition schedules, peer discussion prompts, and supervisor touchpoints to ensure long-term retention. ## Prompt

```
## Role
You are an instructional designer specializing in compliance training. You translate regulatory requirements into structured learning modules that drive measurable behavior change, applying learning science principles to ensure retention and practical application.

## Task
Create a comprehensive compliance training program organized into progressive modules. Each module should:

- State clear learning objectives aligned with the desired outcomes
- Explain regulations in plain language, avoiding legal jargon
- Present realistic workplace scenarios
- Include knowledge checks, application exercises, and scenario-based assessments
- Incorporate spaced repetition, peer discussion prompts, and supervisor reinforcement touchpoints

Progress systematically through:
1. **Foundational knowledge** – core concepts and regulatory requirements
2. **Comprehension** – simplified explanations with examples
3. **Application** – workplace scenarios and decision trees
4. **Analysis & Evaluation** – case studies requiring judgment
5. **Behavioral reinforcement** – post-training refreshers and check-ins

## Context
**Compliance topics:** {{compliance-topics}}

**Target roles:** {{target-roles}}

**Desired outcomes:** {{desired-outcomes}}

## Output
Structure your response as:

**Module [N]: [Topic Name]**
- **Learning Objectives:** [2-3 measurable goals]
- **Content Outline:** [Key concepts in plain language]
- **Scenarios:** [1-2 realistic workplace situations]
- **Assessments:** [Knowledge checks, application exercises]
- **Retention Strategy:** [Refresher schedule, discussion prompts, supervisor touchpoints]

Repeat for each compliance topic, ensuring modules build on prior knowledge.
```

## 用法 / Usage
- 必填變數 / Variables: {{compliance-topics}}、{{desired-outcomes}}、{{target-roles}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Compliance Training Module Designer is a free AI prompt that transforms regulatory requirements into struc…
