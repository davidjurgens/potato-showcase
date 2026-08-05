# Template Designs

This category contains generic annotation templates without specific paper references. These templates provide starting points for common annotation patterns that can be customized for your specific needs.

> Copy any template and run it in [Potato](https://www.potatoannotator.com). New to the tool? Start with the [quick-start guide](https://www.potatoannotator.com/docs/getting-started/quick-start).

## Subcategories

### [Comparison](https://github.com/davidjurgens/potato-showcase/tree/main/templates/comparison)

| Design | Description | Reference |
|--------|-------------|-----------|
| [best-worst-scaling](https://github.com/davidjurgens/potato-showcase/tree/main/templates/comparison/best-worst-scaling) | MaxDiff annotation where annotators select the best and worst items from a set for relative comparison | Template |
| [pairwise-preference](https://github.com/davidjurgens/potato-showcase/tree/main/templates/comparison/pairwise-preference) | Compare two items and select the preferred one | Template |
| [ranking-task](https://github.com/davidjurgens/potato-showcase/tree/main/templates/comparison/ranking-task) | Drag-and-drop ranking interface to order items from best to worst | Template |

### [Image](https://github.com/davidjurgens/potato-showcase/tree/main/templates/image)

| Design | Description | Reference |
|--------|-------------|-----------|
| [image-classification](https://github.com/davidjurgens/potato-showcase/tree/main/templates/image/image-classification) | Multi-class image classification with thumbnail preview and zoom controls | Template |
| [image-segmentation](https://github.com/davidjurgens/potato-showcase/tree/main/templates/image/image-segmentation) | Draw polygon masks around objects for semantic segmentation tasks | Template |
| [object-detection](https://github.com/davidjurgens/potato-showcase/tree/main/templates/image/object-detection) | Draw bounding boxes around objects for object detection model training | Template |

### [Surveys](https://github.com/davidjurgens/potato-showcase/tree/main/templates/surveys)

| Design | Description | Reference |
|--------|-------------|-----------|
| [likert-scale-survey](https://github.com/davidjurgens/potato-showcase/tree/main/templates/surveys/likert-scale-survey) | Multi-question survey using Likert scales to measure agreement, satisfaction, or frequency | Template |
| [survey-feedback](https://github.com/davidjurgens/potato-showcase/tree/main/templates/surveys/survey-feedback) | Multi-question survey with Likert scales, text fields, and multiple choice | Template |

### [Text](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text)

| Design | Description | Reference |
|--------|-------------|-----------|
| [dialogue-act-labeling](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/dialogue-act-labeling) | Classify utterances in conversations by their communicative function (question, statement, request, etc.) | Template |
| [fact-verification](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/fact-verification) | Verify claims as supported, refuted, or not enough information based on provided evidence | Template |
| [hate-speech-detection](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/hate-speech-detection) | Identify and categorize hate speech, offensive language, and toxic content in text | Template |
| [intent-classification](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/intent-classification) | Classify user utterances into intents for chatbot and virtual assistant training | Template |
| [named-entity-recognition](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/named-entity-recognition) | Span-based entity labeling for identifying people, organizations, locations, and more | Template |
| [reading-comprehension](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/reading-comprehension) | Evaluate question-answer pairs for reading comprehension by verifying answers and rating quality | Template |
| [relation-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/relation-extraction) | Identify and classify relationships between entities in text (e.g., works-for, located-in, married-to) | Template |
| [sarcasm-detection](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/sarcasm-detection) | Identify sarcastic statements and label their type and target in social media and conversational text | Template |
| [semantic-similarity](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/semantic-similarity) | Rate the semantic similarity between pairs of sentences on a continuous scale | Template |
| [sentiment-analysis](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/sentiment-analysis) | Simple 3-way sentiment classification with radio buttons | Template |
| [toxicity-detection](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/toxicity-detection) | Multi-label toxicity classification with severity ratings for content moderation | Template |
| [triage-quick-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/triage-quick-annotation) | A reusable template for quick triage annotation | N/A (Template) |

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
