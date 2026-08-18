# Custom Platform Builder With AI Prompt

## 簡介

The Custom Platform Builder With AI Prompt is a free AI prompt that generates complete technical architecture and implementation plans for developers building intelligent platform customization engines. This custom platform builder prompt for ChatGPT, Claude, and Gemini produces detailed technical specifications across seven key areas: platform analysis and system architecture, AI-powered requirements processing, modular component frameworks, real-time preview infrastructure, CI/CD pipelines, user interface design, and phased implementation roadmaps. You provide the platform scope and your tech stack, and the prompt returns actionable code examples, step-by-step instructions, and best practices for building engines that parse natural language requirements and generate fully functional customized applications. Use it when you need to architect a system that lets users recreate or modify platforms like CRMs, dashboards, or internal tools with personalized features, live previews, and enterprise deployment capabilities. ● Produces platform architecture designs with microservices, APIs, data models, and enterprise security considerations. ● Delivers natural language processing pipelines and intelligent code generation logic for converting user requirements into working features. ● Includes real-time preview environment setup, hot-reloading systems, and automated testing frameworks. ● Provides CI/CD configurations for web apps, browser extensions, and desktop applications, plus monitoring and rollback strategies. ## Prompt

```
## Role

You are a full-stack platform architect and AI integration specialist designing production-ready customization engines.

## Task

Create a comprehensive technical implementation plan for building an intelligent platform customization engine that transforms user requirements into fully functional applications with real-time previews, AI-powered processing, and enterprise deployment capabilities.

## Context

**Platform and Customization Requirements:**
{{platform-scope}}

**Technical Environment:**
{{tech-stack}}

## Output

Provide a complete technical solution covering:

### Platform Analysis and Architecture Planning
- Core platform structure analysis and component mapping
- System architecture design (microservices, APIs, data models)
- Scalability and security considerations for enterprise deployment

### AI-Powered Requirements Processing System
- Natural language processing pipeline for user requirements
- Feature extraction and validation logic
- Intelligent code generation and customization engine

### Component Development Framework
- Modular component library architecture
- Reusable templates and abstraction layers
- Integration patterns for third-party services

### Real-Time Preview and Testing Infrastructure
- Live preview environment setup
- Hot-reloading and incremental build systems
- Automated testing frameworks and quality assurance

### Build and Deployment Pipeline
- CI/CD configuration for target formats (web app, browser extension, desktop application)
- Environment management and configuration
- Monitoring and rollback strategies

### User Experience and Interface Design
- Customization dashboard and control panel design
- Visual editor and configuration interfaces
- Responsive design implementation

### Technical Implementation Roadmap
- Phased development timeline with milestones
- Dependency management and critical path
- Resource allocation and technical requirements

For each section, provide:
- Complete code examples with explanations
- Detailed technical specifications
- Step-by-step implementation instructions
- Best practices and optimization techniques
```

## 用法 / Usage
- 必填變數 / Variables: {{platform-scope}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Custom Platform Builder With AI Prompt is a free AI prompt that generates complete technical architecture …
