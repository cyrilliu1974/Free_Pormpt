# Responsive Navigation Menu Builder

## 簡介

The Responsive Navigation Menu Builder is a free AI prompt that generates complete, accessible navigation systems for web developers and UX designers. This responsive navigation menu prompt for ChatGPT produces semantic HTML markup, mobile-first CSS with breakpoints, minimal JavaScript for toggle behavior, and WCAG-compliant accessibility features. It analyzes your site structure through the {{site-context}} variable and delivers a hamburger menu for mobile (below 768px) that expands into horizontal or dropdown menus for desktop. The prompt runs on ChatGPT, Claude, and Cursor, outputting code that respects cognitive psychology principles and industry conventions - ensuring users find what they need without confusion. Real use cases include SaaS product sites, portfolio pages, e-commerce storefronts, and content-heavy blogs where predictable navigation reduces bounce rates. Reach for this prompt when you need a navigation system that feels invisible yet effective, balancing familiarity with modern responsive design requirements. ● Outputs semantic HTML with proper ARIA landmarks, roles, and labels for screen readers and keyboard navigation. ● Includes mobile-first CSS with smooth transitions, hover states, focus indicators, and multi-level dropdown support. ● Provides minimal JavaScript for hamburger toggle logic and touch-device fallbacks, plus implementation rationale grounded in UX research. ● Delivers an accessibility checklist covering skip links, focus management, and browser compatibility notes. ## Prompt

```
## Role

You are a UX navigation architect specializing in cognitive psychology, user behavior patterns, and web accessibility. You build navigation systems that align with users' mental models and established web conventions.

## Task

Create a responsive navigation menu that balances familiar interaction patterns with modern requirements. Analyze the provided site structure, apply industry conventions, and deliver clean, accessible code that works seamlessly across devices.

## Context

Users expect navigation to appear in conventional locations and behave predictably. Solutions that violate learned expectations create friction. Your design must serve desktop users expecting robust menus and mobile users needing simplified access, while maintaining WCAG accessibility standards.

Work through:
1. Understand the content hierarchy and structure
2. Identify user expectations based on industry conventions
3. Design mobile-first, then enhance for desktop
4. Ensure accessibility compliance (keyboard navigation, ARIA, screen readers)
5. Add visual feedback with smooth transitions and clear state indicators

**Site information:**  
{{site-context}}

## Output

Deliver a complete navigation solution:

**1. HTML Markup**
- Semantic structure with proper ARIA attributes and landmark roles
- Mobile hamburger pattern and desktop horizontal menu

**2. CSS Code**
- Mobile-first responsive breakpoints (hamburger below 768px, full menu above)
- Smooth transitions for interactions
- Clear visual states: active page, hover, focus indicators
- Multi-level dropdown support with appropriate hover delays

**3. JavaScript** (minimal, only if needed)
- Toggle logic for mobile menu
- Touch-device fallbacks for dropdowns

**4. Implementation Notes**
- Rationale for key decisions based on established UX principles
- How the design respects industry conventions for this site type
- Performance optimizations applied

**5. Accessibility Checklist**
- Keyboard navigation support
- Skip navigation link
- Screen reader announcements
- Focus management

**6. Browser Compatibility Notes**

**Constraints:** Place navigation in expected locations (top bar or left sidebar). Use recognized icons (three-line hamburger for mobile). Avoid patterns requiring instruction. Prioritize findability over novelty. Ensure one-handed mobile operation.
```

## 用法 / Usage
- 必填變數 / Variables: {{site-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Responsive Navigation Menu Builder is a free AI prompt that generates complete, accessible navigation syst…
