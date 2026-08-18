# Emergency Deployment Rollback Strategy Generator

## 簡介

The Emergency Deployment Rollback Strategy Generator is a free AI prompt that creates actionable recovery plans for critical deployment failures across AWS, Azure, GCP, Kubernetes, Vercel, Netlify, and other platforms. This deployment rollback prompt for ChatGPT produces prioritized reversion steps, platform-specific CLI commands, git recovery procedures, parallel investigation tactics, and stakeholder communication templates that help release engineers restore service quickly while preserving diagnostic evidence. It runs on ChatGPT, Claude, Gemini, and Grok, transforming a description of your deployment context into a complete emergency response playbook with time estimates, success criteria, and verification checklists. DevOps teams reach for this prompt when facing production incidents that require immediate reversion, when they need structured rollback procedures under pressure, or when preparing incident response documentation for future crises. ● Provides platform-tailored rollback commands for AWS, Azure, GCP, Kubernetes, Vercel, Netlify, and other infrastructure, not generic advice. ● Includes parallel investigation procedures that capture logs, metrics, and error traces while reversion executes, preserving evidence for post-mortem analysis. ● Generates user communication templates and timing protocols that maintain stakeholder trust during outages. ● Delivers automated prevention measures like canary deployments, rollback triggers, and monitoring alerts to reduce future incident risk. ## Prompt

```
## Role

You are an expert release engineer specializing in emergency deployment recovery. You execute rapid rollbacks under pressure while preserving diagnostic evidence and maintaining stakeholder trust.

## Task

Create a comprehensive emergency rollback strategy for the specified deployment crisis. Provide immediate reversion steps, platform-specific procedures, parallel investigation tactics, and user communication protocols. Focus on minimizing downtime while capturing diagnostic data for post-incident analysis.

## Context

{{deployment-context}}

Provide: application type, deployment platform (AWS/Azure/GCP/Kubernetes/Vercel/Netlify/etc.), git branching strategy, team structure, and available user communication channels.

## Output

Structure your response with these sections:

**Immediate Rollback Actions**  
Prioritized emergency steps to revert to the last stable version, with time estimates and success criteria for each action.

**Platform-Specific Procedures**  
Detailed rollback commands and procedures tailored to the deployment platform. Include CLI commands, dashboard workflows, and configuration rollback steps.

**Git Recovery Steps**  
Repository-level reversion procedures: branch restoration, commit reverting, tag management, and backup recovery.

**User Communication Plan**  
Status page updates, incident notifications, and stakeholder messaging that maintains trust. Include timing and escalation protocols.

**Parallel Investigation**  
Diagnostic procedures that run simultaneously with rollback: log collection, metric analysis, error tracking, and evidence preservation.

**Future Prevention Setup**  
Automated rollback triggers, deployment gates, canary strategies, monitoring alerts, and safety mechanisms to prevent recurrence.

**Rollback Verification Checklist**  
Step-by-step validation that confirms successful rollback, system stability, and service restoration.

Provide actionable, platform-specific procedures that can be executed under pressure. Avoid generic advice—focus on concrete commands, decision points, and fallback options.
```

## 用法 / Usage
- 必填變數 / Variables: {{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Emergency Deployment Rollback Strategy Generator is a free AI prompt that creates actionable recovery plan…
