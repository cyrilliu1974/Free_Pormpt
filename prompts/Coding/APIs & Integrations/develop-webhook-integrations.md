# Webhook Integration Development Prompt

## 簡介

The Webhook Integration Development Prompt is a free AI prompt that generates complete, production-ready webhook listener implementations for developers building secure event-driven integrations. This webhook integration prompt for ChatGPT, Claude, and Cursor produces full-stack code covering signature validation, idempotency keys, duplicate event prevention, transactional database updates, retry logic, and security hardening tailored to your framework and third-party service. It outputs working examples for Next.js API routes and Express endpoints with inline comments explaining security decisions, failure modes, and enterprise-grade defensive patterns that address real-world edge cases like replay attacks, malformed payloads, database deadlocks, and cascading failures. Use it when you need to integrate payment processors, CRM webhooks, notification services, or any event-driven API that demands reliability and cannot tolerate silent failures or data corruption. ● Cryptographic signature validation with timing-attack-safe comparison and secret rotation support ● Idempotency enforcement and duplicate event detection to prevent double-processing ● Structured logging, metrics tracking (latency, error rates, duplicate events), and alerting thresholds ● Security checklist covering HTTPS enforcement, rate limiting, payload size caps, IP allowlisting, and common attack vectors ● Testing strategies with webhook proxies (ngrok, localtunnel), integration test patterns, and zero-downtime deployment guidance ## Prompt

```
## Role

You are a senior API architect specializing in production-grade webhook integrations. You design defensive systems that handle signature validation, duplicate events, payload anomalies, and graceful degradation under real-world failure conditions.

## Task

Create a complete, production-ready webhook listener implementation that securely receives, validates, and processes incoming webhook events from {{third-party-service}}.

Provide step-by-step implementation covering:

- Signature validation using cryptographic verification
- Idempotency and duplicate event prevention
- Comprehensive logging and monitoring
- Database persistence and transactional updates
- Notification triggers
- Retry logic and graceful failure recovery
- Security hardening (rate limiting, payload size checks, HTTPS enforcement)

Include working code examples for both Next.js API routes and Express endpoints tailored to {{stack-details}}.

Focus on enterprise-grade patterns that assume failures, prevent data corruption, and maintain system reliability. Address edge cases tutorials ignore: malformed payloads, replay attacks, database deadlocks, and cascading failures.

## Context

{{stack-details}} should specify: application framework (Next.js 14 app router, Express 4.x, etc.), database system (PostgreSQL, MongoDB, etc.), notification channels (email, Slack, push, etc.), and any compliance or security constraints (PCI-DSS, HIPAA, SOC 2, etc.).

## Output

Structure your response with these sections:

**Implementation Overview**  
Architecture diagram (ASCII or description), security model, and data flow.

**Signature Validation**  
Complete code for verifying webhook signatures with timing-attack-safe comparison and secret rotation support.

**Webhook Endpoint Code**  
Production-ready endpoint implementation with request parsing, validation middleware, and response handling.

**Payload Processing**  
Event handler logic with database transactions, idempotency keys, and notification dispatch.

**Error Handling & Retries**  
Exponential backoff, dead-letter queues, circuit breakers, and failure alerting.

**Logging & Monitoring**  
Structured logging examples, metrics to track (latency, error rates, duplicate events), and alerting thresholds.

**Security Checklist**  
Validation steps: HTTPS-only, IP allowlisting options, rate limiting, payload size caps, and common attack vectors to prevent.

**Testing & Deployment**  
Local testing with webhook proxies (ngrok, localtunnel), integration test patterns, and zero-downtime deployment strategies.

Provide copy-paste-ready code with inline comments explaining security decisions and failure modes.
```

## 用法 / Usage
- 必填變數 / Variables: {{stack-details}}、{{third-party-service}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Webhook Integration Development Prompt is a free AI prompt that generates complete, production-ready webho…
