# Build Authentication Systems

## 簡介

The Build Authentication Systems prompt is a free AI prompt that generates enterprise-grade authentication code with defense-in-depth security for regulated industries like fintech, healthcare, and government. It produces complete React/Next.js 14 implementations including secure login and signup forms with real-time validation, password reset flows, session management with JWT tokens and bcrypt hashing, rate limiting, CSRF protection, XSS prevention, optional 2FA, brute-force mitigation, admin dashboards, route protection middleware, audit logging, and error handling. This authentication system prompt for ChatGPT, Claude, and Cursor uses TypeScript, Tailwind CSS, Prisma ORM, and PostgreSQL to deliver reusable UI components, secure API routes, database schemas, and testing strategies for security edge cases. Reach for it when you need to build scalable auth infrastructure for millions of concurrent users under zero-trust principles while meeting compliance standards like HIPAA, GDPR, or PCI-DSS. ● Outputs full database schemas for users, sessions, tokens, and audit tables with proper indexing and constraints. ● Provides secure API route implementations for registration, login, logout, password reset, and token refresh with comprehensive error handling. ● Includes React components for forms with client-side validation, route guards, session checks, and admin dashboards styled with Tailwind CSS. ● Delivers security implementations covering CSRF tokens, XSS sanitization, rate limiting per endpoint, session expiry automation, and audit logging for compliance. ## Prompt

```
## Role

You are an expert full-stack security architect specializing in enterprise authentication systems for regulated industries. You design auth flows that balance defense-in-depth security with seamless user experience, treating every system as mission-critical infrastructure.

## Task

Create a complete, production-ready authentication system including:

- Secure login/signup forms with real-time validation
- Password reset flows and session management
- Rate limiting, CSRF protection, and XSS prevention
- Optional 2FA and brute-force mitigation
- Admin dashboard and route protection middleware
- Audit logging and comprehensive error handling

Use React/Next.js 14, TypeScript, Tailwind CSS, JWT tokens, bcrypt hashing, Prisma ORM, and PostgreSQL. Provide reusable UI components, secure API routes, proper database schemas, and testing strategies for security edge cases. Focus on scalable architecture for millions of concurrent users under zero-trust principles.

## Context

{{project-requirements}}

*Include: industry/use case (fintech, healthcare, government, etc.), expected user scale and growth projections, compliance standards (HIPAA, GDPR, PCI-DSS, etc.), tech stack preferences or constraints, threat model and security level.*

## Output

Structure your response as:

**Security Analysis**  
Assess required security level and compliance needs based on the industry.

**Database Schema**  
Complete design with users, sessions, and security tables.

**Auth API Routes**  
Secure implementations for registration, login, logout, password reset, and session management.

**UI Components**  
React components for forms, validation, route protection, and admin dashboard with clean, modern aesthetic.

**Security Implementation**  
CSRF protection, XSS prevention, rate limiting, session security, and audit logging.

**Middleware & Protection**  
Route guards, token refresh mechanisms, and session cleanup automation.

**Testing Strategy**  
Security testing for edge cases, penetration testing guidance, and vulnerability assessment.

**Deployment Guide**  
Production setup, environment variables, monitoring tools, and security best practices.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Authentication Systems prompt is a free AI prompt that generates enterprise-grade authentication cod…
