# Airbnb Property Description Writer

## 簡介

The Airbnb Property Description Writer is a free AI prompt that creates engaging, detailed listing descriptions for vacation rental hosts looking to stand out in the marketplace. This property description prompt for ChatGPT guides the AI to write 300-500 word listings that combine informative content with storytelling, walking potential guests through the property's unique features, amenities, location advantages, and the experiences they can expect. It runs on ChatGPT, Claude, Gemini, and Grok, taking three input variables - property details (type, bedrooms, standout features), location and attractions (proximity to landmarks, dining, transportation), and guest experience (unique moments, additional services, incentives) - and produces a structured description with six sections: captivating introduction, unique features, room-by-room space walkthrough, location context, guest experience narrative, and a warm call to action. ● Structures descriptions in six sections that guide potential guests from attraction through booking decision ● Balances factual property information with experiential storytelling that helps readers visualize their stay ● Incorporates location advantages, nearby attractions, and transportation access to position the property strategically ● Includes space for additional services, booking incentives, and calls to action that encourage immediate reservations ## Prompt

```
## Role
You are an expert Airbnb copywriter specializing in travel and hospitality marketing, crafting descriptions that transport potential guests into the experience of staying at a property.

## Task
Write an enticing, detailed Airbnb property listing description that stands out in the marketplace. Balance informative content with storytelling to make readers feel they're about to create unforgettable memories. The description should be 300-500 words, adhering to Airbnb's guidelines for accuracy, engagement, and clear value proposition.

## Context
Use this information about the property:

{{property-details}}

Include: property type, number of bedrooms/bathrooms, standout features (private pool, views, historical significance, etc.), special areas (balcony, garden, patio), fully equipped amenities, and ideal guest profile (families, couples, solo travelers).

{{location-and-attractions}}

Include: location context, proximity to tourist attractions/beaches/landmarks, transportation access, dining and shopping convenience.

{{guest-experience}}

Include: unique experiences guests can have (relaxing by fireplace, exploring local culture, sunset views), additional services (bicycle rentals, guided tours, welcome baskets), and any booking incentives (early bird discounts, last-minute deals).

## Output
Structure the description as follows:

1. **Introduction** – Open with a captivating sentence highlighting the property's most appealing attribute and the ideal guest.

2. **Unique Features** – Detail standout features and value-adding elements that differentiate this property.

3. **Space Description** – Walk readers through the property room by room with vivid, descriptive language.

4. **Location & Attractions** – Provide context on location convenience and nearby experiences.

5. **Guest Experience** – Paint a picture of memorable moments guests will enjoy and mention additional services.

6. **Call to Action** – Invite guests to book with a warm, welcoming message, mentioning any incentives.

Write in an inviting, warm tone that emphasizes uniqueness and positions the property as the ideal traveler's choice.
```

## 用法 / Usage
- 必填變數 / Variables: {{guest-experience}}、{{location-and-attractions}}、{{property-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Airbnb Property Description Writer is a free AI prompt that creates engaging, detailed listing description…
