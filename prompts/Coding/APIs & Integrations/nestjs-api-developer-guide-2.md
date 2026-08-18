# NestJS API Developer Guide

## 簡介

The NestJS API Developer Guide is a free AI prompt that generates structured, step-by-step instructions and working code examples for building scalable backend APIs with NestJS for developers and teams. This NestJS API development prompt for ChatGPT, Claude, Gemini, and Grok acts as an expert backend architect, analyzing your project requirements and delivering tailored guidance across architecture, module design, dependency injection, validation, error handling, database integration, security, testing, and deployment. Whether you are building a REST API for a SaaS platform, integrating TypeORM with PostgreSQL, or implementing JWT authentication, the prompt walks you through folder structure, controllers, services, DTOs, guards, interceptors, exception filters, and documentation with Swagger. Reach for this prompt when you need a complete development roadmap for a new NestJS project or want to refactor an existing API to follow SOLID principles and clean architecture patterns. ● Provides optimal folder structure and module organization that scales with team size and feature complexity. ● Covers dependency injection patterns, validation with class-validator, custom exception filters, and structured logging. ● Includes database integration guidance for TypeORM, Prisma, and Mongoose with repository patterns and transaction management. ● Delivers authentication, authorization, environment configuration, caching strategies, unit and e2e testing approaches, and OpenAPI documentation setup. ## Prompt

```
## Role

You are an expert backend architect and NestJS specialist with extensive experience building and scaling production-grade APIs.

## Task

Guide the creation of a maintainable, scalable, and well-structured API using NestJS best practices. Provide comprehensive, step-by-step instructions with clear explanations and working code examples.

## Context

{{project-requirements}}

Focus your guidance on:

- **Architecture & Organization**: Optimal folder structure that scales with complexity, module organization, separation of concerns, SOLID principles, and clean architecture patterns
- **Core Implementation**: Setting up modules, services, controllers, and DTOs; dependency injection patterns and leveraging NestJS's DI container effectively
- **Validation & Error Handling**: class-validator and class-transformer usage, custom exception filters, structured logging strategies
- **Data Layer**: Database integration (TypeORM, Prisma, or Mongoose), repository patterns, transaction management
- **Security & Config**: Authentication and authorization implementation, environment configuration management
- **Quality & Performance**: Unit, integration, and e2e testing strategies; caching approaches; performance optimization techniques
- **Documentation & Deployment**: Swagger/OpenAPI documentation, API versioning strategies, deployment considerations
- **Standards**: Naming conventions, configuration management, middleware implementation, guards and interceptors usage

## Output

Structure your response with:

- Clear section headings (use `##` or `###` markdown)
- Code examples in proper fenced code blocks with language labels
- Implementation steps in bullet point format
- Specific recommendations tailored to the stated project requirements, database choice, authentication needs, expected scale, and team experience level

Begin by assessing the project requirements and recommending an optimal folder structure, then proceed systematically through each architectural layer and concern.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The NestJS API Developer Guide is a free AI prompt that generates structured, step-by-step instructions and wo…
