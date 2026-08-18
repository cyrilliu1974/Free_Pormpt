# Reference Management System Design Prompt

## 簡介

The Reference Management System Design Prompt is a free AI prompt that generates detailed implementation plans for building reference management tools tailored to educational institutions and research teams. This reference management system prompt for ChatGPT, Claude, and Gemini produces a structured technical specification covering citation generation, source organization, collaboration features, database integration, and deployment strategy. You provide your institution details and technical requirements, and the AI outputs a comprehensive plan with core features (multi-format citation generation, PDF annotation, duplicate detection), integration specifications for academic databases and writing software, architecture recommendations for security and scalability, and a phased rollout strategy. Software developers, IT administrators, and academic technology teams use it to blueprint custom reference management solutions that fit institutional needs. ● Outputs structured plans with automatic citation generation supporting APA, MLA, Chicago, IEEE, and other academic styles ● Includes real-time collaboration tools, shared libraries with permissions, and integration specs for PubMed, JSTOR, Google Scholar, and writing platforms ● Addresses user experience design for novice and advanced researchers, data security compliance, and cloud versus on-premise deployment ● Provides rollout phases, training material recommendations, and API design guidance for third-party integrations ## Prompt

```
## Role
You are an expert software developer specializing in reference management systems.

## Task
Design a comprehensive reference management tool for an educational institution that helps students and researchers organize, store, and cite research sources.

## Context
Institution and users: {{institution-and-users}}
Technical requirements: {{technical-requirements}}

## Output
Provide a detailed implementation plan structured with main sections and subsections. Use bullet points for features and design considerations.

Your plan must address:

**Core Features**
- Automatic citation generation supporting multiple styles (APA, MLA, Chicago, IEEE)
- Source organization with tags, folders, and smart collections
- PDF annotation and note-taking capabilities
- Duplicate detection and metadata cleanup

**Collaboration & Integration**
- Real-time collaboration tools for research teams
- Shared libraries with permission controls
- Integration with academic databases (PubMed, IEEE Xplore, JSTOR, Google Scholar)
- Plugins for writing software (Microsoft Word, Google Docs, LaTeX, Overleaf)
- Browser extensions for one-click citation capture

**Architecture & Implementation**
- User experience design principles for both novice and advanced users
- Data security measures including encryption, backup strategies, and compliance with institutional policies
- Scalability considerations for concurrent users and growing reference libraries
- Cloud vs. on-premise deployment options
- API design for third-party integrations

**Deployment & Support**
- Rollout phases and user onboarding strategy
- Training materials and documentation
- Maintenance and update procedures

Format your response with clear headings, subheadings, and actionable bullet points.
```

## 用法 / Usage
- 必填變數 / Variables: {{institution-and-users}}、{{technical-requirements}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Reference Management System Design Prompt is a free AI prompt that generates detailed implementation plans…
