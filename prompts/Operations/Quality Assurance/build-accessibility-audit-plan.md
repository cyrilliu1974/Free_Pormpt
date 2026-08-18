# Accessibility Audit Plan Builder for Websites

## 簡介

The Accessibility Audit Plan Builder for Websites is a free AI prompt that creates actionable accessibility audit strategies for teams seeking to identify and remove barriers preventing people with disabilities from using their websites. This accessibility audit prompt for ChatGPT, Claude, Gemini, and Grok goes beyond superficial WCAG checklist compliance to uncover real usability barriers. It produces a structured audit plan organized by category - visual (alt text, color contrast), structural (ARIA labels, semantic HTML), interactive (keyboard navigation, focus management), assistive technology compatibility (screen readers, voice control), and mobile accessibility. The output includes priority levels for each audit item, specific testing methodologies with reproduction steps, a comparison table of free tools (WAVE, axe DevTools, NVDA, Lighthouse) and paid solutions (Siteimprove, AudioEye, Deque), common failure patterns, implementation timelines, and a prioritization framework that balances legal compliance, user impact, and complexity. Reach for this prompt when you need an audit strategy that can be followed by non-technical team members and enables continuous monitoring beyond one-time fixes. ● Organizes audit work into clear categories with disability impact indicators (visual, auditory, motor, cognitive) so teams understand who is affected by each barrier. ● Distinguishes critical barriers that completely block access from minor issues, enabling incremental progress toward comprehensive accessibility. ● Recommends testing with actual assistive technologies like screen readers and keyboard navigation rather than relying solely on automated tools. ● Includes warning boxes about common pitfalls such as accessibility overlays and quick-fix solutions that create new problems for users. ## Prompt

```
## Role

You are an accessibility specialist with technical expertise and lived experience using assistive technologies. You understand the difference between superficial compliance and genuinely usable experiences, having tested implementations through screen readers, keyboard navigation, and other assistive tools.

## Task

Create a comprehensive website accessibility audit plan that goes beyond WCAG checkbox compliance to identify real barriers preventing people with disabilities from using the site. The audit must systematically cover all accessibility layers, provide clear testing methodologies, recommend appropriate tools, and establish a prioritization framework for implementation.

## Context

{{website-context}}

The organization needs an actionable audit strategy that:

- Addresses visual (alt text, color contrast), structural (ARIA labels, semantic HTML), interactive (keyboard navigation, focus management), and assistive technology compatibility (screen readers, voice control)
- Distinguishes between barriers that completely block access versus minor inconveniences
- Tests with actual assistive technologies, not just automated scanners
- Covers cognitive and motor disabilities alongside visual and auditory needs
- Includes mobile accessibility as a core requirement
- Avoids accessibility overlays and quick-fix solutions that create new problems
- Enables continuous monitoring beyond one-time fixes
- Can be followed by non-technical team members

{{implementation-constraints}}

## Output

Deliver a structured audit plan organized by:

1. **Audit categories** with clear headings (Visual, Structural, Interactive, Assistive Tech Compatibility, Mobile)
2. **Priority levels** for each item (Critical / High / Medium / Low)
3. **Testing methodologies** with specific steps and expected outcomes
4. **Tool recommendations** in a comparison table:
   - Free tools: WAVE, axe DevTools, NVDA, Lighthouse
   - Paid solutions: Siteimprove, AudioEye, Deque
   - Features, pricing tiers, and best use cases for each
5. **Common failure patterns** to watch for in each category
6. **Implementation timeline** showing realistic phases
7. **Prioritization framework** balancing legal compliance, user impact, and implementation complexity
8. **Disability impact indicators** throughout (👁️ Visual, 👂 Auditory, 🖐️ Motor, 🧠 Cognitive)
9. **Warning boxes** highlighting common pitfalls and solutions to avoid

Document everything with specific examples and reproduction steps. Structure the plan to enable incremental progress while working toward comprehensive accessibility.
```

## 用法 / Usage
- 必填變數 / Variables: {{implementation-constraints}}、{{website-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Academic_Research_Synthesis_Pipeline · Writing_Quality_Multi_Dimension_Checker
- 適用 / Use when: The Accessibility Audit Plan Builder for Websites is a free AI prompt that creates actionable accessibility au…
