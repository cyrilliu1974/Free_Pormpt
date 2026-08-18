# Pricing Perception Analysis

## 簡介

The Pricing Perception Analysis is a free AI prompt that evaluates product pricing through your target customer's eyes and recommends three commercially viable pricing tiers. Instead of guessing what customers will pay, this pricing strategy prompt for ChatGPT asks the AI to adopt your audience's perspective and calculate what "no-brainer," "middle ground," and "investment" price points should look like based on expected ROI multiples - 100×, 20×, and 5–10× respectively. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured markdown table that specifies the price, monetization model (subscription, one-time, usage-based), audience expectations, and the value justification required at each tier. Marketing teams, product managers, and founders use it when launching new products, repositioning existing offerings, or testing pricing hypotheses against real customer psychology. ● Generates three pricing tiers with explicit ROI multiples so you understand what value delivery is required at each level. ● Surfaces customer psychology for each tier, including why a buyer might hesitate or purchase immediately. ● Recommends realistic monetization models (one-time, monthly, annual, usage-based) that fit each price point. ● Outputs a clean markdown table ready to drop into strategy decks, investor updates, or product briefs. ## Prompt

```
## Role
You are a pricing strategy expert analyzing product pricing from the target customer's perspective.

## Task
Adopt the viewpoint of the described target audience and recommend three pricing tiers—no-brainer, middle ground, and investment—for the given product. For each tier, specify the price point, monetization model, audience expectations, and required value justification.

## Context
**Pricing Framework:**
- **No-brainer:** A price so compelling the customer wants to buy immediately; expected ROI is 100× the price. Customers may wonder why it's priced this low.
- **Middle ground:** A fair price for the promised value; expected ROI is 20× the price. Customers recognize cheaper and pricier alternatives exist.
- **Investment:** A premium price requiring deliberation; expected ROI is 5–10× the price. Customers perceive this as a high-end option.

**Business & Audience:**
{{business-and-product}}

{{target-audience}}

## Output
Return a markdown table with four columns:

| Pricing Range | Price & Model | Expectations from Audience | Value Justification |
|---------------|---------------|----------------------------|---------------------|
| No-brainer | | | |
| Middle ground | | | |
| Investment | | | |

Ensure all prices are commercially viable and reflect realistic monetization models (one-time payment, monthly/annual subscription, usage fees, etc.).
```

## 用法 / Usage
- 必填變數 / Variables: {{business-and-product}}、{{target-audience}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · Minimalist_Pricing_Engine
- 適用 / Use when: The Pricing Perception Analysis is a free AI prompt that evaluates product pricing through your target custome…
