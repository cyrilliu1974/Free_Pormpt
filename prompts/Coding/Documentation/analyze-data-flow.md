# Data Flow Tracing Prompt for Code Analysis

## 簡介

The Data Flow Tracing Prompt for Code Analysis is a free AI prompt that maps how information enters, transforms, and exits through code for systems analysts, data architects, and software engineers. It identifies every entry point, documents transformations, tracks conditional logic, maps storage operations, and follows data to its final output destinations in a structured, step-by-step narrative. This data flow analysis prompt for ChatGPT, Claude, Gemini, and Grok produces five organized sections - Data Entry Points, Transformation Steps, Decision Points, Storage Operations, and Final Outputs - that reveal hidden dependencies, bottlenecks, and failure points in code systems. Reach for it when you need to understand how a complex codebase processes information, debug unexpected data behavior, or document system architecture for onboarding or audits. ● Identifies all data entry points and systematically documents each transformation, modification, and processing step. ● Maps decision points and conditional branching paths to show how logic affects data flow. ● Tracks storage and retrieval operations, including reads, writes, and state changes throughout the code. ● Highlights dependencies between data elements and surfaces potential bottlenecks or failure points. ## Prompt

```
## Role
You are a systems analyst specializing in data flow tracing. Your task is to map how information moves and transforms through code.

## Task
Analyze the provided code and systematically trace each data element through its complete journey:

1. Identify all entry points where data enters
2. Document every transformation or modification step
3. Map decision points and conditional flows
4. Track storage and retrieval operations
5. Follow data to final output destinations

Create a step-by-step narrative explaining what happens to each piece of information at every stage. Highlight dependencies between data elements and potential bottlenecks or failure points.

## Context
Code to analyze:
{{code-section}}

Analysis focus:
{{analysis-focus}}

## Output
Structure your analysis with these sections:

### Data Entry Points
List all inputs and their sources.

### Transformation Steps
Document each processing operation in sequence.

### Decision Points
Map conditional logic and branching paths.

### Storage Operations
Track reads, writes, and state changes.

### Final Outputs
Identify all output destinations and formats.

Use bullet points and numbered steps to create a logical flow. Apply clear naming conventions and trace dependencies between data elements throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{analysis-focus}}、{{code-section}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Data Flow Tracing Prompt for Code Analysis is a free AI prompt that maps how information enters, transform…
