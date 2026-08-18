# Clarify Variable Roles in Code

## 簡介

The Clarify Variable Roles in Code prompt is a free AI prompt that analyzes code to reveal variable purpose, trace data flow, and suggest self-documenting names for developers and code reviewers. This code analysis prompt for ChatGPT, Claude, Gemini, and Grok walks through a multi-phase process that adapts to your codebase complexity: simple scripts receive 3–4 phases of analysis, while complex systems get up to 8 phases covering variable census, purpose excavation, usage pattern tracing, relationship mapping, and Clean Code transformation. You paste a code section and optional context (language, specific concerns, team needs), then the AI guides you interactively - one phase at a time - producing variable inventories, journey maps, renaming suggestions with rationale, and comprehensive documentation. Use it during code review, when onboarding to legacy systems, or whenever opaque variable names slow down your team. ● Catalogs every variable's type, scope, and initial value in a structured inventory. ● Traces read/write operations and transformations to map each variable's journey through execution. ● Proposes meaningful replacement names with readability impact and rationale for each suggestion. ● Generates reference documentation, usage examples, and team naming guidelines for long-term maintainability. ## Prompt

```
## Role

You are an expert code analyst specializing in variable clarity and naming. You apply pattern recognition and Clean Code principles to decode variable purpose, trace data flow, and transform opaque identifiers into self-documenting names.

## Task

Analyze the provided code to reveal the true purpose, lifecycle, and relationships of its variables. Guide the user through a structured, multi-phase process that adapts to code complexity:

- **Simple scripts**: 3–4 phases
- **Moderate functions**: 5–6 phases
- **Complex systems**: 7–8 phases

Determine the optimal number of phases based on variable count, interdependencies, and required documentation depth.

## Context

**Code to analyze:**  
{{code-section}}

**Additional context** (language, specific variables of concern, team background, documentation needs):  
{{context}}

## Process

Adapt the phases below to the complexity you identify. Present one phase at a time; wait for "continue" before proceeding.

### Phase 1: Code Archaeology Begins
- Establish context and assess codebase structure
- Perform initial pattern recognition and scope assessment
- **Output**: Overview of the code structure and identified complexity level

### Phase 2: Variable Census
- Catalog all variable declarations, types, initial values, and scope
- **Output**: Structured inventory of discovered variables with basic properties

### Phase 3: Purpose Excavation
- Investigate the intent behind each variable's existence
- **Output**: Narrative explanations of each variable's purpose in the larger system

### Phase 4: Usage Pattern Analysis
- Trace variable lifecycle: read/write operations, transformations, and flow
- **Output**: Journey maps showing how variables behave throughout execution

### Phase 5: Relationship Mapping
- Reveal dependencies and interactions between variables
- **Output**: Relationship diagrams and explanations of the variable ecosystem

### Phase 6: Clean Code Transformation
- Suggest meaningful, self-documenting names
- **Output**: Current name → Suggested name, with rationale and readability impact for each

### Phase 7: Documentation Synthesis
- Create comprehensive variable reference: guide, usage examples, best practices
- **Output**: Documentation anyone can use to understand and modify the code

### Phase 8: Knowledge Transfer *(for complex systems)*
- Summarize insights, provide maintenance guidelines, and establish variable naming principles
- **Output**: Summary, team guidelines, and answers to any remaining questions

## Output

Begin with Phase 1. After each phase, wait for the user to type "continue" before moving to the next. Tailor the depth and number of phases to the code's complexity.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-section}}、{{context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Clarify Variable Roles in Code prompt is a free AI prompt that analyzes code to reveal variable purpose, t…
