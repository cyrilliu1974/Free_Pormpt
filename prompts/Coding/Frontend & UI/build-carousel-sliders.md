# Build Carousel Sliders

## 簡介

The Build Carousel Sliders prompt is a free AI prompt that generates accessible, usability-focused carousel slider code for frontend developers and designers. This carousel slider prompt for ChatGPT produces complete HTML, CSS, and JavaScript implementations that prioritize user control over automatic behaviors. It creates carousels with always-visible navigation arrows, keyboard accessibility, screen reader support, and optional auto-rotation that respects user interaction by pausing on hover and focus. The prompt runs on ChatGPT, Claude, and Cursor, delivering code that follows Nielsen Norman Group guidelines to avoid common carousel pitfalls like hidden controls, forced auto-play that interrupts reading, and inaccessible content. Real-world use cases include product showcases, testimonial sections, image galleries, and content features that need to balance interactivity with accessibility standards. Reach for this prompt when you need a carousel that works for all users across devices, especially when accessibility compliance and usability testing are priorities. ● Outputs semantic HTML with proper ARIA roles, labels, and keyboard navigation support for screen readers and assistive technology. ● Includes CSS for always-visible navigation controls, direct-access dot indicators, touch-friendly targets (44×44px minimum), and motion-safe transitions. ● Provides JavaScript for previous/next arrows, dot navigation, full keyboard control (arrow keys, tab, enter, space), and touch gestures that respect page scrolling. ● Delivers implementation notes explaining how each feature addresses specific usability guidelines, plus a testing checklist covering keyboard navigation, screen reader compatibility, mobile gestures, and performance validation. ## Prompt

```
## Role
You are a carousel implementation specialist focused on usability and accessibility, following Nielsen Norman Group guidelines: user-controlled navigation, visible controls, accessible content, and no forced auto-rotation.

## Task
Generate a carousel slider implementation that prioritizes usability over trends. The carousel must provide obvious navigation, keyboard accessibility, screen reader support, and respect user agency.

## Context
Most carousels fail because they auto-rotate content users are reading, hide controls, and make content inaccessible. This implementation avoids those pitfalls while meeting modern expectations for interactivity and mobile support.

**Requirements:**
{{carousel-requirements}}

*Specify: slide content type, autoplay preference (yes/no + timing if yes), target audience, specific accessibility needs, and technology stack/framework.*

## Output
Provide production-ready code with:

**1. HTML Structure**
- Semantic markup with appropriate ARIA roles and labels
- Clear content hierarchy

**2. CSS Styling**
- Always-visible navigation arrows
- Position indicator dots that allow direct slide access
- Smooth, non-jarring transitions
- Mobile-responsive layout

**3. JavaScript Functionality**
- Previous/next arrow controls
- Dot navigation for direct slide access
- Full keyboard navigation (arrow keys, tab, enter, space)
- Touch/swipe gestures that don't interfere with scrolling
- If autoplay requested: pause-on-hover, pause-on-focus, and visible pause/play controls

**4. Implementation Notes**
- Explain how each feature addresses specific usability guidelines
- Note how content remains accessible outside the carousel interaction
- Document interaction patterns and states

**5. Testing Checklist**
- Keyboard navigation verification
- Screen reader compatibility checks
- Mobile gesture testing
- Performance and layout shift validation

Ensure controls are large enough for touch targets (minimum 44×44px), transitions respect `prefers-reduced-motion`, and all content is reachable without the carousel interface.
```

## 用法 / Usage
- 必填變數 / Variables: {{carousel-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Carousel Sliders prompt is a free AI prompt that generates accessible, usability-focused carousel sl…
