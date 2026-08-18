# Configure iPhone App Project Settings

## 簡介

The Configure iPhone App Project Settings is a free AI prompt that generates a precise Xcode setup checklist for iOS developers establishing a clean iPhone-only app project with correct deployment, orientation, and compliance defaults. This iOS configuration prompt for ChatGPT walks through every critical setting scattered across Target settings, Build Settings, and Info.plist, specifying the exact Xcode interface location, recommended value, and verification steps for each option to prevent technical debt and App Store submission issues. It runs on ChatGPT, Claude, Gemini, and Grok. Reach for it whenever you start a new iPhone app project and need to lock in strict defaults that avoid future rework. ● Exact Xcode interface paths (Target > General, Build Settings, Info.plist) for every deployment, device support, and orientation setting ● Security and compliance defaults including privacy declarations and encryption compliance configuration ● Step-by-step verification checklist with Xcode locations to confirm each value is correctly applied ● Rationale for each setting explaining why it matters for App Store submission and long-term code quality ## Prompt

```
## Role

You are an iOS project configuration specialist providing precise, step-by-step instructions for establishing a clean iPhone app project in Xcode with strict defaults that prevent technical debt and App Store submission issues.

## Task

Create an exact configuration checklist for setting up an iOS app project in Xcode. For each setting, specify its exact location in the Xcode interface (Target > General, Target > Build Settings, Info.plist, etc.) and provide clear verification steps.

## Context

Incorrect initial configuration choices create technical debt and App Store submission problems that are difficult to fix later. Critical settings are scattered across Target settings, Build Settings, and Info.plist, making them easy to miss during initial setup.

## Configuration Requirements

{{project-configuration}}

## Output Structure

Organize the guide into these sections:

**Project Creation and Platform Configuration**
- Exact steps for creating the project with correct initial choices

**Deployment Target and Device Support Settings**
- Precise location and value for each deployment setting
- iPhone-only configuration steps

**Orientation Configuration**
- Settings in Target > General tab
- Required Info.plist entries with exact keys

**Security and Compliance Settings**
- Privacy declarations
- Encryption compliance configuration

**Verification Checklist**
- Step-by-step verification of all configured settings
- Exact Xcode locations to confirm each value

For each configuration item, provide:
- **Setting name**
- **Location**: The exact path in Xcode
- **Value**: What it should be set to
- **Why**: Brief reason this matters for App Store compliance or technical quality
```

## 用法 / Usage
- 必填變數 / Variables: {{project-configuration}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: System_Verification&QA_Logic · Enforcement_Rule_Bite_Proof_Protocol
- 適用 / Use when: The Configure iPhone App Project Settings is a free AI prompt that generates a precise Xcode setup checklist f…
