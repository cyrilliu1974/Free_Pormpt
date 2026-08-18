# Defensive Input Validation Code Generator

## 簡介

The Defensive Input Validation Code Generator is a free AI prompt that creates bulletproof validation layers for function boundaries in any codebase. This input validation prompt for ChatGPT analyzes your function details and produces comprehensive precondition checks, validation code, and informative error messages that catch bugs before they propagate. It works on ChatGPT, Claude, and Cursor to identify every assumption about input types, formats, ranges, null states, and parameter relationships, then generates the exact validation logic needed to enforce those contracts. Software engineers use it to prevent runtime errors, eliminate silent failures, and build systems that fail fast with clarity when given invalid data. Reach for this prompt when you need to harden function interfaces, document implicit assumptions as explicit preconditions, or prevent technical debt from defensive programming gaps. ● Systematically documents every assumption about input parameters - type constraints, value ranges, format requirements, and interdependencies ● Generates actual validation code in your target language that checks preconditions before function logic executes ● Designs error messages that explain what failed, what was expected, and what was received to guide developers toward correct usage ● Provides working examples of both valid and invalid function calls with their expected outcomes ## Prompt

```
## Role

Defensive programming architect specializing in Design by Contract principles.

## Task

Fortify function boundaries with comprehensive input validation that catches errors before they propagate. Analyze each function to identify all assumptions about inputs, define precise preconditions, implement validation checks, and design informative error messages that fail fast and guide developers toward correct usage.

## Context

{{function-details}}

Apply these validation principles:

- **Identify all assumptions**: Document every expectation about input type, format, range, null states, and parameter relationships
- **Define explicit contracts**: State preconditions using precise, unambiguous language
- **Validate comprehensively**: Check types, value ranges, formats, edge cases, and unexpected combinations
- **Fail fast with clarity**: Halt execution immediately upon detecting violations, providing error messages that explain what went wrong, what was expected, and what was received
- **Prevent silent failures**: Never allow invalid inputs to proceed into function logic
- **Avoid defensive copying**: Validate without modifying inputs unless explicitly required

## Output

For each function, provide:

**Function Name: [name]**

*Identified Assumptions:*  
• [List each assumption about inputs]

*Preconditions:*  
• [State each required condition formally]

*Validation Code:*
```
[Actual validation code in the specified language]
```

*Error Messages:* 
• [Exact error message for each validation failure]

*Example Usage:*
```
[Valid and invalid function calls with expected outcomes]
```
```

## 用法 / Usage
- 必填變數 / Variables: {{function-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Defensive Input Validation Code Generator is a free AI prompt that creates bulletproof validation layers f…
