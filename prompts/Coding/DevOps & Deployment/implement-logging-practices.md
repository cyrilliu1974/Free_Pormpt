# Logging Implementation Prompt for Production Code

## 簡介

The Logging Implementation Prompt for Production Code is a free AI prompt that generates complete logging frameworks, team standards, and sanitization patterns for developers building observable applications. This logging practices prompt for ChatGPT, Claude, and Cursor takes your technology stack, application type, and compliance requirements and produces working code with dependency setup, environment-specific configuration, structured JSON logging patterns, and integration guidance for platforms like ELK, Datadog, CloudWatch, and Grafana Loki. It defines clear log-level semantics (DEBUG for flow, INFO for business events, WARN for recoverable issues, ERROR for failures), injects required context fields like request IDs and user identifiers for distributed tracing, and provides concrete examples of logging application startup, HTTP request lifecycles, business transactions, error conditions with stack traces, and performance-critical operations. Use it when your team struggles with noisy logs that obscure real issues, lacks context during incident response, or risks exposing sensitive data in production logs. ● Framework setup with dependency commands, JSON output configuration, and development versus production environment switches ● Team logging standards defining when to use each log level, which contextual identifiers to include, and how to write self-explanatory messages ● Code examples for startup, request handling, business transactions, errors with stack traces, and timing instrumentation ● Sensitive data protection with redaction, masking, and hashing patterns for PII, passwords, tokens, and API keys ● Sample JSON log output showing timestamp, service name, environment, log level, structured context fields, and error details ● Monitoring integration guidance for connecting logs to observability platforms and designing automated alerting rules ## Prompt

```
## Role

You are a logging and observability specialist who designs production-grade logging strategies that tell a coherent story of application behavior, enable rapid troubleshooting, and protect sensitive data while providing sufficient debugging context.

## Task

Generate production-ready logging code and implementation guidelines tailored to the provided technology stack. Follow structured logging best practices and modern observability patterns.

## Context

Poor logging creates noise that obscures real issues, missing critical context forces code inspection during incidents, and sensitive data leaks violate compliance requirements. Your implementation must balance completeness, performance, and security.

**Project details:**
{{tech-stack-and-requirements}}

*Include: application type, language/framework, specific events or flows to log, sensitive data types to protect, preferred logging library (or request a recommendation), and target observability platform if any.*

## Output

Provide a complete logging implementation:

### 1. Framework Setup
- Dependency installation commands
- Configuration code (output format, log levels, destinations)
- Environment-specific settings (development vs production)

### 2. Logging Standards
Team guidelines:
- **Log Levels**: DEBUG (detailed flow), INFO (business events, audit trails), WARN (recoverable issues), ERROR (failures requiring attention)
- **Required Context**: Request ID, user ID (when authenticated), relevant business identifiers for tracing
- **Structured Format**: JSON or key-value pairs for machine parsing
- **Message Clarity**: Self-explanatory messages that assume no code access
- **Performance**: Avoid logging in tight loops; use sampling or rate limiting for high-frequency paths

### 3. Code Examples
Logging statements for common scenarios with inline comments:
- Application startup and shutdown
- Request handling (entry and exit points)
- Business transactions
- Error conditions with stack traces
- Performance-critical operations with timing

### 4. Sensitive Data Protection
Concrete sanitization examples:
- Redact PII, passwords, tokens, API keys
- Hash or mask identifiers when required
- Log sufficient context without exposing protected data

### 5. Sample Log Output
JSON-formatted examples showing:
- Timestamp, service name, environment
- Log level and message
- Structured context fields
- Error details when applicable

### 6. Monitoring Integration
Guidance on connecting logs to observability platforms (ELK, Datadog, CloudWatch, Grafana Loki) and designing for automated alerting.
```

## 用法 / Usage
- 必填變數 / Variables: {{tech-stack-and-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Logging Implementation Prompt for Production Code is a free AI prompt that generates complete logging fram…
