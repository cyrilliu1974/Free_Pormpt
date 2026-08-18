# Cloud Archive Comparison for Education Institutions

## 簡介

The Cloud Archive Comparison for Education Institutions is a free AI prompt that helps IT consultants and education technology leaders evaluate and compare cloud storage providers against criteria specific to schools and universities. This cloud storage comparison prompt for ChatGPT guides the model to research 4-5 major archiving platforms - analyzing storage capacity, data security and encryption, compliance with FERPA, COPPA, and GDPR, pricing models, integration with existing educational systems, backup options, and user access controls. You specify your institution name, the data types you need to archive (student records, learning management data, research files), and the table columns you want, and the prompt returns a structured markdown table with actionable insights and a recommendation summary. Use it when evaluating vendors for a cloud migration project, responding to an RFP, or advising administrators on secure, compliant data storage. ● Compares storage capacity, scalability, encryption, and compliance (FERPA, COPPA, GDPR) across multiple providers ● Evaluates cost-effectiveness, pricing models, and integration with learning management systems ● Outputs findings in a customizable markdown table with your chosen columns ● Includes a recommendation summary explaining which solution best fits your institution and data types ## Prompt

```
## Role
You are an expert IT consultant specializing in cloud storage solutions for educational institutions.

## Task
Research and compare cloud archiving solutions suitable for educational institutions. Conduct a thorough analysis considering:
- Storage capacity and scalability
- Data security features and encryption
- Compliance with educational regulations (FERPA, COPPA, GDPR where applicable)
- Cost-effectiveness and pricing models
- Integration capabilities with existing educational systems
- Backup and disaster recovery options
- User access controls and administrative features

## Context
Institution: {{institution-name}}
Data types to be stored: {{data-types}}

## Output
Present your findings in a markdown table with these columns: {{table-columns}}

Ensure the table:
- Compares at least 4-5 major cloud archiving providers
- Provides specific, actionable information in each cell
- Highlights strengths and limitations relevant to educational use cases
- Includes a brief recommendation summary below the table explaining which solution best fits the institution's needs based on the data types specified
```

## 用法 / Usage
- 必填變數 / Variables: {{data-types}}、{{institution-name}}、{{table-columns}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Cloud Archive Comparison for Education Institutions is a free AI prompt that helps IT consultants and educ…
