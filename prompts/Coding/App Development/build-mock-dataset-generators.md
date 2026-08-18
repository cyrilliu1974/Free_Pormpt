# Build Mock Dataset Generators

## 簡介

The Build Mock Dataset Generators prompt is a free AI prompt that produces a full-stack TypeScript React application for generating realistic, culturally authentic mock datasets suitable for investor demos, client presentations, and application testing. This mock dataset generator prompt for ChatGPT, Claude, and Cursor delivers production-ready code with a professional Linear.app-inspired UI, Faker.js integration for locale-aware data generation, and multi-format export capabilities including JSON, CSV, and SQL. The generated application features a configuration interface, live preview panel with real-time updates, syntax highlighting, and advanced options for edge cases, null values, and relational data. Real use cases include building demo environments with believable customer data, populating test databases with properly distributed values, and creating presentation-ready datasets that pass technical scrutiny. Reach for this prompt when you need to scaffold a complete data generation tool rather than writing one-off mock data scripts, or when your datasets must reflect regional nuances and statistical realism for stakeholder presentations. ● Outputs complete TypeScript React code with proper hooks, type definitions, and Tailwind CSS styling for immediate deployment. ● Integrates Faker.js with cultural authenticity controls to generate datasets with realistic formatting, proper statistical distributions, and regional nuances. ● Includes multi-format export functions (JSON, CSV, SQL) with syntax highlighting and one-click copy for seamless workflow integration. ● Provides advanced data generation features including edge case handling, null value simulation, relational data support, and pre-built templates for common schemas. ## Prompt

```
## Role

You are an expert data architect and full-stack developer building a production-ready mock data generator.

## Task

Build a complete TypeScript React application that generates realistic, culturally authentic datasets suitable for investor demos, client presentations, and application testing.

**Core Components**
- Configuration interface (left sidebar, 35% width) for dataset building
- Live preview panel (right side, 65% width) with real-time updates
- Multi-format export tabs with syntax highlighting and one-click copy
- Smart data generation engine using Faker.js with proper statistical distributions and cultural authenticity
- Advanced options: edge cases, null values, relational data, and pre-built templates
- Professional UI styled with Tailwind CSS (Linear.app-inspired design)
- Performance-optimized rendering with batch generation for large datasets

**Data Generation Requirements**

{{requirements}}

## Output

Provide complete, production-ready code including:
- TypeScript interfaces and type definitions
- React components with proper hooks (useState, useEffect, useMemo)
- Tailwind CSS styling classes
- Faker.js integration with locale-aware generation
- Export functions for all specified formats
- Commented code explaining key architectural decisions

Ensure the application generates data that passes scrutiny from technical and business stakeholders with realistic formatting, proper distributions, and regional nuances.
```

## 用法 / Usage
- 必填變數 / Variables: {{requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Build Mock Dataset Generators prompt is a free AI prompt that produces a full-stack TypeScript React appli…
