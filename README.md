# Potato Annotation Showcase

A curated collection of **361** example annotation task configurations for [Potato](https://github.com/davidjurgens/potato), the lightweight annotation tool for NLP research. Covers all 22 Potato annotation types, 90 SemEval shared tasks (2013-2025), and benchmarks from ACL, EMNLP, NeurIPS, ICML, ICLR, CVPR, and more.

## Categories

| Category | Description | Tasks |
|----------|-------------|-------|
| [**text/**](./text/) | Text-based NLP tasks (emotion, NER, IE, QA, parsing, etc.) | 111 |
| [**image/**](./image/) | Image annotation (classification, VQA, grounding, medical) | 33 |
| [**video/**](./video/) | Video annotation (action recognition, QA, summarization) | 37 |
| [**audio/**](./audio/) | Audio annotation (transcription, commands, captioning) | 17 |
| [**evaluation/**](./evaluation/) | AI output evaluation (LLM judging, code, benchmarks) | 23 |
| [**preference-learning/**](./preference-learning/) | RLHF, DPO, and preference annotation tasks | 18 |
| [**multimodal/**](./multimodal/) | Cross-modal tasks (robotics, chart analysis, science QA) | 9 |
| [**agentic/**](./agentic/) | Agent evaluation tasks (web agents, code agents) | 3 |
| [**semeval/**](./semeval/) | SemEval shared tasks (2013-2025, 90 tasks) | 90 |
| [**templates/**](./templates/) | Generic reusable annotation templates | 20 |

---

## Text Annotation (111 tasks)

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Emotion & Sentiment](./text/emotion-sentiment/) | 8 | GoEmotions, SemEval Sentiment, Multirate Sentiment |
| [Hate Speech & Moderation](./text/hate-speech-moderation/) | 6 | HateXplain, Implicit Hate, Social Bias Frames, Toxic Spans |
| [Named Entity Recognition](./text/named-entity-recognition/) | 5 | CoNLL-2003, WNUT-2017, Biomedical NER, Complex NER |
| [Information Extraction](./text/information-extraction/) | 7 | KG-BERT, Event Arguments, Dialogue Relations |
| [Argumentation & Stance](./text/argumentation-stance/) | 5 | Argument Quality, Stance Detection, Rumor Stance |
| [Fact Verification](./text/fact-verification/) | 8 | FActScore, FAVA, Scientific Claims, Propaganda |
| [Commonsense & Ethics](./text/commonsense-ethics/) | 5 | Social Chemistry, Moral Stories, Commonsense Inference |
| [Explainability](./text/explainability/) | 2 | Rationale Annotation, NLI Explanation |
| [Dialogue](./text/dialogue/) | 2 | SWBD-DAMSL Dialogue Acts, Conversation Quality |
| [Political & Media](./text/political-media/) | 1 | Political Discourse |
| [Discourse](./text/discourse/) | 3 | PDTB Discourse Trees, DISRPT, Timeline Relations |
| [Coreference](./text/coreference/) | 4 | OntoNotes, CorefUD, MAVEN-ERE, Legal Coreference |
| [Cross-lingual](./text/cross-lingual/) | 5 | XNLI, Belebele, FLORES MT Quality, IndicNLP |
| [Domain-specific](./text/domain-specific/) | 8 | BioNLP, ChemProt, Clinical NER, Legal, Medical |
| [Computational Social Science](./text/computational-social-science/) | 7 | OffensEval, Moral Foundations, Politeness, Media Frames |
| [Relation Extraction](./text/relation-extraction/) | 6 | MultiTACRED, CrossRE, RadGraph, SciER |
| [Entity Linking](./text/entity-linking/) | 2 | AIDA-CoNLL, MedMentions |
| [Code Annotation](./text/code-annotation/) | 1 | CodeXGLUE Defect Detection |
| [Tabular](./text/tabular/) | 1 | Tabular Data Annotation |
| [Reading Comprehension](./text/reading-comprehension/) | 1 | SQuAD Extractive QA |
| [Natural Language Inference](./text/natural-language-inference/) | 2 | SNLI, MultiNLI |
| [Question Answering](./text/question-answering/) | 2 | Natural Questions, TriviaQA |
| [Information Retrieval](./text/information-retrieval/) | 2 | MS MARCO, TREC-DL |
| [Semantic Similarity](./text/semantic-similarity/) | 1 | STS Benchmark |
| [Word Sense](./text/word-sense/) | 1 | SemEval-2007 WSD |
| [Parsing](./text/parsing/) | 1 | Universal Dependencies |
| [Education](./text/education/) | 3 | Essay Scoring, MathDial Tutoring, Student Essay Discourse |
| [Financial](./text/financial/) | 3 | FinBERT, FLARE NER, Financial PhraseBank |
| [Bias & Toxicity](./text/bias-toxicity/) | — | See subcategories |

---

## Image Annotation (33 tasks)

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Classification](./image/classification/) | 6 | MS-COCO, ImageNet, Places365, CUB-200 |
| [Segmentation](./image/segmentation/) | 3 | Cityscapes, ADE20K, LIP Human Parsing |
| [Visual QA](./image/visual-qa/) | 2 | VQAv2, TextVQA |
| [Visual Grounding](./image/visual-grounding/) | 1 | RefCOCO |
| [Medical Imaging](./image/medical/) | 3 | CheXpert, MIMIC-CXR, Camelyon Pathology |
| [Human Pose](./image/human-pose/) | 1 | ViTPose Keypoint Annotation |
| [Generation Evaluation](./image/generation-eval/) | 1 | T2I-CompBench |
| [Autonomous Driving](./image/driving/) | 2 | KITTI, BDD100K |
| [Aerial & Remote Sensing](./image/aerial/) | 3 | BigEarthNet, xView, DOTA |
| [Specialized Domains](./image/specialized/) | 6 | MVTec-AD, DeepFashion, CelebA, iWildCam |
| [Document Analysis](./image/) | 3+ | DocLayNet, OmniDocBench, SA-1B |

---

## Video Annotation (37 tasks)

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Action Recognition](./video/action-recognition/) | 8 | AVA, Charades, THUMOS14, EPIC-KITCHENS |
| [Temporal Grounding](./video/temporal-grounding/) | 3 | ActivityNet Captions, DiDeMo, Charades-STA |
| [Video Summarization](./video/summarization/) | 4 | TVSum, SumMe, YouTube Highlights, LSMDC |
| [Boundary Detection](./video/boundary-detection/) | 3 | Scene/Shot Boundary, MovieScenes |
| [Video QA](./video/video-qa/) | 2 | NExT-QA, MVBench |
| [Scene Understanding](./video/scene-understanding/) | 1 | MovieNet Scene Classification |
| [Instructional Video](./video/instructional/) | 2 | HowTo100M, YouCook2 |
| [Other Video Tasks](./video/) | 14 | Video-ChatGPT, Sign Language, Child Language, etc. |

---

## Audio Annotation (17 tasks)

| Task | Description |
|------|-------------|
| [librispeech-transcription](./audio/librispeech-transcription) | Audio quality + transcription (slider, audio_annotation) |
| [speech-commands-recognition](./audio/speech-commands-recognition) | Speech command labeling (audio_annotation) |
| [covost-speech-translation](./audio/covost-speech-translation) | Speech translation evaluation |
| [clotho-audio-captioning](./audio/clotho-audio-captioning) | Audio event captioning |
| [audio-transcription](./audio/audio-transcription) | Speech transcription review |
| [speaker-diarization](./audio/speaker-diarization) | Speaker identification |
| [emotion-recognition](./audio/emotion-recognition) | Speech emotion classification |
| [music-genre-classification](./audio/music-genre-classification) | Music genre tagging |
| + 9 more | DiSPLACE, DoReCo, EmoBox, VoiceMOS, etc. |

---

## Evaluation Tasks (23 tasks)

| Task | Paper | Types |
|------|-------|-------|
| [wildbench-llm-eval](./evaluation/wildbench-llm-eval) | WildBench (COLM 2024) | pairwise, likert, text |
| [mt-bench-judge-consistency](./evaluation/mt-bench-judge-consistency) | MT-Bench (NeurIPS 2023) | pairwise, likert, radio |
| [arena-hard-auto](./evaluation/arena-hard-auto) | Arena Hard (2024) | pairwise (scale), likert |
| [rewardbench-reward-eval](./evaluation/rewardbench-reward-eval) | RewardBench (ICML 2024) | pairwise, radio, multirate |
| [mmlu-knowledge-eval](./evaluation/mmlu-knowledge-eval) | MMLU (ICLR 2021) | radio, text |
| [humaneval-code-correctness](./evaluation/humaneval-code-correctness) | HumanEval (2021) | radio, text, number |
| [gpqa-expert-qa](./evaluation/gpqa-expert-qa) | GPQA (ICLR 2024) | number, radio, text |
| [big-bench-task-eval](./evaluation/big-bench-task-eval) | BIG-Bench (TMLR 2023) | radio, text, number |
| [helm-model-card-display](./evaluation/helm-model-card-display) | HELM (TMLR 2023) | pure_display, likert |
| [chatbot-arena-pairwise-bws](./evaluation/chatbot-arena-pairwise-bws) | Chatbot Arena (ICML 2024) | bws, pairwise |
| + 13 more | AlpacaEval, DoNotAnswer, ESA-MT, IFEval, etc. |

---

## Preference Learning & RLHF (18 tasks)

| Task | Paper | Types |
|------|-------|-------|
| [dpo-preference-data](./preference-learning/dpo-preference-data) | DPO (NeurIPS 2023) | pairwise, radio, text |
| [ultrafeedback-multiaspect](./preference-learning/ultrafeedback-multiaspect) | UltraFeedback (ICML 2024) | multirate, likert, text |
| [spin-self-play](./preference-learning/spin-self-play) | SPIN (ICML 2024) | pairwise, radio |
| [constitutional-ai-harmlessness](./preference-learning/constitutional-ai-harmlessness) | Constitutional AI (2022) | radio, likert, text |
| [mmlu-pro-tiered-eval](./preference-learning/mmlu-pro-tiered-eval) | MMLU-Pro (NeurIPS 2024) | tiered_annotation, radio |
| + 13 more | HH-RLHF, SafeRLHF, BeaverTails, WebGPT, etc. |

---

## SemEval Shared Tasks (90 tasks)

Comprehensive coverage of SemEval shared tasks from 2013-2025. See [SEMEVAL.md](./SEMEVAL.md) for details.

| Year | Tasks | Highlights |
|------|-------|------------|
| [2025](./semeval/2025/) | 10 | Multimodal idiomaticity, entity-aware MT, emotion detection |
| [2024](./semeval/2024/) | 9 | Semantic relatedness, persuasion in memes, BRAINTEASER |
| [2023](./semeval/2023/) | 10 | Visual WSD, clickbait spoiling, AfriSenti |
| [2022](./semeval/2022/) | 10 | Patronizing language, idiomaticity, news similarity |
| [2021](./semeval/2021/) | 9 | Lexical complexity, humor detection, MeasEval |
| [2020](./semeval/2020/) | 9 | Commonsense validation, counterfactuals, code-mixed |
| [2019](./semeval/2019/) | 7 | HatEval, hyperpartisan news, suggestion mining |
| [2018](./semeval/2018/) | 10 | Emoji prediction, irony, cybersecurity NER |
| [2017](./semeval/2017/) | 5 | Financial sentiment, humor, pun detection |
| [2016](./semeval/2016/) | 7 | Stance detection, aspect sentiment, clinical TempEval |
| [2013-2015](./semeval/) | 4 | Drug interactions, ABSA, timeline ordering, clinical |

---

## Annotation Type Coverage

All 22 Potato annotation types are represented:

| Type | Count | Example Tasks |
|------|-------|---------------|
| radio | 483 | GoEmotions, SNLI, MMLU, most classification tasks |
| text | 160 | SQuAD, Natural Questions, code review, translations |
| likert | 128 | STS-B, essay scoring, MT quality, humor ratings |
| multiselect | 126 | GoEmotions, moral foundations, persuasion techniques |
| span | 110 | NER tasks, PICO extraction, SQuAD answer spans |
| video_annotation | 46 | Action recognition, temporal grounding, MVBench |
| pairwise | 16 | DPO, Arena Hard, WildBench, MT-Bench |
| slider | 8 | STS-B similarity, essay scoring, word similarity |
| image_annotation | 6 | ViTPose, RefCOCO, Camelyon pathology |
| select | 6 | MS MARCO, WSD, Financial PhraseBank |
| number | 5 | GPQA confidence, HumanEval, NumEval, event counting |
| multirate | 3 | UltraFeedback, RewardBench, SemEval sentiment |
| audio_annotation | 3 | LibriSpeech, Speech Commands, CoVoST |
| tree_annotation | 3 | PDTB, UD parsing, RumourEval thread structure |
| video | 2 | Video-ChatGPT display |
| triage | 2 | CoNLL-2003 triage, triage template |
| tiered_annotation | 1 | MMLU-Pro tiered evaluation |
| bws | 1 | Chatbot Arena best-worst scaling |
| pure_display | 1 | HELM model card display |
| event_annotation | 1 | BioNLP gene regulation events |
| coreference | 1 | OntoNotes coreference resolution |
| span_link | 9 | Chemical-disease relations, structured sentiment |

---

## Structure

Each task folder contains:
- `metadata.json` - Task metadata (title, description, tags, paper reference, citation)
- `config.yaml` - Potato configuration file
- `sample-data.json` - Example data for testing (8-12 items)

## Quick Start

```bash
# Clone this repository
git clone https://github.com/davidjurgens/potato-showcase.git

# Navigate to a task
cd potato-showcase/text/emotion-sentiment/goemotions

# Run with Potato
potato start config.yaml
```

## Usage

1. Clone this repository
2. Browse categories to find a relevant task
3. Copy the task folder to your project
4. Customize the `config.yaml` for your needs
5. Run with: `potato start config.yaml`

## Contributing

We welcome contributions! To add a new task:
1. Create a folder in the appropriate category
2. Add required files (`metadata.json`, `config.yaml`, `sample-data.json`)
3. Include paper reference and BibTeX citation if based on published work
4. Submit a pull request

## License

MIT License - feel free to use these configurations in your projects.
