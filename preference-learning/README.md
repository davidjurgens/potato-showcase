# Preference Learning & RLHF Tasks

This category contains annotation task designs for reinforcement learning from human feedback (RLHF), preference learning, and AI alignment research.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [annotation types](https://www.potatoannotator.com/docs/annotation-types/radio-multiselect) and [quality control](https://www.potatoannotator.com/docs/features/quality-control) docs to build reliable preference-annotation tasks.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [alpacafarm-simulation](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/alpacafarm-simulation) | Simulate human preferences for instruction-following responses | Dubois et al., NeurIPS 2023 |
| [beavertails-safety-preference](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/beavertails-safety-preference) | Annotate AI responses for safety across multiple harm categories | Ji et al., NeurIPS 2023 |
| [constitutional-ai-harmlessness](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/constitutional-ai-harmlessness) | Evaluate AI assistant responses for harmlessness and helpfulness based on the Constitutional AI framework… | Bai et al., arXiv 2022 |
| [dpo-preference-data](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/dpo-preference-data) | Pairwise preference annotation for Direct Preference Optimization, based on Rafailov et al., NeurIPS 2023 | Rafailov et al., NeurIPS 2023 |
| [helpsteer-multiattribute-rating](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/helpsteer-multiattribute-rating) | Multi-dimensional response quality rating for reward model training | Wang et al., NAACL 2024 |
| [hh-rlhf-pairwise-preference](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/hh-rlhf-pairwise-preference) | Classic pairwise preference annotation for helpfulness and harmlessness | Bai et al., 2022 |
| [instructgpt-preference](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/instructgpt-preference) | Evaluate how well AI responses follow user instructions | Ouyang et al., NeurIPS 2022 |
| [mmlu-pro-tiered-eval](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/mmlu-pro-tiered-eval) | Tiered evaluation for multi-subject question answering, based on MMLU-Pro | Wang et al., NeurIPS 2024 (Datasets & Benchmarks) |
| [oasst-conversation-quality](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/oasst-conversation-quality) | Rate AI assistant responses across multiple quality dimensions | Köpf et al., NeurIPS 2023 |
| [pairwise-preference-rationale](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/pairwise-preference-rationale) | Compare two AI responses and select the better one while providing a written justification | Wang et al., 2024 |
| [redteam-adversarial-eval](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/redteam-adversarial-eval) | Evaluate AI responses to adversarial prompts | Ganguli et al., 2022 |
| [rewardbench-reward-model-eval](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/rewardbench-reward-model-eval) | Reward model evaluation through pairwise preference annotation | Lambert et al., Findings NAACL 2025 |
| [saferlhf-dual-preference](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/saferlhf-dual-preference) | Safety-aware preference annotation with separate judgments for helpfulness and harmlessness | Dai et al., ICLR 2024 |
| [spin-self-play](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/spin-self-play) | Human vs. AI response discrimination for Self-Play Fine-Tuning, plus fluency ratings for both responses | Chen et al., ICML 2024 |
| [summary-preference-comparison](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/summary-preference-comparison) | Pairwise comparison of text summaries with axis-based quality ratings | Stiennon et al., NeurIPS 2020 |
| [ultrafeedback-multiaspect](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/ultrafeedback-multiaspect) | UltraFeedback is a 64k-prompt preference dataset where GPT-4 rates model responses on four aspects | Cui et al., ICML 2024 |
| [ultrafeedback-rubric-evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/ultrafeedback-rubric-evaluation) | Fine-grained response evaluation across 4 dimensions with written rationales | Cui et al., ICML 2024 |
| [webgpt-comparison](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/webgpt-comparison) | Compare answers with and without web search access | Nakano et al., 2021 |

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

## The Three H's

Many RLHF tasks evaluate responses on:

1. **Helpful**: Does the response help achieve the user's goal?
2. **Honest**: Is the information accurate and uncertainty acknowledged?
3. **Harmless**: Does the response avoid causing harm?

## Task Count

**Total: 18 preference learning tasks**
