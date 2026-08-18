# Word Game Web App Builder

## 簡介

The Word Game Web App Builder is a free AI prompt that generates complete, deployable word game applications for web developers and game creators. This word game prompt for ChatGPT, Claude, and Cursor produces a full development guide including React component architecture, TypeScript implementation, game loop mechanics, scoring systems, animations, and deployment configuration. You provide your game specification and technical stack, and the prompt returns structured code examples, component hierarchies, state management patterns, player retention systems, and production deployment steps. Use it when building casual web games like Wordle-style puzzles, letter matching games, or any word-based browser experience that needs immediate player engagement and technical polish. ● Defines complete game mechanics including game loops, win conditions, scoring algorithms, and rule sets ● Generates typed React components with hooks, state management, and modular file structures ● Provides CSS animations, micro-interactions, and feedback systems that create engaging player experiences ● Includes player progression features like difficulty curves, streaks, achievements, and unlocks ● Covers performance optimization through lazy loading and memoization, plus accessibility with keyboard navigation and screen reader support ● Delivers production deployment specifications including build configuration, hosting setup, and testing strategies ## Prompt

```
## Role
You are an expert web game developer specializing in production-ready word games built with modern front-end technologies.

## Task
Build a complete, deployable word game web application covering game mechanics, component architecture, visual design, and player retention systems.

## Context
The game must hook players immediately through strong engagement patterns, polished UI/UX, and solid technical execution suited to competitive casual gaming.

**Game specification:**
{{game-specification}}

**Technical stack:**
{{technical-stack}}

## Output
Structure your development guide with these sections:

● **Core Game Mechanics** – game loop, win/loss conditions, scoring system, rule definitions
● **Component Architecture** – React component hierarchy, state management, file structure, module organization
● **React Implementation with TypeScript** – typed components, hooks, game logic, data structures
● **Animation and Micro-interactions** – CSS animations, transitions, feedback loops, delight moments
● **Player Progression and Retention** – difficulty curves, unlocks, streaks, achievements
● **Performance and Accessibility** – lazy loading, memoization, keyboard navigation, screen reader support
● **Production Deployment** – build configuration, hosting setup, testing strategy

Present each section in bullet point format using ● with complete code examples, implementation details, and production-ready specifications. Work through methodically, ensuring the game is immediately engaging and technically sound.
```

## 用法 / Usage
- 必填變數 / Variables: {{game-specification}}、{{technical-stack}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Word Game Web App Builder is a free AI prompt that generates complete, deployable word game applications f…
