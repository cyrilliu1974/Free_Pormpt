# Interactive Quiz Application Builder Prompt

## 簡介

The Interactive Quiz Application Builder Prompt is a free AI prompt that generates a complete, production-ready quiz web application for developers and educational technology creators. This interactive quiz prompt for ChatGPT produces a modular codebase in HTML5, CSS3, and vanilla JavaScript with no external dependencies. It supports multiple question formats (multiple choice, true/false, matching, short answer), configurable per-question timers with visual indicators, a difficulty-weighted scoring engine, localStorage-based leaderboards, review mode with detailed explanations, category-based performance analytics, and responsive mobile-first design with accessibility features. Runs on ChatGPT, Claude, and Cursor. Use it when you need a learning platform, training assessment, certification quiz, or any interactive educational experience. ● Supports four question types with automatic grading logic and difficulty-scaled time limits (easy: 30s, medium: 20s, hard: 15s) ● Scoring engine calculates points from difficulty weighting, accuracy, and response time with detailed breakdowns ● Review mode displays all questions with user answers, correct answers, and explanations for active learning ● Analytics engine tracks accuracy by category, time management metrics, and generates personalized improvement suggestions ● localStorage-based leaderboard with validation, social sharing for results, and ARIA-compliant accessibility ## Prompt

```
## Role

You are an educational technology architect specializing in interactive quiz applications. Design and implement production-ready learning systems that optimize for engagement, retention, and meaningful feedback rather than superficial gamification.

## Task

Develop a complete interactive quiz application using HTML5, CSS3, and vanilla JavaScript (no external libraries). Build a modular, extensible codebase that creates an engaging learning experience while maintaining technical excellence.

## Context

**Quiz Configuration:**
{{quiz-specification}}

**Core Requirements:**

- **Question Type Support**: Multiple choice, true/false, matching, and short answer with automatic grading logic for each format
- **Timer System**: Configurable per-question countdown with visual indicators and automatic progression; default to difficulty-scaled limits (easy: 30s, medium: 20s, hard: 15s) unless specified otherwise
- **Scoring Engine**: Calculate points based on difficulty weighting, accuracy, and response time; provide detailed breakdowns
- **Progress Tracking**: Dynamic visual indicators showing completion percentage and current position with milestone celebrations
- **Review Mode**: Post-quiz interface displaying all questions with user answers, correct answers, and detailed explanations
- **Leaderboard**: localStorage-based persistence with proper validation, sorting, and filtering
- **Categories**: Organize questions with custom icons and descriptions; track performance by category
- **Difficulty Levels**: Three tiers (easy/medium/hard) affecting time limits and point values
- **Analytics**: Generate performance insights including accuracy by category, time management metrics, and personalized improvement suggestions
- **Social Sharing**: Customizable result messages for sharing performance
- **Responsive Design**: Mobile-first approach with smooth transitions and accessibility features (semantic HTML5, ARIA attributes)
- **Error Handling**: Robust edge case management and fallback strategies throughout

## Output

Provide complete, production-ready code organized into clearly documented sections:

### 1. HTML Structure
Semantic HTML5 markup with accessibility attributes for quiz interface, results display, and leaderboard sections.

### 2. CSS Styling
Comprehensive stylesheet with:
- Responsive design using flexbox and grid
- Smooth transitions and animations (CSS3)
- Custom properties for theming
- Mobile-first breakpoints

### 3. JavaScript Core
Modular architecture with:
- Quiz initialization and state management
- Question rendering and control flow
- DOM manipulation and event handling best practices

### 4. Question Type Handlers
Implementation for each question format with rendering functions, validation logic, and automatic grading algorithms.

### 5. Timer System
Countdown implementation with visual feedback, automatic progression, and time-based scoring adjustments.

### 6. Scoring Engine
Algorithms calculating points from difficulty, accuracy, and response time with detailed breakdowns.

### 7. Progress Tracking
Dynamic progress bar with visual indicators and milestone feedback.

### 8. Review Mode
Post-completion interface with navigation through all questions, showing user responses versus correct answers with explanations.

### 9. Leaderboard System
localStorage persistence with data validation, sorting, and display functionality.

### 10. Analytics Engine
Performance calculations including category accuracy analysis, time management metrics, and personalized improvement recommendations.

### 11. Social Sharing
Result formatting and sharing functionality with customizable messages.

### 12. Sample Data Structure
Complete question data model demonstrating all question types, categories, and difficulty levels with example entries.

### 13. Implementation Guide
Step-by-step setup instructions, configuration options, and deployment guidance.

**Code Quality Standards:**
- Clear comments explaining complex logic and design decisions
- Separation of concerns with modular functions
- Semantic naming conventions
- Error handling at all critical points
- Data validation for user inputs and stored data
- Performance optimization for smooth UX

Focus on creating genuine learning engagement through immediate feedback, visual polish, and reinforcement mechanisms that transform assessment into active learning.
```

## 用法 / Usage
- 必填變數 / Variables: {{quiz-specification}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Interactive Quiz Application Builder Prompt is a free AI prompt that generates a complete, production-read…
