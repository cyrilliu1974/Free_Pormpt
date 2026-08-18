# Placeholder Content Generator Development Guide

## 簡介

The Placeholder Content Generator Development Guide is a free AI prompt that produces a full-stack technical specification for building a React-based placeholder content tool tailored to designers and developers. This placeholder content generator prompt for ChatGPT walks through project architecture, content generation algorithms, UI component libraries, customization features, performance optimization, and deployment strategies. It runs on ChatGPT, Claude, Gemini, and Grok, accepting a single {{project-context}} variable that captures your skill level, design preferences, target users, timeline, and deployment platform. The output is a structured development guide with TypeScript code examples, testing strategies, and CI/CD pipeline recommendations. Teams building internal tools, agencies creating client deliverables, and solo developers shipping content utilities will find it immediately actionable. ● Architects a React application stack with content generation algorithms, UI component libraries, and export functionality. ● Provides code examples in React and TypeScript, covering setup, generation logic, responsive design, and accessibility. ● Includes testing strategy, CI/CD pipeline configuration, and deployment steps for your chosen platform. ● Tailors recommendations to skill level, design preferences, and timeline specified in the {{project-context}} variable. ## Prompt

```
## Role

You are an expert full-stack developer and product architect specializing in React application development.

## Task

Create a complete technical development guide for building a context-aware placeholder content generator—a React application that goes beyond basic Lorem Ipsum by understanding industry requirements, tone preferences, and content types to deliver production-ready output for designers and developers.

## Context

{{project-context}}

Include: technical skill level (React/TypeScript/frontend experience), UI/UX design preferences, target users (designers/developers/agencies), development timeline, and deployment platform.

## Output

Structure your guide with these sections:

### Project Architecture and Setup
- Technology stack recommendations tailored to the skill level
- Project structure and configuration
- Dependencies and tooling setup

### Content Generation Engine
- Algorithm design for context-aware generation
- Support for multiple content types (text, images, data)
- Tone and industry-specific customization logic

### UI Component Library
- Component architecture aligned with design preferences
- Reusable UI patterns
- Responsive design implementation

### Customization and Export Features
- User configuration options
- Export formats and integration methods
- Template management system

### Performance and Accessibility
- Code splitting and lazy loading strategies
- WCAG compliance approach
- Performance benchmarks

### Testing, Deployment, and Production Readiness
- Testing strategy (unit, integration, e2e)
- CI/CD pipeline setup
- Deployment steps for the specified platform
- Monitoring and maintenance recommendations

Provide detailed technical specifications, React/TypeScript code examples, and implementation roadmaps. Present information clearly with bullet points for actionable clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{project-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Placeholder Content Generator Development Guide is a free AI prompt that produces a full-stack technical s…
