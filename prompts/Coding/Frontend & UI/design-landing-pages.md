# WebGL Landing Page Design Prompt

## 簡介

The WebGL Landing Page Design Prompt is a free AI prompt that generates full creative direction and technical specifications for immersive, shader-driven landing pages for companies launching visually distinct digital products. This WebGL landing page design prompt for ChatGPT, Claude, Gemini, and Grok produces a nine-section specification document covering aesthetic foundations, scroll narratives, shader behaviors, interaction patterns, responsive strategies, and developer handoff instructions. It translates reference aesthetics, company context, and technical constraints into actionable visual systems that front-end teams can implement using Three.js, GSAP, and custom shaders. Use it when you need to design scroll-reactive experiences with dithered effects, organic 3D displacement, and particle systems that balance experimental visuals with performance and accessibility. This prompt is built for creative technologists, design teams, and agencies working on high-impact product launches in competitive markets. ● Extracts color palettes with hex codes, textures, and mood from reference aesthetics and adapts them to brand personality ● Specifies scroll-driven narratives with shader transformations, timing curves, and transition choreography across hero, content, and CTA sections ● Describes shader behaviors in natural language that developers can translate into working dithering effects, displacement maps, and particle systems ● Includes component states, responsive strategies, performance targets, accessibility considerations, and technical architecture requirements ## Prompt

```
## Role

You are a creative technologist and WebGL visualization specialist designing immersive landing page experiences. You balance experimental shader aesthetics with performance, accessibility, and developer feasibility—creating visually distinct experiences that achieve high engagement without sacrificing clarity.

## Context

The company is launching an AI product in a visually homogeneous market where gradient meshes and generic futuristic designs dominate. Previous attempts failed by going too abstract (message lost) or too literal (forgettable). The goal is a landing page that sets a new visual standard—memorable, screenshot-worthy, and distinctly future-forward—while remaining legible and technically achievable.

## Task

Design a full-screen, scroll-reactive landing page featuring custom dithered shader effects, organic 3D displacement, and particle systems built on Three.js/WebGL with GSAP orchestration. Focus on **visual system and creative direction**, not code implementation. Provide specifications developers can translate directly into working experiences.

Extract the aesthetic foundation (colors with hex codes, textures, mood, visual language) from {{reference-aesthetic}}. Incorporate the product positioning, target audience, and brand personality from {{company-context}}. Respect the development limitations, browser support, hosting environment, performance budgets, and framework preferences in {{technical-constraints}}.

## Output

Structure your response with these nine sections clearly labeled:

1. **Aesthetic Foundation** – Colors (hex codes), textures, mood, and visual language
2. **Hero Section Design** – Canvas setup, shader states, typography treatment, load-in animations
3. **Scroll Narrative** – Section-by-section journey with shader transformations, content reveals, transition choreography, and timing
4. **Component Specifications** – Buttons, cards, navigation, interactive elements with all states (default, hover, active, disabled)
5. **Shader Behaviors** – Natural-language descriptions of dithering effects, displacement patterns, color transitions, particle systems that developers can implement
6. **Interaction Patterns** – Hover states, click responses, scroll behaviors, mouse tracking, micro-interactions with timing (ease curves, duration)
7. **Responsive Strategy** – Multi-device adaptation, performance optimization, graceful degradation for lower-end devices
8. **Technical Architecture** – Required stack (Three.js, GSAP, etc.), file structure, performance targets (60fps, load time), accessibility considerations (reduced motion, keyboard nav, screen readers)
9. **Developer Handoff** – Clear specs, animation timing charts, quality standards

Balance experimental visual boundaries with enterprise-grade polish. Every specification should be actionable for a developer without requiring interpretation or follow-up questions.
```

## 用法 / Usage
- 必填變數 / Variables: {{company-context}}、{{reference-aesthetic}}、{{technical-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: RPG&Immersive_World_Systems · Multi_Agent_Scene_Pressure_Design
- 適用 / Use when: The WebGL Landing Page Design Prompt is a free AI prompt that generates full creative direction and technical …
