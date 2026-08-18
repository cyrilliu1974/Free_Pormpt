# Grocery List Generator From Meal Plan

## 簡介

The Grocery List Generator From Meal Plan is a free AI prompt that transforms meal plans into categorized, cost-estimated shopping lists for home cooks and meal planners. This grocery list prompt for ChatGPT extracts every ingredient from your weekly or monthly meal plan, groups items by food category (produce, proteins, dairy, grains, pantry staples), estimates costs based on typical pricing and seasonal availability, and organizes the list to follow standard grocery store layout so you shop efficiently. It accounts for household size to calculate quantities, flags conflicts with dietary restrictions, and suggests budget-friendly substitutions that preserve nutritional value. The output is a markdown table showing each meal, its ingredients with quantities, and itemized cost estimates, plus a total. Use it on ChatGPT, Claude, Gemini, or Grok. Reach for this prompt when you have a meal plan but need a shopping-ready list that respects your budget, dietary needs, and time. ● Extracts and categorizes all ingredients by food group for faster in-store navigation ● Estimates costs per meal and provides a total budget forecast ● Flags dietary restriction conflicts and recommends nutritionally equivalent substitutions ● Organizes items to match typical grocery store flow, reducing shopping time ## Prompt

```
## Role
You are an expert nutritionist and meal planner creating an optimized grocery list.

## Task
Analyze the provided meal plan and produce a complete grocery list that maximizes nutrition, budget efficiency, and shopping convenience.

## Process
1. Extract all ingredients from the meal plan
2. Group ingredients by food category (produce, proteins, dairy, grains, pantry staples, etc.)
3. Estimate costs based on typical pricing, considering seasonal availability
4. Identify cost-effective alternatives that maintain nutritional value
5. Organize the list to match standard grocery store flow (produce → dairy → meat → dry goods)
6. Account for household size to calculate appropriate quantities
7. Flag any conflicts with stated dietary restrictions

## Context
**Meal plan:** {{meal-plan}}

**Dietary restrictions:** {{dietary-restrictions}}

**Budget and household:** {{budget-and-household}}

## Output
Provide a markdown table with three columns:

| Meal | Ingredients | Estimated Cost |
|------|-------------|----------------|

Include:
- One row per meal with all ingredients listed
- Quantity indicators where relevant
- Itemized cost estimates
- A final row showing **Total Estimated Cost**

Below the table, note any recommended substitutions for budget or dietary needs.
```

## 用法 / Usage
- 必填變數 / Variables: {{budget-and-household}}、{{dietary-restrictions}}、{{meal-plan}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Grocery List Generator From Meal Plan is a free AI prompt that transforms meal plans into categorized, cos…
