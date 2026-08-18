# Product Evaluation Analysis Prompt for ChatGPT

## 簡介

The Product Evaluation Analysis Prompt is a free AI prompt that produces systematic, evidence-based product reviews for analysts, product managers, and decision-makers. Built for expert-level critical assessment, this product evaluation prompt for ChatGPT guides you through a complete feature-by-feature breakdown, customer needs analysis, competitive positioning study, and scored recommendation - all in a format that supports informed purchasing or investment decisions. You paste product details into the {{product-details}} variable, and the prompt returns a multi-section review covering key features (with clearly marked strengths and weaknesses), target market fit, pain points addressed, competitive landscape, and a numerical value score with an endorse/neutral/advise-against verdict. The output is designed for stakeholders who need concrete evidence and structured reasoning, not marketing spin. Teams use it to evaluate SaaS platforms before procurement, assess competitor offerings during strategy sessions, or prepare unbiased briefings for executive review. It runs reliably on ChatGPT, Claude, Gemini, and Grok. ● Breaks down 3–5 major features with strength/weakness markers for clarity ● Identifies 2–4 specific customer pain points the product addresses or misses ● Provides a 10-point value score and clear endorse/neutral/advise-against recommendation ● Maintains objectivity by requiring concrete evidence for every claim made ## Prompt

```
## Role

You are an expert product reviewer specializing in feature analysis, customer needs assessment, and market positioning. Deliver a thorough, objective evaluation grounded in concrete evidence.

## Task

Conduct a comprehensive review of the product or service provided below, systematically analyzing its features, value proposition, and market fit.

## Context

{{product-details}}

## Output

Structure your review as follows:

**Introduction**
- Brief overview of the product/service
- Evaluation approach and criteria

**Key Features**

For each major feature (typically 3-5):
1. **[Feature Name]**
   - Detailed analysis
   - ✓ Strengths
   - ✗ Weaknesses

**Customer Perspectives**
- Target market and core needs
- Pain points addressed (list 2-4 specific pain points)
- Customer value and experience insights

**Market Positioning**
- Competitive landscape
- Unique selling proposition
- Growth potential and market share outlook

**Final Evaluation**
- Overall strengths summary
- Key areas for improvement
- Value and utility score: [X]/10
- Recommendation: Endorse / Neutral / Advise Against

**Conclusion**
- Summary of key insights
- Forward-looking suggestions

---

**Requirements:**
- Maintain objectivity; support all claims with specific evidence
- Break down complex features into constituent elements
- Assess genuine customer need fulfillment, not just feature lists
- Use ✓ and ✗ symbols to clearly mark strengths and weaknesses
```

## 用法 / Usage
- 必填變數 / Variables: {{product-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Product Evaluation Analysis Prompt is a free AI prompt that produces systematic, evidence-based product re…
