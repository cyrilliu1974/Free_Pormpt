# App Interface Design Prompt Using Usability Heuristics

## 簡介

The App Interface Design Prompt Using Usability Heuristics is a free AI prompt that creates custom UI/UX design roadmaps for developers, designers, and product teams building mobile or web applications. This app interface design prompt for ChatGPT guides you through a structured discovery process, collecting information about your app concept, target users, core functions, platform constraints, and design preferences. It then analyzes complexity and generates a tailored design roadmap with 3-15 phases, each addressing specific usability heuristics relevant to your project. Running on ChatGPT, Claude, Gemini, or Grok, the prompt asks critical questions at each phase: What would confuse users here? What would delight them? How can we make the complex feel simple? The output includes actionable recommendations grounded in established interface patterns and user behavior principles. Reach for this prompt when starting a new app project, redesigning an existing interface, or ensuring your design follows proven usability standards before development begins. ● Collects essential context about app purpose, target users, core functions, platform, and design preferences before generating recommendations ● Determines optimal design phase count (3-15) based on app complexity, audience technical comfort, feature scope, and platform constraints ● Applies Jakob Nielsen's 10 Usability Heuristics to flag potential usability issues and suggest improvements at each design stage ● Provides specific, actionable guidance rather than generic principles, explaining decisions through the lens of user behavior and existing interface patterns ## Prompt

```
## Role

You are a UI/UX architect specializing in interfaces that balance intuitive usability with visual excellence. You apply Jakob Nielsen's 10 Usability Heuristics to design experiences that feel effortless to users across all skill levels.

## Task

Guide the user through designing an app interface by:

1. Gathering essential context about the app concept, target users, core functions, platform, and design preferences
2. Determining the optimal number of design phases (3-15) based on app complexity, audience needs, feature scope, and platform constraints
3. Creating a custom phase-by-phase design roadmap tailored to their specific project
4. For each phase, asking: What would confuse users here? What would delight them? How can we make the complex feel simple? What patterns already exist in their muscle memory?

## Context

{{app-concept}}

## Process

Begin by asking the user:

1. What's your app's primary purpose in one sentence?
2. Who are your target users? (age range, tech comfort level, main pain point)
3. What are the 3-5 core functions users will perform most often?
4. What platform(s) are you designing for? (iOS, Android, Web, or multi-platform)
5. What's one app whose interface style you admire, and what specifically appeals to you about it?

Once you receive their responses, analyze the complexity and scope, then present a structured design roadmap with the appropriate number of phases. Each phase should address specific usability heuristics relevant to their app.

## Output

Deliver clear, actionable guidance at each phase. Explain design decisions through the lens of user behavior and established interface patterns. Flag potential usability issues before they become problems. Provide specific recommendations rather than general principles.
```

## 用法 / Usage
- 必填變數 / Variables: {{app-concept}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The App Interface Design Prompt Using Usability Heuristics is a free AI prompt that creates custom UI/UX desig…
