# Text Annotation Tasks

This category contains annotation task designs for text-based NLP research, including sentiment analysis, named entity recognition, information extraction, and more.

## Subcategories

### [Emotion & Sentiment](./emotion-sentiment/)
Tasks for detecting and classifying emotions and sentiment in text.

| Design | Description | Reference |
|--------|-------------|-----------|
| [goemotions](./emotion-sentiment/goemotions) | Fine-grained 27-emotion classification for Reddit | Demszky et al., ACL 2020 |
| [semeval-emotion-detection](./emotion-sentiment/semeval-emotion-detection) | Multi-label emotion with intensity ratings | Mohammad et al., SemEval 2018 |
| [emotion-cause-extraction](./emotion-sentiment/emotion-cause-extraction) | Extract causes of emotions in dialogue | Poria et al., EMNLP 2020 |
| [empathetic-dialogues](./emotion-sentiment/empathetic-dialogues) | Annotate empathetic responses | Rashkin et al., ACL 2019 |
| [news-emotion-roles](./emotion-sentiment/news-emotion-roles) | Emotion semantic roles in headlines | Bostan et al., LREC 2020 |
| [rusentiment](./emotion-sentiment/rusentiment) | 5-class social media sentiment | Rogers et al., COLING 2018 |

### [Hate Speech & Content Moderation](./hate-speech-moderation/)
Tasks for detecting and classifying harmful content, hate speech, and toxicity.

| Design | Description | Reference |
|--------|-------------|-----------|
| [hatexplain](./hate-speech-moderation/hatexplain) | Explainable hate speech with rationales | Mathew et al., AAAI 2021 |
| [dynamic-hate-speech](./hate-speech-moderation/dynamic-hate-speech) | Fine-grained hate type classification | Vidgen et al., ACL 2021 |
| [implicit-hate-speech](./hate-speech-moderation/implicit-hate-speech) | 6-category implicit hate taxonomy | ElSherief et al., EMNLP 2021 |
| [social-bias-frames](./hate-speech-moderation/social-bias-frames) | Structured bias annotation with stereotypes | Sap et al., ACL 2020 |
| [toxic-spans](./hate-speech-moderation/toxic-spans) | Character-level toxicity spans | Pavlopoulos et al., SemEval 2021 |

### [Named Entity Recognition](./named-entity-recognition/)
Tasks for identifying and classifying named entities in text.

| Design | Description | Reference |
|--------|-------------|-----------|
| [biomedical-ner](./named-entity-recognition/biomedical-ner) | Proteins, DNA, RNA, cell entities | Kim et al., BioNLP 2004 |
| [complex-ner](./named-entity-recognition/complex-ner) | Creative works, products, groups | Malmasi et al., SemEval 2022 |
| [adverse-drug-events](./named-entity-recognition/adverse-drug-events) | Drug safety entity extraction | Karimi et al., J Biomed Inform 2015 |

### [Information Extraction](./information-extraction/)
Tasks for extracting structured information from unstructured text.

| Design | Description | Reference |
|--------|-------------|-----------|
| [event-argument-extraction](./information-extraction/event-argument-extraction) | Document-level event arguments | Wang et al., ACL 2024 |
| [dialogue-relation-extraction](./information-extraction/dialogue-relation-extraction) | 36 relation types in dialogue | Yu et al., ACL 2020 |
| [chemical-disease-relations](./information-extraction/chemical-disease-relations) | Chemical-disease causal relations | Li et al., Database 2016 |
| [temporal-relations](./information-extraction/temporal-relations) | Event temporal ordering | UzZaman et al., SemEval 2013 |
| [coreference-resolution](./information-extraction/coreference-resolution) | Pronoun-entity linking | Pradhan et al., CoNLL 2012 |
| [sdoh-extraction](./information-extraction/sdoh-extraction) | Social determinants of health | Lybarger et al., JAMIA 2023 |

### [Argumentation & Stance](./argumentation-stance/)
Tasks for analyzing arguments, claims, and stance in text.

| Design | Description | Reference |
|--------|-------------|-----------|
| [argument-quality](./argumentation-stance/argument-quality) | Cogency, effectiveness, reasonableness | Wachsmuth et al., EACL 2017 |
| [argument-reasoning](./argumentation-stance/argument-reasoning) | Implicit warrant identification | Habernal et al., NAACL 2018 |
| [claim-perspectives](./argumentation-stance/claim-perspectives) | Diverse perspectives on claims | Chen et al., NAACL 2019 |
| [stance-detection](./argumentation-stance/stance-detection) | Zero-shot stance classification | Allaway & McKeown, EMNLP 2020 |
| [rumor-stance](./argumentation-stance/rumor-stance) | Stance toward rumors in threads | Zubiaga et al., ACL 2016 |

### [Fact Verification](./fact-verification/)
Tasks for verifying claims and detecting misinformation.

| Design | Description | Reference |
|--------|-------------|-----------|
| [scientific-claim-verification](./fact-verification/scientific-claim-verification) | Verify claims against abstracts | Wadden et al., EMNLP 2020 |
| [propaganda-techniques](./fact-verification/propaganda-techniques) | 14 fine-grained propaganda types | Da San Martino et al., EMNLP 2019 |
| [clickbait-detection](./fact-verification/clickbait-detection) | Clickbait headline classification | Potthast et al., ECIR 2016 |
| [deceptive-review-detection](./fact-verification/deceptive-review-detection) | Fake vs genuine reviews | Ott et al., ACL 2011 |

### [Commonsense & Ethics](./commonsense-ethics/)
Tasks for annotating social norms, moral reasoning, and commonsense knowledge.

| Design | Description | Reference |
|--------|-------------|-----------|
| [social-chemistry](./commonsense-ethics/social-chemistry) | 12-dimension social norm annotation | Forbes et al., EMNLP 2020 |
| [moral-stories](./commonsense-ethics/moral-stories) | Moral reasoning in narratives | Emelin et al., EMNLP 2021 |
| [commonsense-inference](./commonsense-ethics/commonsense-inference) | If-then commonsense knowledge | Hwang et al., AAAI 2021 |
| [commonsense-qa-explanation](./commonsense-ethics/commonsense-qa-explanation) | Explain QA with properties | Aggarwal et al., ACL 2021 |
| [power-agency-frames](./commonsense-ethics/power-agency-frames) | Power and agency connotations | Sap et al., EMNLP 2017 |

### [Explainability & Rationales](./explainability/)
Tasks for annotating explanations and evidence for model predictions.

| Design | Description | Reference |
|--------|-------------|-----------|
| [rationale-annotation](./explainability/rationale-annotation) | Evidence spans for predictions | DeYoung et al., ACL 2020 |
| [nli-explanation](./explainability/nli-explanation) | NLI with natural language explanations | Camburu et al., NeurIPS 2018 |

### [Dialogue](./dialogue/)
Tasks for annotating conversational text and dialogue acts.

| Design | Description | Reference |
|--------|-------------|-----------|
| [swbd-damsl-dialogue-acts](./dialogue/swbd-damsl-dialogue-acts) | Switchboard dialogue act tagging | Jurafsky et al., 1997 |

### [Political & Media](./political-media/)
Tasks for analyzing political discourse and media content.

| Design | Description | Reference |
|--------|-------------|-----------|
| [political-discourse](./political-media/political-discourse) | Multi-task political speech analysis | Sermpezis et al., arXiv 2025 |

## Quick Start

```bash
# Navigate to a specific task
cd text/emotion-sentiment/goemotions

# Run with Potato
potato start config.yaml
```

## Task Count

**Total: 38 text annotation tasks** across 10 subcategories
