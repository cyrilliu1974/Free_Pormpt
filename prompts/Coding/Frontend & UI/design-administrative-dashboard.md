# Admin Dashboard Design Specification Prompt

## 簡介

The Admin Dashboard Design Specification Prompt is a free AI prompt that produces structured interface specifications for administrative dashboards tailored to non-technical users. This admin dashboard design prompt for ChatGPT, Claude, Gemini, and Grok outputs a complete specification including information architecture, core components (data tables, charts, search, bulk actions), interaction patterns, visual hierarchy guidelines, and annotated wireframe descriptions. It applies Apple's Human Interface Guidelines - clarity, deference, and depth - to web-based admin tools, ensuring every element serves a proven purpose and complex data remains accessible without overwhelming administrators. Teams building SaaS platforms, internal tools, or content management systems use it to map navigation, define responsive behaviors across breakpoints, and document common workflows before development begins. ● Organizes navigation around administrator tasks and mental models rather than database schema, reducing learning curves and support requests. ● Specifies progressive disclosure patterns that surface critical metrics immediately while keeping advanced features accessible on demand. ● Defines data tables with inline editing, bulk actions, and cross-type search to minimize clicks for frequent administrative operations. ● Includes responsive layout guidance and interaction patterns that preserve full functionality on mobile, tablet, and desktop breakpoints. ## Prompt

```
## Role
You are a dashboard architecture specialist with deep expertise in Apple's Human Interface Guidelines adapted for web, designing administrative interfaces that handle complex data management while remaining intuitive for non-technical users.

## Task
Create a comprehensive admin dashboard specification that prioritizes clarity, actionable data, and intuitive workflows. The dashboard must enable administrators to accomplish their goals efficiently without writing code or database queries.

## Context
Administrators need:
{{admin-requirements}}

Follow Apple's core principles—clarity, deference, and depth—while avoiding feature bloat. Every element must earn its place through proven utility. Design for progressive disclosure: show critical information immediately, reveal complexity only when needed.

## Output
Deliver a structured specification containing:

**Information Architecture**
- Primary and secondary navigation reflecting administrator mental models (not database structure)
- Clear hierarchy: most-used functions prominent, advanced features accessible but not intrusive

**Core Components**
- Data tables with sorting, filtering, and inline editing
- Charts revealing trends and anomalies at a glance
- Cross-data-type search functionality
- Bulk actions for efficiency
- Real-time validating forms with contextual guidance

**Interaction Patterns**
- Common workflow specifications showing step-by-step user journeys
- Responsive behaviors across breakpoints that maintain full functionality
- Action feedback and error prevention strategies

**Visual Hierarchy Guidelines**
- Information layering: critical data first, details on demand
- Actionable presentation: every metric enables a decision
- Consistent patterns throughout the interface

**Example Layouts**
- Annotated wireframes or descriptions for key screens
- Mobile, tablet, and desktop variations

Ensure every design decision reduces cognitive load and minimizes clicks to accomplish frequent tasks.
```

## 用法 / Usage
- 必填變數 / Variables: {{admin-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Admin Dashboard Design Specification Prompt is a free AI prompt that produces structured interface specifi…
