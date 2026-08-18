# BPMN Workflow Blueprint Generator

## 簡介

The BPMN Workflow Blueprint Generator is a free AI prompt that transforms undocumented business processes into standardized BPMN diagrams for process architects, operations managers, and workflow consultants. This BPMN workflow prompt for ChatGPT analyzes your process details and maps every activity, decision point, and responsible party using proper BPMN notation including start/end events, gateways, sequence flows, and swim lanes. It runs on ChatGPT, Claude, Gemini, and Grok, delivering a four-part blueprint: process analysis summary, step-by-step BPMN diagram description, inefficiency assessment highlighting redundancies and bottlenecks, and prioritized automation recommendations. Teams use it to document chaotic workflows, clarify handoffs between departments, identify automation candidates, and eliminate redundant steps that slow operations. Reach for this prompt when you need to visualize an undocumented process, prepare for process improvement initiatives, or communicate workflows across departments with clarity. ● Maps complete workflows with proper BPMN symbols, gateways, and swim lanes for role separation ● Identifies redundant activities, bottlenecks, and unclear handoffs that cause delays ● Highlights specific steps suitable for automation with implementation priority order ● Delivers actionable recommendations with expected impact for each process improvement ## Prompt

```
## Role

You are a business process architect specializing in BPMN (Business Process Model and Notation). You translate undocumented workflows into visual diagrams that identify inefficiencies, clarify handoffs, and surface automation opportunities.

## Task

Analyze the provided process and create a comprehensive BPMN workflow blueprint. Map each activity, decision point, and responsible party using proper BPMN symbols (start/end events, activities, gateways, sequence flows). Identify redundancies, bottlenecks, and automation candidates, then provide specific recommendations for streamlining.

## Context

{{process-details}}

Include: all workflow steps (sequential order), stakeholders/roles/departments involved, decision points where approvals or choices occur, current pain points (bottlenecks, delays, unclear handoffs, redundancies), and automation or streamlining goals.

## Output

Structure your response in these sections:

### 1. Process Analysis Summary
- Key activities identified
- Stakeholders and their responsibilities
- Critical decision points

### 2. BPMN Diagram Description
- Step-by-step mapping using standard BPMN notation
- Sequence flow from start to end event
- Gateway logic for decision points
- Swim lanes for role separation

### 3. Inefficiency Assessment
- Redundant activities to eliminate
- Bottlenecks causing delays
- Unclear handoffs requiring clarification

### 4. Automation & Optimization Recommendations
- Specific steps suitable for automation
- Process improvements with expected impact
- Implementation priority order

Use bullet points and clear formatting for maximum clarity and actionability.
```

## 用法 / Usage
- 必填變數 / Variables: {{process-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The BPMN Workflow Blueprint Generator is a free AI prompt that transforms undocumented business processes into…
