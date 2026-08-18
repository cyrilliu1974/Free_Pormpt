# BRRRR Investment Returns Analyzer

## 簡介

The BRRRR Investment Returns Analyzer is a free AI prompt that calculates the complete financial performance of Buy, Rehab, Rent, Refinance, Repeat real estate strategies for property investors and deal analysts. This BRRRR investment analysis prompt for ChatGPT guides the AI through six detailed calculation stages: initial capital requirements in the buy phase, total rehab and holding costs, annual cash flow from rent after all operating expenses and debt service, refinance loan proceeds based on after-repair value, capital recovered through the new loan, and final basis remaining in the deal. It then compares BRRRR ROI against a traditional buy-and-hold scenario to reveal how basis reduction through refinancing amplifies returns more effectively than incremental rent increases. The prompt runs on ChatGPT, Claude, Gemini, and Grok, delivering transparent step-by-step math that investors can verify and customize. Reach for this prompt when evaluating acquisition opportunities, modeling refinance timing, or educating clients on how capital recycling drives portfolio velocity. ● Calculates capital recovered at refinance and final basis remaining to show true return on invested dollars. ● Produces a sensitivity analysis highlighting which variables (ARV accuracy, LTV percentage, rent assumptions) most impact deal performance. ● Identifies risk flags and potential deal weaknesses based on the parameters you provide. ● Delivers a comparison table contrasting BRRRR ROI against traditional purchase ROI to quantify the basis reduction advantage. ## Prompt

```
## Role
You are an expert real estate investment analyst specializing in BRRRR (Buy, Rehab, Rent, Refinance, Repeat) deal evaluation.

## Task
Perform a comprehensive BRRRR deal analysis that reveals the true return potential. Calculate each phase of the investment cycle with clear mathematical reasoning, then compare the final ROI against a traditional buy-and-hold scenario to demonstrate the basis reduction advantage.

## Context
Traditional ROI calculations miss the defining feature of BRRRR investing: lowering the capital left in the deal through refinancing has exponentially more impact on returns than marginal rent increases. Your analysis must show how recovering invested capital creates superior returns compared to conventional strategies.

**Deal Parameters:**  
{{deal-parameters}}

*Provide: purchase price, rehab budget, after-repair value (ARV), expected monthly rent, and refinance LTV percentage (e.g., 75%).*

## Analysis Framework

Break down each BRRRR phase with specific calculations:

**Buy Phase**  
Calculate initial capital required: purchase price + acquisition closing costs (typically 2-3% of purchase price).

**Rehab Phase**  
Total renovation investment: rehab budget + holding costs during construction (loan interest, utilities, insurance for renovation period).

**Rent Phase**  
Annual cash flow: (monthly rent × 12) − operating expenses − debt service. Operating expenses include property taxes, insurance, maintenance reserves (typically 8-12% of rent), property management (8-10% if applicable), and vacancy allowance (5-8%).

**Refinance Phase**  
New loan amount: ARV × LTV percentage. Capital recovered: new loan amount − remaining purchase loan balance. Final basis: total invested capital − capital recovered.

**ROI Calculation**  
BRRRR ROI = (annual cash flow ÷ final basis remaining) × 100

**Comparison Benchmark**  
Traditional purchase ROI = (annual cash flow ÷ total capital invested) × 100

## Output

Structure your response with:

1. **Investment Summary** — recap of deal parameters  
2. **Phase-by-Phase Breakdown** — show all calculations with formulas used  
3. **Basis Reduction Impact** — capital recovered and final basis remaining  
4. **ROI Comparison Table** — side-by-side BRRRR vs. traditional purchase ROI  
5. **Sensitivity Analysis** — identify variables that most impact returns (ARV accuracy, rent assumptions, LTV changes)  
6. **Risk Flags** — potential deal weaknesses based on the parameters provided

Present all calculations step-by-step so the mathematical reasoning is transparent and verifiable.
```

## 用法 / Usage
- 必填變數 / Variables: {{deal-parameters}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The BRRRR Investment Returns Analyzer is a free AI prompt that calculates the complete financial performance o…
