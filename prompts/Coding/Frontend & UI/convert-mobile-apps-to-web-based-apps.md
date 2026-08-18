# Convert Mobile Apps to Web-Based Apps

## 簡介

The Convert Mobile Apps to Web-Based Apps prompt is a free AI prompt that creates detailed technical conversion plans for developers migrating mobile applications to web platforms. This mobile-to-web conversion prompt for ChatGPT, Claude, Gemini, and Grok analyzes your mobile app's architecture, maps touch gestures to cursor interactions, designs responsive breakpoints (320-768px mobile preservation, 768-1024px tablet sidebars, 1024px+ desktop multi-column layouts), and generates a React 18+ component library with TypeScript and Tailwind CSS. The prompt addresses the fundamental challenges most conversions face: preserving the mobile app's identity while adapting to desktop interaction patterns, adding keyboard navigation, implementing Progressive Web App offline functionality, and ensuring WCAG 2.1 AA accessibility compliance. It outputs a structured plan covering mobile analysis, responsive strategy, component architecture, desktop enhancements, PWA implementation with service workers, performance optimization through code splitting and lazy loading, and cross-device testing workflows. This prompt is for full-stack developers, frontend engineers, and product teams translating existing mobile apps into web applications that work across desktop, tablet, and mobile browsers. ● Analyzes mobile design systems, component hierarchies, gesture interactions, and navigation patterns to preserve app identity ● Maps swipe, tap, long-press, and pinch gestures to mouse, keyboard, and cursor equivalents with desktop power-user shortcuts ● Designs mobile-first CSS with progressive enhancement across three breakpoint tiers and generates React component architecture ● Implements Progressive Web App capabilities including service workers, offline functionality, install prompts, and push notifications ## Prompt

```
## Role

You are a senior full-stack developer specializing in mobile-to-web application conversions with deep expertise in progressive web apps, responsive design systems, and cross-platform UI translation.

## Task

Create a comprehensive conversion plan that transforms the mobile application into a pixel-perfect web version. Address mobile-to-web-specific challenges: touch-to-cursor interaction mapping, responsive breakpoint strategy (mobile 320-768px preserves original layout; tablet 768-1024px introduces sidebars; desktop 1024px+ uses multi-column layouts with persistent navigation), Progressive Web App implementation with offline capability, and WCAG 2.1 AA accessibility compliance.

## Context

Most mobile-to-web conversions fail because developers simply shrink mobile interfaces or ignore fundamental interaction differences between touch and cursor. This conversion must intelligently adapt the experience for desktop while preserving what makes the mobile app successful.

{{app-details}}

## Requirements

- Match exact visual specifications (colors, fonts, spacing, animation timings) from the mobile app
- Map touch gestures to appropriate mouse/keyboard equivalents and add desktop power-user features
- Build using React 18+, TypeScript, Tailwind CSS, Framer Motion
- Implement mobile-first CSS with progressive enhancement
- Ensure sub-100ms interactions, keyboard navigation, and cross-browser compatibility
- Include code splitting, lazy loading, and performance optimization strategies
- Focus on mobile-to-web translation challenges, not generic responsive design advice

## Output

Structure your conversion plan with these sections:

**Mobile Analysis**: Comprehensive breakdown of the app's design system, component hierarchy, navigation patterns, gesture-based interactions, and architecture

**Responsive Strategy**: Detailed breakpoint planning and gesture-to-web interaction mapping with specific examples

**Component Library**: React component structure matching mobile UI with desktop adaptations

**Desktop Enhancements**: Power-user features and desktop-specific improvements that leverage larger screens and cursor precision

**PWA Implementation**: Progressive Web App setup including service workers, offline functionality, and install prompts

**Performance Optimization**: Specific strategies for code splitting, lazy loading, and cross-device performance

**Testing & Deployment**: Cross-device testing approach and deployment workflow with rollback considerations
```

## 用法 / Usage
- 必填變數 / Variables: {{app-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Convert Mobile Apps to Web-Based Apps prompt is a free AI prompt that creates detailed technical conversio…
