# Build Task Management APIs

## 簡介

The Build Task Management APIs prompt is a free AI prompt that creates a complete, production-ready CRUD API system for task management applications with authentication, clean architecture, and enterprise-grade security patterns. This task management API prompt for ChatGPT, Claude, and Cursor produces a full Next.js App Router (13+) implementation with Prisma ORM, including all four CRUD operations (Create, Read, Update, Delete) for tasks with title, description, status, dueDate, and priority fields. It generates structured code with separated controller, service, and data access layers, authentication middleware for route protection, TypeScript interfaces for type safety, standardized API response formats, input validation schemas, and detailed comments explaining security considerations. Developers use it to build secure, maintainable APIs that handle real user data without creating technical debt or common authentication pitfalls. Reach for this prompt when you need to scaffold a complete API system quickly while maintaining production-grade code quality, proper separation of concerns, and security best practices from day one. ● Produces complete project structure with database schema, authentication middleware, API routes, service layer, utility functions, and TypeScript type definitions. ● Implements authentication middleware and route protection using Supabase or JWT tokens with proper user verification. ● Separates controller logic from business logic services, following clean architecture principles that prevent technical debt. ● Includes input validation schemas, sanitization for all endpoints, standardized API response formats, and consistent error messaging. ## Prompt

```
## Role

You are a senior full-stack architect with deep expertise in Next.js production systems, API design, and authentication patterns. You specialize in building secure, maintainable applications with proper separation of concerns, comprehensive error handling, and patterns that prevent technical debt.

## Task

Create a complete, production-ready CRUD API system for a task management application using Next.js App Router (13+) and Prisma. Build all four operations (Create, Read, Update, Delete) with authenticated route protection. Each task must include title, description, status, dueDate, and priority fields.

## Context

{{api-requirements}}

The application must handle real user data securely. Follow enterprise-grade patterns for:
- Clean architecture with separated controller, service, and data access layers
- Comprehensive authentication middleware and route protection
- TypeScript interfaces and strict type safety
- Standardized API response formats with consistent error messaging
- Input validation schemas and sanitization for all endpoints
- Detailed code comments explaining security considerations and architectural decisions

## Output

Provide complete, implementable code organized as follows:

**Project Structure**
Complete folder and file organization for the API system

**Database Schema**
Prisma schema definition with all required models and relationships

**Authentication Middleware**
Security middleware for route protection and user verification

**API Routes**
Complete CRUD API route implementations with proper error handling

**Service Layer**
Business logic services separated from controller logic

**Utility Functions**
Reusable helper functions for validation, responses, and error handling

**Type Definitions**
TypeScript interfaces and types for type safety

**Implementation Guide**
Step-by-step setup instructions and deployment considerations

Focus on production-ready code quality that handles edge cases. Provide specific, secure implementations following Next.js 13+ App Router conventions and modern best practices.
```

## 用法 / Usage
- 必填變數 / Variables: {{api-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Task Management APIs prompt is a free AI prompt that creates a complete, production-ready CRUD API s…
