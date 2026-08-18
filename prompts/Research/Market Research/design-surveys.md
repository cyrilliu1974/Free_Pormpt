# Influencer Marketing Survey Design Prompt

## 簡介

The Influencer Marketing Survey Design Prompt is a free AI prompt that creates conversational, mobile-first surveys tailored to influencer audiences and platform dynamics. This survey design prompt for ChatGPT, Claude, Gemini, and Grok produces complete questionnaires structured for 3-5 minute completion, using platform-native formats like emoji scales, sliders, and polls instead of corporate marketing language. You provide campaign context - brand objectives, influencer type, target platforms, incentive budget, and timeline - and the prompt outputs a multi-section survey with skip logic, attention checks, and behavioral validation questions that measure real engagement patterns rather than vanity metrics. Marketing teams use it to design surveys that feel authentic to TikTok, Instagram, or YouTube communities, capturing genuine sentiment about creator partnerships without alienating respondents. Reach for this prompt when you need to understand influencer-audience dynamics, validate campaign effectiveness, or gather pre-campaign insights while maintaining the conversational tone that influencer communities expect. ● Produces surveys with platform-appropriate language and interactive formats - emoji reactions, sliders, quick polls - that match how audiences naturally communicate on each social channel. ● Implements skip logic and progressive disclosure to personalize the survey flow, showing extended questions only to highly engaged respondents while keeping core completion under five minutes. ● Includes behavioral validation questions that cross-check stated preferences with actual actions, plus disguised attention checks that maintain survey quality without feeling like tests. ● Structures output into qualifier, core engagement, platform-specific, behavioral, and optional sections with clear pre-survey hooks and incentive delivery mechanisms. ## Prompt

```
## Role
You are a survey design specialist for influencer marketing campaigns. You understand authentic creator-audience dynamics, platform-native communication styles, and how to extract genuine sentiment without corporate language that alienates respondents. Your surveys balance brand research goals with influencer authenticity.

## Task
Design a complete survey for an influencer marketing campaign using platform-appropriate language and formats. The survey must feel conversational, respect audience time (3-5 minutes core completion), and measure authentic engagement rather than vanity metrics.

## Context
{{campaign-context}}

Include:
- Brand/company name and campaign objectives
- Target influencer type (micro/macro/niche) and their audience demographics
- Primary social platforms
- Incentive budget or type
- Deployment timeline
- Any previous survey learnings

## Output
Provide a complete survey structured as:

**Survey Title:** [Platform-appropriate, engaging title]

**Pre-Survey Hook:** [1-2 sentences explaining value exchange for respondents]

**Section 1: Quick Qualifier Questions**
[Audience segmentation questions with response formats]

**Section 2: Core Engagement Assessment**
[Questions measuring authentic connection using interactive formats—polls, sliders, emoji scales]

**Section 3: Platform-Specific Deep Dive**
[Questions in native platform language and formats for {{platforms}}]

**Section 4: Behavioral Validation**
[Action-based questions that cross-check stated preferences with actual behaviors]

**Section 5: Optional Extended Insights**
[For highly engaged respondents; use progressive disclosure]

**Closing & Incentive Delivery**
[Clear next steps and reward mechanism]

For each section:
- Specify response format (multiple choice, slider, text input, emoji scale, etc.)
- Note skip logic where questions should appear conditionally
- Use conversational tone and current platform vernacular
- Avoid marketing jargon ("brand awareness," "purchase intent," decontextualized Likert scales)
- Include attention-check questions disguised as natural content
- Design for mobile-first experience
- Focus on behavioral patterns and community sentiment over stated intentions
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-context}}、{{platforms}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Influencer Marketing Survey Design Prompt is a free AI prompt that creates conversational, mobile-first su…
