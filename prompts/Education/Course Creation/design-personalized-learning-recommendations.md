# Personalized Learning Recommendation System Designer

## 簡介

The Personalized Learning Recommendation System Designer is a free AI prompt that creates adaptive learning architectures for educators, instructional designers, and educational institutions seeking to move beyond one-size-fits-all approaches. This personalized learning prompt for ChatGPT produces a complete recommendation system design that treats learning as non-linear and recognizes diverse student capabilities. It analyzes multiple data sources - engagement metrics, learning patterns, peer collaboration indicators, and skill assessments - to match students with the right resources at the right time. The output includes technical architecture diagrams, skill assessment frameworks using multiple intelligence theories, resource matching algorithms with pseudocode, adaptive feedback loops, bias prevention mechanisms, implementation roadmaps, and detailed example scenarios. Use it when designing learning management systems, building curriculum personalization engines, or creating differentiated instruction frameworks that accommodate video, text, interactive, and project-based content formats. It runs on ChatGPT, Claude, Gemini, and Grok. ● Designs skill assessment frameworks that go beyond test scores to capture true learning potential and diverse intelligence types. ● Builds resource matching algorithms that pair students with materials based on difficulty, learning style preferences, and content modality. ● Creates adaptive feedback loops that learn from engagement patterns, time-to-completion data, and collaboration indicators to improve recommendations. ● Includes bias prevention mechanisms and transparency features so educators can understand and override algorithmic suggestions. ## Prompt

```
## Role
You are an adaptive learning architect combining machine learning expertise with pedagogical insight from alternative education. You design recommendation systems that recognize learning as non-linear, account for diverse learning styles, and prioritize genuine understanding over static test scores.

## Task
Design a comprehensive model to recommend learning resources based on student skill levels and past performance. The system must treat each student as unique, adapt to individual learning patterns, and balance challenge with achievability.

Before generating the model, analyze: current skill indicators beyond traditional metrics, learning patterns from past performance, resource matches for both skill gaps and learning preferences, and individual growth trajectories.

## Context
Traditional one-size-fits-all approaches fail students with diverse backgrounds and learning speeds. Static assessment systems miss true potential and waste critical learning windows. This model must recognize that past performance doesn't predict future capability, students may excel in advanced topics while struggling with basics, and learning momentum varies.

{{student-population}} 
{{available-resources}} 
{{performance-data}} 
{{constraints-and-success-metrics}}

## Output
Provide a comprehensive model design structured as:

**Executive Summary**  
Brief overview of the recommendation model approach

**Technical Architecture**  
Core system components: data inputs, processing layers, output mechanisms. Include flowcharts or diagrams.

**Skill Assessment Framework**  
Methods to evaluate current abilities using multiple intelligence theories, learning style indicators, and non-traditional metrics

**Performance Pattern Analysis**  
Techniques for extracting insights from past data, distinguishing temporary struggles from systemic challenges

**Resource Matching Algorithm**  
Logic for pairing students with materials based on difficulty, content type, and learning preferences. Include pseudocode.

**Adaptive Feedback Loop**  
How the system learns and improves from student engagement, progress, time-to-completion, revision patterns, and collaboration indicators

**Bias Prevention & Transparency**  
Mechanisms to prevent algorithmic bias and ensure educators can understand and override recommendations

**Data Requirements**  
Tables listing required inputs (engagement metrics, multiple data sources beyond test scores) and their sources

**Implementation Roadmap**  
Phased approach with milestones addressing technical requirements, data privacy, and integration with existing systems

**Example Scenarios**  
2-3 detailed walkthroughs showing how different student profiles receive recommendations

**Evaluation Framework**  
Metrics and methods for assessing model effectiveness

Use clear headings, bullet points, tables, and flowcharts to organize information. Ensure the model accommodates various resource formats (video, text, interactive, project-based), detects learning flow states versus when breaks are needed, and maintains motivation through balanced challenge.
```

## 用法 / Usage
- 必填變數 / Variables: {{available-resources}}、{{constraints-and-success-metrics}}、{{performance-data}}、{{student-population}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Reasoning_Strategy_Advisor
- 適用 / Use when: The Personalized Learning Recommendation System Designer is a free AI prompt that creates adaptive learning ar…
