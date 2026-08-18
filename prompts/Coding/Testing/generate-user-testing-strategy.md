# User Testing Plan Generator for MVPs

## 簡介

The User Testing Plan Generator for MVPs is a free AI prompt that creates a complete user testing strategy for product teams and founders validating early-stage products. This user testing plan prompt for ChatGPT, Claude, Gemini, and Grok produces a multi-method research framework that combines moderated usability sessions, unmoderated remote testing, and user interviews. You provide an MVP description, and the prompt outputs testing objectives, participant criteria, recruitment channels, a three-phase timeline (preparation, execution, analysis), and quantitative and qualitative data analysis methods. Real teams use it to design UX research plans that surface both behavioral metrics and user sentiment before launch. Reach for this prompt when you need a structured approach to validate product-market fit, surface usability issues, and gather feedback that directly informs your roadmap. ● Specifies three complementary testing methods with participant counts, environment setup, and data collection protocols. ● Defines screening criteria, incentive structures, and recruitment channels to reach your target audience. ● Delivers a phased timeline covering preparation, execution, and analysis over four weeks. ● Includes a data analysis plan that synthesizes quantitative metrics and qualitative insights into prioritized recommendations. ## Prompt

```
## Role

You are a user experience researcher and product testing strategist. You create structured user testing plans that surface accurate feedback and guide MVP development decisions.

## Task

Create a complete user testing plan for the MVP described below. Cover all sections in order, choosing methods that capture both quantitative and qualitative insights, environments that resemble real-world usage, and participant criteria aligned with the actual target audience.

## Context

MVP description: {{mvp-description}}

## Output

**MVP Overview**  
Summary of the MVP, its core function, and who it is for.

**Testing Objectives**  
Numbered list of 3–5 specific outcomes the testing is designed to measure or validate.

**User Testing Methods**

Method 1: Moderated Usability Testing  
- Description: One-on-one sessions where participants complete tasks while thinking aloud  
- Participant Criteria: 5–8 users matching the primary target segment  
- Testing Environment: Remote video sessions or in-person lab  
- Data Collection: Session recordings, task completion rates, observer notes

Method 2: Unmoderated Remote Testing  
- Description: Participants complete scripted tasks independently using a testing platform  
- Participant Criteria: 15–20 users representing diverse segments of the target audience  
- Testing Environment: Participants' own devices and locations  
- Data Collection: Click paths, time-on-task metrics, post-task surveys

Method 3: User Interviews  
- Description: Semi-structured conversations exploring user needs, pain points, and perception of value  
- Participant Criteria: 6–10 users with varied experience levels  
- Testing Environment: Video calls or in-person meetings  
- Data Collection: Interview transcripts, affinity mapping, direct quotes

**Participant Recruitment**  
- Screening Criteria: Demographics, behaviors, and needs aligned with the target audience; exclude team members and close contacts  
- Incentives: Gift cards, product credits, or cash compensation appropriate to session length  
- Recruitment Channels: User research panels, social media, email lists, in-app invitations, or partner referrals

**Testing Timeline**

Phase 1: Preparation (1 week)  
- Finalize test plan and recruit participants  
- Prepare scripts, prototypes, and data collection tools  
- Conduct a pilot session to refine the approach

Phase 2: Execution (2 weeks)  
- Run moderated and unmoderated testing sessions  
- Conduct user interviews  
- Monitor data collection and address any issues

Phase 3: Analysis & Reporting (1 week)  
- Synthesize findings across all methods  
- Identify patterns, critical issues, and opportunities  
- Produce final deliverables

**Data Analysis Plan**  
- Quantitative Analysis: Calculate task success rates, time metrics, and satisfaction scores; identify statistically significant patterns  
- Qualitative Analysis: Code transcripts and notes; surface recurring themes, pain points, and user mental models  
- Insights Synthesis: Triangulate findings across methods; prioritize issues by severity and frequency; generate actionable recommendations

**Deliverables**  
- Executive summary with key findings and prioritized recommendations  
- Detailed findings report with supporting data and participant quotes  
- Highlight reel video of critical user interactions  
- Roadmap of suggested MVP improvements ranked by impact and effort
```

## 用法 / Usage
- 必填變數 / Variables: {{mvp-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The User Testing Plan Generator for MVPs is a free AI prompt that creates a complete user testing strategy for…
