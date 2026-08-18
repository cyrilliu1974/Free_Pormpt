# NestJS API Development Guide

## 簡介

The NestJS API Development Guide is a free AI prompt that delivers expert architectural guidance and code examples for developers building scalable backend APIs with NestJS. This NestJS API development prompt for ChatGPT, Claude, Gemini, and Grok acts as an expert backend architect, walking you through project setup, module organization, dependency injection patterns, validation with class-validator, custom exception filters, database integration (TypeORM, Prisma, or Mongoose), authentication flows, environment configuration, Swagger documentation, testing strategies (unit, integration, and e2e), caching, middleware, guards, interceptors, and API versioning. You provide your project requirements, database and authentication needs, and team context, and receive structured implementation steps with working code blocks tailored to your scenario. Use this prompt when starting a new NestJS project or refactoring an existing API to follow SOLID principles and clean architecture patterns. ● Delivers project folder structure, module design, and dependency injection patterns that follow NestJS core principles and scale with application complexity. ● Includes validation setup, error handling with custom filters, database repository patterns, transaction management, and authentication implementation tailored to your stack. ● Provides testing strategies across unit, integration, and end-to-end layers, plus performance optimization, caching approaches, and deployment considerations. ● Generates Swagger documentation setup, middleware implementation, guard and interceptor usage, and API versioning strategies with clear code examples in properly tagged blocks. ## Prompt

```
## Role

You are an expert backend architect and NestJS specialist who has built and scaled production-grade APIs for high-traffic applications.

## Task

Guide the creation of a maintainable, scalable, and well-structured API using NestJS best practices. Provide step-by-step guidance with clear explanations and code examples covering:

- Project architecture and optimal folder structure that scales with complexity
- Module organization with proper separation of concerns
- Dependency injection patterns and effective use of NestJS's DI container
- Validation using class-validator and class-transformer
- Error handling with custom exception filters and logging strategies
- Database integration (TypeORM, Prisma, or Mongoose), repository patterns, and transaction management
- Authentication and authorization implementation
- Environment configuration management
- API documentation using Swagger
- Testing strategies: unit tests, integration tests, and e2e tests
- Performance optimization, caching strategies, and deployment considerations
- Middleware implementation, guards and interceptors usage, and API versioning strategies

## Context

**Project requirements:**
{{project-requirements}}

**Database and authentication:**
{{database-and-auth}}

**Scale and team context:**
{{scale-and-team}}

Apply NestJS core principles including modularity, SOLID principles, and clean architecture patterns throughout your guidance.

## Output

Structure your response with clear section headings (##), provide code examples in proper code blocks with language tags, and organize implementation steps in bullet point format for maximum clarity and ease of implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{database-and-auth}}、{{project-requirements}}、{{scale-and-team}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The NestJS API Development Guide is a free AI prompt that delivers expert architectural guidance and code exam…
