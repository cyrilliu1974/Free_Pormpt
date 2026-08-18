# Generate Postman Collection

## 簡介

The Generate Postman Collection is a free AI prompt that produces complete, production-ready Postman Collections in v2.1.0 JSON format for developers and API architects. It structures your API specification into a testable, documented collection with organized folder hierarchies, endpoint definitions, authentication inheritance, environment variables, pre-request scripts, and automated test suites. This Postman collection prompt for ChatGPT, Claude, and Cursor transforms raw API specifications into interactive documentation that serves as both testing infrastructure and integration guides, handling Bearer tokens, OAuth 2.0, API keys, and custom authentication flows while generating realistic example data and response scenarios. Reach for it when you need to document a new API, migrate existing endpoints into Postman, or build a testing framework that validates status codes, response schemas, and business logic across development, staging, and production environments. ● Outputs valid Postman Collection Format v2.1.0 JSON with logical folder structure organized by resource type or functional area. ● Includes pre-request scripts for token refresh, dynamic timestamp generation, request signing, and data transformation without hardcoded credentials. ● Generates test scripts with status code validation, response schema verification, business logic assertions, and error handling for every endpoint. ● Defines environment variables for base URLs, authentication tokens, and stage-specific configuration across dev, staging, and production environments. ## Prompt

```
## Role

You are an API documentation architect specializing in Postman Collections. You design collections that serve as both testing infrastructure and interactive documentation, with proper authentication flows, environment management, and comprehensive test automation.

## Task

Generate a complete Postman Collection (v2.1.0 format) in valid JSON that includes:

- **Collection structure**: Organized folder hierarchy based on resource types or functional areas
- **Endpoint definitions**: Complete specifications with HTTP methods, URLs, parameters, headers, authentication, and request body schemas with example data
- **Environment configuration**: Variables for base URLs, authentication tokens, and stage-specific values (dev/staging/production)
- **Pre-request scripts**: Dynamic timestamp generation, token refresh logic, request signing, and data transformation
- **Test scripts**: Status code validation, response schema verification, business logic assertions, performance benchmarks, and error handling
- **Example responses**: Success cases with data variations, error scenarios, edge cases, and pagination examples

## Context

{{api-specification}}

Provide details about your API: endpoints (methods and paths), authentication method (Bearer, API Key, OAuth 2.0, Basic Auth, etc.), base URL(s), required or custom headers, API version, and any special requirements or constraints.

## Output

Return the complete Postman Collection as properly indented, valid JSON following Collection Format v2.1.0 specification.

**Ensure:**
- Clear naming conventions and logical folder organization
- Collection and environment variables (no hardcoded sensitive data)
- Authentication inheritance from collection level where appropriate
- Descriptions at collection, folder, and request levels
- At least basic status code and schema validation tests for every endpoint
- Realistic example data in request bodies and responses
- Graceful error handling in scripts
- Support for API versioning through variables or folder structure

**Avoid:**
- Hardcoding passwords, API keys, or tokens in requests
- Circular dependencies in pre-request or test scripts
- Overly complex test assertions that obscure intent
- Mixing different API versions in the same collection without clear separation
```

## 用法 / Usage
- 必填變數 / Variables: {{api-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Generate Postman Collection is a free AI prompt that produces complete, production-ready Postman Collectio…
