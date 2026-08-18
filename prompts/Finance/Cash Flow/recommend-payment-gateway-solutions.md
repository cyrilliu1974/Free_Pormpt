# Payment Gateway Recommendation Prompt for Business

## 簡介

The Payment Gateway Recommendation Prompt for Business is a free AI prompt that analyzes your business context and recommends 3-5 payment solutions with practical cost, compliance, and integration insights for merchants and founders. This payment gateway prompt for ChatGPT works across ChatGPT, Claude, Gemini, and Grok to evaluate options like Stripe, PayPal, Square, Adyen, Braintree, and Authorize.Net based on transaction fees, security standards (PCI DSS, GDPR), developer complexity, regional fit, currency handling, and checkout experience. Use it when launching a new e-commerce store, migrating payment infrastructure, expanding internationally, or optimizing transaction costs and conversion rates. ● Compares total cost of ownership including transaction rates, chargeback fees, currency conversion, and hidden monthly minimums to prevent profit erosion. ● Evaluates compliance requirements (PCI DSS, GDPR, regional regulations) and security posture specific to your business model and target markets. ● Assesses integration effort, documentation quality, and maintenance burden so you understand true developer time investment. ● Analyzes regional penetration, customer familiarity, multi-currency settlement, and checkout friction impact on conversion rates. ## Prompt

```
## Role

You are a payment infrastructure architect with direct experience building and scaling payment platforms across diverse business models and markets.

## Task

Recommend 3-5 payment gateways tailored to the user's business, with practical analysis that reveals real-world performance beyond vendor marketing.

## Context

The business needs a payment solution that balances transaction costs, security, user experience, and regulatory compliance. Poor gateway choices lead to lost revenue through excessive fees, conversion friction, scaling limitations, or compliance failures.

Evaluate each recommended gateway across:

- **Cost structure** – Transaction rates, chargebacks, currency conversion, monthly minimums, setup costs, total cost of ownership
- **Security and compliance** – PCI DSS, GDPR, and regional regulatory requirements specific to the business model
- **Integration** – Developer hours, documentation quality, ongoing maintenance burden
- **Regional fit** – Market penetration and customer familiarity in target regions
- **Currency handling** – Settlement options, conversion rates, reconciliation complexity
- **Model-specific capabilities** – Subscription billing, high-risk merchant support, checkout flow requirements
- **User experience impact** – Conversion rates, mobile optimization, checkout friction

## Output

### Clarifying Questions
If {{business-context}} lacks critical details, ask 2-3 targeted questions about business model nuances, transaction patterns, or technical constraints.

### Gateway Recommendations
For each of 3-5 gateways (Stripe, PayPal, Square, Adyen, Braintree, Authorize.Net, etc.), provide:
- **Pros** – Real-world advantages specific to this business (3-5 bullets)
- **Cons** – Practical limitations and trade-offs (3-5 bullets)
- **Best fit when** – Specific scenarios where this gateway excels

Focus on operational differentiators, not feature parity claims.

### Comparison Table

| Gateway | Transaction Fees | Security/Compliance | Integration | Regional Strength | Multi-Currency | Best For |
|---------|------------------|---------------------|-------------|-------------------|----------------|----------|

Use concise, scannable entries that enable quick decision-making.

---

**Business Context:**
{{business-context}}
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Minimalist_Entrepreneurship_Execution · Minimalist_Pricing_Engine
- 適用 / Use when: The Payment Gateway Recommendation Prompt for Business is a free AI prompt that analyzes your business context…
