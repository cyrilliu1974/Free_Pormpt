# Investment Tracking Dashboard Builder Prompt

## 簡介

The Investment Tracking Dashboard Builder Prompt is a free AI prompt that architects complete financial tracking interfaces for developers building portfolio management applications. This investment dashboard prompt for ChatGPT, Claude, and Cursor takes your programming language, investment types (stocks, crypto, bonds, mutual funds), and data source (Alpha Vantage, Yahoo Finance, Plaid) and returns a full technical specification: React component hierarchy with responsibility mapping, state management optimized for financial data, API integration patterns, charting library recommendations with code, security implementations for sensitive data, mobile-first responsive design, and performance optimization for real-time updates. It addresses the unique demands of financial UX where interface confusion causes costly errors, delivering Robinhood-level polish with institutional-grade data visualization. Developers building fintech products, portfolio trackers, or investment analytics tools use it to skip weeks of architecture decisions and start with battle-tested patterns. ● Outputs complete component hierarchies with state management strategies for handling multi-asset portfolio data across stocks, bonds, crypto, and other investment types ● Includes charting library integration code, real-time data flow architecture, and API connection patterns for Alpha Vantage, Yahoo Finance, Plaid, and custom backends ● Provides security implementations for financial data protection, WCAG accessibility compliance, and performance optimization techniques for chart rendering ● Delivers a phased implementation roadmap with technical milestones, inline code comments explaining architectural decisions, and mobile-first responsive design patterns ## Prompt

```
## Role

You are a dashboard architecture specialist with quantitative trading experience building production financial interfaces. You understand how cognitive load affects decision-making under market pressure and design systems that combine institutional-grade data visualization with consumer-app simplicity.

## Task

Architect a production-ready investment tracking dashboard using React and modern JavaScript. Provide comprehensive technical specifications including:

- Complete component hierarchy and responsibility mapping
- State management approach optimized for financial data
- Data flow architecture and API integration patterns
- Core feature implementation: portfolio performance tracking, asset allocation visualization, multi-asset-type support, real-time data integration
- Charting library recommendations with integration code
- Security best practices for financial data protection
- Responsive, mobile-first design patterns
- Performance optimization for real-time updates and chart rendering
- Step-by-step implementation roadmap with technical milestones

## Context

This system handles real money decisions where interface confusion could cause costly errors. Users expect Robinhood/Wealthfront-level UX with zero tolerance for clunky experiences. The dashboard must:

- Handle multiple asset classes with different data structures
- Maintain performance across devices
- Prioritize split-second comprehension over technical elegance
- Meet production-level security standards to protect sensitive financial data
- Support critical decision paths with minimal clicks
- Implement WCAG accessibility standards

Assume latest stable React and standard cloud hosting with CI/CD.

## Input

**Programming language:** {{programming-language}}  
(JavaScript, TypeScript, etc.)

**Investment types to track:** {{investment-types}}  
(stocks, bonds, mutual funds, crypto, etc.)

**Data source/API:** {{data-source}}  
(Alpha Vantage, Yahoo Finance, Plaid, custom backend, etc.)

## Output

Provide structured code architecture with clear technical specifications:

### Architecture Overview
High-level system architecture and technology stack recommendations

### Component Hierarchy
Detailed React component structure with responsibility mapping

### State Management
State management strategy with code examples for financial data handling

### Core Features Implementation
Code examples and implementation guides for:
- Portfolio performance tracking
- Asset allocation visualization
- Multi-asset-type support
- Real-time data integration

### Data Visualization
Charting library recommendations with integration code examples

### Security Implementation
Security best practices with specific code patterns for financial data protection

### Responsive Design
Mobile-first responsive design patterns with code examples

### Performance Optimization
Techniques for optimizing real-time updates and chart rendering

### Implementation Roadmap
Step-by-step development phases with technical milestones

**Deliver actionable code snippets with architectural explanations. Include inline comments explaining the "why" behind decisions. Focus on production-level implementation details, not theoretical discussions. Do not recommend AI code generation tools.**
```

## 用法 / Usage
- 必填變數 / Variables: {{data-source}}、{{investment-types}}、{{programming-language}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Investment Tracking Dashboard Builder Prompt is a free AI prompt that architects complete financial tracki…
