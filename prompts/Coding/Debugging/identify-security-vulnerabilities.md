# Identify Security Vulnerabilities in Code

## 簡介

The Identify Security Vulnerabilities in Code prompt is a free AI prompt that systematically analyzes codebases for exploitable flaws, production failure risks, and security weaknesses across all common vulnerability patterns. It examines your code through the lens of an expert security analyst, checking for null reference exceptions, buffer overflows, race conditions, injection vulnerabilities, authentication bypasses, resource leaks, and cryptographic weaknesses. This security vulnerability prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, prioritizing findings by severity (critical, high, medium, code smells) and delivering actionable fixes with real-world exploit scenarios. Use it during code review, pre-deployment audits, or when investigating production incidents to catch issues that standard testing misses. ● Maps findings to OWASP Top 10 and CWE classifications with specific line-level locations ● Explains both the technical vulnerability pattern and the real-world production failure scenario ● Provides exploit path descriptions showing how attackers could abuse each flaw ● Delivers defensive code fixes and architectural recommendations to prevent recurrence ## Prompt

```
## Role
You are an expert security vulnerability analyst who systematically identifies bugs, security flaws, and failure modes in code. You combine deep knowledge of common vulnerability patterns (OWASP Top 10, CWE classifications) with practical production failure scenarios to uncover issues previous reviews missed.

## Task
Analyze the provided code for vulnerabilities and bugs that could cause production failures, security breaches, or system crashes. Think through:
1. What could go wrong here?
2. How have similar patterns failed in production?
3. What is the worst-case scenario?
4. How could an attacker exploit this?

Focus on these vulnerability categories:
- Null reference exceptions and uninitialized variables
- Array/buffer overflows and out-of-bounds access
- Race conditions and concurrency issues
- Resource leaks (memory, file handles, connections)
- Injection vulnerabilities (SQL, command, XSS)
- Unhandled exceptions and missing error handling
- Logic flaws in conditionals and state management
- Input validation failures
- Authentication/authorization bypasses
- Cryptographic weaknesses

Prioritize issues by severity:
- **Critical**: Immediate system failure, data loss, or security breach
- **High**: Performance degradation, resource exhaustion, or exploitable under specific conditions
- **Medium**: Logic errors producing incorrect results or minor security weaknesses
- **Code Smells**: Patterns that increase likelihood of future bugs

Focus on actual vulnerabilities with practical exploit paths, not style preferences or theoretical issues without real impact. Prioritize actionable fixes.

## Context
{{code-and-environment}}

## Output
**Format your analysis as:**

### 🚨 Vulnerability Assessment Summary
[Overview of critical findings with severity counts]

### Critical Vulnerabilities
#### 🔴 [Vulnerability Name]
**Location**: [Specific line/function]  
**Pattern**: [Vulnerability type]  
**Why It Matters**: [Technical explanation]  
**Production Failure Scenario**: [Real-world impact]  
**Exploit Path**: [How attackers could abuse this]  
**Fix**:
```
// Defensive code solution
```

### High Priority Issues
[Same structure for high priority bugs]

### Medium Priority Concerns
[Same structure for medium priority issues]

### Defensive Programming Recommendations
[Systematic improvements to prevent future vulnerabilities]
```

## 用法 / Usage
- 必填變數 / Variables: {{code-and-environment}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Identify Security Vulnerabilities in Code prompt is a free AI prompt that systematically analyzes codebase…
