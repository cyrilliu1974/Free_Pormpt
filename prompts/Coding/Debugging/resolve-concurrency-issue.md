# Concurrency Issue Resolution Prompt

## 簡介

The Concurrency Issue Resolution Prompt is a free AI prompt that systematically detects and resolves deadlocks, livelocks, and thread starvation in multi-threaded code for developers and debugging specialists. This concurrency debugging prompt for ChatGPT applies lock ordering analysis, resource allocation graph construction, and wait-free algorithm evaluation to examine your code sample. It maps thread dependencies, detects circular waits, identifies livelock conditions where threads change state without making progress, and flags thread starvation risks where resources are perpetually denied. The prompt runs on ChatGPT, Claude, and Gemini, delivering a structured diagnostic report that includes issue severity classification, risk assessment with failure triggers, root cause explanations tied to specific code patterns, and concrete fixes with alternative concurrency patterns such as immutable data structures, message-passing architectures, lock-free algorithms, and actor model implementations. Reach for this prompt when analyzing enterprise systems with complex thread coordination, debugging production concurrency failures, or refactoring legacy multi-threaded code that exhibits synchronization problems. ● Traces lock acquisition sequences to detect ordering violations and circular dependencies that cause deadlocks ● Constructs resource allocation graphs to visualize thread interactions and identify cycles indicating potential synchronization failures ● Assesses livelock conditions and thread starvation risks with severity classification and likelihood scoring ● Recommends concrete refactorings with code examples, including lock-free algorithms and message-passing alternatives suited to your requirements ## Prompt

```
## Role
You are a concurrency analysis specialist with expertise in multiprocessor programming and enterprise debugging.

## Task
Systematically identify and resolve concurrency issues—deadlocks, livelocks, and thread starvation—in the provided code. Deliver a comprehensive diagnostic report with actionable recommendations.

## Analysis Method
Apply systematic techniques:

- **Lock ordering analysis** – trace acquisition sequences and identify violations
- **Resource allocation graph construction** – map thread dependencies and detect cycles
- **Wait-free algorithm evaluation** – assess progress guarantees

Examine:
1. Locking patterns and thread coordination mechanisms
2. Circular dependencies and deadlock scenarios
3. Livelock conditions (threads changing state without progress)
4. Thread starvation risks (perpetual resource denial)

Recommend safer patterns:
- Immutable data structures
- Message-passing architectures
- Lock-free algorithms
- Actor model implementations

## Context
{{code-sample}}

## Output
Structure your analysis with these sections:

### Issue Detection
- List each identified concurrency problem
- Classify severity for each issue

### Risk Assessment
- Evaluate likelihood and impact
- Identify conditions that trigger failures

### Root Cause Analysis
- Explain why each issue occurs
- Reference specific code patterns or thread interactions

### Recommended Solutions
- Provide concrete fixes with code examples
- Suggest alternative concurrency patterns suited to the requirements
- Outline migration path if architectural changes are needed
```

## 用法 / Usage
- 必填變數 / Variables: {{code-sample}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Concurrency Issue Resolution Prompt is a free AI prompt that systematically detects and resolves deadlocks…
