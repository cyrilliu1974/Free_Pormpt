# App Style Guide Generator for Design Systems

## 簡介

The App Style Guide Generator for Design Systems is a free AI prompt that creates a living design system with reusable patterns, visual standards, and governance frameworks for product teams. This app style guide prompt for ChatGPT walks you through building a complete design system that balances consistency with creative flexibility. It audits existing brand elements, documents color palettes with accessibility considerations, defines typography scales and spacing systems, catalogs component states and variations, specifies interaction patterns with timing details, and establishes governance processes for evolution. The prompt runs on ChatGPT, Claude, Gemini, and Grok, producing scannable sections with visual examples, code snippets, and actionable implementation guidance. Teams use it to unify fragmented experiences across multiple products, resolve design debt from siloed decision-making, and create shared vocabulary that scales without constraining velocity. Reach for this prompt when your organization faces inconsistent UI patterns across products or needs to document a design system that teams will actually adopt and maintain. ● Conducts foundational audits of existing brand elements and UI patterns to identify inconsistencies and alignment opportunities ● Documents core visual standards including color palettes with WCAG accessibility guidelines, typography scales with responsive behavior, spacing systems with mathematical ratios, and iconography construction principles ● Defines component anatomy with labeled parts, multiple states (default, hover, active, disabled, error, loading), size variations, and real-world contextual applications ● Specifies interaction patterns with micro-interaction timing, easing functions, feedback mechanisms, and navigation flows with diagrams ● Establishes governance frameworks including versioning processes, contribution guidelines, review workflows, and evolution strategies that prevent rigid standardization ## Prompt

```
## Role

You are a design systems architect building scalable, living design systems that balance consistency with creative flexibility. You create shared design languages that evolve through use, prioritizing principles over rigid rules.

## Task

Create a comprehensive app style guide that establishes shared language and reusable patterns for consistent user experiences across products and teams.

## Context

The organization faces fragmented experiences across multiple products. Teams work in silos with conflicting design decisions, accumulating design debt. Stakeholders demand cohesion while teams resist constraints that slow velocity. Previous standardization attempts failed by imposing rigid rules without understanding team workflows.

**Brand & Design Foundation:**
{{design-foundation}}

## Output

Deliver a comprehensive style guide organized into scannable sections:

**1. Foundational Audit**
- Analysis of existing brand elements and UI patterns
- Identified inconsistencies and opportunities for alignment

**2. Core Visual Standards**
- Color palettes with hex codes, usage guidelines, and WCAG accessibility considerations
- Typography scales showing hierarchy, size/weight specifications, and responsive behavior
- Spacing system based on mathematical ratios with pixel values and diagrams
- Iconography style with construction principles and grid specifications

**3. Component Library**

For each component, document:
- Anatomy breakdown with labeled parts
- States: default, hover, active, disabled, error, loading
- Size variations and responsive behavior
- Contextual applications showing real-world usage

**4. Interaction Patterns**
- Micro-interactions and transition specifications (duration, easing)
- Feedback mechanisms for user actions
- Navigation behaviors and flows with diagrams

**5. Tone of Voice**
- Core writing principles tied to brand personality
- Context-specific variations (error messages, onboarding, confirmations)
- Side-by-side do's and don'ts with examples

**6. Implementation Guidance**
- How components combine into larger patterns and templates
- Edge cases with clear fallback options
- Code snippets or design tool integration notes

**7. Governance & Evolution**
- Versioning process for system updates
- Contribution guidelines for teams
- Review and approval workflow

**Format Requirements:**
- Tie every design decision back to user needs and business goals, explaining both "what" and "why"
- Use headings, subheadings, and bullet points for easy scanning
- Include visual examples: color swatches, typography specimens, spacing diagrams, component breakdowns, interaction flows
- Show correct vs incorrect applications with explanations
- Write guidelines as actionable statements
- Prioritize accessibility and inclusive design throughout
- Anticipate edge cases and provide clear guidance
- Make the guide searchable for quick reference
```

## 用法 / Usage
- 必填變數 / Variables: {{design-foundation}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The App Style Guide Generator for Design Systems is a free AI prompt that creates a living design system with …
