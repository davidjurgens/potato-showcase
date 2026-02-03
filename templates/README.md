# Template Designs

This category contains generic annotation templates without specific paper references. These templates provide starting points for common annotation patterns that can be customized for your specific needs.

## Subcategories

### [Text Annotation](./text/)
General-purpose text annotation templates.

| Design | Description | Complexity |
|--------|-------------|------------|
| [sentiment-analysis](./text/sentiment-analysis) | Multi-class sentiment classification | Beginner |
| [named-entity-recognition](./text/named-entity-recognition) | Span-based NER | Intermediate |
| [toxicity-detection](./text/toxicity-detection) | Multi-label toxicity classification | Beginner |
| [dialogue-act-labeling](./text/dialogue-act-labeling) | Utterance communicative function | Intermediate |
| [fact-verification](./text/fact-verification) | Claim verification | Intermediate |
| [hate-speech-detection](./text/hate-speech-detection) | Hate speech categorization | Intermediate |
| [sarcasm-detection](./text/sarcasm-detection) | Sarcasm detection and typing | Intermediate |
| [reading-comprehension](./text/reading-comprehension) | QA evaluation | Intermediate |
| [relation-extraction](./text/relation-extraction) | Entity relationship identification | Advanced |
| [semantic-similarity](./text/semantic-similarity) | Sentence pair similarity | Beginner |
| [intent-classification](./text/intent-classification) | Chatbot intent classification | Beginner |

### [Image Annotation](./image/)
General-purpose image annotation templates.

| Design | Description | Complexity |
|--------|-------------|------------|
| [image-classification](./image/image-classification) | Multi-label image classification | Beginner |
| [object-detection](./image/object-detection) | Bounding box annotation | Intermediate |
| [image-segmentation](./image/image-segmentation) | Polygon segmentation | Advanced |

### [Comparison Tasks](./comparison/)
Templates for preference and ranking annotations.

| Design | Description | Complexity |
|--------|-------------|------------|
| [pairwise-preference](./comparison/pairwise-preference) | Side-by-side preference | Beginner |
| [best-worst-scaling](./comparison/best-worst-scaling) | MaxDiff annotation | Beginner |
| [ranking-task](./comparison/ranking-task) | Drag-and-drop ranking | Beginner |

### [Surveys](./surveys/)
Templates for collecting user feedback and attitudes.

| Design | Description | Complexity |
|--------|-------------|------------|
| [survey-feedback](./surveys/survey-feedback) | User experience survey | Beginner |
| [likert-scale-survey](./surveys/likert-scale-survey) | Attitude measurement | Beginner |

## Quick Start

```bash
# Navigate to a template
cd templates/text/sentiment-analysis

# Copy to your project
cp -r . /path/to/your/project/

# Customize config.yaml for your needs
# Then run with Potato
potato start config.yaml
```

## Customization Tips

1. **Modify labels**: Update the label list in `config.yaml` for your categories
2. **Add instructions**: Expand `annotation_instructions` with your guidelines
3. **Adjust data format**: Update `sample-data.json` to match your data structure
4. **Configure annotators**: Set `instances_per_annotator` and `annotation_per_instance`

## Task Count

**Total: 19 template designs** across 4 subcategories
