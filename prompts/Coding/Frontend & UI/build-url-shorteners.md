# URL Shortener App Builder Prompt

## 簡介

The URL Shortener App Builder Prompt is a free AI prompt that generates production-ready code for a full-stack URL shortening service with enterprise features and mobile-first design. This URL shortener prompt for ChatGPT, Claude, Gemini, and Grok produces structured implementation guides covering HTML5 markup, CSS3 responsive styling, JavaScript validation logic, backend API integration patterns, QR code generation, custom alias systems, password protection, expiration controls, click analytics dashboards, and security hardening. You input your technical requirements and receive complete code examples organized by component - from file structure and frontend forms through data visualization and deployment checklists. Use it to build competing services with features like copy-to-clipboard, URL history management, and advanced filtering. This prompt is for full-stack developers, startups launching link-management tools, and teams prototyping URL shortening MVPs who need working code fast. ● Outputs semantic HTML5, mobile-first CSS3, and validated JavaScript for instant URL shortening ● Includes QR code generation logic, custom alias validation, and password-protection UI components ● Provides analytics dashboard code with click tracking, data visualization, and search filtering ● Delivers input sanitization methods, XSS prevention techniques, and CSRF protection strategies ## Prompt

```
## Role

You are an expert full-stack web developer and UX architect building a production-ready URL shortening service that competes with established players through superior user experience, robust validation, and enterprise features.

## Task

Design and implement a complete frontend application with backend API integration that delivers professional URL shortening, QR code generation, analytics tracking, and security features in a clean, responsive, mobile-first interface.

## Context

Users demand instant functionality and will abandon services with clunky interfaces, validation failures, or poor mobile responsiveness. The service must hide complex backend operations behind an elegant frontend while differentiating through features like custom aliases, password protection, and analytics.

**Integration Details:**
{{technical-requirements}}

## Output

Provide a complete implementation guide structured as follows:

### Project Architecture Overview
File structure, technology stack, and component organization

### HTML5 Structure
Semantic markup for main interface, input fields, dashboard, and history sections

### CSS3 Styling System
Responsive design framework, mobile-first approach, animations, and visual feedback mechanisms

### JavaScript Core Functionality
- URL validation and sanitization logic
- API integration patterns
- Error handling and user feedback

### URL Shortening Implementation
Input processing, backend communication, response handling, and display logic

### QR Code Generation
Integration approach, rendering method, and download functionality

### Custom Alias System
Validation rules, availability checking, and user feedback mechanisms

### Advanced Features
- Password protection UI
- Expiration date picker
- Copy-to-clipboard with confirmation

### Analytics Dashboard
Click tracking display, data visualization, filtering and search functionality

### URL History Management
Storage strategy (local storage or database), search implementation, and filtering options

### Security Implementation
- Input sanitization methods
- XSS prevention techniques
- CSRF protection strategies

### Testing and Deployment
- Browser compatibility checklist
- Performance optimization steps
- Deployment instructions

Present complete code examples with clear implementation instructions for each component.
```

## 用法 / Usage
- 必填變數 / Variables: {{technical-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The URL Shortener App Builder Prompt is a free AI prompt that generates production-ready code for a full-stack…
