# Business Process Waste Elimination Prompt

## 簡介

The Business Process Waste Elimination Prompt is a free AI prompt that analyzes workflows to identify inefficiencies, quantify waste, and deliver actionable optimization recommendations for business process analysts and operations managers. This workflow optimization prompt for ChatGPT walks through any business process step-by-step, examining time efficiency, resource utilization, and productivity barriers. It produces a structured markdown table with three columns - Current Process, Identified Waste, and Optimized Process - covering 5-8 process steps with bottleneck identification, root cause analysis, and implementation considerations. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting two variables: a process description and specific optimization focus areas (time management, cost reduction, resource allocation). Real-world applications include manufacturing line analysis, customer onboarding streamlining, procurement cycle reduction, and administrative task consolidation. Reach for this prompt when you need to document inefficiencies in an existing workflow and present improvement recommendations to stakeholders in a clear, comparable format. ● Maps each process step against inefficiencies and proposes specific alternatives ● Quantifies waste in time, resources, and cost rather than generic observations ● Outputs a side-by-side comparison table that clarifies before-and-after states for stakeholder review ● Includes implementation considerations to bridge analysis and execution ## Prompt

```
## Role
You are an expert business process analyst specializing in workflow optimization and waste elimination.

## Task
Analyze the specified business process to identify inefficiencies and waste, then propose concrete optimization solutions. Work systematically through each process step, examining time efficiency, resource utilization, and productivity barriers.

## Context
Business process: {{process-description}}

Focus areas: {{optimization-focus}}

## Output
Present your analysis in a markdown table with three columns:

| Current Process | Identified Waste | Optimized Process |
|----------------|------------------|-------------------|

Each row should represent a distinct step or aspect of the business process. Include:
- Specific bottlenecks and their root causes
- Quantifiable waste (time, resources, cost)
- Actionable recommendations with expected improvements
- Implementation considerations

Provide 5-8 process steps with analysis depth appropriate to the complexity described.
```

## 用法 / Usage
- 必填變數 / Variables: {{optimization-focus}}、{{process-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Business Process Waste Elimination Prompt is a free AI prompt that analyzes workflows to identify ineffici…
