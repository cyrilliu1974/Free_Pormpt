# Crisis Communication Template Builder for Operations

## 簡介

The Crisis Communication Template Builder for Operations is a free AI prompt that creates channel-specific response frameworks for businesses facing operational failures like delays, outages, and product recalls. It produces ready-to-deploy templates for email, SMS, and social media, each calibrated to three severity levels - minor inconvenience, major disruption, and safety concern - with clear escalation triggers and compensation language. This crisis communication prompt for ChatGPT, Claude, Gemini, and Grok helps organizations respond authentically when service failures threaten customer trust, providing structured messaging that acknowledges harm, offers tangible remedies, and prevents reputational escalation. Reach for this prompt when you need to prepare crisis protocols before incidents occur or respond immediately to unfolding operational problems. ● Delivers distinct templates for email (full body with subject line), SMS (160-character limit with character count), and social media (platform-aware formats for Twitter, Facebook, Instagram) tailored to the communication norms of each channel. ● Implements a three-level severity scale with tone guidance - informative for minor issues, apologetic for major disruptions, urgent for safety concerns - so messages match the gravity of each situation. ● Provides decision trees showing how to assess customer impact, select the correct template, trigger escalation structures, and identify when legal review is required. ● Uses active voice and first-person accountability ("we failed" rather than passive constructions), addressing emotional impact before operational details and avoiding hollow corporate language. ## Prompt

```
## Role
You are a crisis communication strategist specializing in operational failures that threaten customer trust. You craft authentic, channel-appropriate responses that acknowledge harm, offer tangible remedies, and prevent escalation.

## Task
Create a multi-channel crisis communication framework for operational failures (delays, outages, recalls). Develop distinct templates for email, SMS, and social media that adapt to three severity levels: minor inconvenience, major disruption, and safety concern.

## Context
{{business-and-risk-profile}}

Assess potential reputational threats and design communication strategies that match both operational reality and customer expectations across channels.

## Output
Deliver ready-to-use templates structured by:

**Severity Scale Reference**
- Level 1 (minor inconvenience): informative tone
- Level 2 (major disruption): apologetic tone
- Level 3 (safety concern): urgent tone
- Clear triggers for legal review or senior leadership escalation

**Channel-Specific Templates**

For each channel (email, SMS, social media) at each severity level, include:

1. **Immediate acknowledgment** – Name the issue directly, no euphemisms
2. **Clear explanation** – Plain language, no jargon
3. **Specific remedy** – Concrete compensation based on {{compensation-options}}
4. **Resolution timeline** – Exact dates or hourly update schedule
5. **Escalation contact** – Named person or direct line

**Format by channel:**
- **Email**: Subject line + full body with emotional acknowledgment before operational details
- **SMS**: Max 160 characters with link to full details (show character count)
- **Social media**: Platform-aware (Twitter brevity, Facebook detail, Instagram visual-first)

**Decision Tree**
Provide a flowchart showing:
- How to assess severity based on customer impact
- Which template to select
- When to trigger {{escalation-structure}}
- Legal review checkpoints for safety issues

**Tone Guidelines**
- Active voice, first person ("we failed" not "mistakes were made")
- Address emotional impact first, then logistics
- Avoid empty phrases like "apologize for any inconvenience"
- Focus on fix, not blame

Use [PLACEHOLDER] format for customizable details within templates. Include real-time update mechanisms for evolving situations.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-risk-profile}}、{{compensation-options}}、{{escalation-structure}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Reasoning_Strategy_Advisor
- 適用 / Use when: The Crisis Communication Template Builder for Operations is a free AI prompt that creates channel-specific res…
