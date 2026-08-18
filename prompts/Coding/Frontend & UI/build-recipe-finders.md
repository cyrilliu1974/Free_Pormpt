# Recipe Finder App Front-End Blueprint Prompt

## 簡介

The Recipe Finder App Front-End Blueprint Prompt is a free AI prompt that generates a step-by-step technical guide for building a feature-rich recipe discovery and meal planning application using only front-end technologies. This recipe finder prompt for ChatGPT produces a structured implementation blueprint covering architecture, UI/UX design systems, advanced search algorithms, offline-first data strategies, meal planning calendars, nutrition dashboards, and cooking mode interfaces. You specify your coding experience level, preferred recipe API (Spoonacular, Edamam, TheMealDB), and target audience, and the prompt returns a phased development roadmap with code examples, component structures, and performance optimization techniques. It runs on ChatGPT, Claude, Gemini, and Grok, adapting the technical depth and explanations to match your skill level while maintaining professional front-end architecture standards. Reach for this prompt when you need to build a modern recipe application without backend infrastructure, whether you're a junior developer learning API integration or an experienced engineer prototyping a food-tech MVP. ● Outputs a 12-section technical guide covering API integration, offline-first service workers, IndexedDB persistence, responsive design systems, and accessibility compliance ● Includes implementation logic for advanced search with multi-parameter filtering, dynamic serving size calculators, drag-and-drop meal planning calendars, and hands-free cooking mode ● Provides phased development roadmaps separating MVP features from advanced enhancements, with complexity rankings and performance optimization strategies ● Delivers food-photography-driven design recommendations including appetite-optimized color palettes, typography hierarchies, and responsive grid layouts ## Prompt

```
## Role

You are an expert front-end architect and food-tech UX specialist building a complete recipe finder application that combines discovery, personalization, meal planning, and practical cooking assistance.

## Task

Create a comprehensive technical implementation blueprint for a feature-rich recipe application that transforms API data into an engaging cooking companion. Deliver a structured, step-by-step development guide covering architecture, UI/UX, and advanced features—all implementable without backend infrastructure.

## Context

**User requirements:**
- Coding experience level: {{coding-experience}}
- Preferred recipe API: {{recipe-api}}
- Target audience: {{target-audience}}
- Design preferences: modern, appetite-driven visuals with large food photography, warm accent colors, and clean responsive grid (recommend specific palette and typography if none specified)
- Development approach: phased build with functional MVP first, advanced features layered incrementally

**Technical constraints:**
Front-end only application using the specified API, offline-first architecture, no custom backend required.

## Output

Provide an implementation guide organized into these sections:

**1. Architecture & Technology Stack**
- API integration strategy and data management
- Offline-first architecture with service workers
- Local storage and IndexedDB implementation
- State management patterns

**2. Visual Design System**
- Food photography integration best practices
- Recommended color palette optimized for appetite appeal
- Typography hierarchy for readability
- Responsive grid layouts and component library structure

**3. Advanced Search & Filtering Engine**
- Multi-parameter search (ingredients, cuisine, dietary restrictions, prep time)
- Real-time filtering logic and algorithms
- Search result optimization and performance

**4. User Rating & Review System**
- Star rating component implementation
- Review submission forms and validation
- Rating aggregation algorithms
- Content moderation considerations

**5. Nutritional Information Dashboard**
- API data parsing for calories, macros, and allergens
- Visual indicators (progress bars, pie charts)
- Allergen warning system with iconography

**6. Recipe Collection Management**
- Save functionality with localStorage/IndexedDB
- Categorization and tagging system
- Collection CRUD operations and data persistence

**7. Meal Planning Calendar**
- Drag-and-drop implementation
- Calendar grid structure and recipe scheduling logic
- Weekly/monthly view toggles

**8. Dynamic Serving Size Calculator**
- Mathematical recalculation functions
- Ingredient quantity adjustment algorithms
- Real-time UI updates

**9. Interactive Cooking Mode**
- Step-by-step instruction interface
- Built-in timer with notifications
- Hands-free navigation and progress tracking

**10. Offline Functionality**
- Service worker setup and caching strategies
- Sync mechanisms for saved recipes
- Offline-first data architecture

**11. Social Sharing Integration**
- Web Share API implementation
- Platform-specific meta tags for rich previews
- Recipe card image generation

**12. Code Structure & Best Practices**
- File organization and component architecture
- Performance optimization techniques
- Accessibility standards (WCAG compliance)

**Format:** Present as structured bullet points with code examples, implementation priorities ranked by complexity, and a phased development roadmap showing MVP features versus advanced enhancements.
```

## 用法 / Usage
- 必填變數 / Variables: {{coding-experience}}、{{recipe-api}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Recipe Finder App Front-End Blueprint Prompt is a free AI prompt that generates a step-by-step technical g…
