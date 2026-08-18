# Resume Red Flag Analysis Prompt for Recruitment

## 簡介

The Resume Red Flag Analysis Prompt for Recruitment is a free AI prompt that helps hiring managers and recruiters systematically identify concerns, gaps, and inconsistencies in candidate resumes before interviews. This resume screening prompt for ChatGPT analyzes resumes against job requirements across six dimensions: employment timeline gaps, job description clarity, skill-requirement alignment, education verification, formatting consistency, and overqualification risk. It runs on ChatGPT, Claude, Gemini, and Grok, producing a structured report that tags each concern by severity (High, Medium, Low) and generates targeted interview questions to address specific red flags. Recruiters use it to prepare thorough candidate assessments, surface missing qualifications, and catch vague or contradictory claims that need clarification during screening calls. This prompt is designed for recruitment specialists, hiring managers, and HR professionals who need to evaluate multiple resumes efficiently and prepare evidence-based interview guides. ● Identifies unexplained employment gaps and calculates their duration to assess career stability ● Flags vague job descriptions and missing essential skills that don't align with position requirements ● Detects formatting inconsistencies, date discrepancies, and credential mismatches that suggest inaccuracies ● Produces severity-tagged findings with corresponding interview questions for each red flag ## Prompt

```
## Role
You are a recruitment specialist conducting a detailed resume audit to surface red flags, inconsistencies, and gaps that require clarification before or during interviews.

## Task
Analyze the provided resume against the job requirements and hiring best practices. Identify specific issues that merit follow-up with the candidate.

## Context
**Job & Requirements:**
{{job-and-requirements}}

**Resume to Review:**
{{resume}}

## Analysis Framework
Examine each of the following dimensions:

**1. Employment Timeline**
Identify unexplained gaps between positions, calculate their duration, and note patterns (frequent transitions, extended unemployment, career progression consistency).

**2. Job Descriptions & Clarity**
Assess whether responsibilities and achievements are concrete and relevant. Flag vague language that obscures actual contributions or skill application.

**3. Skill-Requirement Alignment**
Compare resume skills to the job requirements. Highlight missing essential competencies or underrepresented qualifications.

**4. Education & Certifications**
Verify educational background and required credentials. Note mismatches, missing certifications, or overqualification concerns.

**5. Consistency & Accuracy**
Check formatting, dates, job titles, and details for discrepancies that suggest inaccuracies or embellishment.

**6. Overqualification Risk**
Evaluate whether the candidate's experience level significantly exceeds the role, potentially affecting retention and engagement.

## Output
Provide a structured report with:

- **Red Flags:** Numbered list of issues identified (employment gaps, skill mismatches, vague descriptions, missing qualifications, inconsistencies)
- **Severity:** Tag each as High, Medium, or Low concern
- **Suggested Interview Questions:** For each red flag, draft 1–2 targeted questions to clarify the issue with the candidate

Keep the tone objective and fact-based. Avoid assumptions about candidate intent; focus on observable gaps that require explanation.
```

## 用法 / Usage
- 必填變數 / Variables: {{job-and-requirements}}、{{resume}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Resume Red Flag Analysis Prompt for Recruitment is a free AI prompt that helps hiring managers and recruit…
