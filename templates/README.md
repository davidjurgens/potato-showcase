# Template Designs

This category contains generic annotation templates without specific paper references. These templates provide starting points for common annotation patterns that can be customized for your specific needs.

> Copy any template and run it in [Potato](https://www.potatoannotator.com). New to the tool? Start with the [quick-start guide](https://www.potatoannotator.com/docs/getting-started/quick-start).

## Subcategories

### [Comparison Tasks](./comparison/)
Templates for preference and ranking annotations.

| Design | Description | Reference |
|--------|-------------|-----------|
| [best-worst-scaling](./comparison/best-worst-scaling) | MaxDiff annotation | Beginner |
| [pairwise-preference](./comparison/pairwise-preference) | Side-by-side preference | Beginner |
| [ranking-task](./comparison/ranking-task) | Drag-and-drop ranking | Beginner |

### [Image Annotation](./image/)
General-purpose image annotation templates.

| Design | Description | Reference |
|--------|-------------|-----------|
| [image-classification](./image/image-classification) | Multi-label image classification | Beginner |
| [image-segmentation](./image/image-segmentation) | Polygon segmentation | Advanced |
| [object-detection](./image/object-detection) | Bounding box annotation | Intermediate |

### [Surveys](./surveys/)
Templates for collecting user feedback and attitudes.

| Design | Description | Reference |
|--------|-------------|-----------|
| [likert-scale-survey](./surveys/likert-scale-survey) | Attitude measurement | Beginner |
| [survey-feedback](./surveys/survey-feedback) | User experience survey | Beginner |

### [Text Annotation](./text/)
General-purpose text annotation templates.

| Design | Description | Reference |
|--------|-------------|-----------|
| [dialogue-act-labeling](./text/dialogue-act-labeling) | Utterance communicative function | Intermediate |
| [fact-verification](./text/fact-verification) | Claim verification | Intermediate |
| [hate-speech-detection](./text/hate-speech-detection) | Hate speech categorization | Intermediate |
| [intent-classification](./text/intent-classification) | Chatbot intent classification | Beginner |
| [named-entity-recognition](./text/named-entity-recognition) | Span-based NER | Intermediate |
| [reading-comprehension](./text/reading-comprehension) | QA evaluation | Intermediate |
| [relation-extraction](./text/relation-extraction) | Entity relationship identification | Advanced |
| [sarcasm-detection](./text/sarcasm-detection) | Sarcasm detection and typing | Intermediate |
| [semantic-similarity](./text/semantic-similarity) | Sentence pair similarity | Beginner |
| [sentiment-analysis](./text/sentiment-analysis) | Multi-class sentiment classification | Beginner |
| [toxicity-detection](./text/toxicity-detection) | Multi-label toxicity classification | Beginner |
| [triage-quick-annotation](./text/triage-quick-annotation) | A reusable template for quick triage annotation | N/A (Template) |

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

**Total: 20 template designs** across 4 subcategories
