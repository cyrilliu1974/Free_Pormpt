# Technical Blueprint Generator for Software Projects

## 簡介

The Technical Blueprint Generator for Software Projects is a free AI prompt that transforms business ideas into executable technical documentation for development teams. This technical blueprint prompt for ChatGPT produces a comprehensive nine-section document covering product design requirements, tech stack recommendations with architectural rationale, application flowcharts, project rules, phased implementation timelines, frontend and backend guidelines, React optimization patterns, and integrated security checklists. It runs on ChatGPT, Claude, Gemini, and Grok, delivering markdown-formatted output that includes specific technology selections, code-level guidance, and security-first design principles. Software architects use it to create complete technical specifications that development teams can execute without additional consultation, turning a project brief into actionable implementation plans with milestone dates, component architecture, API design patterns, and WCAG 2.1 accessibility standards. Reach for this prompt when you need to document a new software project with enterprise-grade technical detail and security considerations built in from the start. ● Produces nine structured sections covering product vision, tech stack selection, user flows, development workflows, and phased implementation timelines with milestone dependencies. ● Includes frontend component architecture with performance budgets, backend API design patterns, database schema guidance, and authentication touchpoints. ● Delivers React-specific optimization techniques with code examples demonstrating memoization, code splitting, TypeScript patterns, and custom hooks. ● Integrates an 11-point security checklist addressing XSS prevention, SQL injection protection, JWT authentication, HTTPS encryption, rate limiting, CORS configuration, and penetration testing schedules. ## Prompt

```
## Role
You are a senior technical architect specializing in full-stack system design, security engineering, and technical documentation for enterprise software projects.

## Task
Transform the provided business concept into a complete technical implementation blueprint with nine structured sections that a development team can execute without further consultation.

## Context
The blueprint must address:
{{project-brief}}

Include specific technology recommendations with architectural rationale, security-first design principles, phased implementation timelines, and code-level guidance suitable for modern web applications.

## Output
Deliver a comprehensive technical blueprint in markdown format with these nine sections:

### 1. Product Design Requirements
- Product vision and core value proposition
- Target user personas and market positioning
- Problem-solution fit analysis
- Key features and functionality scope

### 2. Tech Stack
- Frontend framework, state management, and UI libraries with selection rationale
- Backend runtime, framework, and API architecture
- Database choice and data modeling approach
- Infrastructure, hosting, and deployment pipeline
- Third-party services and integrations

### 3. App Flowchart
- Complete user journey from entry to key outcomes
- System component interactions and data flow
- Authentication and authorization touchpoints
- Error handling and edge case paths

### 4. Project Rules
- Development workflow (branching strategy, code review, CI/CD)
- Coding standards and style conventions
- Testing requirements (unit, integration, e2e coverage thresholds)
- Documentation and knowledge transfer protocols

### 5. Implementation Plan
- Phase 1: Foundation (auth, core data models, basic UI)
- Phase 2: Core Features (primary user workflows)
- Phase 3: Advanced Features (secondary functionality)
- Phase 4: Optimization & Launch (performance, security audit, deployment)
- Milestone dates and dependencies

### 6. Frontend Guidelines
- Component architecture and folder structure
- State management patterns
- Responsive design principles and breakpoints
- Accessibility standards (WCAG 2.1 AA minimum)
- Performance budgets (FCP, LCP, TTI targets)

### 7. Backend Guidelines
- API design (RESTful or GraphQL patterns, versioning)
- Database schema and relationships
- Authentication and session management
- Background job processing
- Logging, monitoring, and observability

### 8. Optimized React Code Guidelines
- Performance optimization techniques (memoization, code splitting, lazy loading)
- Custom hooks for reusable logic
- Component composition patterns
- Type safety with TypeScript
- Example code snippets demonstrating best practices

### 9. Integrated Security Checklist
Weave these 11 security measures into relevant sections above, then summarize enforcement:
1. Input validation and sanitization (XSS prevention)
2. Parameterized queries (SQL injection prevention)
3. Authentication (JWT/OAuth2, MFA)
4. Authorization and role-based access control
5. HTTPS/TLS encryption for data in transit
6. Environment variable management for secrets
7. Rate limiting and DDoS protection
8. CORS configuration
9. Dependency vulnerability scanning
10. Security headers (CSP, HSTS, X-Frame-Options)
11. Regular security audits and penetration testing schedule

Use markdown headings (#, ##, ###), bullet points, numbered lists, tables where appropriate, and code blocks for technical examples. Provide specific, actionable recommendations rather than generic advice.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-brief}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Technical Blueprint Generator for Software Projects is a free AI prompt that transforms business ideas int…
