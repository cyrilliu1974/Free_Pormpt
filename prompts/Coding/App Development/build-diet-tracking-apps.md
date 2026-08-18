# Diet Tracking App Development Prompt

## 簡介

The Diet Tracking App Development Prompt is a free AI prompt that generates complete, production-ready progressive web applications for developers building calorie tracking and nutrition tools. This diet tracking app prompt for ChatGPT delivers full-stack code with TypeScript interfaces, state management, data persistence, and behavioral design patterns that reduce user friction. Running on ChatGPT, Claude, or Cursor, it produces a single-artifact application with meal logging, macro visualization, streak tracking, and PWA capabilities including service workers and offline support. Developers use it to build health apps that prioritize habit formation over feature bloat, applying behavioral psychology principles that keep users engaged beyond the typical 3-day dropout window. It outputs complete file structures, dependencies, configuration, and inline comments explaining friction-reduction decisions. Reach for this prompt when you need to ship a calorie tracking app quickly without sacrificing user experience, or when building health tech that must balance simplicity with powerful analytics. ● Outputs complete application architecture with TypeScript, state management, and data persistence layer ready to deploy ● Includes dashboard with circular progress trackers, macro breakdowns, and real-time calorie updates ● Delivers meal logging with smart search, quick-add shortcuts, and intuitive input flows that minimize data-entry friction ● Generates history views, calendar tracking, streak counters, and motivational progress charts that encourage habit formation ● Provides PWA manifest, service worker, smooth animations, micro-interactions, and WCAG accessibility standards ## Prompt

```
## Role
You are a full-stack developer specializing in behavioral design and progressive web applications.

## Task
Build a complete, production-ready calorie tracking PWA that minimizes friction and maximizes retention through behavioral psychology principles. Prioritize effortless interaction over feature bloat.

## Context
Most diet apps fail within days due to overwhelming interfaces and complexity. This app must learn from those failures: make healthy habits feel natural, not burdensome.

{{app-specification}}
Provide the app name, core concept, target user demographics and behavior patterns, key features, and user flow priorities.

{{tech-stack}}
Specify your preferred technology stack, development constraints, design aesthetic, and brand identity direction.

## Output
Deliver a complete, runnable single-artifact application with:

**Architecture**
- Full file structure, dependencies, and configuration
- TypeScript interfaces, state management, and data persistence layer

**Core Features**
- Dashboard: circular progress tracker, macro visualization, real-time updates
- Meal logging: smart search, quick-add shortcuts, intuitive input
- History & analytics: calendar view, streak tracking, motivational progress charts

**UX Layer**
- Smooth animations, micro-interactions, encouraging feedback
- Performance optimization, WCAG accessibility, PWA manifest and service worker

Include inline comments explaining complex logic and behavioral design decisions that reduce friction and support habit formation.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-specification}}、{{tech-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Diet Tracking App Development Prompt is a free AI prompt that generates complete, production-ready progres…
