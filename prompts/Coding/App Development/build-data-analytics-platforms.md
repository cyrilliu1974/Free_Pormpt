# Data Analytics Platform Builder Prompt

## 簡介

The Data Analytics Platform Builder Prompt is a free AI prompt that generates complete, enterprise-grade data visualization applications for businesses and developers who need to transform raw data into interactive dashboards. This data analytics platform prompt for ChatGPT, Claude, and Cursor produces a fully functional React application with TypeScript that accepts CSV, Excel, and JSON uploads, automatically selects appropriate chart types, integrates Claude API to analyze datasets and surface actionable recommendations, and exports visualizations as PDFs. The output includes organized component architecture, file processing modules, a visualization engine with Recharts, glassmorphism styling with Tailwind CSS, state management patterns, and working sample implementations. Use it when you need to quickly prototype or deploy a data analytics tool without building the entire infrastructure from scratch, or when your business needs a polished dashboard that interprets data patterns and suggests specific actions. ● Outputs complete React + TypeScript application structure with proper typing, component hierarchy, and error handling ready for deployment. ● Integrates Claude API for intelligent data analysis that identifies trends, anomalies, and generates business recommendations automatically. ● Includes robust file processing for CSV, Excel, and JSON formats with validation, auto-detection of chart types, and export functionality for reports and visualizations. ● Delivers glassmorphism design system with Tailwind CSS, smooth animations, loading states, and accessibility features for an enterprise-level user experience. ## Prompt

```
## Role
You are an expert full-stack developer specializing in data visualization platforms. You design enterprise-grade analytics applications that transform raw data into actionable insights through intuitive interfaces and automated analysis.

## Task
Build a complete, production-ready data visualization and analysis platform as a single-page React application. The platform must:

- Accept CSV, Excel, and JSON file uploads
- Automatically parse data and generate appropriate visualizations
- Integrate with Claude API to analyze datasets and generate actionable recommendations
- Present insights through an interactive dashboard with smooth animations and loading states
- Support exporting visualizations and reports
- Feel polished and professional, not prototypical

## Context
{{business-context}}

## Technical Requirements

**Stack & Architecture:**
- React with TypeScript, properly typed throughout
- Tailwind CSS with glassmorphism design system
- Recharts for chart rendering
- Organized component hierarchy suitable for scaling
- Comprehensive error handling and accessibility features

**Core Features:**
1. **File Processing** – Robust ingestion and validation for CSV, Excel, and JSON formats
2. **Visualization Engine** – Auto-detection of relevant chart types based on data structure
3. **AI Analysis** – Claude API integration that identifies patterns, anomalies, and recommends specific actions
4. **Export System** – PDF generation and chart export functionality

## Output

Provide:

### Project Structure
Complete folder organization and file hierarchy

### Core Components
Main React components with TypeScript interfaces, props, and component relationships

### File Processing Module
Data ingestion, parsing, and validation logic for all supported formats

### Visualization Engine
Chart generation system with auto-detection logic and customization options

### AI Integration
Claude API implementation for insight generation, including prompt structure and response handling

### Styling System
Tailwind configuration, glassmorphism utilities, and responsive design patterns

### State Management
Data flow architecture and state handling approach

### Export Functionality
Implementation details for PDF generation and chart exports

### Sample Implementation
Working code example with a sample dataset for testing

Use modern React patterns (hooks, composition). Every feature should demonstrate enterprise-level polish.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Data Analytics Platform Builder Prompt is a free AI prompt that generates complete, enterprise-grade data …
