# Test Results Analysis and Intervention Planning Prompt

## 簡介

The Test Results Analysis and Intervention Planning Prompt is a free AI prompt that helps educators systematically evaluate test data and create actionable intervention strategies tailored to their classroom context. This test results analysis prompt for ChatGPT walks you through identifying performance patterns, distinguishing surface errors from conceptual gaps, and prioritizing interventions based on available resources. You provide test scores, question-level performance, error patterns, grade level, subject, class size, and resource constraints, and the prompt produces a markdown table that maps specific areas of improvement to concrete intervention strategies and measurable expected outcomes. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible across major text models. Use this prompt when you need to move beyond surface-level test score summaries and develop a coherent action plan that connects diagnostic insights to classroom practice. ● Identifies 4-6 priority learning gaps by analyzing score distributions, question-level performance, and common error patterns ● Maps each identified weakness to feasible intervention strategies based on your actual class size, materials, technology, and time allocation ● Defines measurable expected outcomes for each intervention, including score targets, mastery benchmarks, or behavioral changes ● Distinguishes between procedural errors and deeper conceptual misunderstandings to ensure interventions address root causes ## Prompt

```
## Role
You are an educational analyst specializing in test result evaluation and intervention design.

## Task
Analyze the provided test data to identify learning gaps, then develop targeted intervention strategies with measurable expected outcomes. Present your findings in a structured format that connects specific weaknesses to actionable solutions.

## Context
{{test-data-and-context}}

Include:
- Test results (scores, question-level performance, common error patterns)
- Grade level and subject
- Class size and available resources (materials, technology, support staff, time allocation)

## Analysis Approach
1. Identify patterns in student performance: which concepts, skills, or question types showed the lowest mastery
2. Distinguish between surface errors and deeper conceptual gaps
3. Consider the feasibility of interventions given your class size and resources
4. Prioritize areas by impact and urgency

## Output
Deliver your analysis as a markdown table with three columns:

| Areas of Improvement | Intervention Strategies | Expected Outcomes |
|---------------------|------------------------|-------------------|

Each row should present:
- **Areas of Improvement**: Specific skill, concept, or performance gap identified in the data
- **Intervention Strategies**: Concrete, actionable teaching methods or activities tailored to your context
- **Expected Outcomes**: Measurable improvements you anticipate (score increases, mastery benchmarks, behavioral changes)

Include 4-6 priority areas. Ensure each row forms a coherent chain from diagnosis to action to result.
```

## 用法 / Usage
- 必填變數 / Variables: {{test-data-and-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Test Results Analysis and Intervention Planning Prompt is a free AI prompt that helps educators systematic…
