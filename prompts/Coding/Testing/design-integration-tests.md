# Integration Test Design Prompt for Distributed Systems

## 簡介

The Integration Test Design Prompt for Distributed Systems is a free AI prompt that creates comprehensive integration testing strategies for architects and developers working with complex, multi-component applications. This integration testing prompt for ChatGPT, Claude, and Gemini analyzes your system architecture - components, databases, APIs, message queues, and third-party services - then produces a structured testing plan that validates real component interactions, database operations, and external service communications. It generates concrete test scenarios for happy paths, error conditions, timeouts, and edge cases, along with infrastructure setup instructions for isolated test databases, mock services, and reproducible environments. Real use cases include preventing cascading failures in microservices, validating API contracts between frontend and backend layers, and ensuring proper error propagation across distributed systems. Reach for this prompt when you need to move beyond unit tests and verify that components actually work together as intended in production-like conditions. ● Maps all component boundaries, database touchpoints, and external service dependencies to identify critical integration paths ● Designs test scenarios covering success flows, failure modes, timeout handling, and retry logic across system layers ● Provides test infrastructure configuration for spinning up isolated databases, mock APIs, and clean test environments ● Generates concrete test implementation code with real HTTP requests, database assertions, and API contract validation ● Includes cleanup procedures and diagnostic guidance to reset state between test runs and troubleshoot integration failures ## Prompt

```
## Role

You are an expert integration testing architect specializing in complex distributed systems.

## Task

Create a comprehensive integration testing strategy for the described system. Cover architecture analysis, test scenario design, infrastructure setup, test implementation, and cleanup procedures.

## Context

Integration tests validate real-world scenarios across system boundaries—component interactions, database operations, external service communications, happy paths, error conditions, timeouts, and edge cases. Effective tests prevent integration bugs from reaching production and causing cascading failures.

## Input

{{system-architecture}}: Describe your application's main components and layers, database types, external service dependencies (third-party APIs, message queues, caches), current testing framework (e.g., Jest, pytest, JUnit), and deployment environment (containers, cloud services).

## Output

Provide:

1. **Architecture Analysis**: Identify all interaction points between components, databases, APIs, and external services. Map critical user journeys and data flows that span system boundaries.

2. **Test Scenario Design**: Integration test scenarios covering:
   - Happy paths across multiple layers
   - Error conditions and failure modes
   - Timeout and retry scenarios
   - Edge cases where components communicate

3. **Test Infrastructure Setup**: Configuration that:
   - Spins up isolated test databases
   - Configures mock external services
   - Creates clean, reproducible test environments

4. **Test Implementation**: Concrete test code that:
   - Makes real HTTP requests between services
   - Verifies database state changes
   - Validates API contracts
   - Ensures proper error propagation between layers

5. **Cleanup & Diagnostics**: Comprehensive cleanup procedures that reset environments between runs and provide clear failure diagnostics when integration points break.

Structure your response with clear headings for each phase. Provide actionable implementation steps with specific code examples and configuration snippets tailored to the testing framework and infrastructure described.
```

## 用法 / Usage
- 必填變數 / Variables: {{system-architecture}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Integration Test Design Prompt for Distributed Systems is a free AI prompt that creates comprehensive inte…
