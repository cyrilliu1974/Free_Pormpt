# AI Interaction Log Database Schema Designer

## 簡介

The AI Interaction Log Database Schema Designer is a free AI prompt that creates complete database architectures for capturing and storing conversational AI interactions with privacy compliance and performance optimization. This database design prompt for ChatGPT, Claude, and Gemini produces SQL table definitions, indexing strategies, session management patterns, and analytical query templates tailored to AI conversation logging. It addresses real-world challenges including user consent workflows, ephemeral and persistent session handling, metadata capture for model versions and token usage, and time-series partitioning for high-volume platforms. Use it when building logging infrastructure for chatbots, AI assistants, or any application that needs to track prompt-response pairs across user journeys. ● Outputs complete SQL CREATE TABLE statements with relationships for users, sessions, prompts, responses, and metadata including foreign keys and constraints. ● Provides indexing recommendations for conversation retrieval, user lookup, and time-range queries to maintain sub-second response times at scale. ● Includes privacy compliance patterns for consent tracking, data retention policies, anonymization workflows, and GDPR-compliant deletion. ● Delivers sample insertion code with transaction handling, analytical query templates for usage metrics and behavior analysis, and partitioning strategies for archival and performance. ## Prompt

```
## Role
You are a database architect specializing in high-performance logging systems for conversational AI platforms.

## Task
Create a comprehensive database schema and implementation strategy for logging AI prompt history. Design tables that efficiently capture user prompts, AI responses, and associated metadata while maintaining proper relationships and performance. Provide SQL table creation statements, indexing strategies, and data insertion patterns.

## Context
The developer needs to implement AI interaction logging in an environment where:
- Data privacy regulations are strict and user consent must be managed
- User sessions can be ephemeral or persistent
- The application must scale efficiently without performance bottlenecks
- Prompts and responses are part of complex user journeys, not isolated events

{{application-context}}

## Output
Provide a complete implementation guide structured as:

**Database Schema**
Complete SQL table creation statements with proper relationships, data types, and constraints for users, sessions, prompts, responses, and metadata.

**Indexing Strategy**
Recommended indexes for optimal query performance on conversation retrieval, user lookup, and time-based queries.

**Session Management**
Implementation approach for associating prompts with user sessions, handling ephemeral and persistent users.

**Metadata Capture**
Strategy for storing AI model information (model version, temperature, tokens), interaction timing, and performance metrics.

**Privacy Compliance**
Data handling approaches for user consent management, data retention policies, anonymization, and deletion workflows.

**Insertion Patterns**
Code examples for efficiently inserting prompt and response data with proper transaction handling.

**Analytical Queries**
Sample queries for common analysis needs: conversation retrieval, usage metrics, performance analysis, and user behavior patterns.

**Scaling Considerations**
Performance optimization strategies including partitioning, archival patterns, and caching for high-volume usage.

**Implementation Roadmap**
Step-by-step deployment plan for integrating logging into the existing application, including migration strategies and rollback approaches.

Focus on practical, production-ready solutions specific to AI conversation logging.
```

## 用法 / Usage
- 必填變數 / Variables: {{application-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The AI Interaction Log Database Schema Designer is a free AI prompt that creates complete database architectur…
