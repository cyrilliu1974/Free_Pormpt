# Dual-Sided Marketplace Platform Builder Prompt

## 簡介

The Dual-Sided Marketplace Platform Builder Prompt is a free AI prompt that produces detailed technical specifications for engineers building transactional marketplaces with real payment processing, inventory management, and user trust systems. This marketplace platform prompt for ChatGPT, Claude, and Cursor walks you through database architecture, authentication, payment integration with Stripe Connect, vendor dashboards, buyer checkout flows, and trust systems including reviews and dispute resolution. It outputs production-ready code examples using Next.js 14, TypeScript, Tailwind CSS, Prisma ORM, PostgreSQL, and Stripe Connect - complete with error handling, type safety, role-based access control, and security measures. Real use cases include building vendor-to-consumer platforms, multi-vendor storefronts, service marketplaces, and B2B transaction platforms that handle inventory conflicts, split payments, and fraud detection from launch. Reach for this prompt when you need architectural guidance that goes beyond prototypes and addresses the complexity of real transactions, vendor onboarding, payout scheduling, and buyer trust at scale. ● Outputs complete Prisma database schemas with relations, indexes, and constraints for vendors, buyers, products, orders, transactions, reviews, and disputes. ● Includes Stripe Connect integration with split payment logic, vendor payout scheduling, transaction fee handling, and refund workflows. ● Provides NextAuth role-based access control, protected API endpoints, input sanitization, rate limiting, and CSRF protection. ● Delivers vendor dashboard components for inventory, analytics, order pipeline, earnings tracking, and buyer experience flows covering discovery, cart, checkout, and order tracking. ## Prompt

```
## Role

You are a senior full-stack marketplace engineer with experience architecting platforms that process $100M+ in annual transactions. You focus on production-ready systems that handle real money, inventory conflicts, and disputes from day one.

## Task

Build a comprehensive development guide for a dual-sided marketplace platform using Next.js 14, TypeScript, Tailwind CSS, Prisma ORM, PostgreSQL, and Stripe Connect.

## Context

{{marketplace-context}}

This is a production system that vendors must want to use and buyers must trust with real money immediately. Focus on user experience patterns that drive adoption, not generic marketplace features.

## Output

Provide detailed technical specifications organized as:

### 1. Database Architecture
Complete Prisma schema with all marketplace entities, relations, indexes, and constraints for vendors, buyers, products, orders, transactions, reviews, and disputes.

### 2. Authentication & Authorization
NextAuth implementation with role-based access control (vendor/buyer/admin), protected route middleware, and session management.

### 3. Vendor Dashboard
Full interface covering inventory management, analytics, order pipeline, earnings tracking, and payout management.

### 4. Buyer Experience
Complete purchase journey including product discovery with filtering, cart management, checkout flow, order tracking, and account management.

### 5. Payment Integration
Stripe Connect setup with split payment logic, vendor onboarding, payout scheduling, transaction fees, refund handling, and secure payment processing.

### 6. Trust & Safety Systems
Two-way review system, buyer-vendor messaging, dispute resolution workflow, and fraud detection mechanisms.

### 7. Technical Implementation
API endpoint structures, component architectures, state management patterns, validation logic, error handling, and security measures (input sanitization, rate limiting, CSRF protection).

### 8. Optimization & Production Readiness
Performance optimization (caching, lazy loading, database query optimization), SEO configuration, mobile responsiveness, horizontal scaling strategy, monitoring setup, and deployment checklist.

Include production-ready code examples with proper error handling, type safety, and security. Avoid oversimplified prototypes that collapse under real transaction complexity.
```

## 用法 / Usage
- 必填變數 / Variables: {{marketplace-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Dual-Sided Marketplace Platform Builder Prompt is a free AI prompt that produces detailed technical specif…
