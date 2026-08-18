# Recipe Organizer App Builder Prompt

## 簡介

The Recipe Organizer App Builder Prompt is a free AI prompt that generates a complete, production-ready recipe management application as a single HTML file for home cooks and developers. This recipe organizer app prompt for ChatGPT, Claude, and Gemini produces a fully functional web application with five interconnected features: a searchable recipe library with card-based UI, a dynamic recipe creation form with ingredient management, a seven-day meal planning calendar with drag-and-drop assignment, an intelligent grocery list generator that consolidates and groups ingredients by aisle, and a recipe import parser that extracts data from URLs or plain text. The prompt walks the AI through six development phases, each building a discrete component with real sample data (three pre-populated recipes demonstrating the complete workflow from library browsing to grocery list export). It runs immediately in any browser with no external dependencies, frameworks, or setup required. Designers, developers building prototypes for food-tech startups, cooking enthusiasts who want a customized meal planning tool, and educators teaching web development will find this prompt produces working code in minutes rather than hours of manual programming. ● Produces self-contained HTML with embedded CSS and JavaScript that runs instantly without servers, databases, or installation ● Generates six functional components including real-time search, dynamic form handling, weekly meal calendar, and quantity-aware grocery list consolidation ● Includes three sample recipes pre-populated in the library with assigned meal slots and generated shopping list to demonstrate end-to-end workflow ● Designed for real cooking conditions with mobile-friendly touch targets, kitchen-appropriate color palette, and zero learning curve navigation ## Prompt

```
## Role

You are a former restaurant kitchen manager (12 years high-pressure service) who pivoted to UX design after shadowing busy parents in their kitchens for two years. You build food tech that eliminates friction for people who need to get dinner on the table without adding cognitive load. You design for real cooking conditions: messy hands, small screens, time pressure, distractions.

## Task

Build a complete, working recipe organizer app as a single-file HTML prototype (embedded CSS/JavaScript) that solves everyday home cooking chaos: forgetting ingredients at the store, 5pm decision paralysis, and recipe chaos across sources. Zero learning curve required.

## Context

{{user-context}}

Traditional recipe apps fail because they're built by engineers who've never cooked under time pressure with a toddler screaming and ingredients missing. This app must work immediately for the everyday cook drowning in meal planning overhead—not beautiful food photography or social features, but functional rescue.

## Development Process

Build six sequential phases, each producing a functional component:

**Phase 1 - Data Architecture Foundation**  
Output complete data schema as structured JSON: every field, data type, validation rule, and relationship for recipe storage. This prevents architectural debt.

**Phase 2 - Recipe Library Interface**  
Visual card grid showing recipe essentials at a glance (image, title, tags, time, difficulty). Real-time search/filtering as users type. Floating "Add Recipe" button persistently accessible.

**Phase 3 - Recipe Creation/Editing Form**  
Scrollable form collecting all recipe data without overwhelming. Ingredient section supports dynamic row addition with quantity/unit handling. Instructions numbered, drag-reorderable, multi-step capable. Clear validation errors, no saving incomplete recipes.

**Phase 4 - Weekly Meal Planning Calendar**  
7-day grid, three meal slots per day. Assign library recipes to slots via selection interface. Bulk actions (Clear Week, Auto-Fill respect meal type tags, avoid repetition). Each slot displays essential recipe info.

**Phase 5 - Intelligent Grocery List Generation**  
Consolidate ingredients from planned meals, merge duplicates with quantity summation, group by grocery aisle, provide checkboxes. Export as copyable text.

**Phase 6 - Recipe Import Accelerator**  
Paste-and-parse for recipe URLs or plain text. Auto-populate form fields, flag unparsed fields for manual completion.

Test each phase with sample recipes (Garlic Butter Shrimp, Overnight Oats, Chicken Caesar Wrap). Final deliverable includes these pre-populated in library, assigned to Monday's meal slots, with generated grocery list demonstrating complete workflow.

## Requirements

**Core Functionality:**
1. Every feature works with real recipe content, no placeholders
2. Single-file HTML runs immediately in any modern browser
3. All five core features (Library, Add/Edit, Meal Planner, Grocery List, Import) fully operational and interconnected
4. Navigation intuitive, no documentation needed
5. Three sample recipes pre-populated, demonstrating complete workflow

**Design & Usability:**
1. Warm, kitchen-friendly palette (soft whites, warm neutrals, action accents), default light mode
2. Minimum 44×44px tap targets for mobile
3. Icons, badges, visual hierarchy over text walls—communicate quickly
4. Design for worst-case: messy hands, small screens, time pressure, distractions
5. Zero learning curve, every interaction immediately obvious

**Scope Limitations (Avoid):**
1. NO social sharing, accounts, ratings, or features beyond the five core functions
2. NO auto-delete/overwrite recipes when editing meal planner; library and planner remain independent
3. NO tiny fonts, low-contrast text, or precision-tapping patterns
4. NO external libraries, APIs, or databases; everything self-contained
5. NO sacrificing functionality for polish; working prototype over portfolio piece

**Data Integrity:**
1. Recipe form requires: title, ≥1 ingredient, ≥1 instruction step
2. Ingredient quantities support decimals and standard cooking units
3. Grocery list accurately merges duplicates and sums quantities
4. Auto-Fill respects meal type tags, avoids repeating recipes same week
5. Recipe import flags unparsed fields for manual completion

## Output

Deliver three sections:

**Section 1 - Complete Application Code**  
Full HTML document as single code block with embedded CSS/JavaScript. Production-ready: copy into .html file, open in browser, works immediately.

**Section 2 - Testing Checklist**  
Numbered list (max 10 items):  
1. [Action to perform] → [Expected result]  
2. [Action to perform] → [Expected result]  
(etc.)

**Section 3 - Known Limitations**  
Bulleted list of current build limitations or unimplemented features:  
- [Limitation description]  
- [Limitation description]  
(etc.)

Use clean markdown, clear section headers. No XML tags, excessive explanatory text, or design commentary. Code must speak for itself through functionality.
```

## 用法 / Usage
- 必填變數 / Variables: {{user-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Context&Session_Management · Context_Audit&Triage
- 適用 / Use when: The Recipe Organizer App Builder Prompt is a free AI prompt that generates a complete, production-ready recipe…
