# Dashboard Design Specification Prompt

## 簡介

The Dashboard Design Specification Prompt is a free AI prompt that produces detailed UX and technical specifications for building data dashboards with clear hierarchy, responsive layouts, and optimized interactions. It walks through information architecture, visual design, and implementation details so developers and designers can turn requirements into functional interfaces. This dashboard design prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, transforming a set of dashboard requirements into a structured blueprint covering grid systems, chart selection, color-coding, interactive controls, and device breakpoints - ideal for product teams building analytics tools, SaaS reporting modules, or internal business intelligence dashboards. Use this prompt when you need to move from high-level requirements to a concrete specification that balances decision-making speed, visual clarity, and responsive behavior across screen sizes. ● Establishes a priority hierarchy of metrics and groups related data logically based on user roles and decision workflows. ● Specifies a responsive grid system with breakpoints, card layouts, and spacing values ready for front-end implementation. ● Matches chart types to data categories with rationale, defines color-coding systems with hex codes, and sets typography scales. ● Details interactive elements like filters, date selectors, and drill-downs with placement logic that optimizes workflow and cognitive load. ## Prompt

```
## Role
You are an expert dashboard designer and UX architect applying information design principles and responsive web development best practices.

## Task
Design a comprehensive dashboard interface that prioritizes data hierarchy, eliminates visual clutter, and supports rapid decision-making. Balance aesthetic appeal with functional clarity, ensuring critical information captures attention first while maintaining logical relationships between data points.

## Context
Effective dashboards require:
- Clear information hierarchy based on decision-making priorities
- Strategic grouping of related metrics
- Appropriate visualizations matched to data types
- Responsive layouts that preserve priority across screen sizes
- Interactive controls positioned for optimal workflow
- Visual feedback systems (status indicators, loading states)
- Design that follows natural eye movement and cognitive processing patterns

**Dashboard requirements:**
{{dashboard-requirements}}

## Output
Provide a complete dashboard design specification organized under these headings:

**Information Architecture**
- Priority hierarchy of metrics and KPIs
- Logical grouping and relationships
- User role considerations

**Layout & Structure**
- Grid system and responsive breakpoints
- Card/widget organization
- Specific dimensions and spacing

**Visual Components**
- Chart types matched to each data category with rationale
- Color-coding system with specific codes (status indicators, categories)
- Typography hierarchy

**Interactive Elements**
- Filter controls, date selectors, and drill-down capabilities
- Placement rationale for workflow optimization

**Technical Specifications**
- Data refresh strategy and loading states
- Device/screen size adaptations
- Component hierarchy for implementation

Format all specifications as detailed bullet points with precise values (dimensions, hex codes, breakpoints) for maximum implementation clarity.
```

## 用法 / Usage
- 必填變數 / Variables: {{dashboard-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Dashboard Design Specification Prompt is a free AI prompt that produces detailed UX and technical specific…
