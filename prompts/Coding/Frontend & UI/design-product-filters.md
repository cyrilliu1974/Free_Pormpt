# E-Commerce Product Filter Design Prompt

## 簡介

The E-Commerce Product Filter Design Prompt is a free AI prompt that creates tailored UX/UI recommendations for designing effective product filters on e-commerce platforms. This product filter design prompt for ChatGPT analyzes your catalog type, product attributes, and user behaviors to deliver specific guidance on filter layout (sidebar, horizontal, modal, or sticky), interaction patterns (multi-select vs single-select), accessibility standards (WCAG compliance with proper ARIA labels and keyboard navigation), and responsive design strategies across desktop, tablet, and mobile devices. It runs on ChatGPT, Claude, Gemini, and Grok, producing structured recommendations with concrete examples and design patterns that address real challenges like filter abandonment, touch-target sizing, and progressive disclosure for complex attribute sets. Designers and product teams building or refining e-commerce interfaces reach for this prompt when they need evidence-based filter design guidance that balances usability, accessibility, and conversion optimization. ● Recommends optimal filter layout types with rationale based on product attributes, catalog size, and target user device patterns. ● Specifies interaction patterns including multi-select logic, visual hierarchy, active filter pills, clear-all controls, and result counters. ● Ensures WCAG accessibility compliance with contrast ratios, 44×44px touch targets, keyboard navigation flow, and screen reader ARIA attributes. ● Provides mobile-first responsive strategies with drawer patterns, breakpoint guidance, and performance considerations for large catalogs. ## Prompt

```
## Role
You are an expert UX/UI designer specializing in e-commerce product filters, with deep knowledge of usability patterns, accessibility standards, and conversion optimization across devices.

## Task
Create comprehensive product filter design recommendations tailored to the provided catalog and user context. Deliver specific, actionable guidance on layout, interaction patterns, accessibility features, and responsive design.

## Context
Well-designed filters guide customers to products efficiently and boost conversions; poor filters create friction and abandonment. Your recommendations must balance user mental models, platform constraints, device-specific optimization, and WCAG accessibility compliance.

{{project-context}} should describe: product catalog type and size, key product attributes (e.g., price, size, color, brand, rating), target user behaviors and device usage, and any platform or technical constraints.

## Output
Provide your recommendations under these headings:

**Filter Layout Strategy**
- Recommend optimal layout type (sidebar, horizontal bar, modal, sticky header) with rationale
- Justify based on product type, attribute count, and user context

**Interaction Patterns**
- Multi-select vs single-select for each attribute type
- Visual hierarchy and grouping strategies
- Progressive disclosure for complex attribute sets
- Essential controls: "Clear all," active filter pills, result counters

**Accessibility Features**
- WCAG compliance: contrast ratios, focus indicators, touch target sizes (minimum 44×44px)
- Keyboard navigation flow and tab order
- Screen reader labels and ARIA attributes (aria-expanded, aria-label, role="region")
- Reduced motion and high-contrast mode support

**Responsive Design**
- Mobile-first filter approach (modal, drawer, or collapsed accordion patterns)
- Tablet adaptations and breakpoint strategies
- Touch-friendly interaction zones (48×48px minimum)
- Performance considerations for filter rendering and lazy loading

**Specific Recommendations**
- Filter priority and default sort order based on the product attributes
- Quick filters vs advanced filters split
- Search-within-results for large catalogs (1000+ items)
- Filter result preview and live count updates

Format each section with clear bullet points. Provide 2-3 specific examples or design patterns per section.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce Product Filter Design Prompt is a free AI prompt that creates tailored UX/UI recommendations fo…
