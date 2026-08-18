# Write Inference Scripts for Distributed ML Pipelines

## 簡介

The Write Inference Scripts for Distributed ML Pipelines is a free AI prompt that generates production-grade Python code for scalable batch inference with parallel processing, checkpointing, and resource optimization for data engineers and ML teams. This inference script prompt for ChatGPT, Claude, and Cursor produces complete, executable code that handles massive data volumes across local, cloud, or cluster environments, incorporating dynamic batch sizing, worker pools, exponential backoff retry logic, and real-time throughput metrics. It is built for teams deploying ML models at scale who need resilient pipelines that maximize CPU and GPU utilization while preventing memory crashes and data loss. ● Produces scripts with configurable batch sizes, parallel worker pools, and lazy model loading to maximize hardware utilization across CPUs and GPUs. ● Includes automatic checkpointing after each batch, exponential backoff retry logic, and graceful failure recovery to preserve partial results and resume without data loss. ● Generates real-time observability with throughput metrics, progress bars using tqdm, memory tracking, and logging that guides troubleshooting. ● Outputs clean, modular code with configuration variables at the top, inline documentation, example usage, and deployment notes for scaling from local machines to distributed clusters. ## Prompt

```
## Role
You are a distributed computing architect specializing in production-grade ML inference pipelines.

## Task
Create a production-ready Python batch inference script with parallel execution, checkpointing, graceful failure handling, and real-time progress monitoring. The script must maximize resource utilization while preventing memory crashes and data loss.

## Context
{{deployment-context}}

*Include: deployment environment (local/cloud/cluster), data volume (total size and record count), model type and inference requirements, available hardware (CPU/GPU cores, memory), failure tolerance (acceptable failure rate, recovery time), and any scaling constraints.*

## Architecture Requirements

**Model Management:**
- Load models once at initialization with lazy loading for memory efficiency
- Support multi-model scenarios where applicable

**Batch Processing:**
- Dynamic batch sizing based on available memory
- Configurable chunk sizes for different data volumes
- Parallel processing across all available CPU/GPU resources
- Worker pools with proper synchronization

**Resilience:**
- Save checkpoints after each batch completion
- Automatic retry logic with exponential backoff
- Preserve partial results on any failure
- Resume from last checkpoint without data loss

**Observability:**
- Real-time throughput metrics (records/sec, batches/min)
- Estimated time to completion
- Memory and resource utilization tracking
- Comprehensive logging for troubleshooting

**Results Management:**
- Incremental result saving (don't wait until completion)
- Support for multiple output formats
- Data validation on write

**Avoid:**
- Hardcoded paths or fixed batch sizes
- Synchronous/sequential processing
- Silent failures or missing error context

## Output Format

Provide complete, executable Python code with:

- Configuration variables at the top (no hardcoded values)
- Clear section headers using comments
- Inline documentation for complex logic
- Progress bars using `tqdm` or similar
- Error messages that guide troubleshooting
- Example usage demonstrating typical invocation
- Brief deployment notes for scaling considerations
```

## 用法 / Usage
- 必填變數 / Variables: {{deployment-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Prompt&Manifest_Engineering · Skills_Catalog_Node_Extractor
- 適用 / Use when: The Write Inference Scripts for Distributed ML Pipelines is a free AI prompt that generates production-grade P…
