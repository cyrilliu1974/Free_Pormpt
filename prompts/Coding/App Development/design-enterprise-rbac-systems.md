# Enterprise RBAC System Design Prompt for ChatGPT

## 簡介

The Enterprise RBAC System Design Prompt is a free AI prompt that generates complete, production-ready access control architectures for SaaS platforms and enterprise applications. This RBAC system design prompt for ChatGPT walks through seven implementation phases, producing PostgreSQL schemas with row-level security, a TypeScript permission evaluation engine with Redis caching for sub-20ms latency, a React admin console with role management UI, developer SDKs with hooks and middleware, and audit infrastructure for SOC 2 compliance. It handles multi-tenant isolation, custom roles, granular action-based permissions, resource-level scoping, time-bound access, and 10,000+ permission checks per second. The prompt works on ChatGPT, Claude, and Cursor for full-stack code generation, covering backend services, frontend dashboards, and monitoring setup. Ideal for engineering teams building SaaS products that require enterprise-grade security, compliance officers preparing for audits, or architects replacing hardcoded permission checks with scalable systems. ● Outputs PostgreSQL migrations with tables for roles, permissions, organizations, and immutable audit logs, plus row-level security policies for tenant isolation. ● Generates a React + TypeScript admin console using shadcn/ui with permission assignment grids, drag-and-drop trees, bulk operations, real-time activity feeds, and dark mode styling. ● Builds a Node.js permission evaluation engine with Redis caching, handles conflicting roles and circular inheritance, and enforces separation of duties with automated escalation alerts. ● Creates JavaScript/TypeScript SDKs with React hooks, Express middleware, migration guides, and an interactive permission playground for testing before deployment. ● Includes Prometheus metrics, Grafana dashboards, feature flag rollout strategy, shadow mode logging, and emergency rollback runbooks for phased production migration. ## Prompt

```
## Role

You are an expert security architect and full-stack engineer specializing in enterprise access control systems.

## Task

Design and implement a production-grade Role-Based Access Control (RBAC) system with complete audit trails, multi-tenant isolation, and enterprise compliance readiness.

## Context

{{business-context}}

Tech stack: {{tech-stack}}

## Requirements

The system must support:
- Multi-tenant isolation with organization boundaries
- Standard roles (Admin, Manager, Editor, Viewer) plus custom roles
- Granular action-based permissions (users:read, projects:write, billing:delete)
- Resource-level permissions for per-project/per-team scoping
- Permission inheritance and role composition
- Time-bound access grants
- Immutable audit trails capturing who/what/when/why
- Sub-20ms permission check latency at p99
- 10,000+ permission checks per second
- SOC 2 compliance readiness

## Output

Deliver a complete implementation plan with production-ready code across these phases:

**Phase 1 - Foundation Architecture**
PostgreSQL schema with tables for organizations, users, roles, permissions, role_permissions, user_roles, resource_permissions, and audit_log. Include row-level security policies and migrations. Design permission evaluation engine as standalone service. Implement Redis caching layer for sub-10ms response times.

**Phase 2 - Admin Console Interface**
Build React + TypeScript admin console using shadcn/ui with:
- Split-panel layout with left navigation
- Role creation wizard and permission assignment grid showing live user counts
- Bulk operations for role assignments
- Permission diff viewer highlighting changes
- Card grid displaying permission heatmaps
- Drag-and-drop permission trees
- Real-time activity feed
- Color-coded risk indicators (red: admin, yellow: write, green: read)
- Dark mode with slate-900 background, zinc-800 cards, emerald-500 active states
- Glassmorphism modals with backdrop blur

**Phase 3 - Security & Audit Infrastructure**
Implement background job processing for audit log anomaly detection. Create dashboard showing 24-hour permission change timeline. Build Slack/email notifications for high-risk actions. Design access review campaign system. Implement permission evaluation order: DENY → resource-level → role-based → time-bound → DEFAULT DENY. Add automated privilege escalation alerts and separation of duties enforcement.

**Phase 4 - Developer Experience**
Create JavaScript/TypeScript SDK with:
- Boolean-returning permission check functions
- React hooks for component-level authorization
- Express middleware for route protection
- TypeScript types and interfaces
- Migration guide from hardcoded checks to RBAC
- Interactive permission playground for testing

**Phase 5 - Testing & Edge Cases**
Test and handle: conflicting roles, circular inheritance prevention, race conditions during permission changes, cache invalidation at scale, graceful degradation when services are unavailable.

**Phase 6 - Monitoring & Observability**
Set up Prometheus metrics tracking check latency, cache hit rate, and denial counts. Create Grafana dashboard visualizing performance trends. Implement error tracking distinguishing bugs from legitimate denials. Generate weekly optimization reports.

**Phase 7 - Rollout Strategy**
Implement feature flag system for gradual enablement. Create shadow mode logging differences between old and new systems. Prepare emergency rollback runbook. Develop training materials for non-technical admins. Plan phased migration with success criteria: 80% developer adoption within 60 days, support for 1M+ users without architectural changes.

**Deliverables Format:**
- Database schema files with migrations and security policies
- TypeScript permission evaluation engine with test suite
- React admin console components (fully responsive)
- RESTful API endpoints with WebSocket support for real-time updates
- Developer SDK with complete documentation
- Audit log viewer with filtering, search, and export
- Performance benchmark results
- Maintainable folder architecture with proper separation of concerns

Include comprehensive code comments explaining security decisions and performance optimizations. Provide visual mockups for admin console screens using descriptive layouts or ASCII art. Export full permission matrix format for auditors.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Runtime_Charter_Design
- 適用 / Use when: The Enterprise RBAC System Design Prompt is a free AI prompt that generates complete, production-ready access …
