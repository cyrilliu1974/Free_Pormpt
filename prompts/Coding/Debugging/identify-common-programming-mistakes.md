# Common Programming Mistakes Analysis Prompt

## 簡介

The Common Programming Mistakes Analysis Prompt is a free AI prompt that identifies and explains the most frequent programming errors in any specified learning context for educators, mentors, and course designers. This prompt acts as an expert computer science educator, analyzing 4-6 predictable beginner mistakes through the lens of cognitive science and education research. It runs on ChatGPT, Claude, Gemini, and Grok, making it a versatile programming mistakes prompt for ChatGPT and other text models that produces structured breakdowns of why errors happen, how to spot them, and how to prevent them through better mental models. Reach for this prompt when designing curriculum, preparing teaching materials, or helping novice developers understand why they struggle with specific concepts. ● Explains the psychological and conceptual reasons behind each common mistake, grounded in computer science education research. ● Provides clear recognition indicators so learners and instructors can quickly identify when a mistake is occurring. ● Delivers actionable prevention strategies that address root causes and build stronger mental models. ● Covers 4-6 context-specific errors tailored to the learning environment you provide via the learning-context variable. ## Prompt

```
## Role
You are an expert computer science educator specializing in evidence-based teaching methodologies for novice developers.

## Task
Identify and explain the most common programming mistakes in the specified learning context. For each mistake, provide:

- **Why This Happens**: The cognitive and conceptual reasons behind the error, including typical beginner misconceptions
- **How to Recognize It**: Clear indicators and symptoms when this mistake is occurring
- **Prevention Strategies**: Actionable approaches that build better mental models and address root causes

Focus on pattern recognition to reduce frustration and accelerate learning progress. Draw from computer science education research to highlight predictable errors that beginners repeatedly encounter.

## Context
{{learning-context}}

## Output
Structure your response with clear headings for each common mistake. Organize information under the three subheadings above using bullet points for clarity and practical application. Cover the 4-6 most frequent errors specific to the learning context provided.
```

## 用法 / Usage
- 必填變數 / Variables: {{learning-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Common Programming Mistakes Analysis Prompt is a free AI prompt that identifies and explains the most freq…
