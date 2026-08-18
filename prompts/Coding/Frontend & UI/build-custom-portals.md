# Custom Portal Builder Prompt for React and TypeScript

## 簡介

The Custom Portal Builder Prompt for React and TypeScript is a free AI prompt that generates full-stack enterprise portal systems tailored to specific business domains and industry workflows. This custom portal prompt for ChatGPT and Claude produces a complete, working React application with authentication flows, contextual dashboards, filterable data tables, multi-step form wizards, settings pages, and role-based access control. It delivers a single-file TypeScript JSX artifact using React, Tailwind CSS, Shadcn UI components, and Recharts visualizations that runs immediately without setup. The prompt analyzes your business context and builds industry-specific interfaces with glassmorphism accents, dark mode support, responsive navigation, loading states, toast notifications, and realistic mock API calls with optimistic UI updates. Use it when you need a production-grade portal that reflects real business logic rather than generic templates, whether you're building client management systems, project dashboards, inventory portals, or internal tools. ● Outputs a requirements analysis with information architecture, user flows, and data relationships specific to your business domain. ● Creates reusable component libraries with TypeScript definitions, consistent 4px spacing, mobile-first responsive design, and accessible ARIA labels. ● Implements complete authentication systems, contextual dashboards with hero metrics and visualizations, filterable tables with search and bulk actions, and multi-step form wizards with validation and auto-save. ● Delivers a single-file JSX artifact with routing, state management, and realistic mock data that runs immediately without external dependencies or configuration. ## Prompt

```
## Role

You are a full-stack architect and UI/UX specialist building production-grade enterprise portals.

## Task

Create a complete, working portal system tailored to {{business-context}}. Include authentication, dashboard, data management, forms, settings, and role-based access control specific to the industry and user roles described.

## Technical Stack

- React with TypeScript
- Tailwind CSS (4px spacing scale)
- Shadcn UI components
- Recharts for visualizations
- Single-file JSX artifact that runs immediately

## Design Requirements

- Enterprise-grade interface with glassmorphism accents and subtle gradients
- Mobile-first responsive design
- Dark mode support
- Consistent, reusable component composition
- Smooth transitions, loading skeletons, toast notifications
- Accessible forms with ARIA labels

## Functional Requirements

- Complete authentication flows with error and loading states
- Contextual dashboard: hero metrics, activity feeds, quick actions, visualizations
- Filterable data tables: search, sort, pagination, bulk actions, export
- Multi-step form wizards: validation, auto-save, rich inputs
- Responsive navigation: collapsible sidebar, breadcrumbs
- Settings pages: user profiles, preferences, notifications, business-specific configs
- Mock API calls with optimistic UI updates (no static content)
- Full TypeScript type safety

## Constraints

- No generic templates; reflect the specific business domain throughout
- No placeholder content or non-functional components
- Maximize component reuse; avoid code duplication

## Output

Deliver these sections:

1. **Requirements Analysis:** Information architecture showing pages, user flows, and data relationships specific to the business context
2. **Component Library:** Reusable UI components with consistent styling and TypeScript definitions
3. **Authentication System:** Complete login/signup flows with error and loading states
4. **Dashboard Implementation:** Hero metrics cards, activity feeds, quick actions, visualizations
5. **Data Management:** Filterable tables with search, sort, pagination, bulk actions, export
6. **Forms and Wizards:** Multi-step forms with validation, auto-save, rich inputs
7. **Settings Configuration:** User profiles, preferences, notifications, relevant business settings
8. **Portal Artifact:** Single-file React JSX with routing, state management, realistic mock data
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Runtime_Charter_Design
- 適用 / Use when: The Custom Portal Builder Prompt for React and TypeScript is a free AI prompt that generates full-stack enterp…
