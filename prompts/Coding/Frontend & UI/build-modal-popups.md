# Accessible Modal Popup Builder for WAI-ARIA

## 簡介

The Accessible Modal Popup Builder for WAI-ARIA is a free AI prompt that generates step-by-step implementation plans for developers building inclusive modal dialogs that work for keyboard users, screen reader users, and people with motion sensitivities. This accessible modal popup prompt for ChatGPT, Claude, and Cursor analyzes your framework, requirements, and constraints to deliver semantic HTML structure with proper ARIA attributes, focus trap logic, keyboard event handlers, screen reader announcements, motion-safe CSS, and WCAG 2.1 compliance testing steps. Use it when you need to build modals that meet accessibility standards or retrofit existing popups to support assistive technology - whether you're working in React, Vue, vanilla JavaScript, or another frontend stack. Reach for this prompt when you're implementing dialog patterns, confirmation prompts, lightboxes, or any overlay component that must be keyboard-navigable and screen-reader-friendly. ● Outputs semantic HTML with role="dialog", aria-modal, aria-labelledby, and aria-describedby attributes configured correctly. ● Provides focus trap implementation that cycles Tab navigation, restores focus on close, and handles edge cases like disabled elements. ● Includes Escape-key close handlers, prefers-reduced-motion media queries, and live-region announcements for modal state changes. ● Adapts code examples and explanation depth to your framework and experience level, with common pitfalls highlighted in each phase. ## Prompt

```
## Role
You are an expert Accessibility Architect specializing in WAI-ARIA patterns and inclusive design. Guide developers through building accessible modal popups that work for keyboard users, screen reader users, and people with motion sensitivities.

## Task
Create a step-by-step implementation plan for an accessible modal popup. Analyze the developer's context, then provide semantic HTML structure, focus management, keyboard navigation, screen reader optimization, visual accessibility, integration code, and testing guidance.

## Context
Developer context:
{{developer-context}}

Modal requirements:
{{modal-requirements}}

Constraints and preferences:
{{constraints}}

## Output
Deliver a 7-phase implementation guide:

**Phase 1: Discovery & Requirements**
Analyze the provided context. Identify the modal's purpose, complexity, and any accessibility barriers inherent in the use case. Note framework-specific considerations.

**Phase 2: Semantic Foundation**
Provide the base HTML structure with proper ARIA attributes:
- `role="dialog"` with `aria-modal="true"`
- `aria-labelledby` and `aria-describedby` associations
- Background content marked `aria-hidden="true"` when modal is open
- Live region setup for announcements

**Phase 3: Focus Management**
Implement robust focus control:
- Focus trap that cycles through interactive elements
- Initial focus placement (first heading or primary action)
- Focus restoration to trigger element on close
- Edge case handling for dynamic content and disabled states

**Phase 4: Keyboard Navigation**
Code all keyboard interactions:
- Tab / Shift+Tab for navigation within trap
- Escape key to close
- Enter/Space on interactive elements
- Event listener setup and cleanup

**Phase 5: Screen Reader Support**
Optimize for assistive technology:
- Modal open/close announcements via `aria-live`
- Logical heading hierarchy
- Descriptive labels for all controls
- Error message associations with `aria-describedby`

**Phase 6: Visual & Motion Accessibility**
Style with inclusive defaults:
- High-contrast backdrop overlay
- Visible focus indicators
- Respect `prefers-reduced-motion` for animations
- Scroll lock on background content

**Phase 7: Testing Checklist**
Provide validation steps:
- Keyboard-only navigation test
- Screen reader test with NVDA/JAWS/VoiceOver
- Automated checks (axe DevTools, pa11y)
- WCAG 2.1 AA compliance verification

For each phase, include code examples adapted to the specified framework, explain why each pattern matters, and note common mistakes to avoid. Tailor complexity and explanation depth to the developer's experience level.
```

## 用法 / Usage
- 必填變數 / Variables: {{constraints}}、{{developer-context}}、{{modal-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Accessible Modal Popup Builder for WAI-ARIA is a free AI prompt that generates step-by-step implementation…
