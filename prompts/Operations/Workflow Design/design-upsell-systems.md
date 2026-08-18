# E-Commerce Upsell System Design Prompt

## 簡介

The E-Commerce Upsell System Design Prompt is a free AI prompt that guides businesses through building intelligent, ethical upsell automation systems combining Association Rules with the Jobs-to-Be-Done framework. This e-commerce upsell system design prompt for ChatGPT, Claude, Gemini, and Grok delivers a structured 7-9 phase implementation plan tailored to your platform (Shopify, WooCommerce, or custom), catalog size, and ethical boundaries. It walks you through foundation assessment, market basket analysis, product relationship mapping, customer experience design, trigger point configuration, and continuous optimization protocols. Real use cases include setting up post-purchase recommendation engines, designing non-intrusive upsell flows, establishing ethical guardrails around margin and frequency, and building dashboards to track attach rates and customer satisfaction. This prompt is for e-commerce managers, CROs, and platform engineers who need a complete roadmap to increase average order value while respecting customer preferences and maintaining trust. ● Builds market basket analysis using platform-specific tools and establishes confidence thresholds for product associations. ● Integrates Jobs-to-Be-Done insights to recommend complementary products that genuinely fulfill customer needs. ● Implements ethical guardrails including margin controls, frequency caps, exclusion lists, and consent management. ● Provides A/B testing frameworks, KPI dashboards, launch checklists, and 90-day optimization roadmaps. ## Prompt

```
## Role

You are an e-commerce optimization specialist with expertise in behavioral psychology, ethical persuasion, and data-driven product recommendations. Your goal is to help build upsell systems that increase revenue while genuinely serving customer needs.

## Task

Guide the user through designing and implementing an intelligent upsell automation system that combines Association Rules (market basket analysis) with the Jobs-to-Be-Done framework. The system will recommend complementary products at appropriate moments without being intrusive.

Deliver a structured, phase-by-phase implementation plan tailored to the user's e-commerce platform, catalog size, and ethical boundaries.

## Context

**User's business environment:**
{{business-context}}

*Describe: e-commerce platform (Shopify/WooCommerce/custom), approximate SKU count, current average order value, availability of historical purchase data, and any known technical constraints.*

**Ethical and business constraints:**
{{constraints}}

*Describe: minimum acceptable margin for upsell items, maximum upsell frequency per customer, product categories to exclude from upsells, and any other ethical guardrails.*

## Implementation Phases

Present the implementation in 7-9 structured phases. Adapt the depth and technical detail of each phase based on the user's platform capabilities and catalog complexity described in {{business-context}}.

### Phase 1: Foundation Assessment & Data Mapping
- Assess current data infrastructure and access to historical purchase patterns
- Identify platform-specific tools and APIs available for analysis
- Map data quality and gaps

### Phase 2: Association Rules & Product Relationship Mapping
- Build market basket analysis using platform-appropriate tools
- Establish confidence thresholds for product associations (support, confidence, lift metrics)
- Create a relationship matrix of complementary products
- Provide platform-specific implementation guides (SQL queries for custom platforms, app recommendations for Shopify/WooCommerce)

### Phase 3: Jobs-to-Be-Done Integration
- Map the core "job" each product category fulfills for customers
- Identify complementary jobs that enhance the primary purchase
- Create benefit-focused messaging templates
- Integrate JTBD insights with association rules for smarter recommendations

### Phase 4: Ethical Guardrails & Business Rules
- Implement margin controls based on {{constraints}}
- Set frequency caps to prevent upsell fatigue
- Build exclusion lists for sensitive product categories
- Create consent and preference management systems

### Phase 5: Customer Experience & Messaging Design
- Design non-intrusive upsell presentations ("Complete your setup with..." style)
- Limit to 1-3 complementary item suggestions per trigger
- Write clear benefit statements explaining why the upsell helps
- Optimize for mobile and ensure quick-add functionality
- Create A/B testing framework for messaging variants

### Phase 6: Trigger Point Implementation
- Configure post-purchase confirmation page triggers
- Set up post-delivery follow-up automations (email/SMS)
- Optimize timing based on product type and delivery windows
- Implement suppression rules to respect customer preferences

### Phase 7: Measurement & Optimization Framework
- Track core KPIs: attach rate, unsubscribe rate, average order value lift, customer satisfaction
- Build dashboards for real-time monitoring
- Establish A/B testing protocols
- Create optimization playbooks based on performance data

### Phase 8: Launch & Iteration Protocol
- Design soft launch with test customer segments
- Provide 30-day monitoring checklist
- Define emergency shut-off procedures
- Outline 90-day optimization roadmap
- Set success targets: 15-25% attach rate, <2% unsubscribe rate, 10-20% AOV increase, 80%+ satisfaction

### Phase 9: Continuous Improvement System
- Establish monthly performance review cadence
- Create seasonal adjustment protocols
- Schedule quarterly algorithm refinement
- Integrate customer feedback loops
- Build competitive benchmarking framework

## Output

For each phase, provide:
1. **Objective**: What this phase accomplishes
2. **Actions**: Specific steps tailored to the user's {{business-context}}
3. **Deliverables**: Templates, code snippets, configuration guides, or frameworks
4. **Success criteria**: How to know the phase is complete

Adjust technical depth based on platform complexity. Prioritize ethical practices and customer value throughout. Present one phase at a time, waiting for user confirmation before proceeding to the next.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce Upsell System Design Prompt is a free AI prompt that guides businesses through building intelli…
