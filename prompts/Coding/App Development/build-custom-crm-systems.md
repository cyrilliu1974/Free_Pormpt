# Build Custom CRM Systems

## 簡介

The Build Custom CRM Systems prompt is a free AI prompt that generates a complete, production-ready React CRM application tailored to specific business workflows and industry requirements. This custom CRM system prompt for ChatGPT delivers a full TypeScript codebase built on React, Tailwind CSS, and shadcn/ui, complete with contact databases, drag-and-drop pipeline management, activity tracking, reporting dashboards, and mobile-responsive design. It runs on ChatGPT, Claude, and Cursor, gathering your business context first, then designing a custom data schema, and finally outputting the complete implementation with sample data and deployment guides. Reach for this prompt when you need to replace spreadsheets and fragmented tools with a unified customer management system that matches your exact processes, or when off-the-shelf CRM platforms feel too generic or expensive for your team. ● Outputs a complete React + TypeScript CRM codebase with contact management, pipeline stages, activity timelines, metrics dashboards, and CSV export functionality. ● Includes advanced filtering, bulk actions, keyboard shortcuts, drag-and-drop pipeline management, and WCAG accessibility standards. ● Generates a custom data schema based on your business context, with realistic sample data to demonstrate system capabilities immediately. ● Delivers mobile-responsive design inspired by Notion and Linear.app, with optimistic UI updates and production-ready localStorage patterns. ## Prompt

```
## Role

You are a senior full-stack developer and CRM architect specializing in React-based customer management systems. You combine enterprise-grade functionality with consumer-app simplicity, creating intuitive data-rich interfaces that teams actually adopt.

## Task

Build a complete, production-ready CRM application tailored to the user's specific workflow needs.

First gather detailed requirements, then design the data schema, then build the full implementation.

## Context

{{business-context}}

## Technical Specifications

**Stack & Architecture:**
- React + TypeScript with strict typing
- Tailwind CSS + shadcn/ui components
- Browser localStorage with production-ready patterns
- Lucide icons throughout
- React Query for state management

**Design Standards:**
- Clean interfaces inspired by Notion and Linear.app
- Generous white space and subtle shadows
- Mobile-responsive across all devices
- WCAG accessibility (ARIA labels, keyboard navigation)
- Components under 200 lines

**Core Features:**
- Metrics dashboard with visualizations
- Contact database with advanced filtering
- Drag-and-drop pipeline management
- Activity tracking and timeline
- Reporting charts
- Bulk actions and CSV export
- Keyboard shortcuts for power users
- Comprehensive validation and error handling
- Optimistic UI updates

**Data Handling:**
- Support real-world data volumes
- Include realistic sample data
- Ensure data relationships and integrity

## Output Structure

Deliver in this sequence:

1. **Requirements Analysis** — Detailed breakdown of business needs, custom field requirements, and industry-specific pain points
2. **Data Schema** — Complete structure for contacts, deals, stages, activities, and relationships
3. **Core Application** — Full React implementation with dashboard, contacts view, pipeline, and reporting modules
4. **Advanced Features** — Bulk operations, search, filtering, and workflow automation
5. **Mobile Optimization** — Responsive design ensuring full functionality on all devices
6. **Sample Data** — Realistic test dataset demonstrating system capabilities
7. **Implementation Guide** — Step-by-step customization and deployment instructions

Focus on creating a customized solution that addresses specific workflow needs rather than generic CRM functionality.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Custom CRM Systems prompt is a free AI prompt that generates a complete, production-ready React CRM …
