# Potato Annotation Showcase

A collection of 121 example annotation task configurations for [Potato](https://github.com/davidjurgens/potato), the lightweight annotation tool for NLP research.

## Categories

| Category | Description | Tasks |
|----------|-------------|-------|
| [**text/**](./text/) | Text-based NLP tasks (emotion, NER, IE, argumentation, etc.) | 38 |
| [**image/**](./image/) | Image annotation (classification, detection, segmentation) | 22 |
| [**video/**](./video/) | Video annotation (action recognition, summarization, etc.) | 21 |
| [**audio/**](./audio/) | Audio annotation (transcription, diarization, etc.) | 4 |
| [**preference-learning/**](./preference-learning/) | RLHF and preference annotation tasks | 12 |
| [**evaluation/**](./evaluation/) | AI output evaluation tasks | 5 |
| [**templates/**](./templates/) | Generic annotation templates | 19 |

---

## Text Annotation (38 tasks)

Tasks for text-based NLP research.

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Emotion & Sentiment](./text/emotion-sentiment/) | 6 | GoEmotions, SemEval Emotion, Empathetic Dialogues |
| [Hate Speech & Moderation](./text/hate-speech-moderation/) | 5 | HateXplain, Implicit Hate, Social Bias Frames |
| [Named Entity Recognition](./text/named-entity-recognition/) | 3 | Biomedical NER, Complex NER, Adverse Drug Events |
| [Information Extraction](./text/information-extraction/) | 6 | Event Arguments, Dialogue Relations, Temporal Relations |
| [Argumentation & Stance](./text/argumentation-stance/) | 5 | Argument Quality, Stance Detection, Rumor Stance |
| [Fact Verification](./text/fact-verification/) | 4 | Scientific Claims, Propaganda, Clickbait, Deceptive Reviews |
| [Commonsense & Ethics](./text/commonsense-ethics/) | 5 | Social Chemistry, Moral Stories, Commonsense Inference |
| [Explainability](./text/explainability/) | 2 | Rationale Annotation, NLI Explanation |
| [Dialogue](./text/dialogue/) | 1 | SWBD-DAMSL Dialogue Acts |
| [Political & Media](./text/political-media/) | 1 | Political Discourse |

---

## Image Annotation (22 tasks)

Tasks for computer vision research.

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Classification](./image/classification/) | 6 | MS-COCO, ImageNet, Places365, CUB-200 Birds |
| [Segmentation](./image/segmentation/) | 3 | Cityscapes, ADE20K, LIP Human Parsing |
| [Medical Imaging](./image/medical/) | 2 | CheXpert, MIMIC-CXR |
| [Autonomous Driving](./image/driving/) | 2 | KITTI, BDD100K |
| [Aerial & Remote Sensing](./image/aerial/) | 3 | BigEarthNet, xView, DOTA |
| [Specialized Domains](./image/specialized/) | 6 | MVTec-AD, DeepFashion, CelebA, iWildCam |

---

## Video Annotation (21 tasks)

Tasks for video understanding research.

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Action Recognition](./video/action-recognition/) | 8 | AVA, Charades, THUMOS14, EPIC-KITCHENS |
| [Temporal Grounding](./video/temporal-grounding/) | 3 | ActivityNet Captions, DiDeMo, Charades-STA |
| [Video Summarization](./video/summarization/) | 4 | TVSum, SumMe, YouTube Highlights, LSMDC |
| [Boundary Detection](./video/boundary-detection/) | 3 | Scene/Shot Boundary, MovieScenes |
| [Scene Understanding](./video/scene-understanding/) | 1 | MovieNet Scene Classification |
| [Instructional Video](./video/instructional/) | 2 | HowTo100M, YouCook2 |

---

## Audio Annotation (4 tasks)

Tasks for audio and speech processing.

| Task | Description |
|------|-------------|
| [audio-transcription](./audio/audio-transcription) | Speech transcription review |
| [speaker-diarization](./audio/speaker-diarization) | Speaker identification |
| [emotion-recognition](./audio/emotion-recognition) | Speech emotion classification |
| [music-genre-classification](./audio/music-genre-classification) | Music genre tagging |

---

## Preference Learning & RLHF (12 tasks)

Tasks for AI alignment and preference learning research.

| Task | Description | Reference |
|------|-------------|-----------|
| [helpsteer-multiattribute-rating](./preference-learning/helpsteer-multiattribute-rating) | Multi-attribute quality rating | Wang et al., 2023 |
| [hh-rlhf-pairwise-preference](./preference-learning/hh-rlhf-pairwise-preference) | Helpfulness/harmlessness preference | Bai et al., 2022 |
| [saferlhf-dual-preference](./preference-learning/saferlhf-dual-preference) | Dual-dimension safety annotation | Dai et al., NeurIPS 2023 |
| [summary-preference-comparison](./preference-learning/summary-preference-comparison) | Summary quality comparison | Stiennon et al., NeurIPS 2020 |
| [ultrafeedback-rubric-evaluation](./preference-learning/ultrafeedback-rubric-evaluation) | Rubric-based response evaluation | Cui et al., 2023 |
| [beavertails-safety-preference](./preference-learning/beavertails-safety-preference) | Multi-category safety classification | Ji et al., NeurIPS 2023 |
| [redteam-adversarial-eval](./preference-learning/redteam-adversarial-eval) | Red team attack evaluation | Ganguli et al., 2022 |
| [webgpt-comparison](./preference-learning/webgpt-comparison) | Web-augmented QA comparison | Nakano et al., 2021 |
| [instructgpt-preference](./preference-learning/instructgpt-preference) | Instruction following preference | Ouyang et al., NeurIPS 2022 |
| [oasst-conversation-quality](./preference-learning/oasst-conversation-quality) | Conversation quality rating | Köpf et al., NeurIPS 2023 |
| [alpacafarm-simulation](./preference-learning/alpacafarm-simulation) | Preference simulation | Dubois et al., NeurIPS 2023 |
| [pairwise-preference-rationale](./preference-learning/pairwise-preference-rationale) | Preference with rationales | Template |

---

## Evaluation Tasks (5 tasks)

Tasks for evaluating AI-generated content.

| Task | Description |
|------|-------------|
| [text-summarization-eval](./evaluation/text-summarization-eval) | Summary quality evaluation |
| [machine-translation-eval](./evaluation/machine-translation-eval) | Translation quality (MQM) |
| [question-answering](./evaluation/question-answering) | QA response evaluation |
| [image-captioning-eval](./evaluation/image-captioning-eval) | Caption quality evaluation |
| [visual-qa](./evaluation/visual-qa) | VQA response evaluation |

---

## Templates (19 tasks)

Generic templates for common annotation patterns.

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Text](./templates/text/) | 11 | Sentiment, NER, Toxicity, Intent Classification |
| [Image](./templates/image/) | 3 | Classification, Detection, Segmentation |
| [Comparison](./templates/comparison/) | 3 | Pairwise Preference, Best-Worst Scaling, Ranking |
| [Surveys](./templates/surveys/) | 2 | Survey Feedback, Likert Scale |

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

# Navigate to a design (new path structure)
cd potato-showcase/text/emotion-sentiment/goemotions

# Run with Potato
potato start config.yaml
```

## Usage

1. Clone this repository
2. Browse categories to find a relevant design
3. Copy the design folder to your project
4. Customize the `config.yaml` for your needs
5. Run with: `potato start config.yaml`

## Contributing

We welcome contributions! To add a new design:
1. Create a folder in the appropriate category
2. Add required files (`metadata.json`, `config.yaml`, `sample-data.json`)
3. Include paper reference and BibTeX citation if based on published work
4. Submit a pull request

## License

MIT License - feel free to use these designs in your projects.
