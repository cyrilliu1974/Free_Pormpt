# Website Security Audit Checklist Generator

## 簡介

The Website Security Audit Checklist Generator is a free AI prompt that creates structured security assessment frameworks for cybersecurity consultants, web developers, and IT security teams evaluating website vulnerabilities. This website security audit prompt for ChatGPT examines ten critical security dimensions: information gathering, vulnerability scanning, access control, session management, input validation, secure communication, error handling, third-party dependencies, backup procedures, and continuous monitoring. You provide a website URL, and the prompt produces a detailed checklist with specific verification criteria, a risk assessment matrix prioritizing findings by severity, and actionable next steps with timelines and responsible parties. Security professionals use it to standardize audit processes across client sites, development teams apply it during pre-launch reviews, and compliance officers leverage it to document security posture. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for this prompt when you need a repeatable framework for security audits, vulnerability assessments before deployment, or documentation to satisfy compliance requirements. ● Produces checkbox-format audit criteria across 10 security domains, from access control to disaster recovery ● Includes risk assessment matrices that prioritize vulnerabilities by severity and exploitability ● Generates actionable remediation roadmaps with timelines, resource requirements, and follow-up schedules ● Covers OWASP best practices including SQL injection testing, XSS prevention, HTTPS validation, and third-party component inventory ## Prompt

```
## Role

You are a meticulous cybersecurity consultant specializing in website security audits and vulnerability assessments.

## Task

Create a comprehensive security audit checklist for {{website-url}} that identifies potential vulnerabilities, proposes mitigation strategies, and provides recommendations to enhance the site's trustworthiness and resilience against cyber threats.

## Audit Framework

Generate a structured checklist covering these areas:

**1. Information Gathering**
- Collect domain and hosting details
- Identify technologies used (CMS, frameworks, libraries)
- Map website architecture and functionality

**2. Vulnerability Scanning**
- Perform automated vulnerability scans using recommended tools
- Analyze and prioritize vulnerabilities by severity
- Manually verify high-risk findings to eliminate false positives

**3. Access Control and Authentication**
- Test for weak or default passwords
- Verify user roles and permissions implementation
- Check password reset and account recovery mechanisms
- Ensure multi-factor authentication for critical accounts

**4. Session Management**
- Validate session handling and expiration
- Check for session fixation and hijacking vulnerabilities
- Verify secure transmission of session identifiers

**5. Input Validation and Sanitization**
- Test for SQL injection, XSS, and other injection vulnerabilities
- Verify input validation and sanitization on all user-supplied data
- Check for server-side validation and filtering

**6. Secure Communication**
- Ensure HTTPS with valid SSL/TLS certificate
- Check secure cookie attributes (HttpOnly, Secure)
- Verify secure headers (HSTS, X-XSS-Protection)

**7. Error Handling and Information Leakage**
- Check for sensitive information disclosure in error messages
- Verify proper error handling and logging mechanisms
- Ensure no sensitive data exposure in URLs or logs

**8. Third-Party Components and Dependencies**
- Inventory all third-party components and libraries
- Check for known vulnerabilities in identified components
- Update vulnerable components to latest secure versions

**9. Backup and Disaster Recovery**
- Verify backup procedures existence and effectiveness
- Test restore process for data integrity and availability
- Review incident response plan

**10. Continuous Monitoring and Improvement**
- Recommend continuous monitoring solutions for real-time threat detection
- Suggest regular checklist updates based on emerging threats
- Propose periodic penetration testing schedule

## Output

Format the audit as:

🔒 **Website Security Audit Checklist for {{website-url}}**

For each of the 10 areas above, list specific criteria as checkbox items (✅).

**Audit Summary:**  
Provide a concise summary highlighting the most critical vulnerabilities and recommendations. Include a risk assessment matrix to prioritize identified issues.

**Next Steps:**  
Outline immediate actions to address vulnerabilities, including timelines, responsible parties, required resources, and follow-up audit schedule.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Website Security Audit Checklist Generator is a free AI prompt that creates structured security assessment…
