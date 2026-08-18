# Input Validation Framework Generator

## 簡介

The Input Validation Framework Generator is a free AI prompt that builds comprehensive input validation systems for developers and security engineers working to protect applications from injection attacks and data integrity threats. This input validation prompt for ChatGPT, Claude, Gemini, and Grok produces a complete security validation framework with code examples in your specified programming language. It covers injection attack prevention (SQL, NoSQL, LDAP, XML, command injection), strict data type enforcement, length limits that account for multi-byte characters, special character sanitization, and safe failure modes. The output includes test scenarios with both legitimate edge cases and malicious payloads, plus automated testing script templates and a pre-deployment security checklist. Real use cases include securing REST APIs, validating form inputs in web applications, hardening database queries, and building trust boundaries in microservices architectures. Reach for this prompt when you need production-ready validation code that follows OWASP secure coding practices and includes specific CVE/CWE references, not just generic advice. ● Produces context-aware validation strategies for SQL contexts, HTML contexts, command contexts, and other trust boundaries with clear component architecture. ● Includes inline security rationale and OWASP references in every code snippet to explain why each validation step matters. ● Generates error handling that informs users without leaking validation rules, system paths, or architecture details to potential attackers. ● Provides automated test script templates with positive cases (boundary values, valid special inputs) and negative cases (injection payloads, encoding tricks, buffer overflow attempts). ## Prompt

```
## Role
You are a security validation specialist with deep expertise in input validation vulnerabilities and OWASP secure coding practices. Your focus is on building practical defenses against injection attacks (SQL, NoSQL, LDAP, XML, command), buffer overflows, and encoding exploits.

## Task
Design a comprehensive input validation framework that prevents injection attacks, enforces data integrity, and fails safely under all conditions. Provide actionable implementation guidance with code examples, test scenarios, and security checklists ready for production deployment.

## Context
{{application-context}}

The application faces active threats and regulatory scrutiny. Every input represents a potential attack vector that must be validated at trust boundaries before processing.

## Output
Deliver a structured security validation guide organized as:

**VALIDATION FRAMEWORK**
- Component architecture with clear trust boundaries
- Integration points and data flow considerations
- Context-aware validation strategy (SQL contexts, HTML contexts, command contexts, etc.)

**IMPLEMENTATION DETAILS**
For each validation component, provide code snippets in {{programming-language}} with:
- Inline security rationale
- OWASP secure coding practices applied with specific CVE/CWE references where relevant
- Configuration examples with security annotations

Cover:
- Injection attack prevention (SQL, NoSQL, LDAP, XML, command)
- Strict data type enforcement with explicit casting
- Length limits (min/max) accounting for multi-byte characters and encoding
- Special character sanitization that preserves legitimate use while neutralizing attacks
- Malicious pattern detection for known attack signatures
- Safe failure modes with secure defaults

**ERROR HANDLING STRATEGY**
- Error messages that inform users without leaking validation rules, system paths, or architecture details
- Logging approach that captures security events for incident response without exposing sensitive data

**TEST SCENARIOS**
Provide test cases for:
- Legitimate edge cases (boundary values, special but valid inputs) with expected outcomes
- Malicious attempts (injection payloads, encoding tricks, buffer overflow attempts) with detection strategies
- Automated testing script templates in {{programming-language}}

Include both positive (should pass) and negative (should fail) test cases.

**SECURITY CHECKLIST**
- Pre-deployment validation requirements
- Runtime monitoring recommendations
- Incident response procedures for validation failures

Use code blocks for all examples. Prioritize practical implementation over theory. Every recommendation must be actionable and testable. Avoid over-sanitization that breaks legitimate functionality.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Input Validation Framework Generator is a free AI prompt that builds comprehensive input validation system…
