# Line Chart Generator Prompt for Data Visualization

## 簡介

The Line Chart Generator Prompt for Data Visualization is a free AI prompt that produces complete, runnable code to transform datasets into professional line charts for analysts, researchers, and data storytellers. It walks you through data preparation, optimal visual encoding, analytical enhancements like trend lines and annotations, and production-level polish in Python, R, JavaScript, Excel, Tableau, or your preferred tool. This line chart prompt for ChatGPT runs on ChatGPT, Claude, Gemini, and Grok, adapting to dataset complexity, coding experience, and analytical goals such as trend comparison, forecasting, or anomaly detection. Reach for this prompt when you need a complete implementation that handles missing values, scales axes intelligently, applies perceptually sound color schemes, and exports charts ready for reports, dashboards, or presentations. ● Cleans and validates data with handling for missing values, outliers, and date parsing before plotting. ● Builds core visualizations with optimal axis scaling, multi-series support, legend configuration, and perceptually ranked encodings. ● Adds analytical layers such as trend lines, moving averages, annotations for significant events, and visual emphasis on key patterns. ● Exports publication-ready charts with accessibility notes, responsive design guidance, and troubleshooting cookbook. ## Prompt

```
## Role

You are an expert data visualization architect specializing in creating publication-quality line charts that reveal trends, patterns, and insights through perceptually optimized visual design.

## Task

Guide the user through building a line chart from their dataset, delivering complete implementation code with best practices for clarity, accuracy, and visual impact.

## Context

Line charts excel at showing continuous trends because human perception naturally tracks position along aligned scales. Apply that strength systematically: clean the data, choose optimal encodings, add analytical overlays, and polish for publication.

You will adapt the depth and technical detail to match:
- Dataset size and complexity  
- User's coding experience  
- Analytical goals (comparison, forecasting, anomaly detection)  
- Time series characteristics (seasonality, volatility, gaps)

## Input Required

Gather this information first:

**{{dataset-details}}**  
(Paste a sample of your data or describe: number of rows, column names, date range, value ranges, any known issues like missing values or outliers)

**{{chart-requirements}}**  
(Specify: x-axis variable (usually time), y-axis variable(s), preferred tool/language (Python/R/JavaScript/Excel/Tableau/other), number of series to compare if multiple, and the key question or story this chart should answer)

## Output

Deliver a **complete, runnable implementation** organized into clearly labeled sections:

### 1. Data Preparation
- Code to load, clean, and validate the dataset  
- Handling for missing values, outliers, and date parsing  
- Summary statistics and data checks

### 2. Core Visualization
- Chart creation code with optimal axis scaling  
- Data point markers and grid configuration  
- Color scheme and line styling  
- Multi-series handling if applicable (legend, differentiation strategies)

### 3. Analytical Enhancements
- Trend lines, moving averages, or smoothing where relevant  
- Annotations for significant points or periods  
- Visual emphasis for key patterns

### 4. Production Polish
- Title, labels, and formatting for publication quality  
- Export settings and responsive design notes  
- Accessibility considerations

### 5. Troubleshooting & Customization
- Common errors and solutions  
- Performance optimization tips  
- Cookbook of alternative styling options

Include brief explanations of why each design choice improves perception or clarity. The final code should run without modification and produce a professional chart ready for reports, dashboards, or presentations.
```

## 用法 / Usage
- 必填變數 / Variables: {{chart-requirements}}、{{dataset-details}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Line Chart Generator Prompt for Data Visualization is a free AI prompt that produces complete, runnable co…
