# Evaluation Tasks

This category contains annotation task designs for evaluating AI-generated content, including text summaries, translations, question answers, and image captions.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [text-summarization-eval](./text-summarization-eval) | Summary quality evaluation (coherence, relevance, fluency) | Template |
| [machine-translation-eval](./machine-translation-eval) | Translation quality assessment (MQM framework) | Template |
| [question-answering](./question-answering) | QA response correctness and completeness | Template |
| [image-captioning-eval](./image-captioning-eval) | Caption accuracy and descriptiveness | Template |
| [visual-qa](./visual-qa) | Visual question answering evaluation | Template |

## Quick Start

```bash
# Navigate to a specific task
cd evaluation/text-summarization-eval

# Run with Potato
potato start config.yaml
```

## Evaluation Dimensions

### Text Summarization
- **Coherence**: Logical flow and readability
- **Relevance**: Coverage of important information
- **Fluency**: Grammatical correctness
- **Faithfulness**: Factual accuracy to source

### Machine Translation
- **Accuracy**: Meaning preservation
- **Fluency**: Natural target language
- **Terminology**: Domain-specific correctness
- **Style**: Register appropriateness

### Question Answering
- **Correctness**: Factual accuracy
- **Completeness**: Full answer coverage
- **Relevance**: Addresses the question
- **Conciseness**: Appropriate length

## Task Count

**Total: 5 evaluation tasks**
