# Industry-Specific Invoice Generator Builder

## 簡介

The Industry-Specific Invoice Generator Builder is a free AI prompt that produces a full-stack, client-side invoicing system tailored to the billing requirements of construction, legal, consulting, and other industries. This invoice generator prompt for ChatGPT, Claude, and Cursor outputs complete production code, architectural plans, and deployment guidelines for a web application that handles progress billing, retainage tracking, trust accounting, matter-based billing, project milestones, and custom line items - all without backend infrastructure. You specify your industry requirements and customization focus, and the prompt architects a system with Stripe-level design quality, professional PDF generation, multi-jurisdiction tax compliance, and local-storage data management. Reach for this prompt when you need to build or prototype an invoicing tool that respects the unique billing structures of a specific vertical while maintaining enterprise-grade polish and accessibility. ● Outputs complete folder structure, tech stack configuration, and dependency management for immediate project setup. ● Generates configurable invoice templates for construction, legal, consulting, and other verticals with specialized fields and calculations. ● Includes a smart form builder with real-time validation, auto-calculations, conditional fields, and dynamic line items. ● Produces a tax calculation engine that handles multi-jurisdiction rules and compliance requirements client-side. ## Prompt

```
## Role
You are an expert full-stack developer and enterprise software architect.

## Context
Business invoicing requirements vary by industry. Construction needs progress billing and retainage tracking; legal firms need trust accounting and matter-based billing; consultants need project milestones and custom line items. The system must maintain professional design while accommodating these complex requirements without backend infrastructure.

## Task
Architect and implement a production-ready, client-side invoicing web application that adapts to multiple business verticals with Stripe-level design quality.

**Industry requirements:**
{{industry-requirements}}

**Key customization needs:**
{{customization-focus}}

## Output
Provide a comprehensive, production-ready codebase and implementation plan covering:

- **Project architecture and setup**: Tech stack, folder structure, dependency management
- **Industry template system**: Configurable templates for each vertical with specialized fields and calculations
- **Smart form builder**: Dynamic generation with real-time validation, auto-calculations, conditional fields
- **Professional PDF generation**: High-quality output with industry-specific formatting and branding
- **Data management**: Local storage architecture, client database, invoice history, search
- **Tax calculation engine**: Multi-jurisdiction tax handling with compliance features
- **Production polish**: Performance optimization, WCAG accessibility, responsive design, error handling

Include complete code, architectural decisions, best practices, and deployment guidelines. Use bullet points for readability.
```

## 用法 / Usage
- 必填變數 / Variables: {{customization-focus}}、{{industry-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Adaptive_Checkpoint_System
- 適用 / Use when: The Industry-Specific Invoice Generator Builder is a free AI prompt that produces a full-stack, client-side in…
