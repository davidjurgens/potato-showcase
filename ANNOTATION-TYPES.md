# Annotation Type Reference

A guide to all **22** annotation types supported by [Potato](https://github.com/davidjurgens/potato), with example configurations from this showcase.

---

## radio

**Description:** Single-choice selection from a list of mutually exclusive labels. The most common annotation type, used for classification tasks where exactly one option applies.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [GoEmotions](./text/emotion-sentiment/goemotions/) -- Fine-grained emotion classification
- [ToxiGen Implicit Hate Speech](./text/bias-toxicity/toxigen-implicit-hate/) -- Implicit hate speech detection and classification
- [Stance Detection (VAST)](./text/argumentation-stance/stance-detection/) -- Zero-shot stance detection toward topics

---

## multiselect

**Description:** Multi-label selection where annotators can choose one or more labels from a list. Used when multiple categories can apply simultaneously to a single item.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [GoEmotions](./text/emotion-sentiment/goemotions/) -- Multi-label emotion tagging with 27+ categories
- [PASCAL VOC](./image/classification/pascal-voc/) -- Multi-label object category annotation
- [SemEval Emotion Detection](./text/emotion-sentiment/semeval-emotion-detection/) -- Multi-label tweet emotion classification

---

## text

**Description:** Free-text input field for open-ended responses. Used for tasks requiring written explanations, translations, captions, or any unstructured textual annotation.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [TriviaQA](./text/question-answering/triviaqa-reading-comprehension/) -- Reading comprehension with free-text answers
- [Politeness Annotation](./text/computational-social-science/politeness-annotation/) -- Text rewrite suggestions for politeness transfer
- [WavCaps Audio Captioning](./audio/wavcaps-audio-captioning/) -- Free-text audio descriptions

---

## likert

**Description:** Ordinal rating scale for measuring degree or intensity. Produces a fixed set of ordered response levels (e.g., 1-5 stars, Strongly Disagree to Strongly Agree).

**Required fields (one of):**
- `labels`: List of ordered label strings, OR
- `min_label`, `max_label`, `size`: Endpoint labels and scale size (integer >= 2)

**Example tasks:**
- [HelpSteer Multi-Attribute Rating](./preference-learning/helpsteer-multiattribute-rating/) -- Multi-dimensional quality rating on 0-4 scales
- [Stance Detection (VAST)](./text/argumentation-stance/stance-detection/) -- Confidence rating for stance judgments
- [VoiceMOS Quality Assessment](./audio/voicemos-quality-assessment/) -- Speech synthesis quality ratings

---

## slider

**Description:** Continuous or semi-continuous numeric scale with a draggable handle. Used when fine-grained numeric ratings are needed rather than discrete categories.

**Required fields (one of):**
- `labels`: List of label strings for discrete positions, OR
- `min_value`, `max_value`, `starting_value`: Numeric range and initial position

**Example tasks:**
- [STS Benchmark](./text/semantic-similarity/stsb-sentence-similarity/) -- Continuous 0-5 semantic similarity scoring
- [Automated Essay Scoring](./text/education/automated-essay-scoring/) -- Holistic essay quality rating
- [Semantic Similarity Template](./templates/text/semantic-similarity/) -- Reusable slider-based similarity template

---

## span

**Description:** Text span annotation where annotators highlight words or character ranges and assign labels. The core annotation type for NER, keyphrase extraction, and any task requiring in-text markup.

**Required fields:**
- `labels`: Non-empty list of span label strings

**Example tasks:**
- [WNUT-2017 Emerging Entities](./text/named-entity-recognition/wnut2017-emerging-entities/) -- Named entity recognition in social media text
- [FAVA Hallucination Spans](./text/fact-verification/fava-hallucination-spans/) -- Fine-grained hallucination span detection
- [Toxic Spans](./text/hate-speech-moderation/toxic-spans/) -- Character-level toxicity span identification

---

## span_link

**Description:** Relation annotation between two text spans. Annotators first mark entity or event spans, then draw typed links between them to represent relationships such as causation, part-of, or semantic roles.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [MultiTACRED](./text/relation-extraction/multitacred-multilingual-relations/) -- Multilingual relation extraction with 41 relation types
- [CrossRE](./text/relation-extraction/crossre-cross-domain-relations/) -- Cross-domain relation extraction across 6 domains
- [RadGraph-XL](./text/relation-extraction/radgraph-radiology-relations/) -- Radiology entity and relation extraction

---

## select

**Description:** Dropdown selection from a list of options. Similar to radio but rendered as a dropdown menu, useful when the number of options is large and would be unwieldy as radio buttons.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [WSD SemEval-2007](./text/word-sense/wsd-semeval2007/) -- Word sense disambiguation from sense inventories
- [MS MARCO Passage Ranking](./text/information-retrieval/msmarco-passage-ranking/) -- Graded passage relevance selection
- [Financial PhraseBank](./text/financial/financial-phrasebank-sentiment/) -- Financial sentiment classification via dropdown

---

## number

**Description:** Numeric input field for entering integer or decimal values. Used for counting, scoring, or any task requiring a precise numeric response.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [SemEval-2018 Event Counting](./semeval/2018/task05-event-counting/) -- Counting events and participants in news
- [GPQA Expert QA](./evaluation/gpqa-expert-qa/) -- Graduate-level science question evaluation
- [BIG-Bench Task Evaluation](./evaluation/big-bench-task-eval/) -- Confidence scoring for model outputs

---

## multirate

**Description:** Rate multiple items on the same scale simultaneously. Displays a matrix where rows are items (e.g., model responses, attributes) and columns are rating levels, enabling efficient batch rating.

**Required fields:**
- `labels`: List of rating level strings
- `options` or `options_from_data`: List of items to rate, or a data field name to pull items from

**Example tasks:**
- [UltraFeedback Multi-Aspect](./preference-learning/ultrafeedback-multiaspect/) -- Rate AI responses on helpfulness, honesty, instruction-following, and truthfulness
- [SemEval Sentiment Multi-Rating](./text/emotion-sentiment/semeval-sentiment-multirate/) -- Multi-dimensional sentiment rating of tweets
- [RewardBench Reward Evaluation](./evaluation/rewardbench-reward-eval/) -- Multi-aspect reward model evaluation

---

## pure_display

**Description:** Display-only element that shows information to the annotator without collecting any input. Used for presenting context, instructions, model cards, or reference material alongside active annotation fields.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [HELM Model Card Display](./evaluation/helm-model-card-display/) -- Display model performance summaries for review

---

## pairwise

**Description:** Side-by-side comparison of two items where annotators judge which is better, or rate relative quality. The standard annotation type for preference learning and RLHF data collection.

**Required fields:**
- Optional `labels` (list of >= 2 labels for named choices)
- Optional `mode`: `"binary"` (win/lose/tie) or `"scale"` (graded preference)

**Example tasks:**
- [DPO Preference Data](./preference-learning/dpo-preference-data/) -- Pairwise preference collection for Direct Preference Optimization
- [WildBench LLM Evaluation](./evaluation/wildbench-llm-eval/) -- Pairwise LLM output comparison on real-world tasks
- [MT-Bench](./evaluation/mtbench-llm-evaluation/) -- Multi-turn LLM response quality comparison

---

## bws (Best-Worst Scaling)

**Description:** Best-Worst Scaling (MaxDiff) annotation where annotators select the best and worst items from a set. Produces more reliable rankings than direct rating by reducing scale bias.

**Required fields:**
- Optional `tuple_size`: Number of items shown per comparison (integer >= 2)

**Example tasks:**
- [Chatbot Arena BWS](./evaluation/chatbot-arena-pairwise-bws/) -- Best-worst scaling of chatbot responses

---

## image_annotation

**Description:** Spatial annotation on images using drawing tools such as bounding boxes, polygons, freeform regions, landmarks, and brushes. Used for object detection, segmentation, keypoint annotation, and region labeling.

**Required fields:**
- `tools`: List of drawing tools (e.g., `bbox`, `polygon`, `freeform`, `landmark`, `fill`, `eraser`, `brush`)
- `labels`: Non-empty list of label strings for annotated regions

**Example tasks:**
- [RefCOCO Expression Grounding](./image/visual-grounding/refcoco-expression/) -- Bounding box grounding of referring expressions
- [ViTPose Keypoint Annotation](./image/human-pose/vitpose-keypoint-annotation/) -- Human body keypoint and pose annotation
- [CHART-Infographics Analysis](./multimodal/chartinfo-chart-analysis/) -- Chart element detection with bounding boxes

---

## audio_annotation

**Description:** Temporal segment annotation on audio waveforms. Annotators mark time-aligned regions in audio and assign labels, useful for transcription alignment, speaker diarization, and phonetic annotation.

**Required fields:**
- Optional `mode`: `"label"`, `"questions"`, or `"both"`
- If mode is `"label"` or `"both"`: requires `labels`
- If mode is `"questions"` or `"both"`: requires `segment_schemes`

**Example tasks:**
- [CoVoST Speech Translation](./audio/covost-speech-translation/) -- Audio segment labeling for speech translation
- [LibriSpeech Transcription](./audio/librispeech-transcription/) -- Audio segment classification by content type
- [Speech Commands Recognition](./audio/speech-commands-recognition/) -- Keyword boundary annotation in audio clips

---

## video_annotation

**Description:** Temporal segment annotation on video timelines. Annotators mark start/end times of events, actions, or scenes within a video and assign labels to each segment.

**Required fields:**
- Optional `mode`: `"segment"`, `"frame"`, `"keyframe"`, `"tracking"`, or `"combined"`
- Most modes require `labels`

**Example tasks:**
- [Charades-STA Temporal Grounding](./video/temporal-grounding/charades-sta-grounding/) -- Ground language descriptions to video segments
- [AVA Atomic Visual Actions](./video/action-recognition/ava-atomic-actions/) -- Spatio-temporal action annotation in movie clips
- [Ego4D Episodic Memory](./video/ego4d-episodic-memory/) -- Egocentric video activity segmentation and narration

---

## video (display only)

**Description:** Embeds a video player for display purposes without collecting temporal annotations. Used when annotators need to watch video content before responding with other annotation types (radio, text, etc.).

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [Video-ChatGPT QA Display](./video/video-chatgpt-qa-display/) -- Video display for QA evaluation of model outputs
- [TVSum Summarization](./video/summarization/tvsum-summarization/) -- Video display for frame-level importance scoring

---

## coreference

**Description:** Coreference chain annotation where annotators link mentions (pronouns, noun phrases, names) that refer to the same real-world entity into clusters. Specialized for entity and event coreference resolution.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [OntoNotes Coreference](./text/coreference/ontonotes-coreference-resolution/) -- Full coreference resolution on the OntoNotes 5.0 corpus

---

## tree_annotation

**Description:** Hierarchical tree structure annotation where annotators build parent-child relationships between nodes. Used for syntactic parsing, discourse structure, and any task requiring tree-shaped output.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [Universal Dependencies Parsing](./text/parsing/ud-dependency-parsing/) -- Syntactic dependency tree construction
- [PDTB Discourse Relations](./text/discourse/pdtb-discourse-relations-tree/) -- Hierarchical discourse tree annotation
- [RumourEval Verification](./text/computational-social-science/rumoureval-verification/) -- Thread structure analysis for rumour verification

---

## triage

**Description:** Quick pre-annotation filtering step where annotators flag whether an item needs detailed annotation. Designed to speed up annotation pipelines by letting annotators skip irrelevant items before applying more expensive annotation types.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [CoNLL-2003 NER with Triage](./text/named-entity-recognition/conll2003-ner-triage/) -- Triage step before span-based NER annotation
- [Triage Quick Annotation Template](./templates/text/triage-quick-annotation/) -- Reusable triage template for any workflow

---

## event_annotation

**Description:** Structured event extraction annotation where annotators identify event triggers, arguments, and roles within text. Tailored for tasks that require marking complex event structures with typed participants.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [BioNLP Gene Regulation Events](./text/domain-specific/bionlp-gene-regulation-events/) -- Biomedical event extraction for gene regulation

---

## tiered_annotation

**Description:** Multi-level hierarchical annotation where annotators assign labels at multiple tiers (e.g., topic then subtopic, coarse then fine category). Each tier can have its own label set, enabling structured taxonomic annotation.

**Required fields:**
- `tiers`: List of tier definitions (each a dict with at least a `name` key)
- `source_field`: The data field to annotate

**Example tasks:**
- [MMLU-Pro Tiered Evaluation](./preference-learning/mmlu-pro-tiered-eval/) -- Tiered topic and subtopic categorization for multi-subject QA
