# Brand Mention Monitoring App Builder

## 簡介

The Brand Mention Monitoring App Builder is a free AI prompt that generates production-ready monitoring dashboards for agencies, developers, and brand managers who need real-time social listening systems. This brand mention monitoring prompt for ChatGPT produces a complete, single-file React + TypeScript application that aggregates mentions across platforms, scores sentiment in real-time, and sends customizable alerts - all without external dependencies or API setup. It runs on ChatGPT, Claude, and Cursor, delivering copy-paste-ready code that rivals enterprise tools like Brandwatch or Mention. The output includes WebSocket-simulated live feeds, multi-criteria filtering, analytics widgets with trend detection, and export functionality. Use it when you need a working prototype for client demos, want to avoid subscription fees for basic monitoring, or need a foundation to extend with live API integrations. ● Produces a three-column dark-themed dashboard with real-time mention streams, sentiment analysis, and historical trend charts ● Includes customizable alert rules, multi-workspace support for tracking different brands, and CSV/JSON export for reporting ● Implements professional performance optimizations like virtualization, memoization, and efficient state management for high-volume feeds ● Generates realistic mock data and inline documentation so the code runs immediately and serves as a learning reference ## Prompt

```
## Role
You are an expert full-stack engineer and real-time systems architect building a production-ready brand mention monitoring dashboard.

## Task
Create a complete, single-file React + TypeScript application that aggregates multi-platform mentions, analyzes sentiment, and provides real-time alerts. The solution should rival enterprise monitoring services in functionality and polish.

## Context
{{monitoring-requirements}}

## Technical Requirements

### Architecture
- Single-file React application with TypeScript interfaces
- Organized component hierarchy and clear separation of concerns
- WebSocket simulation for real-time mention updates
- Mock data system generating realistic brand mentions

### Dashboard Interface
- Three-column layout with dark theme (slate grays, electric blue accents, Linear.app aesthetic)
- Smooth animations and professional micro-interactions
- Responsive design optimized for desktop monitoring workflows

### Core Features
- **Live mention feed**: Real-time stream of brand mentions across platforms
- **Sentiment analysis**: Visual sentiment scoring and trend indicators
- **Filtering system**: Multi-criteria filtering (platform, sentiment, date range, keywords)
- **Analytics widgets**: Mention volume charts, sentiment distribution, top sources
- **Alert system**: Customizable notification rules with browser alerts
- **Export functionality**: CSV/JSON export of mentions and analytics
- **Trend analysis**: Historical patterns and anomaly detection
- **Multi-workspace support**: Switch between different brand monitoring profiles

### Performance
- Optimized rendering for high-volume mention streams
- Efficient state management and memoization
- Lazy loading and virtualization where appropriate

## Output Format
Deliver a complete, copy-paste-ready React application that:
- Runs immediately without additional setup
- Demonstrates all monitoring capabilities with realistic mock data
- Includes inline comments explaining key architectural decisions
- Uses modern React patterns (hooks, context, custom hooks for business logic)
- Implements professional error handling and loading states
```

## 用法 / Usage
- 必填變數 / Variables: {{monitoring-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Agent_Runtime_Charter_Design
- 適用 / Use when: The Brand Mention Monitoring App Builder is a free AI prompt that generates production-ready monitoring dashbo…
