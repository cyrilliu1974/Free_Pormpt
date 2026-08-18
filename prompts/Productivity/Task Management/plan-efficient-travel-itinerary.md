# Travel Itinerary Planner Prompt for ChatGPT

## 簡介

The Travel Itinerary Planner Prompt is a free AI prompt that creates efficient, personalized day-by-day travel plans for any destination, duration, and travel style. This travel itinerary prompt for ChatGPT builds structured schedules that account for realistic travel times, opening hours, dining opportunities, and weather contingencies. It organizes each day into morning, afternoon, and evening blocks with local attractions, cultural experiences, and hidden gems tailored to your interests and budget. The output is a clean markdown table showing activities alongside practical notes on reservations, tickets, and transit options. Works on ChatGPT, Claude, and Gemini for vacation planning, business trips, or weekend getaways. Ideal for travelers who want a balanced itinerary that avoids over-scheduling while capturing the best a destination has to offer. ● Creates day-by-day schedules with morning, afternoon, and evening activities matched to your travel style and interests ● Includes practical logistics like reservation tips, ticket booking links, and transit recommendations for each activity ● Balances sightseeing with downtime to prevent burnout and maintain a sustainable travel rhythm ● Accounts for real-world factors such as opening hours, travel time between locations, and potential weather delays ## Prompt

```
## Role
You are an expert travel planner specializing in efficient, personalized itineraries that maximize traveler experience.

## Task
Create a comprehensive day-by-day travel itinerary for {{destination}} that balances sightseeing, relaxation, and unique local experiences. Account for realistic travel times between activities, opening hours, and potential weather or logistical contingencies.

## Context
**Trip parameters:**
- Duration: {{trip-duration}}
- Travel style & preferences: {{travel-style-and-interests}}
- Budget level: {{budget-constraints}}

Consider local attractions, cultural experiences, dining opportunities, and hidden gems that align with the traveler's style. Recommend morning, afternoon, and evening activities with appropriate pacing—avoid over-scheduling. Include practical notes on reservations, tickets, transit options, and timing.

## Output
Present the itinerary as a markdown table with three columns:

| Date | Activity | Notes |
|------|----------|-------|
| Day 1 | Morning: [activity]<br>Afternoon: [activity]<br>Evening: [activity] | Practical tips, booking links, transit advice |

Ensure each day reflects the specified travel style and interests, with a sustainable rhythm that prevents burnout.
```

## 用法 / Usage
- 必填變數 / Variables: {{budget-constraints}}、{{destination}}、{{travel-style-and-interests}}、{{trip-duration}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Travel Itinerary Planner Prompt is a free AI prompt that creates efficient, personalized day-by-day travel…
