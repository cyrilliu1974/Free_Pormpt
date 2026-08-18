# Cookie Banner Design and Compliance Implementation

## 簡介

The Cookie Banner Design and Compliance Implementation is a free AI prompt that produces a detailed, legally compliant cookie management system guide for web developers and privacy officers. It analyzes your cookie inventory, target regions, platform, skill level, and privacy policy status to deliver technical implementation steps, consent logic, banner UX specifications, and compliance validation checklists that meet GDPR and ePrivacy Directive requirements. This cookie banner prompt for ChatGPT, Claude, Gemini, and Grok balances legal compliance with user experience by generating category-based controls, persistent consent storage architecture, and testing procedures tailored to your exact setup. Reach for it when you need to implement or audit a cookie consent system that passes regulatory scrutiny while respecting user choice. ● Analyzes regional compliance requirements for GDPR, ePrivacy Directive, and other jurisdictions based on your target user locations. ● Delivers complete banner design specifications including appearance, copy, consent management logic, and category-based cookie controls. ● Provides platform-specific technical implementation steps adapted to your skill level, from basic HTML/JavaScript to enterprise CMS integrations. ● Includes compliance validation checklists, testing procedures, and maintenance protocols to ensure ongoing regulatory adherence. ## Prompt

```
## Role
You are an expert web developer and privacy compliance specialist with experience implementing GDPR-compliant cookie management systems across multiple jurisdictions.

## Task
Create a comprehensive, legally compliant cookie banner implementation guide that ensures full GDPR and ePrivacy Directive compliance while maintaining optimal user experience.

## Context
Privacy regulations are constantly evolving, with non-compliance resulting in substantial fines. Legal teams require bulletproof compliance while marketing teams need granular tracking capabilities. Users expect full transparency and control over their data.

Analyze the specific cookie usage patterns and regional compliance requirements provided below, then design a complete cookie banner system including:
- Technical implementation architecture
- Legal compliance features
- User experience optimization
- Banner appearance specifications
- Consent management logic
- Category-based cookie controls
- Persistent consent storage mechanisms
- Code structure recommendations
- Compliance validation steps
- Testing procedures

**Website details:**
{{cookie-inventory}}

**Target user regions:**
{{target-regions}}

**Website platform:**
{{platform}}

**Technical skill level:**
{{skill-level}}

**Existing privacy policy status:**
{{privacy-policy-status}}

## Output
Structure your response with clear section headings (##) covering:
1. Regulatory requirements analysis for the specified regions
2. Cookie categorization and consent scope
3. Banner design and UX specifications
4. Technical implementation steps tailored to the platform and skill level
5. Consent management logic and storage
6. Compliance validation checklist
7. Testing and maintenance procedures

Provide all technical specifications, legal requirements, and implementation steps in detailed bullet points for maximum clarity and actionability.
```

## 用法 / Usage
- 必填變數 / Variables: {{cookie-inventory}}、{{platform}}、{{privacy-policy-status}}、{{skill-level}}、{{target-regions}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Cookie Banner Design and Compliance Implementation is a free AI prompt that produces a detailed, legally c…
