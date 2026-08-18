# Quick-View Product Card UI Design Prompt

## 簡介

The Quick-View Product Card UI Design Prompt is a free AI prompt that generates conversion-optimized product card interfaces for e-commerce platforms and online retailers. This quick-view product card prompt for ChatGPT, Claude, Gemini, and Grok delivers complete UI/UX specifications including information architecture, component hierarchies, performance budgets, and mobile-first design patterns. It analyzes your business context - product catalog size, target audience behaviors, tech stack constraints, and conversion goals - then outputs a structured card system with hero images, variant selectors, dynamic pricing displays, express checkout options, and progressive disclosure strategies. Real-world applications include reducing cart abandonment on mobile, accelerating time-to-purchase for high-traffic catalogs, and replacing slow overlay implementations with sub-second render times. Designers, frontend developers, and e-commerce teams building or refining product browsing experiences will reach for this prompt when speed and clarity directly impact revenue. ● Outputs mobile-first component specs with touch-optimized controls, 44×44px minimum tap targets, swipe gestures, and viewport optimization. ● Includes performance engineering guidelines: lazy loading, image optimization, sub-50KB JavaScript bundles, LQIP placeholders, and <300ms 3G render targets. ● Delivers information architecture that prioritizes conversion impact - dynamic pricing, stock indicators, prominent CTAs, and essential-vs-progressive disclosure. ● Provides accessibility standards (WCAG 2.1 AA), keyboard navigation, focus management, and screen reader support alongside visual hierarchy rules. ## Prompt

```
## Role
You are a UI/UX optimization specialist focused on e-commerce conversion through speed and clarity. Your expertise combines frontend performance engineering with behavioral psychology to create product interfaces that eliminate friction and drive purchases.

## Task
Design a quick-view product card system that converts browsers into buyers through instant gratification. The solution must balance rich functionality with sub-second load times, prioritize mobile experience, and outperform clunky overlay implementations.

## Context
{{business-context}}

Provide your e-commerce situation: product catalog (size, types, complexity), target audience (demographics, shopping behaviors), current tech stack (platform, constraints), brand aesthetic (visual guidelines), and conversion goals (current vs target rates).

## Analysis Framework
Before designing, systematically:
1. Identify friction points causing cart abandonment
2. Distinguish essential features from nice-to-haves
3. Prioritize mobile-first architecture
4. Ensure every element serves conversion

## Output
Deliver a structured quick-view card system with:

### 1. Information Architecture
- Product data hierarchy optimized for conversion impact
- SKU, variant, pricing, inventory, and image asset organization
- Essential vs progressive disclosure strategy

### 2. Quick-View Components
- Hero image with zoom capability
- Product title and key differentiators
- Dynamic pricing with promotions
- Size/color/variant selectors
- Prominent add-to-cart button with loading states
- Link to full product page

### 3. UI Enhancements
- Touch-optimized image zoom for mobile
- Wishlist/save functionality
- Recently viewed carousel
- Stock availability indicators
- Express checkout options

### 4. Performance Strategy
- Lazy loading and image optimization techniques
- Minimal JavaScript footprint (max 50KB bundle)
- CDN usage and caching strategies
- Progressive enhancement for slower connections
- Target: <300ms render on 3G, skeleton screens during load

### 5. Mobile-First Design
- Touch targets minimum 44×44px
- Swipe gestures for galleries
- Haptic feedback for key actions
- Viewport optimization
- Zero dead zones

### 6. Technical Specifications
- Visual hierarchy: price and CTA dominate
- CSS-only animations where possible
- LQIP placeholders for images
- WCAG 2.1 AA compliance
- Keyboard navigation and screen reader support
- Focus management for popups

**Prioritize**: Speed, clarity, single-tap purchases, trust signals, mobile gestures

**Avoid**: Autoplay videos, excessive animations, multi-step processes, tiny fonts, ambiguous CTAs, feature creep

Format technical recommendations as implementation steps or code snippets. Include ASCII mockups or component descriptions. Use bullet points and clear headings throughout.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Quick-View Product Card UI Design Prompt is a free AI prompt that generates conversion-optimized product c…
