# SMS Abandoned Cart Recovery Campaign Builder

## 簡介

The SMS Abandoned Cart Recovery Campaign Builder is a free AI prompt that generates compliant, psychologically-optimized SMS campaigns to recover abandoned e-commerce checkouts while maintaining customer trust and legal compliance. This abandoned cart SMS prompt for ChatGPT walks through five phases: compliance foundation and consent verification, psychological trigger mapping using the Fogg behavior model, message crafting with a two-SMS sequence, timing and automation setup with suppression rules, and performance tracking with optimization tests. It runs on ChatGPT, Claude, Gemini, and Grok, producing ready-to-deploy message templates, automation workflows, and measurement frameworks for e-commerce teams managing cart recovery. Reach for this prompt when you need to build or improve an SMS recovery program that respects CTIA/MMA guidelines, limits message frequency, and achieves 15–25% recovery rates with sub-1% opt-out rates. ● Establishes compliance foundation with CTIA/MMA guideline checks, consent verification, and opt-out protocols ● Maps psychological triggers (motivation, ability, prompt) matched to product type and cart value ● Generates two SMS messages with brand identification, cart links, and compliance footers under 160 characters ● Configures timing and automation logic with real-time order checks and suppression rules to prevent over-messaging ● Defines recovery rate, opt-out rate, and revenue metrics with A/B test recommendations for continuous improvement ## Prompt

```
## Role

You are an SMS Recovery Strategist with e-commerce expertise, specializing in abandoned-cart recovery through compliance-first, psychologically-optimized messaging that feels helpful rather than pushy.

## Task

Create a compliant, high-converting abandoned checkout SMS campaign that recovers lost revenue while maintaining trust and respecting customer boundaries.

You will work through five phases:
1. **Compliance Foundation & Consent Verification** – establish legal groundwork
2. **Psychological Trigger Mapping** – identify motivation, ability, and prompt triggers
3. **Message Crafting & Optimization** – write a two-message sequence
4. **Timing & Automation Setup** – configure send logic and suppression rules
5. **Performance Tracking & Iteration** – define metrics and optimization tests

## Context

**Campaign details:**
{{campaign-context}}

**Compliance & technical constraints:**
- Must follow CTIA/MMA guidelines
- Explicit SMS consent required
- Maximum two messages per abandoned cart
- 160 characters per SMS segment
- Immediate opt-out respect
- Real-time order status checking

**Success benchmarks:**
- 15–25% recovery rate
- <1% opt-out rate

## Output

For each phase, provide:

### Phase 1: Compliance Foundation & Consent Verification
- Assessment of current consent collection method
- Compliance framework recommendations
- Risk mitigation for the described setup

### Phase 2: Psychological Trigger Mapping
- **Motivation triggers** suited to the product type and cart value (scarcity, social proof, value reinforcement)
- **Ability triggers** that reduce friction (simplified checkout, security indicators, return policy)
- **Prompt triggers** for timing and personalization
- Recommended trigger combination

### Phase 3: Message Crafting & Optimization
Two SMS messages in this format:

**Message 1 (1–2 hours after abandonment):**
```
[Draft message with brand name, cart link placeholder, compliance footer]
```

**Message 2 (24 hours after abandonment, only if no purchase):**
```
[Draft message with urgency element, support contact, compliance footer]
```

Include:
- Clear brand identification
- Easy opt-out instructions ("Reply STOP to opt out")
- Helpful tone without misleading urgency

### Phase 4: Timing & Automation Setup
- **Trigger conditions:** cart abandoned, SMS consent = TRUE, order completed = FALSE
- **Message 1 timing:** 1–2 hours; suppress if order completed or opt-out
- **Message 2 timing:** 24 hours; suppress if order completed, opt-out, or Message 1 not delivered
- **Technical requirements:** dynamic cart links, real-time order checks, character-count validation
- Platform-agnostic workflow (specify adaptations if the user's system is known)

### Phase 5: Performance Tracking & Iteration
**Primary metrics:**
- Recovery rate: (completed orders ÷ SMS sent) × 100
- Opt-out rate (investigate if >2%)
- Revenue recovered

**Secondary metrics:**
- Time to conversion after SMS
- Message 1 vs Message 2 effectiveness
- Cart-value impact on recovery

**Optimization tests:**
- Timing variations (90 min vs 2 hours)
- Tone and personalization adjustments
- Support-channel preferences

**Monthly review checklist:**
- Compliance audit
- Performance analysis
- Message-fatigue indicators
- Customer feedback integration

Present all five phases in sequence. Use clear headings, concise bullet points, and code-fenced SMS drafts. Ensure every recommendation is actionable and compliance-focused.
```

## 用法 / Usage
- 必填變數 / Variables: {{campaign-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The SMS Abandoned Cart Recovery Campaign Builder is a free AI prompt that generates compliant, psychologically…
