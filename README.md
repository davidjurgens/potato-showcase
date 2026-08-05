<div align="center" markdown="1">

# 🥔 Potato Annotation Showcase

**A library of real-world annotation task designs for [Potato](https://www.potatoannotator.com), the open-source annotation tool for NLP.**

[Website](https://www.potatoannotator.com) · [Docs](https://www.potatoannotator.com/docs) · [Quick Start](https://www.potatoannotator.com/docs/getting-started/quick-start) · [Showcase](https://www.potatoannotator.com/showcase) · [Blog](https://www.potatoannotator.com/blog) · [Community](https://www.potatoannotator.com/community)

![Designs](https://img.shields.io/badge/designs-437-ff6b35?style=flat-square)
![Annotation types](https://img.shields.io/badge/annotation_types-39-555?style=flat-square)
![SemEval tasks](https://img.shields.io/badge/SemEval_tasks-100-555?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-4c9a2a?style=flat-square)

</div>

These **437** [text and multimodal annotation](https://www.potatoannotator.com/why-potato) designs cover 39 Potato annotation types, 100 SemEval shared tasks (2013-2026), 26 agentic evaluation tasks, and benchmarks from ACL, EMNLP, NeurIPS, ICML, ICLR, and CVPR.

The point is to save you from starting an annotation project at a blank config file. Find a task close to what you need, copy the folder, and change the labels and instructions. Most of these are built from a real dataset or paper, so each one shows how a published annotation scheme actually turns into a working Potato setup.

The collection keeps growing. We add tasks as new datasets and SemEval tracks come out, and as Potato itself gains annotation types. The newest batch covers agent evaluation (`process_reward`, `gui_trajectory`, `tool_call_review`, `failure_attribution`, `agent_scorecard`) plus thirteen other new schemes, among them `ranking`, `error_span`, `text_edit`, `soft_label`, and `rubric_eval`. It's maintained by the Potato development team alongside the tool, so the examples stay in step with what Potato can currently do. If a task you need isn't here, [open a pull request](#contributing) or [submit a design](https://www.potatoannotator.com/showcase/submit).

If you're new to Potato, the [quick-start guide](https://www.potatoannotator.com/docs/getting-started/quick-start) and [documentation](https://www.potatoannotator.com/docs) cover the basics, and you can try many of these designs live in the [Potato showcase](https://www.potatoannotator.com/showcase).

## Categories

| Category | Description | Tasks |
|----------|-------------|-------|
| [**text/**](./text/) | Text-based NLP tasks (emotion, NER, IE, QA, parsing, etc.) | 144 |
| [**image/**](./image/) | Image annotation (classification, VQA, grounding, medical) | 34 |
| [**video/**](./video/) | Video annotation (action recognition, QA, summarization) | 40 |
| [**audio/**](./audio/) | Audio annotation (transcription, commands, captioning) | 19 |
| [**evaluation/**](./evaluation/) | AI output evaluation (LLM judging, code, benchmarks) | 27 |
| [**preference-learning/**](./preference-learning/) | RLHF, DPO, and preference annotation tasks | 18 |
| [**multimodal/**](./multimodal/) | Cross-modal tasks (robotics, chart analysis, science QA) | 9 |
| [**agentic/**](./agentic/) | Agent evaluation (traces, coding agents, PRM, safety) | 26 |
| [**semeval/**](./semeval/) | SemEval shared tasks (2013-2026, 100 tasks) | 100 |
| [**templates/**](./templates/) | Generic reusable annotation templates | 20 |

---

## Text Annotation (144 tasks)

*Guides: [Creating a sentiment task](https://www.potatoannotator.com/blog/sentiment-analysis-tutorial) · [Building an NER task](https://www.potatoannotator.com/blog/building-ner-task) · [Content moderation setup](https://www.potatoannotator.com/blog/content-moderation-annotation) · [Finding hallucinations with span annotation](https://www.potatoannotator.com/blog/finding-hallucinations-with-span-annotation)*

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Emotion & Sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment) | 16 | GoEmotions, NRC-VAD & Affect Intensity (Best-Worst Scaling), Words of Warmth, WorryWords, Word-Colour |
| [Hate Speech & Moderation](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation) | 6 | HateXplain, Implicit Hate, Social Bias Frames, Toxic Spans, AfriHate |
| [Named Entity Recognition](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition) | 7 | CoNLL-2003, WNUT-2017, Biomedical NER, Complex NER, MasakhaNER 2.0 |
| [Information Extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction) | 8 | KG-BERT, Event Arguments, Dialogue Relations, MASSIVE (intent + slot filling) |
| [Argumentation & Stance](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance) | 5 | Argument Quality, Stance Detection, Rumor Stance |
| [Fact Verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification) | 9 | FActScore, FAVA, Scientific Claims, Propaganda |
| [Commonsense & Ethics](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics) | 6 | Social Chemistry, Moral Stories, Commonsense Inference |
| [Explainability](https://github.com/davidjurgens/potato-showcase/tree/main/text/explainability) | 2 | Rationale Annotation, NLI Explanation |
| [Dialogue](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue) | 7 | SWBD-DAMSL Dialogue Acts, Conversation Quality |
| [Political & Media](https://github.com/davidjurgens/potato-showcase/tree/main/text/political-media) | 1 | Political Discourse |
| [Discourse](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse) | 4 | PDTB Discourse Trees, DISRPT, Timeline Relations |
| [Coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference) | 5 | OntoNotes, CorefUD, MAVEN-ERE, ECB+ cross-document events |
| [Cross-lingual](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual) | 7 | XNLI, Belebele, FLORES MT Quality, IndicNLP, MasakhaNEWS, NusaX |
| [Domain-specific](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific) | 9 | BioNLP, ChemProt, Clinical NER, Legal, Medical |
| [Computational Social Science](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science) | 9 | OffensEval, Moral Foundations, Ruddit (best-worst scaling), conjoint profiles |
| [Relation Extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction) | 5 | MultiTACRED, CrossRE, RadGraph, SciER |
| [Entity Linking](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking) | 4 | AIDA-CoNLL, MedMentions, DWIE document-level linking |
| [Code Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/text/code-annotation) | 3 | CodeXGLUE Defect Detection |
| [Tabular](https://github.com/davidjurgens/potato-showcase/tree/main/text/tabular) | 2 | Tabular Data Annotation |
| [Reading Comprehension](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension) | 4 | SQuAD Extractive QA |
| [Natural Language Inference](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference) | 3 | SNLI, MultiNLI, ChaosNLI label distributions |
| [Question Answering](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering) | 3 | Natural Questions, TriviaQA |
| [Information Retrieval](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-retrieval) | 2 | MS MARCO, TREC-DL |
| [Semantic Similarity](https://github.com/davidjurgens/potato-showcase/tree/main/text/semantic-similarity) | 1 | STS Benchmark |
| [Word Sense](https://github.com/davidjurgens/potato-showcase/tree/main/text/word-sense) | 2 | SemEval-2007 WSD |
| [Parsing](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing) | 3 | Universal Dependencies, MasakhaPOS, Interlinear Glossing |
| [Education](https://github.com/davidjurgens/potato-showcase/tree/main/text/education) | 4 | Essay Scoring, MathDial Tutoring, JFLEG fluency rewriting |
| [Financial](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial) | 3 | FinBERT, FLARE NER, Financial PhraseBank |
| [Bias & Toxicity](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity) | 3 | Bias and toxicity annotation designs |
| [Topic Classification](https://github.com/davidjurgens/potato-showcase/tree/main/text/topic-classification) | 1 | RCV1 hierarchical topic coding |

---

## Image Annotation (34 tasks)

*Guides: [Image classification](https://www.potatoannotator.com/blog/image-classification-tutorial) · [Bounding boxes for object detection](https://www.potatoannotator.com/blog/bounding-box-annotation) · [Polygon annotation for segmentation](https://www.potatoannotator.com/blog/polygon-annotation-guide) · [Medical image annotation](https://www.potatoannotator.com/blog/medical-imaging-annotation)*

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Classification](https://github.com/davidjurgens/potato-showcase/tree/main/image/classification) | 6 | MS-COCO, ImageNet, Places365, CUB-200 |
| [Segmentation](https://github.com/davidjurgens/potato-showcase/tree/main/image/segmentation) | 3 | Cityscapes, ADE20K, LIP Human Parsing |
| [Visual QA](https://github.com/davidjurgens/potato-showcase/tree/main/image/visual-qa) | 2 | VQAv2, TextVQA |
| [Visual Grounding](https://github.com/davidjurgens/potato-showcase/tree/main/image/visual-grounding) | 1 | RefCOCO |
| [Medical Imaging](https://github.com/davidjurgens/potato-showcase/tree/main/image/medical) | 3 | CheXpert, MIMIC-CXR, Camelyon Pathology |
| [Human Pose](https://github.com/davidjurgens/potato-showcase/tree/main/image/human-pose) | 1 | ViTPose Keypoint Annotation |
| [Generation Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/image/generation-eval) | 1 | T2I-CompBench |
| [Autonomous Driving](https://github.com/davidjurgens/potato-showcase/tree/main/image/driving) | 2 | KITTI, BDD100K |
| [Aerial & Remote Sensing](https://github.com/davidjurgens/potato-showcase/tree/main/image/aerial) | 3 | BigEarthNet, xView, DOTA |
| [Specialized Domains](https://github.com/davidjurgens/potato-showcase/tree/main/image/specialized) | 6 | MVTec-AD, DeepFashion, CelebA, iWildCam |
| [Document & Table Analysis](./image/) | 3 | DocLayNet, OmniDocBench, WTW wired tables |
| [Other Image Tasks](./image/) | 3 | SA-1B, FLAIR land use, xBD building damage |

---

## Video Annotation (40 tasks)

*Guides: [Frame-by-frame video annotation](https://www.potatoannotator.com/blog/video-frame-annotation) · [Multi-object tracking](https://www.potatoannotator.com/blog/multi-object-tracking)*

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| [Action Recognition](https://github.com/davidjurgens/potato-showcase/tree/main/video/action-recognition) | 10 | AVA, Charades, THUMOS14, EPIC-KITCHENS |
| [Temporal Grounding](https://github.com/davidjurgens/potato-showcase/tree/main/video/temporal-grounding) | 4 | ActivityNet Captions, DiDeMo, Charades-STA, QVHighlights |
| [Video Summarization](https://github.com/davidjurgens/potato-showcase/tree/main/video/summarization) | 4 | TVSum, SumMe, YouTube Highlights, LSMDC |
| [Boundary Detection](https://github.com/davidjurgens/potato-showcase/tree/main/video/boundary-detection) | 3 | Scene/Shot Boundary, MovieScenes |
| [Video QA](https://github.com/davidjurgens/potato-showcase/tree/main/video/video-qa) | 2 | NExT-QA, MVBench |
| [Scene Understanding](https://github.com/davidjurgens/potato-showcase/tree/main/video/scene-understanding) | 1 | MovieNet Scene Classification |
| [Instructional Video](https://github.com/davidjurgens/potato-showcase/tree/main/video/instructional) | 2 | HowTo100M, YouCook2 |
| [Other Video Tasks](./video/) | 14 | Video-ChatGPT, Sign Language, Child Language, etc. |

---

## Audio Annotation (19 tasks)

*Guides: [Audio transcription review](https://www.potatoannotator.com/blog/audio-transcription-task) · [Speaker diarization](https://www.potatoannotator.com/blog/speaker-diarization-annotation) · [Speech emotion classification](https://www.potatoannotator.com/blog/audio-emotion-classification) · [Music genre classification](https://www.potatoannotator.com/blog/music-genre-classification)*

| Task | Description |
|------|-------------|
| [librispeech-transcription](https://github.com/davidjurgens/potato-showcase/tree/main/audio/librispeech-transcription) | Audio quality + transcription (slider, audio_annotation) |
| [speech-commands-recognition](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speech-commands-recognition) | Speech command labeling (audio_annotation) |
| [covost-speech-translation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/covost-speech-translation) | Speech translation evaluation |
| [clotho-audio-captioning](https://github.com/davidjurgens/potato-showcase/tree/main/audio/clotho-audio-captioning) | Audio event captioning |
| [audio-transcription](https://github.com/davidjurgens/potato-showcase/tree/main/audio/audio-transcription) | Speech transcription review |
| [speaker-diarization](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speaker-diarization) | Speaker identification |
| [emotion-recognition](https://github.com/davidjurgens/potato-showcase/tree/main/audio/emotion-recognition) | Speech emotion classification |
| [music-genre-classification](https://github.com/davidjurgens/potato-showcase/tree/main/audio/music-genre-classification) | Music genre tagging |
| [sporc-podcast-turn-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/sporc-podcast-turn-annotation) | Podcast speaker-role and turn annotation (audio dialogue display) |
| [podcastfillers-disfluency-tagging](https://github.com/davidjurgens/potato-showcase/tree/main/audio/podcastfillers-disfluency-tagging) | Filler-word and disfluency tagging on speech transcripts |
| + 9 more | DiSPLACE, DoReCo, EmoBox, VoiceMOS, etc. |

---

## Evaluation Tasks (27 tasks)

*Guides: [Calibrating LLM-as-judge against humans](https://www.potatoannotator.com/blog/trust-your-llm-judge-calibration) · [MT-Bench-style rubric evaluation](https://www.potatoannotator.com/blog/rubric-evaluation-mt-bench-style) · [Evaluating RAG systems](https://www.potatoannotator.com/blog/rag-evaluation-with-human-annotation)*

| Task | Paper | Types |
|------|-------|-------|
| [wildbench-llm-eval](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/wildbench-llm-eval) | WildBench (COLM 2024) | pairwise, likert, text |
| [mt-bench-judge-consistency](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/mt-bench-judge-consistency) | MT-Bench (NeurIPS 2023) | pairwise, likert, radio |
| [arena-hard-auto](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/arena-hard-auto) | Arena Hard (2024) | pairwise (scale), likert |
| [rewardbench-reward-eval](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/rewardbench-reward-eval) | RewardBench (ICML 2024) | pairwise, radio, multirate |
| [mmlu-knowledge-eval](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/mmlu-knowledge-eval) | MMLU (ICLR 2021) | radio, text |
| [humaneval-code-correctness](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/humaneval-code-correctness) | HumanEval (2021) | radio, text, number |
| [gpqa-expert-qa](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/gpqa-expert-qa) | GPQA (ICLR 2024) | number, radio, text |
| [big-bench-task-eval](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/big-bench-task-eval) | BIG-Bench (TMLR 2023) | radio, text, number |
| [helm-model-card-display](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/helm-model-card-display) | HELM (TMLR 2023) | pure_display, likert |
| [chatbot-arena-pairwise-bws](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/chatbot-arena-pairwise-bws) | Chatbot Arena (ICML 2024) | bws, pairwise |
| [mqm-mt-error-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/mqm-mt-error-annotation) | MQM (TACL 2021) | error_span |
| [wmt15-relative-ranking](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/wmt15-relative-ranking) | WMT15 (WMT 2015) | ranking |
| [flask-skill-rubric-evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/flask-skill-rubric-evaluation) | FLASK (ICLR 2024) | rubric_eval, radio |
| [godspeed-agent-perception](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/godspeed-agent-perception) | Godspeed (Int J Soc Robotics 2009) | semantic_differential |
| + 13 more | AlpacaEval, DoNotAnswer, ESA-MT, IFEval, etc. |

---

## Preference Learning & RLHF (18 tasks)

*Guides: [Pairwise comparison modes](https://www.potatoannotator.com/blog/pairwise-agent-comparison-guide) · [Trajectory editing for SFT & DPO](https://www.potatoannotator.com/blog/trajectory-editing-sft-dpo-training-data) · [Collecting process-reward data](https://www.potatoannotator.com/blog/process-reward-models-annotation-guide)*

| Task | Paper | Types |
|------|-------|-------|
| [dpo-preference-data](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/dpo-preference-data) | DPO (NeurIPS 2023) | pairwise, radio, text |
| [ultrafeedback-multiaspect](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/ultrafeedback-multiaspect) | UltraFeedback (ICML 2024) | multirate, likert, text |
| [spin-self-play](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/spin-self-play) | SPIN (ICML 2024) | pairwise, radio |
| [constitutional-ai-harmlessness](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/constitutional-ai-harmlessness) | Constitutional AI (2022) | radio, likert, text |
| [mmlu-pro-tiered-eval](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/mmlu-pro-tiered-eval) | MMLU-Pro (NeurIPS 2024) | tiered_annotation, radio |
| + 13 more | HH-RLHF, SafeRLHF, BeaverTails, WebGPT, etc. |

---

## Agentic Evaluation (26 tasks)

Tasks showcasing Potato's [agentic annotation](https://www.potatoannotator.com/docs/features/agentic-annotation) features. See the docs for [live agent evaluation](https://www.potatoannotator.com/docs/features/live-agent-evaluation) and [coding agent annotation](https://www.potatoannotator.com/docs/features/coding-agent-annotation).

*Guides: [Human evaluation of agent traces](https://www.potatoannotator.com/blog/evaluating-ai-agents-with-potato) · [Coding agent annotation](https://www.potatoannotator.com/blog/coding-agent-annotation-with-potato) · [Web agent annotation](https://www.potatoannotator.com/blog/web-agent-annotation-guide) · [Computer-use agent evaluation](https://www.potatoannotator.com/blog/computer-use-agent-evaluation)*

| Subcategory | Tasks | Examples |
|-------------|-------|----------|
| Agent Trace Evaluation | 7 | AgentRewardBench, AgentBoard, MAST, τ-bench, TRAJEVAL, Who&When, MultiAgentBench |
| Coding Agent Evaluation | 6 | SWE-bench, SWE-bench Verified, SWE-bench+, DevBench, RefactorBench, BigCodeBench |
| Visual/GUI Agent Eval | 5 | WebArena, VisualWebArena, OSWorld, AndroidWorld, Android in the Wild |
| Process Reward Models | 4 | PRM800K step verification, SWE-PRM, CodePRM, ProcessBench |
| Safety & Preference | 2 | R-Judge agent safety, CodeUltraFeedback |
| Web Agent Annotation | 1 | Mind2Web |
| Tool-Use Evaluation | 1 | API-Bank tool call review |

---

## SemEval Shared Tasks (100 tasks)

Comprehensive coverage of SemEval shared tasks from 2013-2026. Browse by year below or under [`semeval/`](./semeval/).

| Year | Tasks | Highlights |
|------|-------|------------|
| [2026](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2026) | 10 | Dimensional ABSA, and other 2026 tracks |
| [2025](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2025) | 10 | Multimodal idiomaticity, entity-aware MT, emotion detection |
| [2024](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2024) | 9 | Semantic relatedness, persuasion in memes, BRAINTEASER |
| [2023](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2023) | 10 | Visual WSD, clickbait spoiling, AfriSenti |
| [2022](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2022) | 10 | Patronizing language, idiomaticity, news similarity |
| [2021](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2021) | 9 | Lexical complexity, humor detection, MeasEval |
| [2020](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2020) | 9 | Commonsense validation, counterfactuals, code-mixed |
| [2019](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2019) | 7 | HatEval, hyperpartisan news, suggestion mining |
| [2018](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2018) | 10 | Emoji prediction, irony, cybersecurity NER |
| [2017](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2017) | 5 | Financial sentiment, humor, pun detection |
| [2016](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2016) | 7 | Stance detection, aspect sentiment, clinical TempEval |
| [2013-2015](./semeval/) | 4 | Drug interactions, ABSA, timeline ordering, clinical |

---

## Annotation Type Coverage

These designs use 39 distinct Potato annotation types. Counts below are scheme instances, so a task with three schemes appears in three rows.

| Type | Count | Example Tasks |
|------|-------|---------------|
| radio | 605 | GoEmotions, SNLI, MMLU, most classification tasks |
| text | 211 | SQuAD, Natural Questions, code review, translations |
| likert | 146 | STS-B, essay scoring, MT quality, humor ratings |
| multiselect | 136 | GoEmotions, moral foundations, persuasion techniques |
| span | 124 | NER tasks, PICO extraction, DWIE entity linking |
| video_annotation | 48 | Action recognition, temporal grounding, MVBench |
| pairwise | 18 | DPO, Arena Hard, WildBench, MT-Bench |
| slider | 12 | STS-B similarity, essay scoring, word similarity |
| span_link | 9 | Chemical-disease relations, structured sentiment |
| multirate | 7 | UltraFeedback, RewardBench, AgentRewardBench |
| image_annotation | 6 | ViTPose, RefCOCO, Camelyon pathology |
| select | 6 | MS MARCO, WSD, Financial PhraseBank |
| number | 5 | GPQA confidence, HumanEval, NumEval, event counting |
| semantic_differential | 5 | Godspeed agent perception |
| audio_annotation | 3 | LibriSpeech, Speech Commands, CoVoST |
| tree_annotation | 3 | PDTB, UD parsing, RumourEval thread structure |
| bws | 2 | Chatbot Arena, Ruddit offensiveness |
| triage | 2 | CoNLL-2003 triage, triage template |
| video | 2 | Video-ChatGPT display, TVSum |
| agent_scorecard | 1 | MultiAgentBench collaboration scorecard |
| conjoint | 1 | Conjoint analysis of candidate/immigrant profiles |
| coreference | 1 | OntoNotes coreference resolution |
| error_span | 1 | MQM machine translation error annotation |
| event_annotation | 1 | BioNLP gene regulation events |
| failure_attribution | 1 | Who&When multi-agent failure attribution |
| gui_trajectory | 1 | Android in the Wild mobile trajectory review |
| hierarchical_multiselect | 1 | RCV1 hierarchical topic coding |
| multi_document_event | 1 | ECB+ cross-document event coreference |
| process_reward | 1 | ProcessBench earliest-error identification |
| pure_display | 1 | HELM model card display |
| ranking | 1 | WMT15 relative ranking of translations |
| rubric_eval | 1 | FLASK skill-based rubric evaluation |
| soft_label | 1 | ChaosNLI label distributions |
| speech_transcript | 1 | PodcastFillers disfluency tagging |
| table_grid | 1 | WTW wired table structure annotation |
| temporal_grounding | 1 | QVHighlights moment grounding and saliency |
| text_edit | 1 | JFLEG fluency rewriting |
| tiered_annotation | 1 | MMLU-Pro tiered evaluation |
| tool_call_review | 1 | API-Bank tool call review |

See [ANNOTATION-TYPES.md](./ANNOTATION-TYPES.md) for a per-type reference with required fields and example configurations.

------|-------|---------------|
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

First, [install Potato](https://www.potatoannotator.com/docs/getting-started/installation), then:

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

New tasks are welcome. To add one:
1. Create a folder in the matching category
2. Add the three files (`metadata.json`, `config.yaml`, `sample-data.json`)
3. Include the paper reference and BibTeX citation if it's based on published work
4. Open a pull request

The Potato development team reviews submissions and keeps the collection current as the tool evolves.

## Learn More About Potato

- [Potato website](https://www.potatoannotator.com) and [why Potato](https://www.potatoannotator.com/why-potato)
- [Documentation](https://www.potatoannotator.com/docs) and the [quick-start guide](https://www.potatoannotator.com/docs/getting-started/quick-start)
- [Annotation types](https://www.potatoannotator.com/docs/annotation-types/radio-multiselect), covering radio, span, image, audio, and video
- [Agentic annotation](https://www.potatoannotator.com/docs/features/agentic-annotation) for evaluating LLM and coding agents
- [Showcase](https://www.potatoannotator.com/showcase) and [community](https://www.potatoannotator.com/community)
- [Potato source code](https://github.com/davidjurgens/potato) on GitHub

## License

MIT License - feel free to use these configurations in your projects.
