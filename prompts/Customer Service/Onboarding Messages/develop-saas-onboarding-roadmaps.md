# SaaS Onboarding Roadmap Prompt for ChatGPT

## 簡介

The SaaS Onboarding Roadmap Prompt for ChatGPT is a free AI prompt that builds conversion-optimized user journeys from signup to power-user status for SaaS founders, product managers, and customer success teams. This SaaS onboarding prompt for ChatGPT reverse-engineers the fastest path to your product's "aha moment" and structures 3-5 onboarding phases with concrete milestones, feature utilization targets, and time-to-value benchmarks. It outputs a detailed roadmap table with success criteria for each phase alongside a complete in-app messaging strategy that celebrates progress, prevents drop-off, and identifies at-risk users. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting your product description and current onboarding challenges as inputs. Reach for this prompt when you need to reduce time-to-value, increase feature adoption rates, or systematically diagnose where new users abandon your product. ● Maps Initial Setup, First Value, Habit Formation, Feature Expansion, and Power User phases with measurable success criteria for each milestone. ● Defines feature utilization rate targets and time-to-value benchmarks that distinguish healthy adoption from at-risk cohorts. ● Produces phase-specific in-app messaging examples, drop-off prevention tactics, and expansion opportunities for engaged users. ● Establishes measurement frameworks and intervention triggers so you can track progression and optimize the journey over time. ## Prompt

```
## Role
You are an expert SaaS onboarding architect specializing in conversion-optimized user journeys and feature adoption strategies.

## Task
Create a comprehensive, milestone-driven onboarding roadmap that accelerates time-to-value and maximizes feature adoption for the user's SaaS product.

## Context
Analyze the product to identify the "aha moment" where users experience core value, then reverse-engineer the fastest path to reach it. Map out 3-5 key onboarding phases (Initial Setup, First Value, Habit Formation, Feature Expansion, Power User) with specific milestones and success criteria for each. Define feature utilization rate targets and time-to-value benchmarks that indicate healthy adoption. Create an in-app messaging strategy that celebrates progress, guides next steps, and prevents abandonment at critical junctures. Include intervention triggers for at-risk users and expansion opportunities for engaged users. Establish measurement frameworks to track progression through each milestone and identify optimization opportunities.

**Product context:**
{{product-description}}

**Current onboarding challenges:**
{{onboarding-challenges}}

## Output
Structure your response as:

1. **Onboarding Roadmap Table** in markdown format with columns:
   - Phase
   - Milestone
   - Success Criteria
   - Feature Utilization Target
   - Time-to-Value Benchmark
   - In-App Messaging Strategy
   - Key Metrics

2. **Implementation Details** with bullet points covering:
   - Specific in-app messaging examples for each phase
   - Intervention triggers for at-risk users
   - Expansion opportunities for engaged users
   - Drop-off prevention strategies at critical junctures
```

## 用法 / Usage
- 必填變數 / Variables: {{onboarding-challenges}}、{{product-description}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SaaS Onboarding Roadmap Prompt for ChatGPT is a free AI prompt that builds conversion-optimized user journ…
