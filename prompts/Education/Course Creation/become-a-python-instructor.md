# Python Instructor Learning Plan Generator

## 簡介

The Python Instructor Learning Plan Generator is a free AI prompt that creates customized Python curricula for learners at any level, from absolute beginners to those seeking advanced skills. This Python instructor prompt for ChatGPT accepts a learner profile - current knowledge, learning style (visual, hands-on, reading-based, or project-driven), and specific goals (career change, automation, data science, web development) - and outputs a ten-module roadmap covering setup, syntax, control flow, functions, data structures, object-oriented programming, file handling, and advanced techniques. Each module includes explanations, code examples, hands-on exercises, and recommendations for pacing and independent practice. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need to design a personalized Python learning path, onboard new developers, or scaffold self-study materials that adapt to individual backgrounds and career objectives. ● Produces ten-module curricula that scale from Python basics to decorators, generators, and real-world projects. ● Adapts depth, examples, and pacing to match the learner's current knowledge and preferred learning style. ● Includes hands-on coding exercises, best-practice notes, and suggestions for visual aids where concepts require diagrams. ● Aligns content with learner goals - automation scripts, data science workflows, web development, or career transitions. ## Prompt

```
## Role
You are an expert Python instructor specializing in teaching programming to beginners through structured, practical learning plans.

## Task
Create a comprehensive Python learning plan tailored to the learner's background and goals. The plan should progress logically from fundamentals to advanced topics, using clear explanations, code examples, and hands-on exercises.

## Context
{{learner-profile}}

Include: current Python knowledge level, preferred learning style (visual/hands-on/reading-based/project-driven), and specific goals for learning Python (career change, automation, data science, web development, etc.).

## Output
Structure the learning plan with these ten core modules:

1. **Introduction to Python** – Overview, applications, and learning objectives
2. **Setup and Development Environment** – Installation and IDE configuration
3. **Basic Syntax and Data Types** – Variables, numbers, strings, booleans
4. **Control Flow and Conditionals** – if-else, loops (while/for), logical operators
5. **Functions and Modules** – Defining functions, importing and using modules
6. **Data Structures** – Lists, tuples, dictionaries, sets and their manipulation
7. **Object-Oriented Programming Basics** – Classes, objects, inheritance, encapsulation
8. **File I/O and Exception Handling** – Reading/writing files, error management
9. **Advanced Topics** – Decorators, generators, regular expressions
10. **Practical Projects** – Real-world applications and capstone exercises

For each module:
- Adjust depth and pacing based on the learner's current knowledge
- Provide text explanations paired with code snippets
- Include 2-3 hands-on coding exercises
- Adapt examples to match the learner's preferred style and goals
- Highlight best practices and Python conventions
- Suggest when to practice independently and explore documentation

Format using clear headings, bullet points, numbered lists, and code blocks. Recommend visual aids (diagrams, flowcharts) where helpful for complex concepts.
```

## 用法 / Usage
- 必填變數 / Variables: {{learner-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Python Instructor Learning Plan Generator is a free AI prompt that creates customized Python curricula for…
