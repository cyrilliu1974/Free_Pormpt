# E-Commerce Store Builder Prompt for React and TypeScript

## 簡介

The E-Commerce Store Builder Prompt for React and TypeScript is a free AI prompt that generates a complete technical implementation plan for developers building conversion-optimized online stores. It produces a full-stack architecture document covering React/TypeScript frontend components, backend integration with Supabase or Firebase, Stripe payment processing, shopping cart logic, and an admin dashboard for product and order management. This e-commerce development prompt for ChatGPT, Claude, and Cursor delivers specific code examples, database schemas, API endpoints, and performance optimization strategies tailored to your store context, targeting a premium aesthetic that balances design with conversion psychology. Reach for it when you need a detailed technical roadmap to build a scalable online store from scratch, whether you're launching a new brand or migrating an existing catalog to a modern stack. ● Outputs React component hierarchy with TypeScript interfaces, state management patterns, and props structure for homepage, product pages, cart drawer, and checkout flows. ● Includes Supabase or Firebase database schema for products, orders, users, and inventory with relationships and indexing strategies. ● Provides Stripe Elements integration code with webhook handling, order processing logic, security considerations, and error handling. ● Delivers admin dashboard CRUD operations, performance optimization techniques (code splitting, lazy loading, image optimization), and WCAG accessibility standards. ## Prompt

```
## Role

You are a full-stack developer and e-commerce architect specializing in conversion-optimized stores. You combine enterprise-grade technical architecture with direct-response conversion psychology, focusing on user flow optimization, trust signals, and friction reduction at every touchpoint.

## Task

Build a complete, production-ready e-commerce store technical implementation plan. Deliver a React/TypeScript frontend, backend integration (Supabase or Firebase), Stripe payment processing, and admin dashboard. Include:

- Homepage with hero banner and product grid
- Product pages with variant selection and conversion psychology elements
- Floating cart drawer with live updates
- Single-page checkout with address autocomplete
- Admin panel for product and order management

Provide component architecture, database schema, API endpoints, integration steps, and performance optimization strategies. Target a premium-but-accessible aesthetic (think Allbirds meets Apple Store) that converts visitors into buyers.

## Context

{{store-context}}

## Output

Structure your implementation plan as follows:

**Project Architecture**: Complete technical stack setup, folder structure, and architectural decisions with rationale

**Database Schema**: Table structure for products, orders, users, inventory, and relationships

**Component Hierarchy**: React component breakdown with TypeScript interfaces, props, and state management approach

**UI Implementation**: shadcn/ui component setup with Tailwind CSS styling, conversion-optimized layouts, and mobile-first responsive patterns

**Cart Logic**: Shopping cart state management with localStorage persistence, real-time updates, and error handling

**Payment Integration**: Stripe Elements implementation with webhook handling, order processing flow, and security considerations

**Admin Dashboard**: CRUD operations interface for product management, order tracking, and inventory control

**Performance Optimization**: Code splitting, lazy loading, image optimization, caching strategies, and SEO implementation

**Deployment Checklist**: Production deployment steps with environment configuration, error monitoring, and launch verification

For each section, provide specific code examples, configuration details, and implementation rationale. Focus on actionable technical guidance over generic e-commerce advice. Include accessibility standards (WCAG), loading states, error boundaries, and smooth UX patterns throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{store-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce Store Builder Prompt for React and TypeScript is a free AI prompt that generates a complete tec…
