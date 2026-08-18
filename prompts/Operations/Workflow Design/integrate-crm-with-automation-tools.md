# CRM Marketing Automation Integration Guide Builder

## 簡介

The CRM Marketing Automation Integration Guide Builder is a free AI prompt that creates comprehensive technical integration guides for businesses connecting their CRM software with marketing automation platforms. This CRM integration prompt for ChatGPT walks you through building a complete implementation roadmap, from pre-integration planning and field mapping to lead scoring workflows, campaign trigger setup, and reporting dashboards. It structures the guide across five phases - pre-integration planning, integration architecture, lead management workflow, campaign orchestration, and reporting optimization - with each section delivering step-by-step instructions, technical specifications, common pitfalls, and best practices. You specify your CRM platform (Salesforce, HubSpot, Pipedrive, etc.), marketing automation tool (Marketo, ActiveCampaign, Pardot, etc.), and business context, and the prompt returns a customized guide covering connection methods, data sync frequency, lead routing logic, behavioral triggers, and attribution models. It runs on ChatGPT, Claude, Gemini, and Grok. This prompt is designed for systems integrators, marketing operations teams, RevOps managers, and IT consultants responsible for connecting disparate platforms and automating lead nurturing workflows. ● Produces field mapping requirements, data flow diagrams, and sync frequency recommendations for two-way CRM-marketing automation data exchange ● Defines lead scoring models, qualification criteria, routing rules, and nurture track triggers aligned to your sales funnel ● Maps behavioral triggers (form submissions, email clicks, page visits) to multi-channel campaign touchpoints and personalization tokens ● Includes error handling procedures, unified dashboard configuration, attribution model selection, and data hygiene audit schedules ## Prompt

```
## Role
You are an expert systems integrator specializing in CRM and marketing automation platforms.

## Task
Create a comprehensive integration guide that connects CRM software with marketing automation tools to improve lead nurturing and customer engagement. Structure the guide so each step logically builds upon the previous one, using clear dependencies between implementation phases.

## Context
Integration details:
- CRM platform: {{crm-platform}}
- Marketing automation tool: {{marketing-automation-tool}}
- Business context: {{business-context}}

The guide should address the technical integration workflow, data synchronization requirements, lead scoring and routing logic, campaign trigger setup, and ongoing optimization practices.

## Output
Deliver a structured implementation guide with:

### Pre-Integration Planning
- Current state assessment and data audit
- Field mapping requirements between systems
- User permissions and access controls
- Success metrics and KPIs

### Integration Architecture
- Connection method (native, API, middleware)
- Data flow direction and sync frequency
- Error handling and failover procedures

### Lead Management Workflow
- Lead capture and qualification criteria
- Scoring model and threshold definitions
- Automated routing rules and assignment logic
- Nurture track triggers and progression paths

### Campaign Orchestration
- Behavioral trigger setup (page visits, email engagement, form submissions)
- Multi-channel touchpoint coordination
- Personalization token mapping
- A/B testing framework

### Reporting and Optimization
- Unified dashboard configuration
- Attribution model selection
- Regular audit schedule and data hygiene practices
- Iterative improvement process

For each section, include:
- Step-by-step instructions with technical specifics
- Key benefits and ROI impact
- Common pitfalls and how to avoid them
- Best practices from successful implementations

Format with clear headings, subheadings, and bullet points for immediate implementation.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{crm-platform}}、{{marketing-automation-tool}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The CRM Marketing Automation Integration Guide Builder is a free AI prompt that creates comprehensive technica…
