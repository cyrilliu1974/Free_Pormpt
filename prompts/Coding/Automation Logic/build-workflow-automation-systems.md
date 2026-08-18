# Workflow Automation System Builder

## 簡介

The Workflow Automation System Builder is a free AI prompt that generates complete, production-grade automation systems tailored to specific business workflows and integration requirements. This workflow automation prompt for ChatGPT, Claude, and Cursor produces full-stack code including a React/TypeScript drag-and-drop builder interface, Node.js backend with retry logic and rate limiting, real-time execution dashboards, and scheduling systems that handle edge cases, malformed data, and API failures gracefully. Engineers and technical leaders reach for this prompt when they need to build custom automation tools that go beyond off-the-shelf solutions - transforming manual processes into resilient, monitored systems that scale with business needs. ● Maps complete data flows, trigger conditions, API integrations, and failure scenarios before generating architecture and code ● Produces a React/TypeScript frontend with a node-based workflow builder, live execution dashboard, and mobile-responsive UI following modern design standards ● Builds a Node.js backend engine with retry logic, rate limiting, graceful degradation, and logging systems designed for production reliability ● Includes setup instructions, pre-configured example workflows, and testing protocols to verify resilience under real-world conditions ## Prompt

```
## Role

You are an automation architect and full-stack engineer specializing in production-grade workflow systems. You design for reliability under real-world conditions: edge cases, rate limits, malformed data, and scale. Your systems handle failure gracefully and operate idempotently.

## Task

Build a fully functional, production-ready automation tool for the workflow described below. The system must handle end-to-end automation including trigger detection, data processing, actions, error recovery, and comprehensive logging.

## Context

{{automation-requirements}}

Provide:
- The specific process to automate
- Data flow (sources, formats, transformations)
- Triggers that initiate execution
- Final outputs or actions required
- APIs, services, and systems to integrate

## Technical Requirements

**Stack:**
- Frontend: React + TypeScript + Tailwind CSS + shadcn/ui
- Backend: Node.js with proper API architecture
- TypeScript throughout for type safety

**Core Features:**
- Drag-and-drop workflow builder with node-based interface
- Real-time execution dashboard with live status
- Settings panel for configuration management
- Scheduling, webhook endpoints, and notification systems
- Production-grade error handling: retry logic, rate limiting, graceful degradation
- Comprehensive logging, monitoring, and alerting
- Idempotent workflow design
- Mobile-responsive UI with Linear.app-inspired aesthetics (dark mode, smart spacing)

**Quality Bar:**
- Test with 100+ executions to verify resilience
- Handle rate limits, timeouts, and malformed data gracefully
- Zero-error local execution
- Immediately production-ready

## Output

Deliver in this structure:

### 1. Workflow Analysis
Complete mapping of automation requirements, triggers, data flow, and potential failure points.

### 2. Architecture Design
Technical architecture including API integrations, data transformations, state management, and system components.

### 3. Core Engine Implementation
Backend automation executor with event handling, retry logic, rate limiting, and error recovery. Build the bulletproof engine first.

### 4. Frontend Interface
React dashboard with workflow builder, execution monitoring, and settings management. Include component hierarchy and state flow.

### 5. Monitoring & Operations
Scheduling system, webhook endpoints, alerting mechanisms, and performance analytics.

### 6. Source Code Delivery
Complete file structure with:
- Organized, documented source code
- Setup instructions (dependencies, environment, configuration)
- Pre-configured example workflows
- Inline documentation for key functions

### 7. Testing & Validation
Testing protocols executed and production readiness verification results.
```

## 用法 / Usage
- 必填變數 / Variables: {{automation-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Workflow Automation System Builder is a free AI prompt that generates complete, production-grade automatio…
