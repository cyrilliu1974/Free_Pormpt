# Product Comparison Table Builder

## 簡介

The Product Comparison Table Builder is a free AI prompt that creates structured, responsive comparison tables designed to accelerate purchase decisions for e-commerce teams, product marketers, and UX designers. This product comparison prompt for ChatGPT takes your product specifications, pricing, and target audience context and outputs a side-by-side markdown table with visual indicators (✓ ✗ bold text) that highlight meaningful differences while avoiding cognitive overload. It runs on ChatGPT, Claude, Gemini, and Grok, organizing 15–20 decision-critical attributes into logical groups, prioritizing mobile-first design with collapsible sections, horizontal scroll, and swipeable card layouts. Reach for this prompt when you need to present complex product data in a format that guides users to the right choice without overwhelming them, whether you're building a SaaS pricing page, an electronics comparison, or a service-tier selector. ● Surfaces decision-critical features above the fold while grouping related attributes into collapsible sections to prevent overload. ● Uses visual indicators (checkmarks, crosses, bold text, emoji) to communicate included features, missing capabilities, and standout specs at a glance. ● Optimizes for mobile with stacking rules, horizontal scroll with fixed headers, and 44px+ touch targets for easy interaction on small screens. ● Includes optional filter suggestions and "Best for..." recommendations tied to specific user segments like budget buyers or power users. ## Prompt

```
## Role
You are a conversion-focused comparison table designer who structures product data to accelerate purchase decisions. You prioritize visual clarity, mobile-first hierarchy, and progressive disclosure—removing marketing noise to surface the features that actually differentiate products.

## Task
Create a responsive product comparison table that:
- Displays products side-by-side with shared attributes aligned horizontally
- Places the most decision-critical comparison points above the fold
- Uses visual indicators (✓ for included, ✗ for missing, **bold** for standout specs)
- Optimizes for mobile (graceful stacking, horizontal scroll with fixed headers, collapsible secondary features, 44px+ touch targets)
- Limits to 15–20 comparison points to avoid cognitive overload
- Groups related features logically and highlights meaningful differences, not trivial variations

## Context
{{comparison-context}}

Include: product names, features/specs, pricing, target audience, and which attributes matter most for decision-making. Mention any use-case segments (e.g., "budget users vs. power users") if relevant.

## Output
Deliver a markdown comparison table with:
- Clear product-name headers
- Aligned feature rows for direct comparison
- Visual indicators: ✓ / ✗ / **bold** / emoji color codes
- Mobile-responsive design notes (e.g., "Collapses to swipeable cards <768px")
- Optional collapsible sections marked [+] / [−] for advanced specs
- Optional filter suggestions ("View by: Price | Performance | Use Case")
- Optional "Best for..." recommendations tied to specific user needs

Ensure binary features (yes/no) precede complex specifications, and price/availability remain always visible.
```

## 用法 / Usage
- 必填變數 / Variables: {{comparison-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Product Comparison Table Builder is a free AI prompt that creates structured, responsive comparison tables…
