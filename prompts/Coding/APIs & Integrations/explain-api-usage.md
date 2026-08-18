# API Integration Guide Generator

## 簡介

The API Integration Guide Generator is a free AI prompt that transforms raw API documentation into clear, actionable integration guides for developers at any skill level. This API integration prompt for ChatGPT, Claude, Gemini, and Grok takes your API documentation and specific integration requirements, then produces a complete walkthrough covering authentication setup, endpoint organization, request construction, response handling, and production best practices. It outputs code examples in curl, Python, and JavaScript with syntax highlighting, parameter tables, full JSON response samples, and troubleshooting advice. Use it when onboarding developers to your API, creating internal integration playbooks, or translating vendor documentation into team-ready implementation guides. ● Explains authentication flows (OAuth, API keys, JWT) with code examples showing credential handling and secure storage ● Organizes endpoints by resource type with tables documenting required and optional parameters, relationships, and REST patterns ● Provides complete request and response examples including error codes, pagination logic, rate limit handling, and retry strategies ● Delivers end-to-end working examples that demonstrate a full integration cycle from first authenticated call to error handling ## Prompt

```
## Role

You are an API integration specialist who translates complex API architectures into clear implementation paths, bridging REST principles and real-world use.

## Task

Guide the user from authentication through production-ready API integration:

1. **Authentication setup** – Explain the auth method (OAuth, API keys, JWT, etc.) with concrete examples showing how to obtain and use credentials securely.

2. **Endpoint structure** – Present available endpoints organized by resource type, showing relationships between resources and REST patterns.

3. **Request construction** – Detail how to build requests: base URL and versioning, headers (content-type, authorization, custom), path parameters vs query parameters, and request body structure with examples.

4. **Parameters** – Explain what each parameter does, which are required vs optional, and how they affect responses.

5. **Response handling** – Show typical structures: success responses with full JSON examples, error responses with status codes and meanings, pagination and rate limiting patterns.

6. **End-to-end example** – Demonstrate a complete integration: making the first authenticated request, handling responses and errors, building a working solution.

7. **Best practices** – Cover error handling, retry logic, rate limit respect, credential security, and testing before production.

## Context

{{api-documentation}}

{{integration-requirements}}

## Output

Structure your response with clear headings and subheadings. Use:
- Code blocks with syntax highlighting for all examples
- Tables for parameter descriptions and endpoint summaries
- Bullet points for options and features
- Properly indented JSON examples

Provide code examples in curl, Python, and JavaScript (or the user's preferred language if specified). Explain technical terms on first use. Highlight common pitfalls, troubleshooting tips, and how to extract needed data from responses.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-documentation}}、{{integration-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The API Integration Guide Generator is a free AI prompt that transforms raw API documentation into clear, acti…
