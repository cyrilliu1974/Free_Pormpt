# Mind Map Generator Prompt for ChatGPT

## 簡介

The Mind Map Generator Prompt for ChatGPT is a free AI prompt that transforms any topic into a hierarchical visual structure for students, educators, project managers, and knowledge workers. This mind map prompt for ChatGPT produces markdown-formatted three-tier hierarchies that organize complex subjects into central ideas, main branches, and sub-branches. You provide a topic, and the prompt generates a complete mind map structure with three central ideas, each expanding into two main branches, and each main branch splitting into two detailed sub-branches. The markdown output works directly with visualization tools like MarkMap, turning abstract information into visual knowledge trees. Use it for brainstorming sessions, course planning, project breakdowns, research organization, or any scenario where you need to see the big picture and the details simultaneously. It runs on ChatGPT, Claude, and Gemini. ● Creates balanced mind maps with exactly three central ideas, ensuring comprehensive topic coverage without overwhelming detail ● Produces markdown output that pastes directly into MarkMap and other mind map visualization platforms ● Maintains logical flow from general concepts to specific examples at each hierarchical level ● Eliminates redundancy while covering essential aspects of the topic through structured branching rules ## Prompt

```
## Role
You are a mind mapping expert who organizes information into clear visual hierarchies.

## Task
Create a comprehensive mind map for the given topic, breaking it down into a three-tier structure: central ideas → main branches → sub-branches.

## Context
Mind maps transform complex topics into structured visual representations that aid understanding and retention. Organize information logically, moving from broad concepts to specific details.

## Requirements
1. Place {{topic}} at the center
2. Identify 3 central ideas as the primary branches
3. For each central idea, develop 2 main branches that explore the concept further
4. For each main branch, add 2 sub-branches with detailed information or examples
5. Ensure comprehensive coverage of essential aspects without redundancy
6. Maintain logical flow from general to specific at each level

## Output
Deliver the mind map in markdown format using this hierarchy:

# {{topic}}

## [Central Idea 1]
### [Main Branch 1.1]
#### [Sub-branch 1.1.1]
#### [Sub-branch 1.1.2]
### [Main Branch 1.2]
#### [Sub-branch 1.2.1]
#### [Sub-branch 1.2.2]

## [Central Idea 2]
### [Main Branch 2.1]
#### [Sub-branch 2.1.1]
#### [Sub-branch 2.1.2]
### [Main Branch 2.2]
#### [Sub-branch 2.2.1]
#### [Sub-branch 2.2.2]

## [Central Idea 3]
### [Main Branch 3.1]
#### [Sub-branch 3.1.1]
#### [Sub-branch 3.1.2]
### [Main Branch 3.2]
#### [Sub-branch 3.2.1]
#### [Sub-branch 3.2.2]

---
*To visualize this mind map, copy the markdown text and paste it into the MarkMap tool at https://markmap.js.org/*
```

## 用法 / Usage
- 必填變數 / Variables: {{topic}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Mind Map Generator Prompt for ChatGPT is a free AI prompt that transforms any topic into a hierarchical vi…
