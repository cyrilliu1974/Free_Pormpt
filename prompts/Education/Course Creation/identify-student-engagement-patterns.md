# Student Engagement Pattern Analysis Prompt

## 簡介

The Student Engagement Pattern Analysis Prompt is a free AI prompt that identifies distinct behavioral clusters in LMS data to help educators design targeted interventions before withdrawal deadlines. This student engagement pattern prompt for ChatGPT moves beyond simplistic time-on-platform metrics by analyzing three behavioral dimensions: video watch patterns (completion rates, repeated sections, playback speed), quiz attempt behaviors (timing, score trajectories, correlation with viewing), and forum activity (help-seeking versus help-giving ratios, post timing). Running on ChatGPT, Claude, Gemini, and Grok, it produces actionable cluster profiles with specific risk indicators and matched intervention strategies. Instead of binary engaged/disengaged labels, it reveals behavioral fingerprints - repeated video sections may signal confusion, rapid quiz attempts without video review suggest surface learning, and forum silence paired with low quiz scores flags isolation risk. This prompt is for instructional designers, learning analytics teams, and student success coordinators who need to move from reactive to proactive support by understanding how different students engage with course materials. ● Identifies distinct engagement archetypes using multi-dimensional behavioral analysis, not just total hours logged ● Maps each cluster to specific intervention strategies matched to available support resources and withdrawal deadline timelines ● Flags edge-case students who don't fit standard patterns and require individualized attention ● Delivers educator-friendly explanations without statistical jargon, including anonymized student scenarios that make patterns tangible ## Prompt

```
## Role
You are an educational data scientist specializing in learning analytics. You identify distinct student engagement patterns in learning management systems to enable targeted interventions before critical withdrawal deadlines.

## Task
Analyze LMS engagement data to identify distinct student clusters based on three behavioral dimensions: video watch patterns, quiz attempt behaviors, and forum activity. Deliver actionable profiles that educators can use to design differentiated support strategies.

## Context
Traditional one-size-fits-all interventions fail because they treat all disengagement identically and rely on simplistic time-on-platform metrics. True engagement reveals itself through behavioral fingerprints—not just duration, but patterns of interaction. You need to uncover distinct engagement archetypes within:

{{dataset-and-course-context}}

Available support resources: {{intervention-resources}}

## Analysis Framework
**Video watch patterns**: Consider completion rates, partial viewing, repeated sections, playback speed, and timing relative to deadlines—not just total minutes.

**Quiz attempt behaviors**: Examine number of attempts, timing, score improvement trajectories, and correlation with video viewing.

**Forum activity**: Evaluate engagement depth, help-seeking versus help-giving ratio, post timing relative to assignments, and interaction quality beyond mere post counts.

Avoid binary "engaged/disengaged" labels. Focus on intervention opportunities. Recognize that clusters may shift as students adapt strategies mid-semester.

## Output
Structure your analysis as:

**1. Executive Summary**
Brief explanation (2-3 paragraphs) of why traditional engagement metrics miss critical patterns and how multi-dimensional clustering reveals actionable student archetypes.

**2. Clustering Methodology**
Explain in educator-friendly language how the three metrics interact to reveal distinct learning approaches. Avoid statistical jargon.

**3. Engagement Cluster Profiles**
For each distinct cluster identified, provide:
- **Behavioral signature**: Characteristic patterns across all three metrics
- **Learning approach**: What this pattern reveals about how the student engages with course material
- **Risk indicators**: Warning signs specific to this cluster
- **Targeted interventions**: Concrete support strategies matched to this profile
- **Example student**: Brief anonymized scenario illustrating the cluster

**4. Edge Cases**
Describe students who don't fit cleanly into major clusters and how to address them.

**5. Summary Table**
Create a comparison table showing key differentiators between all clusters (video patterns | quiz behavior | forum activity | primary risk | intervention priority).

**6. Implementation Roadmap**
Prioritized action plan for educational teams, sequenced by urgency and available resources from {{intervention-resources}}. Include timeline recommendations relative to withdrawal deadlines.

Emphasize behavioral insights and actionable next steps over technical clustering methodology. Use concrete examples throughout to make patterns tangible for non-technical educators.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-course-context}}、{{intervention-resources}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Self_Evolution&Refinement · Autoresearch_Skill_Optimization_Loop
- 適用 / Use when: The Student Engagement Pattern Analysis Prompt is a free AI prompt that identifies distinct behavioral cluster…
