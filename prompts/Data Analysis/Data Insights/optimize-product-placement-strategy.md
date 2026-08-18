# Market Basket Analysis Prompt for Cross-Selling

## 簡介

The Market Basket Analysis Prompt for Cross-Selling is a free AI prompt that identifies which products customers frequently buy together and delivers strategic recommendations for product placement, bundling, and targeted campaigns. This market basket analysis prompt for ChatGPT applies the Apriori algorithm to transaction data, calculates support, confidence, and lift metrics for product pairs, and surfaces high-value associations that drive revenue. It runs on ChatGPT, Claude, and Gemini, transforming raw purchase history into a ranked table of product combinations alongside specific recommendations for store layouts, recommendation engines, and marketing campaigns. Retailers use it to redesign shelf arrangements, e-commerce teams deploy it to improve "frequently bought together" widgets, and marketers apply it to design bundles and promotional offers based on real purchase behavior. Reach for this prompt when you have transaction data and need to move from intuition to evidence-based product pairing decisions, whether you manage a physical store, an online catalog, or a subscription service. ● Applies the Apriori algorithm to identify frequent itemsets and association rules from transaction IDs and product lists ● Calculates support, confidence, and lift for every product pair to quantify co-occurrence strength ● Delivers a ranked results table and bullet-point recommendations for bundling, placement, and targeted campaigns ● Explains findings in non-technical language suitable for merchandising teams and marketing stakeholders ## Prompt

```
## Role
You are a Data Analyst specializing in Market Basket Analysis (MBA). Your task is to identify cross-selling and upselling opportunities by analyzing customer purchase patterns and product co-occurrence in transactions.

## Context
You will analyze transaction data to uncover relationships between products that customers frequently buy together. These insights enable strategic product placement in marketing campaigns, recommendation engines, and store layouts to increase sales.

**Business context:** {{business-context}}
(Include your business type, current marketing strategies, and any product categories or customer segments you want to focus on.)

**Transaction data:** {{transaction-data}}
(Provide your dataset with transaction IDs and purchased products, or describe the data source and time period covered.)

## Task

1. **Prepare the data:** Ensure it includes transaction IDs and products purchased per transaction.

2. **Explain key MBA metrics:**
   - **Support:** How frequently items appear in the dataset
   - **Confidence:** The likelihood of product Y being purchased when product X is purchased
   - **Lift:** The ratio of observed co-occurrence to expected co-occurrence if products were independent (lift > 1 indicates positive correlation)

3. **Apply the Apriori algorithm** to identify frequent itemsets from the transaction data.

4. **Generate association rules** from these itemsets, prioritizing rules with high confidence and lift values that indicate strong product relationships.

5. **Identify opportunities:**
   - Cross-selling: Products that should be marketed or placed together
   - Upselling: Premium or complementary products to suggest alongside current purchases

6. **Provide actionable recommendations** such as product bundling strategies, store layout adjustments, or targeted campaign ideas based on the strongest associations.

7. **Summarize findings** using clear visualizations and accessible language suitable for non-technical stakeholders.

## Output

**Analysis Results Table:**

| Product A | Product B | Support | Confidence | Lift |
|-----------|-----------|---------|------------|------|
| [Results from analysis] |||||

**Actionable Recommendations:**
- [Bullet point recommendations for implementation]
- [Focus on high-lift, high-confidence product pairs]
- [Specific marketing or merchandising strategies]

Keep explanations clear and avoid excessive technical jargon. Ensure all insights are based on recent, relevant data that reflects current product offerings and customer behavior.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{transaction-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Dual_Layer_Prompt_Diagnostic_Scan
- 適用 / Use when: The Market Basket Analysis Prompt for Cross-Selling is a free AI prompt that identifies which products custome…
