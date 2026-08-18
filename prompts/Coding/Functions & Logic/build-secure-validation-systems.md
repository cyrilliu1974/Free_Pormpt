# Secure Input Validation System Builder

## 簡介

The Secure Input Validation System Builder is a free AI prompt that generates complete, production-ready validation architectures for developers and security engineers building zero-trust applications. This input validation prompt for ChatGPT produces structured code with schema validators using modern frameworks like Zod or Joi, sanitization layers that neutralize SQL injection and XSS attacks, custom business logic validators, and error handlers with actionable user guidance. It runs on ChatGPT, Claude, and Cursor, outputting complete validation systems tailored to your specific validation target and security context. Real use cases include API endpoint protection, form processing pipelines, database write operations, and user authentication flows where malicious input poses a critical threat. Reach for this prompt when you need to implement defense-in-depth validation that prevents injection attacks, data corruption, CSRF, and business logic bypass in production environments. ● Schema validators with precise type constraints and fallback patterns to catch malformed input before it reaches business logic. ● Sanitization functions that strip or encode dangerous characters, neutralizing SQL injection, cross-site scripting, and command injection payloads. ● Comprehensive error handling that returns actionable user messages without leaking internal system details or stack traces. ● Security test cases covering common attack scenarios and validation bypass attempts, with performance optimization strategies for high-throughput systems. ## Prompt

```
## Role

You are an expert validation architect designing secure, production-grade input validation systems using zero-trust principles.

## Task

Build a complete validation system for {{validation-target}} with layered client-side and server-side checks. Include schema validators with precise constraints, sanitization functions, custom business logic validators, and comprehensive error handling.

## Context

{{security-context}}

Prevent SQL injection, XSS, CSRF, data corruption, and business logic bypass. Use modern validation frameworks (Zod, Joi, or equivalent) with fallback patterns. Include security comments explaining which attack vectors each validator prevents.

## Output

Structure your response with these sections:

**Validation Schema**  
Complete schema definition with precise constraints and type checking

**Core Validators**  
Production-ready validator functions with security rationale for each rule

**Sanitization Layer**  
Input sanitization functions that neutralize malicious content

**Error Handling**  
Comprehensive error responses with actionable user guidance

**Performance Optimization**  
Caching strategies and response time targets

**Security Testing**  
Attack scenarios and validation bypass test cases

**Implementation Guide**  
Deployment instructions with usage examples
```

## 用法 / Usage
- 必填變數 / Variables: {{security-context}}、{{validation-target}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Manifest_Driven_Code_Skeleton_Generator
- 適用 / Use when: The Secure Input Validation System Builder is a free AI prompt that generates complete, production-ready valid…
