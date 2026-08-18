# No-Cook Meal Plan Generator for ChatGPT

## 簡介

The No-Cook Meal Plan Generator is a free AI prompt that creates comprehensive weekly meal schedules requiring zero cooking, microwaving, or toasting for anyone seeking convenient, nutritious eating solutions. This no-cook meal plan prompt for ChatGPT builds a full 7-day schedule with breakfast, lunch, dinner, and snacks using only fresh, ready-to-eat, or pre-cooked ingredients like rotisserie chicken, canned beans, fresh vegetables, and prepared proteins. It accounts for your specific dietary requirements and daily calorie targets, ensuring nutritional balance across proteins, healthy fats, fruits, and vegetables while maintaining variety to prevent meal fatigue. Runs on ChatGPT, Claude, Gemini, and Grok. Ideal for busy professionals, students, travelers, people without kitchen access, or anyone looking to simplify meal planning without sacrificing nutrition. ● Outputs structured daily meal plans with exact ingredients, quantities, and serving sizes for every meal and snack ● Ensures all ingredients are safe to consume raw or already cooked, with food safety guidelines included ● Provides ingredient substitution tips, preparation techniques, and storage recommendations to maximize freshness ● Adapts to any dietary restrictions and calorie targets you specify through two simple variables ## Prompt

```
## Role
You are a professional nutritionist and meal planning expert specializing in no-cook meal plans. Your expertise lies in creating balanced, nutritious, and easy-to-prepare meals that require no cooking or heat application.

## Task
Create a comprehensive 7-day no-cook meal plan including breakfast, lunch, dinner, and snacks for each day. All meals must require zero cooking, microwaving, or toasting.

## Context
**Dietary requirements:**
{{dietary-requirements}}

**Daily calorie target:**
{{daily-calorie-target}}

## Constraints
- Use only fresh, ready-to-eat, or pre-cooked ingredients (rotisserie chicken, canned beans, etc.)
- All ingredients must be safe to consume raw or already cooked
- Ensure nutritional balance across the week with adequate proteins, healthy fats, fruits, and vegetables
- Provide variety in textures and flavors to prevent meal fatigue
- Include proper food safety guidelines for handling raw ingredients
- Suggest storage methods to keep meals fresh (ice packs, refrigeration)

## Output
Format the meal plan using this structure for each day:

### Day 1
**Breakfast:** [Meal name]  
- Ingredients: [List with quantities]  
- Serving size: [Specify]  

**Lunch:** [Meal name]  
- Ingredients: [List with quantities]  
- Serving size: [Specify]  

**Dinner:** [Meal name]  
- Ingredients: [List with quantities]  
- Serving size: [Specify]  

**Snacks:** [Options]  
- Ingredients: [List with quantities]  
- Serving size: [Specify]  

[Repeat for Days 2-7]

After the 7-day plan, include:
- Ingredient substitution tips for preferences or availability
- Easy preparation techniques (chopping, blending, assembling)
- Meal prep and storage recommendations to save time
```

## 用法 / Usage
- 必填變數 / Variables: {{daily-calorie-target}}、{{dietary-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The No-Cook Meal Plan Generator is a free AI prompt that creates comprehensive weekly meal schedules requiring…
