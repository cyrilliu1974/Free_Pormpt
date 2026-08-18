# Exception Handling Refactoring Prompt

## 簡介

The Exception Handling Refactoring Prompt is a free AI prompt that analyzes codebases to identify and eliminate exception handling anti-patterns, replacing silent failures and cryptic error messages with transparent, debuggable error flows for development teams. This exception handling prompt for ChatGPT, Claude, Gemini, and Grok takes your codebase context and produces a structured refactoring guide: it identifies problematic patterns like empty catch blocks and swallowed exceptions, delivers side-by-side before/after code comparisons, creates reusable exception message templates that include failure context and reproduction details, and provides a prioritized implementation checklist. Use it when production errors are opaque, debugging takes hours instead of minutes, or your logs lack the context needed to trace root causes. ● Identifies silent failures, broad exception catches, and log-without-rethrow anti-patterns in existing code ● Produces before/after refactoring examples with explanations of why the original patterns fail during debugging ● Generates exception message templates that include operation context, likely causes, and involved data without exposing sensitive information ● Delivers a step-by-step implementation checklist prioritized by debugging impact ## Prompt

```
## Role

You are a debugging specialist focused on exception handling and error transparency.

## Task

Analyze the provided codebase and refactor its exception handling to eliminate anti-patterns. Deliver before/after code examples, exception message templates, and an implementation checklist.

## Context

The codebase suffers from silent failures, swallowed exceptions, and cryptic error messages that obscure root causes. Apply these exception handling principles:

1. Every exception must include context: what operation failed, why it likely failed, and what data was involved
2. Never catch exceptions you cannot meaningfully handle—propagate them with added context
3. Eliminate silent failures: empty catch blocks and log-without-rethrow patterns are forbidden
4. Use exception chaining to preserve the full error trail
5. Create domain-specific custom exceptions instead of reusing generic ones
6. Avoid catching broad types (Exception, Throwable) except in top-level handlers
7. Log at appropriate levels—expected errors are not ERROR-level events
8. Include reproduction details without exposing sensitive data
9. Write messages for the developer debugging under pressure
10. Distinguish recoverable from unrecoverable errors and handle accordingly

**Codebase details:**

{{codebase-context}}

## Output

Provide your response in this structure:

**Current Anti-Patterns Found**  
Identify problematic exception handling patterns with code examples from the codebase.

**Refactored Solutions**  
Show before/after comparisons for each anti-pattern, explaining why the original fails during debugging and how the refactored version improves traceability.

**Exception Message Templates**  
Provide reusable templates for common failure scenarios in this application type and language.

**Implementation Checklist**  
Step-by-step actions for updating existing code, prioritized by impact.

**Best Practices Summary**  
Key takeaways specific to this language and application type for maintaining error transparency going forward.
```

## 用法 / Usage
- 必填變數 / Variables: {{codebase-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Exception Handling Refactoring Prompt is a free AI prompt that analyzes codebases to identify and eliminat…
