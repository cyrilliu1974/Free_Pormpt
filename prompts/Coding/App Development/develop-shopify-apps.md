# Shopify App Development Prompt

## 簡介

The Shopify App Development Prompt is a free AI prompt that produces a full technical blueprint and code scaffold for building merchant-ready Shopify applications that meet App Store standards. This Shopify app development prompt for ChatGPT, Claude, and Cursor takes your app requirements and returns a structured development plan covering project architecture, database schema, Shopify Polaris UI component selection, GraphQL queries, OAuth 2.0 authentication flows, webhook management, and TypeScript code examples. It addresses the real challenges of Shopify development: maintaining native admin UX, handling rate limits, ensuring GDPR compliance, and designing for performance under merchant workloads. Use it when you need to move from concept to production-grade code quickly, whether you're building a store automation tool, inventory manager, or custom checkout experience. ● Outputs project file structure, dependency setup, and database models tailored to your tech stack and timeline. ● Provides TypeScript code scaffolds for critical paths including OAuth handlers, webhook listeners, and GraphQL mutations. ● Recommends Shopify Polaris components and layout patterns that feel native to the merchant admin. ● Includes testing checklists, rate-limit strategies, background job architecture, and App Store preparation steps. ## Prompt

```
## Role

You are an expert full-stack Shopify app architect who builds production-ready applications that meet App Store standards. You combine technical depth (authentication, webhooks, API design) with native-quality UI/UX using Shopify Polaris.

## Task

Create a complete development plan and scaffold for a Shopify app that integrates seamlessly into the merchant admin experience, performs well under load, and passes App Store compliance review.

## Context

{{app-requirements}}

The Shopify ecosystem demands high-quality apps. Merchants abandon poorly designed applications with clunky interfaces, slow performance, or workflows that feel foreign to Shopify's admin. This must be production-grade: proper OAuth flows, webhook reliability, Polaris UI components, and compliance with Shopify's technical requirements.

## Output

Deliver a structured development plan covering:

### Project Architecture and Technical Foundation
- Recommended tech stack aligned with the developer's experience
- File structure and dependency setup
- Database schema and data modeling

### Shopify Polaris UI Implementation
- Component selection for native admin feel
- Layout patterns and navigation structure
- Responsive design considerations for the target merchant audience

### Core Feature Development Roadmap
- Implementation sequence for main features
- GraphQL queries and mutations with code examples
- State management and data flow

### API Integration and Webhook Management
- Required Shopify API scopes
- Webhook subscriptions and handler architecture
- Error handling and retry logic

### Authentication and Security
- OAuth 2.0 flow implementation
- Session management and token storage
- GDPR compliance for merchant data

### Performance Optimization
- Query batching and caching strategies
- Rate limit management
- Background job processing

### Testing and App Store Preparation
- Testing checklist (functional, security, performance)
- App Store listing requirements
- Deployment configuration

### Code Scaffold
- Complete file structures with TypeScript
- Production-ready examples for critical paths
- Polaris component implementations
- GraphQL queries and webhook handlers
- Environment configuration templates

Account for the stated timeline, resources, and monetization strategy. Provide architectural explanations alongside code examples. Format all deliverables as clear bullet points with nested details.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Shopify App Development Prompt is a free AI prompt that produces a full technical blueprint and code scaff…
