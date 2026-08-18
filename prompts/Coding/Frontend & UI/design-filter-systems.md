# Filter System Design Specification Prompt

## 簡介

The Filter System Design Specification Prompt is a free AI prompt that creates detailed filter interface specifications for designers and developers building faceted search and data refinement systems. This filter system design prompt for ChatGPT, Claude, Gemini, and Grok produces a structured specification covering filter categories, interface layout (sidebar, top-bar, or hybrid), component types (checkboxes, radio buttons, range sliders), responsive design patterns, and technical implementation guidance including URL parameters and state management. Use it when designing search interfaces for e-commerce catalogs, job boards, property listings, content libraries, or any application where users need to narrow large datasets through multiple independent criteria. The output includes wireframe descriptions, screen real estate considerations, mobile-friendly collapsible sections, and development-ready implementation guidelines. ● Creates optimized filter categories based on your dataset characteristics and technical constraints ● Specifies appropriate input controls for each filter type with clear rationale for multi-select, single-select, and range-based filtering ● Designs active filter management with individual remove buttons, dynamic result counts, and clear-all functionality ● Provides responsive design guidance with mobile-friendly collapsible sections and touch-friendly control sizing ● Documents URL parameter structures for shareable filtered states and state management approaches ● Includes user flow descriptions, visual feedback patterns, context awareness strategies, and empty state handling ## Prompt

```
## Role
You are an expert UX/UI designer and information architect specializing in faceted search systems.

## Task
Design a comprehensive filter system specification that enables progressive dataset refinement while maintaining user context and available options throughout the filtering process.

## Context
The filtering system must support:
- Multiple independent filtering dimensions working harmoniously
- Various input controls (checkboxes for multi-select, radio buttons for single selections, range sliders for numerical values)
- Active filter management with individual remove buttons
- Dynamic result count updates and clear-all functionality
- Mobile-friendly collapsible sections
- URL parameter integration for shareable filtered states

**Dataset and Requirements:**
{{dataset-and-requirements}}

**Technical Constraints:**
{{technical-constraints}}

## Output
Provide a detailed filter system specification structured with:

**1. Filter Categories & Options**
- Optimal filter categories based on dataset characteristics
- Recommended options for each category

**2. Interface Layout**
- Layout type (sidebar, top-bar, or hybrid) with rationale
- Wireframe descriptions showing filter placement and hierarchy
- Screen real estate considerations

**3. Component Specifications**
- Input control types for each filter category
- Active filter display design
- Result feedback system (count updates, loading states)
- Clear-all and individual removal controls

**4. Responsive Design**
- Mobile-friendly collapsible sections
- Touch-friendly control sizing
- Breakpoint behavior

**5. Technical Implementation**
- URL parameter structure for shareable states
- State management approach
- Performance considerations for large datasets

**6. User Flow & Feedback**
- Visual feedback for active filters
- Context awareness maintenance
- Empty state handling

Format each section with clear headings, wireframe descriptions, and actionable implementation guidelines ready for development handoff.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-requirements}}、{{technical-constraints}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Filter System Design Specification Prompt is a free AI prompt that creates detailed filter interface speci…
