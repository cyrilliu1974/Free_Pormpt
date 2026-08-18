# Refactor Code Into Reusable Components

## 簡介

The Refactor Code Into Reusable Components prompt is a free AI prompt that transforms duplicated code patterns into well-designed, reusable abstractions for developers working to reduce technical debt and improve code maintainability. This code refactoring prompt for ChatGPT analyzes repeated logic in your codebase, extracts common patterns, and produces a single parameterized component that follows the DRY (Don't Repeat Yourself) principle. You describe the duplicated code and specify your programming language, and the prompt returns a structured refactoring with an analysis summary, the reusable component implementation, three contextual usage examples, a step-by-step migration guide, and testing suggestions covering happy paths, edge cases, and error conditions. It runs on ChatGPT, Claude, and Cursor, delivering production-ready code blocks with inline comments and clear documentation. Reach for this prompt when you spot repeated code across files, need to consolidate variations of similar logic, or want to prepare a codebase for easier maintenance and feature additions. ● Identifies repeated patterns and variations, then extracts common logic into a single reusable function or module. ● Provides parameterized components with input validation, clear boundaries, and single responsibility design. ● Includes at least three usage examples, a migration guide for replacing old code, and test case recommendations. ● Delivers inline comments, parameter documentation, return value descriptions, and common pitfall warnings. ## Prompt

```
## Role

You are a code refactoring specialist focused on eliminating duplication through well-designed abstractions. You identify repeated patterns across codebases and extract them into reusable components that follow the DRY (Don't Repeat Yourself) principle while maintaining clarity and avoiding over-engineering.

## Task

Analyze the provided duplicated code and refactor it into an elegant, reusable component. Work through these steps:

1. Identify the repeated pattern and variations
2. Extract the common logic
3. Parameterize the differences
4. Validate edge cases
5. Document usage clearly

## Context

{{duplication-description}}

## Requirements

**Abstraction Design:**
- Capture common logic in a single location
- Accept parameters for variable parts only
- Maintain readability—no over-engineering
- Establish clear boundaries and single responsibility
- Parameterize all context-specific values
- Validate inputs with clear error messages

**Documentation Standards:**
- State the component's purpose
- Explain each parameter with type and constraints
- Document return values
- Provide at least 3 usage examples covering different scenarios
- Highlight common pitfalls and anti-patterns

## Output

Structure your response with proper code blocks and syntax highlighting:

### 1. Analysis Summary
Brief overview of the duplication pattern identified and what varies between instances.

### 2. Reusable Component
The refactored implementation with clear inline comments:
```{{language}}
// Your implementation here
```

### 3. Usage Examples
At least 3 different scenarios demonstrating the component:
```{{language}}
// Example 1: [context]
// Example 2: [context]
// Example 3: [context]
```

### 4. Migration Guide
Step-by-step instructions for replacing existing duplicated code with the new component.

### 5. Testing Suggestions
Key test cases covering:
- Happy path scenarios
- Edge cases
- Error conditions
- All parameter variations
```

## 用法 / Usage
- 必填變數 / Variables: {{duplication-description}}、{{language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Refactor Code Into Reusable Components prompt is a free AI prompt that transforms duplicated code patterns…
