# HTTPS Setup Plan Generator for Websites

## 簡介

The HTTPS Setup Plan Generator for Websites is a free AI prompt that creates a structured migration plan to secure any website with SSL/TLS encryption and improve search engine visibility. This HTTPS setup prompt for ChatGPT walks through every phase of the transition: selecting and purchasing the right SSL certificate type, installing it on your web server, configuring 301 redirects from HTTP to HTTPS, updating internal links and third-party integrations, verifying the implementation with SSL checker tools, and setting up renewal reminders. It runs on ChatGPT, Claude, Gemini, and Grok, adapting the technical detail to match your server environment and producing time estimates for each phase. DevOps engineers, web developers, and site administrators use it to plan secure deployments, avoid mixed-content warnings, and meet compliance requirements without missing critical configuration steps. Reach for this prompt when migrating an existing site to HTTPS, launching a new domain with security-first architecture, or auditing an SSL setup before a compliance review. ● Recommends the correct SSL certificate type based on site requirements and lists reputable certificate authorities. ● Provides server-specific installation instructions, 301 redirect rules, and mixed-content resolution steps. ● Includes post-deployment testing with SSL checker tools, browser verification, and SEO performance tracking. ● Sets up a maintenance schedule with certificate renewal reminders and security log monitoring. ## Prompt

```
## Role
You are a web security expert specializing in HTTPS implementation, SSL certificate management, and server configuration for security and SEO optimization.

## Task
Create a comprehensive, step-by-step plan for setting up HTTPS on {{website-url}} to enhance security and SEO performance. Include certificate acquisition, installation, redirection configuration, and verification procedures.

## Output
Structure your plan with these sections:

**Objective**
State the primary goal of implementing HTTPS for this website.

**Prerequisites**
- 🔑 Server and domain access requirements
- 💳 Budget considerations
- 📧 Contact information needs

**Step-by-Step Plan**

1. **Purchase SSL Certificate**
   - Recommend certificate type based on website needs
   - List reputable certificate authorities
   - 🕐 Estimated Time: [specify]

2. **Install SSL Certificate**
   - 📌 Key Steps:
     - Certificate generation process
     - Server-specific installation instructions
     - Verification of successful installation
   - 🕐 Estimated Time: [specify]

3. **Update Website Configuration**
   - 📌 Key Steps:
     - Configure HTTP to HTTPS redirects (301 permanent)
     - Update internal links and resources
     - Modify configuration files
   - 🕐 Estimated Time: [specify]

4. **Update External Links and Services**
   - 📌 Key Steps:
     - Update CDN and third-party service configurations
     - Modify API endpoints
     - Update social media and external references
   - 🕐 Estimated Time: [specify]

5. **Test and Verify HTTPS Implementation**
   - 📌 Key Steps:
     - Run SSL checker tools
     - Test redirect functionality
     - Verify mixed content resolution
     - Check browser security indicators
   - 🕐 Estimated Time: [specify]

6. **Monitor and Maintain**
   - 📌 Key Steps:
     - Set up certificate renewal reminders
     - Monitor security logs
     - Track SEO performance changes
   - 🕐 Estimated Time: [specify ongoing]

**Summary**
Provide total estimated implementation time, recap key security and SEO benefits, and emphasize the importance of ongoing certificate renewal and monitoring.

Present all information in clear, accessible language with specific actionable guidance for each step.
```

## 用法 / Usage
- 必填變數 / Variables: {{website-url}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The HTTPS Setup Plan Generator for Websites is a free AI prompt that creates a structured migration plan to se…
