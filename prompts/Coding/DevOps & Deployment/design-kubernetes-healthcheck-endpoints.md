# Kubernetes Healthcheck Endpoint Design Prompt

## 簡介

The Kubernetes Healthcheck Endpoint Design Prompt is a free AI prompt that creates production-grade liveness and readiness probe implementations for DevOps teams running microservices on Kubernetes. It analyzes your application stack, distinguishes health-critical from readiness-critical dependencies, and outputs complete endpoint code with appropriate HTTP status handling, timeout logic, and response formats that orchestration tools can parse for automated recovery decisions. This Kubernetes healthcheck prompt for ChatGPT, Claude, and Cursor takes three inputs - your tech stack, critical dependencies (databases, caches, external APIs), and SLA requirements - then delivers separate liveness endpoint logic (fast process-alive checks) and readiness endpoint logic (dependency verification with retry handling) tailored to your environment. Use it when you need to implement or refactor health monitoring that prevents unnecessary pod restarts while enabling fast traffic rerouting during degraded states. ● Separates liveness logic (minimal, fast process health) from readiness logic (full dependency verification) to prevent cascading failures. ● Defines HTTP status codes, JSON response structures, and timeout strategies that Kubernetes can interpret for automated pod lifecycle decisions. ● Includes inline-commented code examples in your stack, probe configuration parameters (initialDelaySeconds, periodSeconds, failureThreshold), and monitoring integration guidance. ● Handles edge cases like partial degradation, slow dependency checks, and transient network failures with retry and circuit-breaker patterns. ## Prompt

```
## Role
You are a DevOps architect specializing in Kubernetes healthcheck design for microservices architectures. You understand the distinction between liveness (is the process running?) and readiness (can it serve traffic?) and design monitoring that enables automated recovery.

## Task
Create comprehensive healthcheck endpoint implementations following Kubernetes probe patterns. Design separate liveness and readiness endpoints with appropriate HTTP status codes, dependency verification logic, and response formats that orchestration tools can interpret for automated decision-making.

## Context
Application and infrastructure:
{{tech-stack}}

Critical dependencies to verify:
{{dependencies}}

Performance and monitoring requirements:
{{sla-requirements}}

## Process
1. Analyze the application architecture and identify health-critical versus readiness-critical dependencies
2. Design the liveness endpoint (fast, minimal checks—is the process responsive?)
3. Design the readiness endpoint (dependency checks—databases, caches, external APIs)
4. Define HTTP status codes and response structures for both human operators and automation
5. Provide implementation examples with error handling, timeout configurations, and performance considerations

## Output
Deliver your healthcheck implementation structured as:

### Architecture Analysis
- Critical vs. non-critical dependencies
- Appropriate health vs. readiness checks

### Liveness Endpoint Design
- Purpose and check logic
- Response format and status codes
- Implementation example (code block)

### Readiness Endpoint Design
- Dependency verification approach
- Timeout and retry logic
- Response format with actionable detail
- Implementation example (code block)

### Configuration Recommendations
- Kubernetes probe settings (initial delay, period, timeout, thresholds)
- Performance optimization to avoid check overhead
- Monitoring integration points

Provide code examples in the user's stack with inline comments. Use bullet points for explanations and trade-offs.
```

## 用法 / Usage
- 必填變數 / Variables: {{dependencies}}、{{sla-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Kubernetes Healthcheck Endpoint Design Prompt is a free AI prompt that creates production-grade liveness a…
