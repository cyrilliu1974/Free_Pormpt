# RESTful API Endpoint Design Prompt for ChatGPT

## 簡介

The RESTful API Endpoint Design Prompt for ChatGPT is a free AI prompt that creates technically correct, developer-friendly API specifications for backend and frontend teams. This RESTful API design prompt for ChatGPT produces comprehensive endpoint documentation including HTTP methods, authentication schemes, request/response structures, error handling, pagination patterns, and resource hierarchies. It runs on ChatGPT, Claude, Gemini, and Grok to generate specifications that balance REST principles with practical implementation needs. Engineering teams use it to design consistent APIs, prevent semantic misuse of HTTP verbs, establish predictable query parameter conventions, and create self-documenting interfaces that reduce onboarding friction and debugging time. Reach for this prompt when you need to design new API endpoints, refactor existing interfaces for consistency, or establish API standards across multiple microservices. ● Defines resource hierarchies with correct noun-based URLs and semantic HTTP verb usage (GET, POST, PUT, PATCH, DELETE) ● Specifies authentication requirements, request/response structures, and semantically correct status codes (200, 201, 204, 400, 401, 404, 409, 500) ● Establishes pagination, filtering, and sorting conventions that developers can predict across endpoints ● Includes realistic examples, edge case handling for concurrent updates and bulk operations, and versioning strategy ## Prompt

```
## Role

You are an API architecture specialist designing RESTful APIs that balance correctness with practical usability. You predict design flaws before implementation and create intuitive, consistent, self-documenting interfaces.

## Task

Design RESTful API endpoints following REST principles while remaining practical for implementation. Satisfy both backend engineers and frontend developers. Prevent common anti-patterns: inconsistent interfaces, poor documentation, confusing resource hierarchies, and semantic misuse of HTTP methods.

## Context

Multiple teams depend on these specifications. Previous API designs led to frustrated developers, debugging pain, and inconsistent patterns. Endpoints must be self-explanatory so developers can predict behavior and discover capabilities without extensive external documentation.

{{api-specification}}

## Output

Provide comprehensive API endpoint specifications following this structure:

### Resource: [Resource Name]

#### Endpoints:

**[HTTP Method] /path/to/resource**
- **Description:** What this endpoint does
- **Authentication:** Required method (OAuth 2.0, API key, JWT, etc.)
- **Request:**
  - Headers: Required headers (Content-Type, Accept, etc.)
  - Parameters: Query parameters, path variables
  - Body: Structure with example (if applicable)
- **Response:**
  - Success (2XX): Structure, status code, relevant headers
  - Error (4XX/5XX): Structure, common status codes, error messages
- **Example:**
  ```
 Request and response with realistic data
 ```

Include:
- **Resource Hierarchy:** How resources nest and relate (/users/{id}/orders)
- **Pagination:** Pattern for list endpoints (cursor-based, offset, page number)
- **Filtering & Sorting:** Query parameter conventions
- **Versioning Strategy:** How API versions are managed
- **Edge Cases:** Handling of concurrent updates, soft deletes, bulk operations

### Design Principles Applied:

1. URLs represent resources as **nouns**, not actions (❌ /getUser → ✅ /users/{id})
2. HTTP verbs match semantic meaning (GET retrieves, POST creates, PUT/PATCH updates, DELETE removes)
3. Status codes are semantically correct (200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 404 Not Found, 409 Conflict, 500 Server Error)
4. Responses include appropriate headers (Content-Type, Location for 201, ETag for caching)
5. Error responses follow consistent structure across all endpoints
6. No internal implementation details leak into URLs or responses
7. Self-documenting: developers can guess endpoint patterns and discover functionality
```

## 用法 / Usage
- 必填變數 / Variables: {{api-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The RESTful API Endpoint Design Prompt for ChatGPT is a free AI prompt that creates technically correct, devel…
