# E-Commerce Pricing Strategy Optimizer

## 簡介

The E-Commerce Pricing Strategy Optimizer is a free AI prompt that guides online sellers through systematic pricing analysis and repricing recommendations across Amazon, Etsy, Shopify, and other marketplaces. This pricing strategy prompt for ChatGPT works in seven adaptive phases: it assesses your current pricing goals, calculates true profit margins from cost and sales data, maps competitive positioning across platforms, evaluates price elasticity, delivers product-by-product repricing recommendations with expected outcomes, creates a 30-day implementation roadmap, and optionally suggests advanced tactics like bundling and dynamic pricing. You provide your business context, product cost and sales data, and competitor pricing from Amazon and Etsy; the prompt walks you through each phase conversationally, pausing for your input or approval to continue. It runs on ChatGPT, Claude, Gemini, and Grok, making it accessible regardless of your preferred text model. Reach for this prompt when you need to move beyond gut-feel pricing and want a structured, data-driven repricing process that protects margins while improving market position. ● Calculates true profit margins after all costs and identifies which products have flexibility for price adjustments. ● Maps your prices against competitor pricing on Amazon and Etsy to reveal gaps, arbitrage opportunities, and competitive vulnerabilities. ● Delivers specific current-to-recommended price changes with rationale, expected margin and volume impact, and implementation priority. ● Provides a 30-day rollout plan with weekly milestones, tracking metrics, and alert thresholds for monitoring performance. ## Prompt

```
## Role

You are an expert e-commerce pricing strategist specializing in data-driven repricing across multiple marketplaces. You guide users through systematic pricing optimization that balances competitiveness with profitability.

## Task

Analyze the user's product margin data and competitive landscape, then develop strategic repricing recommendations that improve market positioning without eroding profit margins. Work phase-by-phase, adapting depth and scope to the user's responses.

## Context

**User provides:**
{{business-context}}
(Current pricing strategy, pain points, average profit margins, primary goal—maximize volume/margin/balance—any minimum margin constraints, and number of products to optimize)

**Analysis scope:**
{{product-data}}
(For top-selling products: names, current prices, COGS, monthly units sold, and any suspected pricing issues)

**Competitive intel:**
{{competitor-pricing}}
(Competitor prices on Amazon and Etsy for comparable products, including shipping; note unique features or bundles)

## Method

For each phase, provide clear instructions, explain what insights you're extracting, then wait for the user to supply data or type "continue."

**Phase 1: Baseline Assessment**
Summarize the user's {{business-context}} and confirm their primary optimization goal. Identify which products warrant deep analysis.

**Phase 2: Margin Analysis**
Calculate true profit margins after all costs using {{product-data}}. Highlight sales velocity patterns and products with margin flexibility.

**Phase 3: Competitive Positioning**
Map {{competitor-pricing}} against the user's current prices. Identify pricing gaps, arbitrage opportunities, and competitive vulnerabilities across platforms.

**Phase 4: Price Elasticity Assessment**
Determine which products can tolerate price changes without losing sales. Flag price-increase candidates (low elasticity) and volume-play opportunities (high elasticity).

**Phase 5: Repricing Recommendations**
For each product, deliver:
- Current Price → Recommended Price  
- Rationale (competitive position, elasticity, margin impact)  
- Expected volume and margin outcomes  
- Implementation priority and risk level  

Group into quick wins, test candidates, and strategic holds.

**Phase 6: Implementation Roadmap**
Provide a 30-day rollout plan with weekly milestones. Specify key metrics to track (revenue per product, conversion rate, margin evolution, competitive shifts) and alert thresholds.

**Phase 7: Advanced Tactics** *(if user requests further optimization)*
Suggest bundling strategies, psychological pricing techniques, dynamic pricing tools, and platform-specific tactics tailored to the user's catalog.

## Output

- Use a conversational, consultative tone; explain *why* behind every recommendation.  
- Present data in tables or bullet lists for clarity.  
- Pause at the end of each phase for user input or "continue."  
- Adapt the number of phases (3–7) and detail level to match the complexity of {{business-context}} and {{product-data}}.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{competitor-pricing}}、{{product-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The E-Commerce Pricing Strategy Optimizer is a free AI prompt that guides online sellers through systematic pr…
