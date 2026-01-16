# Potato Annotation Showcase

A collection of example annotation task configurations for [Potato](https://github.com/davidjurgens/potato), the lightweight annotation tool for NLP research.

## Available Designs (30+)

### Text Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [sentiment-analysis](./sentiment-analysis) | Multi-class sentiment classification with confidence ratings | Beginner |
| [named-entity-recognition](./named-entity-recognition) | Span-based NER with entity types like Person, Organization, Location | Intermediate |
| [toxicity-detection](./toxicity-detection) | Multi-label toxicity classification for content moderation | Beginner |
| [dialogue-act-labeling](./dialogue-act-labeling) | Classify utterances by communicative function | Intermediate |
| [fact-verification](./fact-verification) | Verify claims as supported, refuted, or not enough info | Intermediate |
| [hate-speech-detection](./hate-speech-detection) | Identify and categorize hate speech and offensive language | Intermediate |
| [sarcasm-detection](./sarcasm-detection) | Detect sarcasm and identify its type and target | Intermediate |
| [reading-comprehension](./reading-comprehension) | Evaluate question-answer pairs for reading comprehension | Intermediate |
| [relation-extraction](./relation-extraction) | Identify relationships between entities in text | Advanced |
| [coreference-resolution](./coreference-resolution) | Link pronouns to their referent entities | Advanced |
| [semantic-similarity](./semantic-similarity) | Rate semantic similarity between sentence pairs | Beginner |
| [intent-classification](./intent-classification) | Classify user utterances for chatbot training | Beginner |

### Evaluation Tasks
| Design | Description | Complexity |
|--------|-------------|------------|
| [text-summarization-eval](./text-summarization-eval) | Evaluate AI-generated text summaries for quality | Intermediate |
| [machine-translation-eval](./machine-translation-eval) | Evaluate translation quality with MQM error taxonomy | Intermediate |
| [question-answering](./question-answering) | Evaluate QA system responses for correctness | Intermediate |
| [image-captioning-eval](./image-captioning-eval) | Evaluate image captions for accuracy and quality | Beginner |
| [visual-qa](./visual-qa) | Evaluate visual question answering responses | Intermediate |

### Image Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [image-classification](./image-classification) | Multi-label image classification with confidence | Beginner |
| [object-detection](./object-detection) | Draw bounding boxes around objects with labels | Intermediate |
| [image-segmentation](./image-segmentation) | Polygon annotation for semantic segmentation | Advanced |

### Audio Annotation
| Design | Description | Complexity |
|--------|-------------|------------|
| [audio-transcription](./audio-transcription) | Review and correct audio transcriptions | Beginner |
| [speaker-diarization](./speaker-diarization) | Identify different speakers in audio recordings | Intermediate |
| [emotion-recognition](./emotion-recognition) | Classify emotional states from speech audio | Intermediate |
| [music-genre-classification](./music-genre-classification) | Classify music clips into genres with mood tags | Beginner |

### Comparison Tasks
| Design | Description | Complexity |
|--------|-------------|------------|
| [pairwise-preference](./pairwise-preference) | Side-by-side comparison for preference selection | Beginner |
| [best-worst-scaling](./best-worst-scaling) | MaxDiff annotation selecting best and worst items | Beginner |
| [ranking-task](./ranking-task) | Drag-and-drop ranking of multiple items | Beginner |

### Surveys
| Design | Description | Complexity |
|--------|-------------|------------|
| [survey-feedback](./survey-feedback) | Multi-question user experience survey | Beginner |
| [likert-scale-survey](./likert-scale-survey) | Likert scale survey for measuring attitudes | Beginner |

## Structure

Each design folder contains:
- `metadata.json` - Design metadata (title, description, tags, category)
- `config.yaml` - Potato configuration file
- `sample-data.json` - Example data for testing

## Quick Start

```bash
# Clone this repository
git clone https://github.com/davidjurgens/potato-showcase.git

# Navigate to a design
cd potato-showcase/sentiment-analysis

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
3. Submit a pull request

## License

MIT License - feel free to use these designs in your projects.
