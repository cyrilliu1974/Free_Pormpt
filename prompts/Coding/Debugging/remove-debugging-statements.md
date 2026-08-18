# Remove Debugging Statements From Code

## 簡介

The Remove Debugging Statements From Code prompt is a free AI prompt that systematically cleans production code by identifying and removing temporary debug output while preserving legitimate logging. This code quality prompt for ChatGPT, Claude, and Cursor scans for common debugging statements - console.log, print, printf, System.out.println, echo, puts, and language equivalents - then analyzes each statement's context to distinguish between temporary investigation scaffolding and production-necessary logging. It returns cleaned code, a detailed changelog documenting every removal decision, and quantified metrics showing performance and readability improvements. Use it during pre-deployment reviews, when preparing code for production release, or when cleaning up codebases after intensive debugging sessions. ● Detects debug statements across languages: console.log, print, echo, System.out.println, puts, printf, and equivalents. ● Preserves production-critical logging for error tracking, audit trails, monitoring, and operational visibility based on your specified requirements. ● Provides a complete removal decision log explaining why each statement was removed or kept. ● Quantifies improvements: number of statements removed, performance impact eliminated, and future logging recommendations. ## Prompt

```
## Role
You are an expert code quality specialist who applies clean code principles to production environments, with deep expertise in distinguishing debugging scaffolding from legitimate production concerns.

## Task
Systematically identify and remove debugging statements from the provided code while preserving necessary production logging. Scan for debug output statements (console.log, print, printf, System.out.println, echo, puts, and language-equivalents), analyze each statement's context and purpose, then deliver cleaned code with clear documentation of all changes.

## Context
Debugging statements are temporary investigation tools that clutter output, slow execution, expose internal details, and can affect program behavior through timing or buffering. Production logging serves different purposes: error tracking, audit trails, monitoring, and operational visibility.

{{code-to-clean}}

{{production-logging-requirements}}

## Output
Structure your response with these sections:

### 1. Debug Statements Found
List each debugging statement discovered, its location, and likely investigative purpose.

### 2. Removal Decisions
For each statement, explain whether it was removed or preserved and why. Highlight the distinction between temporary debugging scaffolding and legitimate production logging.

### 3. Cleaned Code
Provide the complete refactored code with all unnecessary debug statements removed, functionality and readability intact.

### 4. Summary
Quantify improvements: number of statements removed, performance impact eliminated, and any logging patterns recommended for future maintenance.
```

## 用法 / Usage
- 必填變數 / Variables: {{code-to-clean}}、{{production-logging-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Remove Debugging Statements From Code prompt is a free AI prompt that systematically cleans production cod…
