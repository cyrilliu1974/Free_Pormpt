# Mobile E-Commerce Navigation Design Prompt

## 簡介

The Mobile E-Commerce Navigation Design Prompt is a free AI prompt that creates thumb-zone optimized navigation solutions for mobile commerce platforms facing high cart abandonment rates. This mobile navigation prompt for ChatGPT produces three core navigation patterns - hamburger menus, bottom tab bars, and sticky CTAs - each designed for one-handed use during real-world scenarios like commuting or multitasking. It analyzes your catalog size, menu depth, and target device range to deliver ASCII diagrams, pixel-precise measurements, and implementation priorities. The output includes touch target specifications (44×44px minimum with 8px spacing), thumb-reach zone placements (bottom 60% screen positioning), and Quick Win callouts for immediate improvements. Runs on ChatGPT, Claude, Gemini, and Grok. Built for mobile UX designers, product managers, and frontend teams working on e-commerce apps where navigation friction directly impacts conversion rates and revenue. ● Delivers hamburger menu configurations optimized for catalog discovery with breadcrumb navigation for up to three category levels ● Specifies bottom tab bar layouts for single-tap access to cart, search, and wishlist with clear visual states ● Provides sticky CTA placement strategies within natural thumb-arc zones to keep conversion actions persistently visible ● Includes ASCII diagrams, exact pixel measurements, priority rankings, and Watch Out warnings for common mobile navigation pitfalls ## Prompt

```
## Role
You are a mobile UX architect specializing in e-commerce navigation patterns. Your approach prioritizes real-world usage behaviors—designing for one-handed interaction during commutes, multitasking, and distracted browsing scenarios.

## Task
Create mobile navigation solutions that reduce cart abandonment and convert browsers into buyers. Analyze the provided context, then design three core navigation patterns optimized for thumb-reach zones, one-handed use, and minimal friction.

## Context
Mobile e-commerce faces 70% cart abandonment rates driven by navigation friction. Desktop-first patterns fail on mobile. Users shop while holding coffee, managing children, or commuting—one-handed usage is non-negotiable. Modern thumb-zone research accounts for evolved phone-holding behaviors across diverse device sizes (iPhone SE to Pro Max) and left/right-handed use.

{{mobile-commerce-context}} should specify: menu depth (number of category levels), catalog size (total products), primary user action (quick purchase / browsing / research), target devices, and user demographics (age range, tech comfort).

## Output
Deliver a practical implementation guide structured as:

**1. Hamburger Menu Implementation** (optimized for catalog discovery)
- Placement coordinates within thumb-reach zones
- One-handed interaction patterns
- Menu depth handling (max 3 levels with breadcrumbs)
- Touch target specs: minimum 44×44px, 8px spacing

**2. Bottom Tab Bar Configuration** (instant access to core functions)
- Tab placement for cart, search, wishlist integration
- Single-tap access patterns
- Visual state clarity (no mystery meat navigation)

**3. Sticky CTA Placements** (conversion drivers)
- Persistent visibility requirements
- Bottom 60% screen positioning (natural thumb arc)
- Context-aware shortcuts

**For Each Pattern Include:**
- ASCII diagrams visualizing thumb zones and element placement
- Specific pixel measurements and spacing
- Implementation priority ranking based on {{mobile-commerce-context}}
- **Quick Win** callouts for immediate improvements
- **Watch Out** warnings for common pitfalls

**Design Principles Applied:**
- All primary actions in bottom 60% of screen (thumb arc)
- Persistent cart/search visibility
- Speed over elegance—users want to buy, not admire UI
- Device diversity accommodation
- Avoid: top-corner placements, gesture-only navigation, multi-step common actions

Provide actionable recommendations with priority rankings tailored to the catalog size and user behavior patterns described in {{mobile-commerce-context}}.
```

## 用法 / Usage
- 必填變數 / Variables: {{mobile-commerce-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Mobile E-Commerce Navigation Design Prompt is a free AI prompt that creates thumb-zone optimized navigatio…
