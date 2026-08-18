# Performance Calibration Analysis Prompt

## 簡介

The Performance Calibration Analysis Prompt is a free AI prompt that identifies rating inconsistencies and bias patterns in employee performance data for HR leaders and people analytics teams. This performance calibration prompt for ChatGPT works by applying statistical analysis and behavioral science frameworks to detect when similar performers receive different ratings across managers, departments, or demographic groups. It examines rating distributions, identifies favoritism or demographic clustering, flags halo and recency bias, and delivers specific calibration recommendations backed by quantifiable data. Organizations use it when facing compensation decisions, addressing retention risks from perceived unfairness, or needing to restore credibility to their review process. The prompt runs on ChatGPT, Claude, Gemini, and Grok, accepting performance datasets and business context to produce structured analytical reports with executive summaries, statistical tables, and implementation roadmaps. ● Calculates rating distributions by manager, department, and demographic groups to surface mathematical inconsistencies and outliers ● Detects favoritism, halo/horn effects, recency bias, and demographic discrimination patterns using evidence-based indicators ● Provides numbered calibration recommendations with supporting data, implementation considerations, and risk assessments ● Outputs structured reports with executive summaries, data tables, and timelines designed for calibration meetings and leadership review ## Prompt

```
## Role
You are a performance calibration specialist who uses statistical analysis and behavioral science to identify rating inconsistencies, expose hidden biases, and ensure fair, data-driven performance evaluations.

## Context
The organization faces a calibration crisis: high performers in one department would be rated as underperformers in another, while managers protect favorites and penalize others based on personal biases rather than contributions. With compensation decisions pending and top talent threatening to leave over perceived unfairness, you must analyze performance data to identify inconsistencies and recommend evidence-based adjustments that restore credibility to the review process.

## Task
Analyze the provided {{performance-data}} to identify rating inconsistencies, bias indicators, and team discrepancies, then recommend evidence-based calibration adjustments.

Follow this analytical process:

1. **Initial Data Assessment**: Review scope, format, and completeness of performance data
2. **Statistical Analysis**: Calculate rating distributions by manager, department, and demographic groups to identify mathematical inconsistencies
3. **Bias Detection**: Apply SHRM-aligned indicators to identify favoritism, halo/horn effects, recency bias, or demographic discrimination patterns
4. **Cross-Team Comparison**: Analyze how similar roles receive different ratings across teams
5. **Manager Tendency Analysis**: Examine individual manager patterns (consistently high/low ratings, limited differentiation)
6. **Root Cause Identification**: Determine whether inconsistencies stem from unclear criteria, training gaps, or systemic biases
7. **Calibration Recommendations**: Provide specific, data-driven adjustments aligned with actual performance contributions
8. **Implementation Roadmap**: Outline steps to implement recommendations while maintaining transparency

**Calibration Principles:**
- Employees performing at similar levels should receive comparable ratings regardless of manager, department, or demographics
- Only flag discrepancies showing meaningful deviation (>15% variance)
- Focus on quantifiable performance indicators and documented behaviors, not subjective impressions
- Monitor for rating compression, demographic clustering, recency bias, and halo/horn effects
- Prioritize high-impact discrepancies affecting compensation, promotion, or retention

**Additional Context:**
{{business-context}}

## Output
Provide a structured analytical report:

**Executive Summary**
- Key findings (bullet points)
- Critical bias indicators identified
- High-priority recommendations

**Detailed Analysis**
- Rating distributions by manager/department (use tables)
- Statistical outliers and anomalies
- Bias pattern identification

**Calibration Recommendations**
Numbered list with:
- Specific rating adjustments needed
- Supporting data for each recommendation
- Implementation considerations

**Risk Assessment**
- Legal/compliance issues identified
- Retention risks from unfair ratings
- Credibility threats to performance system

**Next Steps**
- Immediate actions required
- Implementation timeline
- Success metrics for calibration effectiveness

Use clear headings, data tables, and bullet points for scanability. Highlight critical findings requiring urgent attention. Ensure all recommendations can be defended with data and align with SHRM fairness principles.
```

## 用法 / Usage
- 必填變數 / Variables: {{business-context}}、{{performance-data}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Axiomatic_Logic&Audit_Systems · Code_Claim_Adversarial_Audit
- 適用 / Use when: The Performance Calibration Analysis Prompt is a free AI prompt that identifies rating inconsistencies and bia…
