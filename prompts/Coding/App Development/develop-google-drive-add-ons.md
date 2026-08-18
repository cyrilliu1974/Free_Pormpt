# Google Drive Add-On Development Prompt

## 簡介

The Google Drive Add-On Development Prompt is a free AI prompt that generates complete implementation guides for building production-ready Google Workspace add-ons tailored to your specification. This Google Drive add-on prompt for ChatGPT, Claude, Gemini, and Grok walks you through every phase of development: architecture planning, Apps Script backend logic, frontend UI design, OAuth security configuration, error handling, and deployment. You provide your add-on specification, and the AI returns structured code examples, file organization strategies, and integration patterns that work natively within Google Drive. Developers use it to build internal tools, automate document workflows, or ship customer-facing extensions with enterprise-grade reliability. Reach for this prompt when you need a clear roadmap from initial setup to production launch, complete with security best practices and real-world error handling. ● Outputs modular Apps Script backend code with Google Drive API integration and data processing logic. ● Provides responsive, accessible frontend UI components and client-server communication patterns. ● Includes OAuth scope definitions, token management, and security configurations for production use. ● Covers testing scenarios, user documentation templates, and deployment monitoring strategies. ## Prompt

```
## Role

You are a full-stack Google Workspace integration specialist building production-ready Google Drive add-ons.

## Task

Create a comprehensive, step-by-step implementation guide for a Google Drive add-on based on the specification below.

## Context

{{add-on-specification}}

## Requirements

- Native Google Drive integration with minimal user friction
- Enterprise-grade architecture with robust error handling
- Modern, accessible UI with responsive design
- Complete OAuth security configuration
- Production-ready deployment strategy

## Output

Structure your implementation guide with these sections, providing complete code examples and specific implementation details for each:

### Architecture Planning and File Structure
- Project organization and module design
- Dependency management and versioning

### Backend Development with Apps Script
- Core business logic implementation
- Google Drive API integration
- Data processing and file manipulation

### Frontend UI Development
- Interface components and layout
- Responsive design patterns
- Accessibility considerations

### Client-Server Communication and State Management
- Asynchronous data flow
- State persistence strategies
- Performance optimization

### OAuth Configuration and Security
- Scope definitions and permissions
- Token management
- Security best practices

### Error Handling and Edge Cases
- Validation logic
- Graceful degradation
- User-facing error messages

### Testing, Documentation, and Deployment
- Test scenarios and validation
- User documentation
- Deployment checklist and monitoring
```

## 用法 / Usage
- 必填變數 / Variables: {{add-on-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Human_In_Loop_Workflow_Engineering · Prompt_Assembly_Integrity_Protocol
- 適用 / Use when: The Google Drive Add-On Development Prompt is a free AI prompt that generates complete implementation guides f…
