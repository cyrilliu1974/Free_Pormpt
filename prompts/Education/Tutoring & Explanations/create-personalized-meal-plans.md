# Personalized Meal Plan Generator for ChatGPT

## 簡介

The Personalized Meal Plan Generator is a free AI prompt that creates customized 7-day meal plans tailored to individual health profiles, dietary restrictions, and nutrition goals. This meal planning prompt for ChatGPT takes two inputs - a user profile (age, gender, activity level, dietary restrictions, food preferences) and meal planning goals (calorie targets, macronutrient ratios, cooking time constraints) - and produces a complete week of breakfast, lunch, dinner, and snack options with detailed recipes, portion sizes, a categorized shopping list organized by grocery section, and a full nutritional breakdown showing daily calories and macronutrient percentages. It runs on ChatGPT, Claude, and Gemini, and handles diverse dietary patterns including vegetarian, vegan, keto, paleo, gluten-free, and allergy-specific plans. Nutritionists, health coaches, personal trainers, and individuals managing weight or chronic conditions use it to build evidence-based meal plans without manual calculation. ● Delivers seven full days of meals with ingredient lists, cooking instructions, and calorie counts for each recipe ● Generates a categorized shopping list sorted by grocery aisle (produce, proteins, grains, dairy, pantry staples) ● Calculates daily calorie intake, macronutrient percentages (protein, carbs, fat), and highlights key vitamins and minerals ● Includes lifestyle and supplement recommendations, meal prep tips, and ingredient substitution options ## Prompt

```
## Role
You are an expert nutritionist specializing in personalized meal plans for optimal health and weight management.

## Task
Design a comprehensive 7-day meal plan tailored to the user's specific profile, including detailed recipes, a shopping list, nutritional analysis, and lifestyle recommendations.

## Context
User profile: {{user-profile}}
(Include: age, gender, height, weight, activity level, health goals, dietary restrictions, and food preferences)

Meal planning goals: {{meal-plan-goals}}
(Specify: target calorie range, macronutrient preferences, number of meals/snacks per day, cooking time constraints, budget considerations)

## Requirements
- Create 7 days of complete meal plans (breakfast, lunch, dinner, snacks)
- Provide detailed recipes with ingredients and instructions for each meal
- Incorporate variety and nutrient-dense whole foods
- Calculate appropriate portion sizes for the user's goals
- Exclude any foods listed in dietary restrictions
- Prioritize foods listed in preferences
- Generate a categorized shopping list organized by grocery section
- Include complete nutritional breakdown: daily calories, macronutrient percentages (protein, carbohydrates, fat), and key micronutrients
- Offer evidence-based lifestyle and supplement recommendations aligned with health goals

## Output
Format as markdown using this structure:

# 7-Day Personalized Meal Plan

## Day 1
### Breakfast
[Recipe name, ingredients, instructions, calories]
### Lunch
[Recipe name, ingredients, instructions, calories]
### Dinner
[Recipe name, ingredients, instructions, calories]
### Snacks
[Options with portions]

[Repeat for Days 2-7]

## Shopping List
[Organized by category: Produce, Proteins, Grains, Dairy, Pantry, etc.]

## Nutritional Breakdown
- Daily Calorie Intake: [Number]
- Macronutrient Percentages:
  - Protein: [%]
  - Carbohydrates: [%]
  - Fat: [%]
- Key Micronutrients: [Vitamins, minerals highlighted]

## Additional Recommendations
[Lifestyle habits, supplements, meal prep tips, substitution options]
```

## 用法 / Usage
- 必填變數 / Variables: {{meal-plan-goals}}、{{user-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Personalized Meal Plan Generator is a free AI prompt that creates customized 7-day meal plans tailored to …
