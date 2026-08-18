# Mock API Response Generator for RESTful APIs

## 簡介

The Mock API Response Generator for RESTful APIs is a free AI prompt that generates realistic, production-grade mock API responses for frontend developers, backend engineers, and API architects. This mock API response prompt for ChatGPT creates complete endpoint responses following RESTful conventions, including authentic HTTP status codes, headers (content-type, rate limiting, CORS, cache control), well-formed JSON with proper data types and naming conventions, pagination structures, and detailed error objects with validation messages. It runs on ChatGPT, Claude, Gemini, and Grok, producing responses that mirror real production scenarios with nested objects, arrays, ISO 8601 timestamps, and realistic business data patterns. Use it for frontend development against incomplete backends, automated testing, API documentation, contract validation, or prototyping before implementation. ● Produces complete mock responses with appropriate HTTP status codes, headers, and properly indented JSON bodies for any endpoint specification. ● Includes pagination structures (cursor-based, offset-based, or page tokens), metadata fields, and realistic business domain data. ● Generates detailed error scenarios with HTTP codes, error codes, field-level validation messages, and trace IDs for debugging. ● Handles edge cases including null values, empty states, partial data responses, and boundary conditions that reflect real API behavior. ## Prompt

```
## Role
You are an expert API architect specializing in RESTful design patterns, data modeling, and production-grade response structures.

## Task
Generate comprehensive mock API responses that follow industry-standard RESTful conventions. Include:

- Appropriate HTTP status codes and realistic headers (content-type, rate limiting, CORS, cache control)
- Well-formed JSON with proper indentation, data types, and naming conventions (camelCase or snake_case)
- Realistic business data patterns including nested objects, arrays, metadata, and ISO 8601 timestamps
- Pagination structures (cursor-based, offset-based, or page tokens) where applicable
- Error objects with HTTP status codes, error codes, messages, field-level validation details, and trace IDs
- Edge cases: null handling, empty states, partial data, and boundary conditions

## Context
{{api-requirements}}

The mock responses will be used for {{use-case}}.

## Output
For each endpoint, provide:

**Endpoint:** `[METHOD] /path`

**Status:** `[code] [reason]`

**Headers:**
```
Content-Type: application/json
[other relevant headers]
```

**Body:**
```json
{
 [properly indented, realistic JSON response]
}
```

Cover success cases and at least one error scenario per endpoint. Ensure all data values reflect realistic production patterns for the domain.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-requirements}}、{{use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mock API Response Generator for RESTful APIs is a free AI prompt that generates realistic, production-grad…
