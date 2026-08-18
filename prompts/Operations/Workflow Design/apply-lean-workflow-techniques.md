# Lean Workflow Optimization Prompt for Business Processes

## 簡介

The Lean Workflow Optimization Prompt for Business Processes is a free AI prompt that analyzes existing workflows, identifies waste, and designs optimized processes using proven Lean manufacturing principles for operations managers, process engineers, and business analysts. This lean workflow prompt for ChatGPT works by applying the seven wastes framework (overproduction, waiting, transport, over-processing, inventory, motion, defects) to any business process you describe. You provide the current process, industry context, and desired outcomes; the prompt returns a three-column markdown table showing your current state, the specific Lean techniques applied (value stream mapping, 5S, kaizen, pull systems, continuous flow, standardization), and the resulting optimized workflow with waste eliminated. It runs on ChatGPT, Claude, Gemini, and Grok, and includes an implementation roadmap prioritizing quick wins. Use it when you need to streamline operations, reduce cycle time, or eliminate non-value-adding activities in manufacturing, service delivery, administrative workflows, or supply chain operations. ● Maps current-state processes against optimized future-state workflows in a clear comparison table ● Identifies all seven categories of waste and matches each inefficiency to a specific Lean countermeasure ● Quantifies potential efficiency gains and highlights value-adding versus non-value-adding activities ● Provides an implementation roadmap that sequences changes by impact and ease of execution ## Prompt

```
## Role
You are a Lean Workflow expert specializing in process optimization and waste elimination.

## Task
Analyze the provided business process, identify waste and inefficiency, then design an optimized workflow using Lean principles. Map the transformation from current state to optimized state, ensuring every step adds value.

## Context
**Business process:** {{business-process}}

**Industry and challenges:** {{industry-context}}

**Desired outcomes:** {{desired-outcomes}}

## Analysis Framework
- Identify the seven wastes (overproduction, waiting, transport, over-processing, inventory, motion, defects)
- Map value-adding vs. non-value-adding activities
- Apply Lean techniques: value stream mapping, 5S, kaizen, pull systems, continuous flow, standardization
- Quantify potential efficiency gains where possible

## Output
Deliver your optimization plan as a markdown table with three columns:

| Current Process | Lean Techniques | Optimized Process |
|-----------------|-----------------|-------------------|
| [Step or activity as it exists today] | [Specific Lean method applied] | [Improved step with waste eliminated] |

Include 5-10 rows covering the most critical process steps. Below the table, provide a brief implementation roadmap prioritizing quick wins and high-impact changes.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-process}}、{{desired-outcomes}}、{{industry-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Lean Workflow Optimization Prompt for Business Processes is a free AI prompt that analyzes existing workfl…
