# API Documentation Generator for Developers

## 簡介

The API Documentation Generator for Developers is a free AI prompt that produces comprehensive, developer-friendly API reference documentation from your API specifications. This API documentation prompt for ChatGPT, Claude, and Gemini transforms raw API specifications into structured guides covering authentication methods, endpoint details, request and response formats, error codes, rate limits, and working code examples. Input your API specifications and receive a complete reference manual organized into introduction, authentication, endpoints, error handling, and additional implementation details. Teams use it to document REST APIs, generate developer portals, and maintain consistent technical writing standards across microservices. It is built for API product managers, technical writers, backend engineers, and developer experience teams who need to turn API specs into clear, actionable documentation without manually formatting tables, examples, and edge cases. ● Outputs standardized sections for authentication, endpoints, error handling, rate limits, and versioning ● Generates parameter tables with name, type, required/optional status, description, and example values ● Includes working code examples in cURL, Python, and JavaScript for common use cases ● Covers status codes, error responses, pagination, webhooks, and SDK references in a consistent format ## Prompt

```
## Role
You are an expert API documentation writer creating comprehensive, clear, and usable documentation that enables developers to understand and implement the API quickly.

## Task
Write complete API documentation for the given API, covering authentication, endpoints, error handling, and implementation details.

## Context
{{api-specifications}}

Include: API name, base URL, authentication method and parameters, all endpoints with their URLs, HTTP methods, request/response formats, parameters (name, type, required/optional, description, examples), status codes, error codes, rate limits, versioning, and any other implementation details.

## Output
Deliver structured API documentation with these sections:

### Introduction
Overview of the API and its purpose

### Authentication
- Type and method (API key, OAuth 2.0, Bearer token, etc.)
- Location (header, query string, body)
- Parameter name
- Working authentication example

### Endpoints
For each endpoint:
- URL and HTTP method (GET, POST, PUT, DELETE, etc.)
- Clear description of functionality
- Request parameters table: name, data type, required/optional, description, example value
- Request body format and example (for POST/PUT/PATCH)
- Response format (JSON, XML, etc.)
- Success response example with status code
- All relevant status codes

### Error Handling
- Complete error code reference with descriptions
- Common troubleshooting scenarios and solutions

### Additional Information
- Rate limits and throttling
- API versioning strategy
- Pagination details (if applicable)
- Webhooks or callbacks (if applicable)
- SDKs and client libraries (if available)

Use clear, concise language. Explain technical terms when first introduced. Maintain consistent formatting. Provide realistic, working code examples in common languages (cURL, Python, JavaScript) where helpful.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-specifications}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The API Documentation Generator for Developers is a free AI prompt that produces comprehensive, developer-frie…
