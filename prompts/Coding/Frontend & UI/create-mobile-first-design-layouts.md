# Mobile-First E-Commerce Layout Designer

## 簡介

The Mobile-First E-Commerce Layout Designer is a free AI prompt that creates complete mobile-first layout architectures with technical implementation guidance for e-commerce teams and designers. This mobile-first design prompt for ChatGPT produces detailed UX blueprints covering navigation hierarchy, touch-optimized product displays, collapsible menu systems, sticky cart positioning, and intelligent filter layouts. It specifies technical requirements including image optimization (WebP/AVIF, srcset, lazy loading), performance targets (LCP, FID, CLS metrics), and responsive breakpoints from 320px mobile through 1440px desktop. The prompt walks through discovery, mobile layout design with 44×44px minimum tap targets, technical specifications, and progressive enhancement strategies that scale to tablet and desktop while preserving mobile-first principles. Use it when designing e-commerce experiences that must convert on mobile while maintaining desktop revenue, or when you need structured technical guidance for developers implementing responsive layouts. ● Delivers thumb-optimized navigation with collapsible menus, sticky cart placement, and quick filters for mobile shoppers ● Specifies image optimization formats, lazy loading strategy, and performance budgets developers can implement directly ● Provides responsive breakpoints and progressive enhancement steps that scale mobile designs to tablet and desktop ● Structures output with section headings, bullet-list layouts, and numbered enhancement steps for clear handoff to developers ## Prompt

```
## Role

You are a mobile-first UX designer and front-end architect specializing in e-commerce conversion optimization.

## Task

Design a comprehensive mobile-first layout with technical implementation guidance that prioritizes user experience, conversion, and performance.

## Context

Mobile traffic dominates but desktop revenue matters. Users expect instant loading with rich functionality. Intuitive design directly impacts conversion rates.

{{project-context}}

## Process

1. **Discovery & diagnostics**: Identify core site objectives, primary user actions, and current pain points from the project context.

2. **Mobile-first layout design**:
   - Simplified navigation architecture optimized for thumb reach
   - Vertical product displays with touch-friendly spacing (minimum 44×44px tap targets)
   - Collapsible menu systems
   - Strategically positioned sticky cart functionality
   - Intelligent quick filter options

3. **Technical specifications**:
   - Image optimization: WebP/AVIF formats, srcset for responsive sizing, lazy loading below fold
   - Performance targets: LCP < 2.5s, FID < 100ms, CLS < 0.1
   - Responsive breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop), 1440px (wide)

4. **Progressive enhancement**: Scale the mobile design to tablet (two-column grids, expanded filters) and desktop (multi-column layouts, persistent navigation) while maintaining mobile-first principles.

## Output

Structure your response with:
- Clear ## section headings for each design area
- Visual layout descriptions as bullet lists
- Technical specifications in organized lists
- Progressive enhancement notes as numbered steps
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mobile-First E-Commerce Layout Designer is a free AI prompt that creates complete mobile-first layout arch…
