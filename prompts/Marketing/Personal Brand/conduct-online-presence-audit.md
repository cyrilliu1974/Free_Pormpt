# Online Presence Audit Generator for Personal Brands

## 簡介

The Online Presence Audit Generator is a free AI prompt that evaluates brand consistency across an individual's digital platforms and returns a structured report with actionable recommendations. This personal brand audit prompt for ChatGPT examines URLs you provide and assesses seven core dimensions: visual identity consistency (profile images, colors, design), messaging and tone alignment, professional positioning clarity, content quality, profile completeness, cross-platform cohesion, and call-to-action effectiveness. It produces a findings table marking each aspect with ✅ or ❌, an overview summary, a platform inventory, and three prioritized improvement actions. Use it when launching a personal brand refresh, preparing for a job search, onboarding a client for brand consulting, or conducting annual digital presence reviews. It runs on ChatGPT, Claude, and Gemini. ● Evaluates visual identity, messaging tone, professional positioning, content quality, profile completeness, cross-platform cohesion, and call-to-action clarity ● Returns a structured table with pass/fail indicators and explanations for each brand aspect ● Provides a 2-3 sentence overview of overall brand positioning and impression ● Delivers three prioritized, specific recommendations ranked by improvement impact ## Prompt

```
## Role

You audit online brand presence across platforms, evaluating consistency in visual identity, messaging, and overall impression.

## Task

Conduct a thorough online presence audit for the provided URLs. Evaluate brand consistency across visual identity, messaging, tone, and overall impression. Use ✅ for well-executed aspects and ❌ for areas needing improvement.

## Input

- **URLs to audit:** {{urls}}

## Output

**Online Presence Overview:**
[Provide a 2-3 sentence summary of the individual's overall online presence and brand positioning]

**Platforms Audited:**
- [List each platform found at the provided URLs]

**Audit Findings:**

| Aspect | Assessment | Explanation |
|--------|------------|-------------|
| Visual Identity Consistency | [✅/❌] | [Evaluate consistency of profile images, colors, design elements] |
| Messaging & Tone | [✅/❌] | [Evaluate alignment of voice, language, and messaging across platforms] |
| Professional Positioning | [✅/❌] | [Evaluate clarity and consistency of expertise, value proposition] |
| Content Quality | [✅/❌] | [Evaluate relevance, polish, and engagement value of content] |
| Profile Completeness | [✅/❌] | [Evaluate whether bios, about sections, and key details are filled out] |
| Cross-Platform Cohesion | [✅/❌] | [Evaluate whether platforms reinforce each other or feel disconnected] |
| Call-to-Action Clarity | [✅/❌] | [Evaluate whether next steps for visitors are clear and consistent] |

**Recommendations:**
1. [Highest-priority improvement with specific action]
2. [Second-priority improvement with specific action]
3. [Third-priority improvement with specific action]
```

## 用法 / Usage
- 必填變數 / Variables: {{urls}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Online Presence Audit Generator is a free AI prompt that evaluates brand consistency across an individual'…
