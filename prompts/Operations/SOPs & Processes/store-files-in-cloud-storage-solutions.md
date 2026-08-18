# Cloud Storage Strategy Prompt for File Organization

## 簡介

The Cloud Storage Strategy Prompt for File Organization is a free AI prompt that creates tailored storage plans balancing security, accessibility, and collaboration for IT administrators and operations teams. This cloud storage prompt for ChatGPT guides the model to act as an expert IT administrator, analyzing your file types, cloud platform, organizational context, and security requirements to produce a detailed markdown table mapping each file type to its optimal storage location and access permissions. It runs on ChatGPT, Claude, and Gemini, delivering both the strategic table and a rationale section that explains key decisions around storage tier optimization, performance needs, compliance considerations, and cost efficiency. Use it when migrating to cloud storage, auditing existing file organization practices, or establishing governance policies for team collaboration. ● Maps file types to storage locations based on size, access frequency, security classification, and collaboration patterns ● Generates access permission recommendations aligned with team roles, compliance requirements, and data protection policies ● Explains the rationale behind storage tier assignments, helping justify decisions to stakeholders and guide rollout planning ● Considers cost efficiency across storage tiers while maintaining performance and security standards ## Prompt

```
## Role
You are an expert IT administrator specializing in cloud storage optimization for productivity and collaboration.

## Task
Create a comprehensive storage strategy that maps file types to optimal storage locations and access permissions. Develop recommendations that balance security, accessibility, collaboration needs, and performance.

## Context
File types: {{file-types}}
Cloud platform: {{cloud-platform}}
Organization context: {{org-context}}
Security requirements: {{security-requirements}}

Consider:
- File size and storage tier optimization
- Access frequency and performance needs
- Collaboration patterns and sharing requirements
- Compliance and data classification
- Cost efficiency across storage tiers

## Output
Deliver your storage strategy as a markdown table:

| File Type | Storage Location | Access Permissions |
|-----------|------------------|--------------------|

Provide at least 5 rows mapping file types to their optimal storage solutions.

Follow the table with a rationale section explaining the key decisions: why each file type was assigned to its storage location, how access permissions support collaboration while maintaining security, and any implementation considerations for rolling out this strategy.
```

## 用法 / Usage
- 必填變數 / Variables: {{cloud-platform}}、{{file-types}}、{{org-context}}、{{security-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Skill_Prompt_Spec_Extractor
- 適用 / Use when: The Cloud Storage Strategy Prompt for File Organization is a free AI prompt that creates tailored storage plan…
