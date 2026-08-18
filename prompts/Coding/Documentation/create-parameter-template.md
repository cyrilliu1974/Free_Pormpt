# YAML Parameter Template Generator for ML Configuration

## 簡介

The YAML Parameter Template Generator for ML Configuration is a free AI prompt that creates structured, hierarchical parameter management systems for machine learning teams who need to separate configuration from code. This configuration management prompt for ChatGPT, Claude, Gemini, and Grok produces a complete set of YAML files organized by model architecture, training settings, data pipelines, and environment overrides. It applies Hydra framework principles to generate base configurations, model-specific templates, environment adjustments (dev/staging/prod), and experiment override examples. Teams use it to replace hardcoded parameters, track experiment settings, enable A/B testing, and ensure reproducibility across different deployment contexts without touching source code. Reach for this prompt when onboarding new ML architectures, standardizing team configuration practices, or setting up experiment tracking infrastructure that supports parameter sweeps and variant comparison. ● Organizes parameters into logical categories (model architecture, training hyperparameters, data paths, logging, infrastructure) with inline documentation for every setting ● Generates base configs plus environment-specific overrides and experiment templates that demonstrate inheritance patterns and reduce duplication ● Documents valid ranges, type constraints, parameter dependencies, and sensible defaults that work out-of-the-box ● Includes usage instructions with code snippets showing how to load configurations and apply overrides for experiments ## Prompt

```
## Role
You are a configuration architecture specialist who designs parameter management systems using Hydra framework principles.

## Task
Create a hierarchical YAML configuration template system for {{model-architecture-and-use-case}}. Design for logical organization, clear documentation, inheritance patterns, and experimentation support across {{environment-and-team-context}}.

Before designing, analyze: What parameters does this model require? How will they change during experiments? What defaults are sensible? How can inheritance reduce duplication?

## Requirements

**Structure**
- Group parameters logically by function: model architecture, training, data, logging, infrastructure
- Avoid nesting deeper than 3 levels
- Support base configurations with override mechanisms for experiments and environments
- Enable parameter sweeps, A/B testing, and experiment comparison

**Documentation**
- Comment every parameter with purpose and impact
- Specify valid ranges and acceptable values (e.g., # Range: [0.0001, 0.1])
- Explain dependencies between parameters
- Include type information and validation constraints

**Defaults & Inheritance**
- Provide sensible defaults that work out-of-the-box
- Follow DRY principle: common settings in base configs, specifics in child configs
- Separate dev/staging/prod environment settings

**Avoid**
- Hardcoded paths
- Mixing concerns across categories
- Parameters without clear documentation

## Output

Provide YAML files with extensive inline comments, structured as:

1. **Base Configuration** (`config.yaml`) - common parameters across all uses
2. **Model-Specific Configuration** (`model/[architecture].yaml`) - architecture-specific settings
3. **Environment Overrides** (`env/dev.yaml`, `env/prod.yaml`) - environment-specific adjustments
4. **Example Experiment Configuration** (`experiments/example.yaml`) - demonstrates override patterns
5. **Usage Instructions** - brief code snippets showing how to load and apply configurations

Use YAML syntax highlighting and clear hierarchical formatting.
```

## 用法 / Usage
- 必填變數 / Variables: {{environment-and-team-context}}、{{model-architecture-and-use-case}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The YAML Parameter Template Generator for ML Configuration is a free AI prompt that creates structured, hierar…
