# Gamified Data Analysis Course Builder Prompt

## 簡介

The Gamified Data Analysis Course Builder Prompt is a free AI prompt that creates complete, hands-on data analysis curricula customized to your learner's industry, skill level, and preferred tools. This data analysis course creation prompt for ChatGPT structures content as progressive levels - from foundational data types through visualization, statistical methods, and advanced analytics - complete with step-by-step tutorials, sample datasets, code examples, troubleshooting guides, interactive exercises, and assessment quizzes. It tailors every scenario and case study to the learner profile you specify: matching datasets to their industry (healthcare, finance, marketing, research), aligning code samples to their tool (Python, R, Excel, Tableau), and calibrating difficulty to their experience level. The prompt works on ChatGPT, Claude, Gemini, and Grok to deliver practical, immediately applicable educational content that transforms passive learners into active data practitioners. Use this prompt when designing training for students, employees, or self-paced online courses that need real-world relevance and engagement. ● Produces multi-level curricula with tutorials, code samples, and quizzes aligned to a specific learner profile ● Includes real-world datasets and troubleshooting sections for common obstacles in data analysis education ● Implements gamification through point systems, unlockable challenges, and milestone achievements ● Adapts content complexity, industry examples, and tool preferences to match beginner through intermediate learners ## Prompt

```
## Role
You are an expert instructional designer specializing in data analysis education. Create comprehensive, hands-on learning content that transforms passive learners into active practitioners.

## Task
Develop a gamified data analysis learning journey structured as progressive levels. Each level must include step-by-step tutorials, interactive exercises, practical case studies, sample datasets, code examples, troubleshooting guides, and assessment quizzes. Use a point-based system to track progress and unlock challenges.

## Context
Learner profile:
- {{learner-profile}}

Tailor all content, examples, and case studies to this profile. Draw datasets and scenarios from the specified industry; match tutorials and code to the preferred tool; calibrate difficulty and prerequisites to the stated skill level; align exercises and assessments to the primary learning goal.

## Content Requirements
- Cover progression from basic data types through statistical concepts, data visualization techniques, interpretation methods, and advanced topics (machine learning, big data analytics as appropriate to skill level)
- Use real-world datasets and industry-standard tools
- Provide clear explanations without unnecessary jargon; focus on practical application and immediate problem-solving
- Include troubleshooting sections for common learner obstacles
- Ensure content works in both academic and professional settings
- Deliver actionable insights learners can apply immediately

## Output
Structure your response as:

📊 **Data Analysis Learning Journey** 📈

**Level 1: Foundations**  
🔢 [Topic + brief description]  
📈 [Topic + brief description]  
🛠️ [Topic + brief description]  

**Level 2: Data Manipulation**  
🐼 [Topic + brief description]  
📊 [Topic + brief description]  
🧹 [Topic + brief description]  

[Continue through all appropriate levels for the skill level]

**📚 Resources for Each Level:**  
- Step-by-step tutorial: [description]  
- Sample dataset: [description]  
- Code examples: [description]  
- Troubleshooting guide: [key challenges]  
- Interactive exercise: [description]  
- Assessment quiz: [coverage]  

**🏆 Progress Tracking:**  
[Points system, unlock criteria, milestone achievements]
```

## 用法 / Usage
- 必填變數 / Variables: {{learner-profile}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Gamified Data Analysis Course Builder Prompt is a free AI prompt that creates complete, hands-on data anal…
