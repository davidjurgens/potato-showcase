# Evaluation Tasks

This category contains annotation task designs for evaluating AI-generated content, including text summaries, translations, question answers, and image captions.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [AI support](https://www.potatoannotator.com/docs/features/ai-support) and [live agent evaluation](https://www.potatoannotator.com/docs/features/live-agent-evaluation) docs for evaluating model outputs.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [alpacaeval-instruction-eval](./alpacaeval-instruction-eval) | Pairwise preference annotation for instruction-following language models | Dubois et al., NeurIPS 2023 (AlpacaFarm) |
| [arena-hard-auto](./arena-hard-auto) | Pairwise evaluation of LLM responses on challenging prompts from the Arena Hard benchmark | Li et al., ICML 2025 |
| [big-bench-task-eval](./big-bench-task-eval) | Evaluate language model responses on diverse reasoning tasks from the BIG-Bench benchmark | Srivastava et al., TMLR 2023 |
| [chatbot-arena-pairwise-bws](./chatbot-arena-pairwise-bws) | Chatbot Arena collects human pairwise preference votes between anonymous LLM responses to rank models with… | Zheng et al., NeurIPS 2023 |
| [donotanswer-safety-eval](./donotanswer-safety-eval) | Do-Not-Answer is a dataset of 939 prompts a responsible LLM should decline, organized by a risk taxonomy… | Wang et al., Findings EACL 2024 |
| [esa-mt-error-spans](./esa-mt-error-spans) | Error span annotation for machine translation output | Kocmi et al., WMT 2024 |
| [flask-skill-rubric-evaluation](./flask-skill-rubric-evaluation) | Fine-grained human evaluation of LLM responses based on FLASK (Fine-grained Language Model Evaluation… | Ye et al., ICLR 2024 |
| [godspeed-agent-perception](./godspeed-agent-perception) | Applies the Godspeed Questionnaire Series — the standard human-robot interaction measurement instrument by… | Bartneck et al., Int J Soc Robotics 2009 |
| [gpqa-expert-qa](./gpqa-expert-qa) | Expert-level question answering evaluation on graduate-level science questions from the GPQA benchmark | Rein et al., COLM 2024 |
| [helm-model-card-display](./helm-model-card-display) | Model performance summary display and evaluation based on the HELM benchmark | Liang et al., TMLR 2023 |
| [humaneval-code-correctness](./humaneval-code-correctness) | Evaluation of code generation correctness based on the HumanEval benchmark | Chen et al., arXiv 2021 |
| [ifeval-instruction-following](./ifeval-instruction-following) | IFEval is the instruction-following benchmark from Google Research with 541 prompts built around 25… | Zhou et al., arXiv 2023 |
| [image-captioning-eval](./image-captioning-eval) | Caption accuracy and descriptiveness | Template |
| [longeval-faithfulness](./longeval-faithfulness) | LongEval is the EACL 2023 protocol for human evaluation of faithfulness in long-form summaries | Krishna et al., EACL 2023 |
| [machine-translation-eval](./machine-translation-eval) | Translation quality assessment (MQM framework) | Template |
| [mmlu-knowledge-eval](./mmlu-knowledge-eval) | Multiple-choice knowledge evaluation across diverse academic subjects, based on the Massive Multitask… | Hendrycks et al., ICLR 2021 |
| [mqm-mt-error-annotation](./mqm-mt-error-annotation) | Expert MQM (Multidimensional Quality Metrics) error annotation for machine translation based on Freitag,… | Freitag et al., TACL 2021 |
| [mt-bench-judge-consistency](./mt-bench-judge-consistency) | Multi-turn conversation evaluation for LLM judge consistency, based on MT-Bench | Zheng et al., NeurIPS 2023 |
| [mtbench-llm-evaluation](./mtbench-llm-evaluation) | MT-Bench is an 80-question multi-turn benchmark for rating LLM chat assistants with an LLM judge, from… | Zheng et al., NeurIPS 2023 |
| [prometheus-rubric-evaluation](./prometheus-rubric-evaluation) | Prometheus is an open-source evaluator LM that scores a response against a user-defined rubric on a 1-5… | Kim et al., ICLR 2024 |
| [question-answering](./question-answering) | QA response correctness and completeness | Template |
| [rewardbench-reward-eval](./rewardbench-reward-eval) | Evaluation of reward model preferences via pairwise comparison of chosen and rejected responses | Lambert et al., Findings of NAACL 2025 |
| [sorrybench-refusal-eval](./sorrybench-refusal-eval) | SORRY-Bench is a benchmark of 440 unsafe instructions across 44 fine-grained risk categories for judging… | Xie et al., ICLR 2025 |
| [text-summarization-eval](./text-summarization-eval) | Summary quality evaluation (coherence, relevance, fluency) | Template |
| [visual-qa](./visual-qa) | Visual question answering evaluation | Template |
| [wildbench-llm-eval](./wildbench-llm-eval) | Evaluation of LLM outputs on challenging real-world user queries from WildBench | Lin et al., COLM 2024 |
| [wmt15-relative-ranking](./wmt15-relative-ranking) | The classic WMT relative-ranking (RR) protocol for machine translation evaluation, from 'Findings of the… | Bojar et al., WMT 2015 |

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

**Total: 27 evaluation tasks**
