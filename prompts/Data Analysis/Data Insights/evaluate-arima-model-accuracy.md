# ARIMA Model Accuracy Evaluation for Time Series

## 簡介

The ARIMA Model Accuracy Evaluation for Time Series is a free AI prompt that rigorously assesses ARIMA forecasting models for specialists working with educational or operational time series data. This time series evaluation prompt for ChatGPT, Claude, Gemini, and Grok goes beyond standard accuracy metrics to expose model weaknesses that MAE and RMSE often hide. It implements time series cross-validation, residual diagnostics, and multi-horizon performance testing to reveal how well an ARIMA model handles seasonal variations, structural breaks, and bounded outcomes like completion rates or utilization percentages. Real-world use cases include validating enrollment forecasts for university resource planning, testing course completion predictions for staffing decisions, and stress-testing operational forecasts against policy changes or external disruptions. Reach for this prompt when you need to validate an ARIMA model against real-world conditions before trusting it for planning decisions, or when standard in-sample fit statistics don't tell you whether your forecast will hold up across changing behavioral patterns. ● Implements rolling-origin and walk-forward cross-validation to test performance across realistic forecasting horizons. ● Diagnoses residual autocorrelation, heteroscedasticity, and normality violations that signal flawed model assumptions. ● Compares bounded-data metrics and directional accuracy alongside MAE, RMSE, and MAPE to avoid misleading conclusions. ● Translates statistical results into decision thresholds for resource allocation, budget planning, and operational staffing. ## Prompt

```
## Role
You are a time series validation specialist focused on educational forecasting. You stress-test ARIMA models against real-world disruptions (seasonal shifts, structural breaks, behavioral pattern changes) that standard accuracy metrics often miss, ensuring forecasts support reliable resource planning.

## Task
Evaluate the predictive performance of an ARIMA model applied to monthly course completion rates. Provide a rigorous assessment that exposes weaknesses hidden by conventional validation approaches.

## Context
{{dataset-and-model-specs}}

**Educational time series challenges:**
- Seasonal variations tied to academic calendars
- External disruptions (policy changes, global events)
- Natural bounds on completion rates (0–100%)
- Unpredictable shifts in student behavior patterns

Standard accuracy metrics may mask critical failures in capturing trend changes essential for planning decisions.

## Output
Deliver a comprehensive evaluation structured as follows:

### 1. Evaluation Methodology Overview
Explain ARIMA model validation tailored to educational time series, emphasizing stress-testing against edge cases.

### 2. Step-by-Step Assessment Process
- **Data preparation:** stationarity checks, handling of academic calendar effects
- **Model specification verification:** confirm ARIMA(p,d,q) parameters are appropriate
- **Accuracy metrics:** calculate and compare MAE, RMSE, MAPE, and bounded-specific measures; explain which matter most for resource planning
- **Time series cross-validation:** implement rolling-origin or walk-forward validation
- **Residual diagnostics:** test for autocorrelation, heteroscedasticity, normality; assess assumption violations
- **Multi-horizon performance:** evaluate accuracy across 1-month, 3-month, 6-month forecasts

### 3. Common Pitfalls
Critically analyze mistakes often made when evaluating ARIMA models on course completion data (e.g., ignoring structural breaks, over-relying on in-sample fit, misinterpreting MAPE with bounded data).

### 4. Practical Interpretation
Translate statistical results into educational context: what error thresholds are acceptable for enrollment planning, budget allocation, staffing decisions?

### 5. Limitations of Standard Metrics
Address why MAE/RMSE alone may mislead; suggest complementary approaches (e.g., directional accuracy, peak-detection performance, interval forecasts).

### 6. Alternative Evaluation Approaches
Recommend methods to capture nuances: scenario analysis, comparison with naïve/seasonal benchmarks, sensitivity testing against parameter uncertainty.

### 7. Summary Table
Present a comparison table of accuracy metrics with practical thresholds and use-case suitability.

### 8. Actionable Next Steps
Provide clear recommendations based on evaluation findings: model adjustments, data collection priorities, or alternative forecasting methods if ARIMA proves inadequate.

**Format:** Use headings, bullet points, and **bold** for critical warnings. Include pseudocode or code snippets for key procedures (backtesting loop, residual tests). Keep explanations practical; avoid jargon without interpretation.
```

## 用法 / Usage
- 必填變數 / Variables: {{dataset-and-model-specs}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The ARIMA Model Accuracy Evaluation for Time Series is a free AI prompt that rigorously assesses ARIMA forecas…
