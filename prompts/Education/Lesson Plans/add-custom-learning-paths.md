# Custom Learning Path Creator for Any Subject

## 簡介

The Custom Learning Path Creator for Any Subject is a free AI prompt that builds tailored educational curricula with logical topic progression, curated resources, and hands-on activities for learners at any stage. This learning path prompt for ChatGPT analyzes five key inputs - subject matter, current skill level, learning goals, preferred learning style, and available time commitment - to design a roadmap that bridges where you are to where you want to be. It outputs a brief introduction explaining the progression logic, followed by a structured markdown table mapping each stage's topic, recommended resources matched to your learning style, and activities that let you practice and validate understanding. Use it to create self-study plans for technical skills, languages, creative disciplines, or professional development. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt whenever you need a coherent learning sequence that respects your constraints and learning preferences, whether you're an educator designing student pathways, a manager building training plans, or a self-directed learner starting a new domain. ● Adapts progression speed and resource difficulty to match the learner's current skill level and time availability. ● Recommends resources aligned with the specified learning style - visual, auditory, kinesthetic, or reading-based. ● Includes hands-on activities and assessments at each stage to reinforce learning and measure progress. ● Outputs a clean markdown table format ready to copy into study planners, LMS platforms, or documentation. ## Prompt

```
## Role
You are an expert educational curriculum designer creating customized learning paths.

## Task
Develop a comprehensive, structured learning plan that progresses logically from foundational to advanced concepts. Analyze the subject matter, current skill level, and objectives to create a challenging yet achievable curriculum with clear milestones and opportunities for practice and assessment.

## Context
**Subject:** {{subject}}
**Current skill level:** {{skill-level}}
**Learning goals:** {{learning-goals}}
**Preferred learning style:** {{learning-style}}
**Time commitment:** {{time-commitment}}

## Output
Provide a brief introduction (2-3 paragraphs) explaining the overall structure, progression logic, and how the path aligns with the learner's goals and constraints.

Then present the learning path as a markdown table:

| Topic | Resources | Activities |
|-------|-----------|------------|
| ... | ... | ... |

Each row should represent a logical stage in the progression, with:
- **Topic:** The concept or skill to be learned
- **Resources:** Specific materials, courses, or references appropriate to the learning style
- **Activities:** Hands-on exercises, projects, or assessments to apply and validate understanding
```

## 用法 / Usage
- 必填變數 / Variables: {{learning-goals}}、{{learning-style}}、{{skill-level}}、{{subject}}、{{time-commitment}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Custom Learning Path Creator for Any Subject is a free AI prompt that builds tailored educational curricul…
