# Preference Learning & RLHF Tasks

This category contains annotation task designs for reinforcement learning from human feedback (RLHF), preference learning, and AI alignment research.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [annotation types](https://www.potatoannotator.com/docs/annotation-types/radio-multiselect) and [quality control](https://www.potatoannotator.com/docs/features/quality-control) docs to build reliable preference-annotation tasks.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [alpacafarm-simulation](./alpacafarm-simulation) | Preference simulation for RLHF research | Dubois et al., NeurIPS 2023 |
| [beavertails-safety-preference](./beavertails-safety-preference) | Multi-category safety classification | Ji et al., NeurIPS 2023 |
| [constitutional-ai-harmlessness](./constitutional-ai-harmlessness) | Evaluate AI assistant responses for harmlessness and helpfulness based on the Constitutional AI framework… | Bai et al., arXiv 2022 |
| [dpo-preference-data](./dpo-preference-data) | Pairwise preference annotation for Direct Preference Optimization, based on Rafailov et al., NeurIPS 2023 | Rafailov et al., NeurIPS 2023 |
| [helpsteer-multiattribute-rating](./helpsteer-multiattribute-rating) | Multi-attribute response quality rating (helpfulness, correctness, coherence, complexity, verbosity) | Wang et al., 2023 |
| [hh-rlhf-pairwise-preference](./hh-rlhf-pairwise-preference) | Pairwise helpfulness and harmlessness preference | Bai et al., 2022 |
| [instructgpt-preference](./instructgpt-preference) | Instruction following preference (3H: helpful, honest, harmless) | Ouyang et al., NeurIPS 2022 |
| [mmlu-pro-tiered-eval](./mmlu-pro-tiered-eval) | Tiered evaluation for multi-subject question answering, based on MMLU-Pro | Wang et al., NeurIPS 2024 (Datasets & Benchmarks) |
| [oasst-conversation-quality](./oasst-conversation-quality) | Multi-dimensional conversation quality rating | Köpf et al., NeurIPS 2023 |
| [pairwise-preference-rationale](./pairwise-preference-rationale) | Preference annotation with natural language rationales | Template |
| [redteam-adversarial-eval](./redteam-adversarial-eval) | Red team adversarial attack evaluation | Ganguli et al., 2022 |
| [rewardbench-reward-model-eval](./rewardbench-reward-model-eval) | Reward model evaluation through pairwise preference annotation | Lambert et al., Findings NAACL 2025 |
| [saferlhf-dual-preference](./saferlhf-dual-preference) | Dual-dimension safety and helpfulness annotation | Dai et al., NeurIPS 2023 |
| [spin-self-play](./spin-self-play) | Human vs | Chen et al., ICML 2024 |
| [summary-preference-comparison](./summary-preference-comparison) | Summary quality pairwise comparison | Stiennon et al., NeurIPS 2020 |
| [ultrafeedback-multiaspect](./ultrafeedback-multiaspect) | UltraFeedback is a 64k-prompt preference dataset where GPT-4 rates model responses on four aspects | Cui et al., ICML 2024 |
| [ultrafeedback-rubric-evaluation](./ultrafeedback-rubric-evaluation) | Multi-aspect rubric-based response evaluation | Cui et al., 2023 |
| [webgpt-comparison](./webgpt-comparison) | Web-augmented QA comparison | Nakano et al., 2021 |

## Quick Start

```bash
# Navigate to a specific task
cd preference-learning/hh-rlhf-pairwise-preference

# Run with Potato
potato start config.yaml
```

## Common Annotation Patterns

### Pairwise Preference
Compare two model responses and select the better one. Used in:
- hh-rlhf-pairwise-preference
- summary-preference-comparison
- webgpt-comparison
- instructgpt-preference
- alpacafarm-simulation

### Multi-Attribute Rating
Rate responses on multiple quality dimensions. Used in:
- helpsteer-multiattribute-rating
- ultrafeedback-rubric-evaluation
- oasst-conversation-quality

### Safety Classification
Identify harmful content and classify by harm type. Used in:
- saferlhf-dual-preference
- beavertails-safety-preference
- redteam-adversarial-eval

## The Three H's Framework

Many RLHF tasks evaluate responses on:

1. **Helpful**: Does the response help achieve the user's goal?
2. **Honest**: Is the information accurate and uncertainty acknowledged?
3. **Harmless**: Does the response avoid causing harm?

## Task Count

**Total: 18 preference learning tasks**
