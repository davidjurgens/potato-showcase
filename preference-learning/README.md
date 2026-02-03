# Preference Learning & RLHF Tasks

This category contains annotation task designs for reinforcement learning from human feedback (RLHF), preference learning, and AI alignment research.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [helpsteer-multiattribute-rating](./helpsteer-multiattribute-rating) | Multi-attribute response quality rating (helpfulness, correctness, coherence, complexity, verbosity) | Wang et al., 2023 |
| [hh-rlhf-pairwise-preference](./hh-rlhf-pairwise-preference) | Pairwise helpfulness and harmlessness preference | Bai et al., 2022 |
| [saferlhf-dual-preference](./saferlhf-dual-preference) | Dual-dimension safety and helpfulness annotation | Dai et al., NeurIPS 2023 |
| [summary-preference-comparison](./summary-preference-comparison) | Summary quality pairwise comparison | Stiennon et al., NeurIPS 2020 |
| [ultrafeedback-rubric-evaluation](./ultrafeedback-rubric-evaluation) | Multi-aspect rubric-based response evaluation | Cui et al., 2023 |
| [pairwise-preference-rationale](./pairwise-preference-rationale) | Preference annotation with natural language rationales | Template |
| [beavertails-safety-preference](./beavertails-safety-preference) | Multi-category safety classification | Ji et al., NeurIPS 2023 |
| [redteam-adversarial-eval](./redteam-adversarial-eval) | Red team adversarial attack evaluation | Ganguli et al., 2022 |
| [webgpt-comparison](./webgpt-comparison) | Web-augmented QA comparison | Nakano et al., 2021 |
| [instructgpt-preference](./instructgpt-preference) | Instruction following preference (3H: helpful, honest, harmless) | Ouyang et al., NeurIPS 2022 |
| [oasst-conversation-quality](./oasst-conversation-quality) | Multi-dimensional conversation quality rating | Köpf et al., NeurIPS 2023 |
| [alpacafarm-simulation](./alpacafarm-simulation) | Preference simulation for RLHF research | Dubois et al., NeurIPS 2023 |

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

**Total: 12 preference learning tasks**
