# Adaptive Planner App Builder for Multiple Contexts

## 簡介

The Adaptive Planner App Builder is a free AI prompt that generates complete, production-ready planning applications for developers and teams building context-aware workflow tools. This planner app prompt for ChatGPT delivers enterprise-grade, multi-file codebases that dynamically adapt based on context - whether users are planning travel itineraries, organizing events, or managing projects. Running on ChatGPT, Claude, or Cursor, it produces a full-stack application with state management, collaborative features like task assignment and commenting, timeline systems, and export capabilities including PDF generation and calendar integration. Developers building SaaS products, agencies creating client planning tools, or startups launching productivity apps will find this prompt saves weeks of architecture and implementation work. ● Outputs complete folder structure with package configuration, dependencies, environment setup, and build files ● Generates context-aware UI components that morph between travel, event, and project planning modes with adaptive panels and timeline systems ● Includes collaboration infrastructure with sharing permissions, task assignment, real-time updates, activity feeds, and commenting ● Delivers export and integration features including PDF generation, iCal and Google Calendar exports, plus data backup and import functionality ● Provides WCAG-compliant responsive design with performance optimization, smooth animations, and comprehensive documentation including README, component guides, and deployment instructions ## Prompt

```
## Role
You are an expert full-stack developer and UX architect specializing in planning applications.

## Task
Build a complete, production-ready adaptive planning application that dynamically morphs based on context (travel, events, projects). Include collaborative features, timeline management, and export capabilities.

## Context
Deliver enterprise-grade code with comprehensive documentation. Provide complete files, not snippets.

{{tech-stack}}

{{feature-requirements}}

## Output
Deliver a comprehensive, multi-file project organized as follows:

**Project Setup and Architecture**
- Complete folder structure
- Dependencies and package configuration
- Environment and build configuration files

**Core Components**
- Landing interface with planner type selection
- Dynamic timeline system
- Context-aware panels that adapt to planner type (travel/events/projects)

**State Management**
- Store implementation with planner detection logic
- Data persistence layer
- Type-safe interfaces throughout

**Collaboration Features**
- Sharing and permissions
- Task assignment system
- Real-time updates
- Commenting and activity feeds

**Export and Integration**
- PDF generation
- Calendar exports (iCal/Google Calendar)
- Data backup and import functionality

**UI/UX and Performance**
- Smooth animations and transitions
- Fully responsive design
- WCAG accessibility compliance
- Performance optimization

**Documentation**
- Comprehensive README with setup instructions
- Component documentation
- Deployment guide
- API reference if applicable

Provide complete, production-ready code with detailed comments, proper TypeScript interfaces, and sample data for testing all planner types. Work through this systematically, ensuring each component is fully functional and well-integrated.
```

## 用法 / Usage
- 必填變數 / Variables: {{feature-requirements}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Strategic_Resource&Sprint_Prioritization
- 適用 / Use when: The Adaptive Planner App Builder is a free AI prompt that generates complete, production-ready planning applic…
