# Potato Annotation Showcase

A collection of example annotation task configurations for [Potato](https://github.com/davidjurgens/potato), the lightweight annotation tool for NLP research.

## Research-Based Designs (38)

These designs are based on published academic papers and shared tasks.

### Emotion & Sentiment
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [goemotions](./goemotions) | Fine-grained 27-emotion classification for Reddit | [Demszky et al., ACL 2020](https://aclanthology.org/2020.acl-main.372/) | Intermediate |
| [semeval-emotion-detection](./semeval-emotion-detection) | Multi-label emotion with intensity ratings | [Mohammad et al., SemEval 2018](https://aclanthology.org/S18-1001/) | Intermediate |
| [emotion-cause-extraction](./emotion-cause-extraction) | Extract causes of emotions in dialogue | [Poria et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.431/) | Advanced |
| [empathetic-dialogues](./empathetic-dialogues) | Annotate empathetic responses | [Rashkin et al., ACL 2019](https://aclanthology.org/P19-1534/) | Intermediate |
| [news-emotion-roles](./news-emotion-roles) | Emotion semantic roles in headlines | [Bostan et al., LREC 2020](https://aclanthology.org/2020.lrec-1.194/) | Advanced |
| [rusentiment](./rusentiment) | 5-class social media sentiment | [Rogers et al., COLING 2018](https://aclanthology.org/C18-1064/) | Beginner |

### Hate Speech & Content Moderation
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [hatexplain](./hatexplain) | Explainable hate speech with rationales | [Mathew et al., AAAI 2021](https://ojs.aaai.org/index.php/AAAI/article/view/17745) | Advanced |
| [dynamic-hate-speech](./dynamic-hate-speech) | Fine-grained hate type classification | [Vidgen et al., ACL 2021](https://aclanthology.org/2021.acl-long.132/) | Intermediate |
| [implicit-hate-speech](./implicit-hate-speech) | 6-category implicit hate taxonomy | [ElSherief et al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.29/) | Advanced |
| [social-bias-frames](./social-bias-frames) | Structured bias annotation with stereotypes | [Sap et al., ACL 2020](https://aclanthology.org/2020.acl-main.409/) | Advanced |
| [toxic-spans](./toxic-spans) | Character-level toxicity spans | [Pavlopoulos et al., SemEval 2021](https://aclanthology.org/2021.semeval-1.6/) | Intermediate |

### Named Entity Recognition
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [biomedical-ner](./biomedical-ner) | Proteins, DNA, RNA, cell entities | [Kim et al., BioNLP 2004](https://aclanthology.org/W04-1213/) | Advanced |
| [complex-ner](./complex-ner) | Creative works, products, groups | [Malmasi et al., SemEval 2022](https://aclanthology.org/2022.semeval-1.196/) | Advanced |
| [adverse-drug-events](./adverse-drug-events) | Drug safety entity extraction | [Karimi et al., J Biomed Inform 2015](https://pubmed.ncbi.nlm.nih.gov/25817970/) | Intermediate |

### Information Extraction
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [event-argument-extraction](./event-argument-extraction) | Document-level event arguments | [Wang et al., ACL 2024](https://aclanthology.org/2024.acl-long.224/) | Advanced |
| [dialogue-relation-extraction](./dialogue-relation-extraction) | 36 relation types in dialogue | [Yu et al., ACL 2020](https://aclanthology.org/2020.acl-main.444/) | Advanced |
| [chemical-disease-relations](./chemical-disease-relations) | Chemical-disease causal relations | [Li et al., Database 2016](https://academic.oup.com/database/article/doi/10.1093/database/baw068/2630414) | Advanced |
| [temporal-relations](./temporal-relations) | Event temporal ordering | [UzZaman et al., SemEval 2013](https://aclanthology.org/S13-2001/) | Advanced |
| [coreference-resolution](./coreference-resolution) | Pronoun-entity linking | [Pradhan et al., CoNLL 2012](https://aclanthology.org/W12-4501/) | Advanced |
| [sdoh-extraction](./sdoh-extraction) | Social determinants of health | [Lybarger et al., JAMIA 2023](https://pubmed.ncbi.nlm.nih.gov/36795066/) | Advanced |

### Argumentation & Stance
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [argument-quality](./argument-quality) | Cogency, effectiveness, reasonableness | [Wachsmuth et al., EACL 2017](https://aclanthology.org/E17-1017/) | Intermediate |
| [argument-reasoning](./argument-reasoning) | Implicit warrant identification | [Habernal et al., NAACL 2018](https://aclanthology.org/N18-1175/) | Advanced |
| [claim-perspectives](./claim-perspectives) | Diverse perspectives on claims | [Chen et al., NAACL 2019](https://aclanthology.org/N19-1053/) | Intermediate |
| [stance-detection](./stance-detection) | Zero-shot stance classification | [Allaway & McKeown, EMNLP 2020](https://aclanthology.org/2020.emnlp-main.197/) | Intermediate |
| [rumor-stance](./rumor-stance) | Stance toward rumors in threads | [Zubiaga et al., ACL 2016](https://aclanthology.org/P16-2061/) | Intermediate |

### Fact Verification & Misinformation
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [scientific-claim-verification](./scientific-claim-verification) | Verify claims against abstracts | [Wadden et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.609/) | Advanced |
| [propaganda-techniques](./propaganda-techniques) | 14 fine-grained propaganda types | [Da San Martino et al., EMNLP 2019](https://aclanthology.org/D19-1565/) | Advanced |
| [clickbait-detection](./clickbait-detection) | Clickbait headline classification | [Potthast et al., ECIR 2016](https://webis.de/publications.html#potthast_2016) | Beginner |
| [deceptive-review-detection](./deceptive-review-detection) | Fake vs genuine reviews | [Ott et al., ACL 2011](https://aclanthology.org/P11-1032/) | Intermediate |

### Commonsense & Ethics
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [social-chemistry](./social-chemistry) | 12-dimension social norm annotation | [Forbes et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.48/) | Advanced |
| [moral-stories](./moral-stories) | Moral reasoning in narratives | [Emelin et al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.54/) | Intermediate |
| [commonsense-inference](./commonsense-inference) | If-then commonsense knowledge | [Hwang et al., AAAI 2021](https://ojs.aaai.org/index.php/AAAI/article/view/16792) | Intermediate |
| [commonsense-qa-explanation](./commonsense-qa-explanation) | Explain QA with properties | [Aggarwal et al., ACL 2021](https://aclanthology.org/2021.acl-long.238/) | Intermediate |
| [power-agency-frames](./power-agency-frames) | Power and agency connotations | [Sap et al., EMNLP 2017](https://aclanthology.org/D17-1247/) | Intermediate |

### Explainability & Rationales
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [rationale-annotation](./rationale-annotation) | Evidence spans for predictions | [DeYoung et al., ACL 2020](https://aclanthology.org/2020.acl-main.408/) | Intermediate |
| [nli-explanation](./nli-explanation) | NLI with natural language explanations | [Camburu et al., NeurIPS 2018](https://proceedings.neurips.cc/paper/2018/hash/4c7a167bb329bd92800a858552f2e32a-Abstract.html) | Intermediate |

### Dialogue
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [swbd-damsl-dialogue-acts](./swbd-damsl-dialogue-acts) | Switchboard dialogue act tagging | [Jurafsky et al., 1997](https://web.stanford.edu/~jurafsky/ws97/manual.august1.html) | Advanced |

### Political & Media
| Design | Description | Reference | Complexity |
|--------|-------------|-----------|------------|
| [political-discourse](./political-discourse) | Multi-task political speech analysis | [Sermpezis et al., arXiv 2025](https://arxiv.org/abs/2501.06265) | Intermediate |

---

## Template Designs (28)

Generic annotation templates without specific paper references.

### Text Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [sentiment-analysis](./sentiment-analysis) | Multi-class sentiment classification | Beginner |
| [named-entity-recognition](./named-entity-recognition) | Span-based NER | Intermediate |
| [toxicity-detection](./toxicity-detection) | Multi-label toxicity classification | Beginner |
| [dialogue-act-labeling](./dialogue-act-labeling) | Utterance communicative function | Intermediate |
| [fact-verification](./fact-verification) | Claim verification | Intermediate |
| [hate-speech-detection](./hate-speech-detection) | Hate speech categorization | Intermediate |
| [sarcasm-detection](./sarcasm-detection) | Sarcasm detection and typing | Intermediate |
| [reading-comprehension](./reading-comprehension) | QA evaluation | Intermediate |
| [relation-extraction](./relation-extraction) | Entity relationship identification | Advanced |
| [semantic-similarity](./semantic-similarity) | Sentence pair similarity | Beginner |
| [intent-classification](./intent-classification) | Chatbot intent classification | Beginner |

### Evaluation Tasks
| Design | Description | Complexity |
|--------|-------------|------------|
| [text-summarization-eval](./text-summarization-eval) | Summary quality evaluation | Intermediate |
| [machine-translation-eval](./machine-translation-eval) | Translation quality (MQM) | Intermediate |
| [question-answering](./question-answering) | QA response evaluation | Intermediate |
| [image-captioning-eval](./image-captioning-eval) | Caption quality evaluation | Beginner |
| [visual-qa](./visual-qa) | VQA response evaluation | Beginner |

### Image Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [image-classification](./image-classification) | Multi-label image classification | Beginner |
| [object-detection](./object-detection) | Bounding box annotation | Intermediate |
| [image-segmentation](./image-segmentation) | Polygon segmentation | Advanced |

### Audio Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [audio-transcription](./audio-transcription) | Transcription review | Intermediate |
| [speaker-diarization](./speaker-diarization) | Speaker identification | Intermediate |
| [emotion-recognition](./emotion-recognition) | Speech emotion classification | Intermediate |
| [music-genre-classification](./music-genre-classification) | Genre and mood tagging | Beginner |

### Comparison Tasks
| Design | Description | Complexity |
|--------|-------------|------------|
| [pairwise-preference](./pairwise-preference) | Side-by-side preference | Beginner |
| [best-worst-scaling](./best-worst-scaling) | MaxDiff annotation | Beginner |
| [ranking-task](./ranking-task) | Drag-and-drop ranking | Beginner |

### Surveys
| Design | Description | Complexity |
|--------|-------------|------------|
| [survey-feedback](./survey-feedback) | User experience survey | Beginner |
| [likert-scale-survey](./likert-scale-survey) | Attitude measurement | Beginner |

---

## Structure

Each design folder contains:
- `metadata.json` - Design metadata (title, description, tags, paper reference, citation)
- `config.yaml` - Potato configuration file
- `sample-data.json` - Example data for testing

## Quick Start

```bash
# Clone this repository
git clone https://github.com/davidjurgens/potato-showcase.git

# Navigate to a design
cd potato-showcase/goemotions

# Run with Potato
potato start config.yaml
```

## Usage

1. Clone this repository
2. Copy a design folder to your project
3. Customize the config.yaml for your needs
4. Run with: `potato start config.yaml`

## Contributing

We welcome contributions! To add a new design:
1. Create a folder with your design name
2. Add required files (metadata.json, config.yaml, sample-data.json)
3. Include paper reference and BibTeX citation if based on published work
4. Submit a pull request

## License

MIT License - feel free to use these designs in your projects.
