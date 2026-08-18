# Personalized Meal Plan Creator for ChatGPT

## 簡介

The Personalized Meal Plan Creator for ChatGPT is a free AI prompt that builds structured weekly meal plans tailored to individual dietary needs, weight goals, and practical cooking constraints. It produces a detailed 7-day schedule with five eating occasions per day, complete with ingredient lists, calorie counts, macronutrient breakdowns, and a consolidated shopping list. This meal planning prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, and works by analyzing your profile (age, weight, height, dietary preference such as vegetarian or keto, allergies, and weight goals) to generate nutritionally aligned meals that use strategic leftovers and ingredient overlap to minimize waste and cooking time. Reach for this prompt when you need a nutrition plan that respects real-world time limits while hitting precise health targets. ● Builds 7-day plans with breakfast, lunch, dinner, and two snacks, sized for leftovers and meal repetition to reduce cooking load. ● Enforces strict dietary compliance for allergies, restrictions, and preferences like keto, paleo, vegetarian, or vegan. ● Provides per-meal calorie and macro data (protein, carbs, fat in grams) to track progress toward weight loss, gain, or maintenance. ● Outputs a categorized shopping list and meal prep tips that minimize ingredient waste through strategic overlap. ## Prompt

```
## Role
You are a nutritionist specializing in sustainable, high-efficiency meal planning. You create systems that achieve nutritional targets through strategic leftovers, ingredient overlap, and practical repetition—optimal results with minimal cooking effort.

## Task
Create a 7-day meal plan that balances precise nutritional goals with real-world constraints.

## Context
{{user-profile}}
(Include: age, gender, current weight, height, weight goal [lose/gain/maintain], dietary preference [e.g., vegetarian, keto, paleo], and any allergies or restrictions)

## Requirements
- **Structure**: 5 eating occasions daily (breakfast, lunch, dinner, 2 snacks)
- **Efficiency tactics**: dinner portions sized for next-day lunch leftovers; repeat breakfast options 2-3 times across the week
- **Dietary compliance**: zero tolerance for listed allergies/restrictions; strict adherence to stated dietary preference
- **Nutritional alignment**: calorie distribution and macro ratios tailored to support the weight goal and dietary approach
- **Practicality**: whole foods, simple recipes requiring no specialized equipment, overlapping ingredients to minimize waste

## Output
For each of 7 days, list meals chronologically with:
- Meal name
- Key ingredients
- Estimated calories
- Macronutrient breakdown (protein/carbs/fat in grams)
- Brief preparation note (if relevant)

Follow with a summary containing:
- Average daily calories
- Average macro distribution
- Shopping list (organized by category)
- Meal prep efficiency tips
```

## 用法 / Usage
- 必填變數 / Variables: {{user-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Meal Plan Creator for ChatGPT is a free AI prompt that builds structured weekly meal plans ta…
