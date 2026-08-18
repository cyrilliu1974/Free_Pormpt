# Idempotency Implementation Code Generator

## 簡介

The Idempotency Implementation Code Generator is a free AI prompt that produces production-ready code to prevent duplicate operations and ensure safe request retries in distributed systems for backend engineers. This idempotency implementation prompt for ChatGPT, Claude, and Cursor generates complete client-side and server-side code tailored to your technical stack and use case. It creates unique identifiers for operations, implements standard idempotency headers (Idempotency-Key or X-Idempotency-Key), handles concurrent requests and timeouts, and includes TTL-based storage schemas for tracking processed requests. The output covers request generation with retry logic, middleware or decorators for server-side validation, database designs with appropriate indexes, and comprehensive error handling for conflicts, expired keys, and partial failures. Reach for this prompt when building payment processors, resource creation APIs, or any distributed system where network failures and retries could cause unintended duplicate side effects. ● Client-side code with idempotency key generation and automatic retry logic that prevents duplicate submissions. ● Server-side middleware or decorators that validate idempotency keys, detect concurrent requests, and enforce single execution. ● Database schemas with TTL-based expiration and indexes optimized for fast idempotency key lookups. ● Error handling patterns covering race conditions, expired keys, timeouts, and partial failure recovery scenarios. ## Prompt

```
## Role

You are an expert backend engineer specializing in distributed systems and API reliability.

## Task

Generate production-ready idempotency implementation code that prevents duplicate operations and ensures safe request retries. Handle network failures, concurrent requests, and retry scenarios common in distributed systems.

## Context

Idempotency prevents duplicate payments, resource creation, and other unintended side effects. Your implementation must:

- Create unique identifiers for each operation
- Implement standard idempotency headers (`Idempotency-Key` or `X-Idempotency-Key`)
- Handle concurrent requests and timeouts
- Provide both client-side request generation and server-side validation
- Include storage with TTL-based expiration for tracking processed requests
- Demonstrate safe retry logic without duplicates
- Cover comprehensive error handling

**Technical stack:** {{technical-stack}}

**Use case:** {{use-case}}

## Output

Provide complete, copy-paste ready code organized into:

1. **Client-Side Implementation** – Request generation with idempotency key creation and retry logic
2. **Server-Side Implementation** – Middleware/decorator for idempotency validation and enforcement
3. **Storage Schema** – Database design for tracking idempotency keys with appropriate indexes
4. **Error Handling** – Scenarios covering conflicts, expired keys, and partial failures
5. **Integration Example** – End-to-end workflow demonstration

Include inline comments explaining idempotency logic at each step. All code should be runnable with minimal setup.
```

## 用法 / Usage
- 必填變數 / Variables: {{technical-stack}}、{{use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Idempotency Implementation Code Generator is a free AI prompt that produces production-ready code to preve…
