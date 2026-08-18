# Build REST API Endpoints

## 簡介

The Build REST API Endpoints prompt is a free AI prompt that generates complete, production-ready CRUD REST API specifications for backend developers and API architects. This REST API prompt for ChatGPT, Claude, and Cursor analyzes your resource structure and produces endpoint definitions with resource-based URLs, HTTP verb mappings, request/response schemas, validation rules, status codes, error handling patterns, and database operation pseudocode. You provide the resource details and stack via the api-specification variable, and the prompt systematically builds CREATE (POST), READ (GET single and collection), UPDATE (PUT/PATCH), and DELETE operations following stateless web service conventions. Use it when designing new web services, documenting existing APIs, or establishing standards-compliant backend architectures. It is built for backend engineers who need structured, implementable API designs that follow resource-oriented principles and HTTP semantics. ● Outputs endpoint specifications for all CRUD operations with URL patterns, route parameters, and HTTP methods. ● Defines request and response schemas with required fields, validation constraints, and error formats. ● Includes database operation logic, status code mappings (200, 201, 204, 400, 404, 409, 500), and error handling for common failure cases. ● Supports query parameters for filtering, pagination, and sorting on collection endpoints. ## Prompt

```
## Role

You are an expert REST API architect with deep knowledge of resource-based design, HTTP semantics, and stateless web service patterns.

## Task

Design a complete, production-ready CRUD REST API for the specified resource. Deliver endpoint specifications, HTTP verb mappings, request/response schemas, status codes, validation rules, error handling patterns, and database operation logic.

## Context

**Resource & stack:**
{{api-specification}}

Analyze the resource structure, identify relationships, and systematically build each endpoint. URLs must represent resources and hierarchies clearly. Maintain consistency across all operations. Follow RESTful conventions: resource-based URLs, proper HTTP verbs, stateless communication, and standards-compliant behavior.

## Output

Organize your response with clear headings for each CRUD operation:

### CREATE (POST)
- URL pattern with route parameters
- HTTP method and status codes (201, 400, 409, 500)
- Request schema (headers, body structure, required fields)
- Response schema (success payload, error format)
- Validation rules and constraints
- Database insert operation pseudocode or implementation snippet
- Error handling for common failure cases

### READ (GET single + GET collection)
- URL patterns for single resource and collection
- Query parameters for filtering, pagination, sorting
- Response schemas for both endpoints
- Database query logic
- Status codes (200, 404, 400, 500)
- Error handling

### UPDATE (PUT/PATCH)
- URL pattern with route parameters
- Partial vs full update handling
- Request payload and validation
- Response schema
- Database update logic
- Status codes (200, 204, 400, 404, 409, 500)
- Error handling

### DELETE (DELETE)
- URL pattern with route parameters
- Confirmation patterns and cascading considerations
- Success/error responses
- Database delete logic
- Status codes (204, 404, 409, 500)
- Error handling

Provide practical, directly implementable code examples in the specified language/framework. Highlight stateless design decisions and scalability considerations where relevant.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build REST API Endpoints prompt is a free AI prompt that generates complete, production-ready CRUD REST AP…
