# Scheduling System Code Generator for ChatGPT

## 簡介

The Scheduling System Code Generator is a free AI prompt that builds complete, production-ready scheduling applications for developers and engineering teams. This scheduling system prompt for ChatGPT outputs full-stack code including a PostgreSQL database schema, availability management engine with recurring patterns, React booking interface using shadcn/ui, admin dashboard with calendar views, automated notification workflows, Express API backend, and Redis caching layer. It handles complex coordination logic like timezone conflicts, double-booking prevention, DST changes, and race conditions while delivering a minimal interface inspired by Linear and Calendly. The prompt runs on ChatGPT, Claude, and Cursor, generating TypeScript code with complete deployment instructions and testing strategies for edge cases. Developers use it to build appointment booking systems, resource schedulers, service reservation platforms, and calendar coordination tools without starting from scratch. Reach for this prompt when you need enterprise-grade scheduling logic paired with an intuitive user experience, or when generic calendar tools fail to handle your business rules and conflict resolution requirements. ● Outputs complete database schema with PostgreSQL tables, relationships, indexes, and timezone-aware migrations ● Generates availability calculation algorithms supporting recurring patterns, buffer times, and custom business constraints ● Builds React booking interface and admin dashboard with calendar views, analytics, and bulk operations ● Includes notification queue system with email and SMS templates for confirmations, reminders, and cancellations ● Provides deployment configuration, environment templates, and edge-case testing scenarios for race conditions and simultaneous bookings ## Prompt

```
## Role

You are an elite systems architect and full-stack engineer with deep expertise in calendar logic, timezone handling, conflict resolution algorithms, and real-time synchronization. You combine enterprise-grade reliability engineering with a mastery of creating intuitive booking experiences.

## Task

Build a complete, production-ready scheduling system with:

- Availability management engine with recurring patterns and business rules
- Smart booking interface with conflict detection
- Automated notification workflows (confirmations, reminders, cancellations)
- Admin dashboard with calendar views and analytics
- Calendar sync capabilities
- Complete tech stack: React/Next.js frontend, Node.js/Express backend, PostgreSQL database, Redis caching

Design with Linear.app's minimalist aesthetic meets Calendly's effortless booking flow.

## Context

The client faces coordination chaos that generic calendar tools cannot solve. Previous systems collapsed under edge cases: double-bookings, timezone disasters, no-show management, and clunky user flows. This system must handle gnarly backend complexity while presenting a dead-simple interface that requires no training, meeting enterprise-grade reliability standards.

**Scheduling Domain:**
{{scheduling-purpose}}

**Business Rules:**
{{business-constraints}}

**System Requirements:**
{{system-requirements}}

## Output

Deliver production-ready code with this structure:

### 1. Domain Analysis
Define the scheduling domain, constraints, and business requirements based on the inputs above.

### 2. Database Schema
Complete PostgreSQL schema with tables, relationships, indexes, and timezone handling. Include migrations.

### 3. Availability Engine
Core algorithm for calculating open slots with recurring patterns, buffer times, and business rules.

### 4. Booking Interface
React components using shadcn/ui for the public-facing booking flow. Mobile-optimized with TypeScript.

### 5. Admin Dashboard
Management panel with calendar views, analytics, bulk operations, and configuration controls.

### 6. Notification System
Email/SMS queue system with templated confirmations, reminders, and cancellation workflows.

### 7. API Architecture
RESTful backend with Express routes, middleware, validation, and comprehensive error handling.

### 8. Deployment Setup
Complete file structure, environment configs (.env templates), and deployment instructions for the specified hosting platform.

### 9. Testing Strategy
Edge case scenarios covering simultaneous bookings, timezone boundaries, DST changes, cancellation workflows, and race conditions.

**Technical Requirements:**

- TypeScript throughout for type safety
- Proper separation of concerns and maintainable architecture
- Performance optimization with Redis caching strategy
- Comprehensive error handling and validation
- Real-time synchronization considerations
- Scalability patterns for enterprise load
- Detailed README with architecture explanations and setup procedures

Focus on bulletproof reliability while maintaining dead-simple user experience. Solve the invisible complexity that makes scheduling systems either bulletproof or brittle.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-constraints}}、{{scheduling-purpose}}、{{system-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Scheduling System Code Generator is a free AI prompt that builds complete, production-ready scheduling app…
