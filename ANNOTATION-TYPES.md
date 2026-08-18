# Annotation Type Reference

A guide to the 39 annotation types used in this showcase, with example configurations for each. [Potato](https://www.potatoannotator.com) supports more scheme types than these; the [annotation types documentation](https://www.potatoannotator.com/docs/annotation-types/radio-multiselect) has the full list.

---

## radio

**Description:** Single-choice selection from a list of mutually exclusive labels, for classification tasks where exactly one option applies.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [GoEmotions](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/goemotions) -- Fine-grained emotion classification
- [ToxiGen Implicit Hate Speech](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity/toxigen-implicit-hate) -- Implicit hate speech detection and classification
- [Stance Detection (VAST)](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/stance-detection) -- Zero-shot stance detection toward topics

---

## multiselect

**Description:** Multi-label selection where annotators can choose one or more labels from a list. Used when multiple categories can apply simultaneously to a single item.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [GoEmotions](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/goemotions) -- Multi-label emotion tagging with 27+ categories
- [PASCAL VOC](https://github.com/davidjurgens/potato-showcase/tree/main/image/classification/pascal-voc) -- Multi-label object category annotation
- [SemEval Emotion Detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/semeval-emotion-detection) -- Multi-label tweet emotion classification

---

## text

**Description:** Free-text input field for open-ended responses. Used for tasks requiring written explanations, translations, captions, or any unstructured textual annotation.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [TriviaQA](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering/triviaqa-reading-comprehension) -- Reading comprehension with free-text answers
- [Politeness Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/politeness-annotation) -- Text rewrite suggestions for politeness transfer
- [WavCaps Audio Captioning](https://github.com/davidjurgens/potato-showcase/tree/main/audio/wavcaps-audio-captioning) -- Free-text audio descriptions

---

## likert

**Description:** Ordinal rating scale for measuring degree or intensity. Produces a fixed set of ordered response levels (e.g., 1-5 stars, Strongly Disagree to Strongly Agree).

**Required fields (one of):**
- `labels`: List of ordered label strings, OR
- `min_label`, `max_label`, `size`: Endpoint labels and scale size (integer >= 2)

**Example tasks:**
- [HelpSteer Multi-Attribute Rating](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/helpsteer-multiattribute-rating) -- Multi-dimensional quality rating on 0-4 scales
- [Stance Detection (VAST)](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/stance-detection) -- Confidence rating for stance judgments
- [VoiceMOS Quality Assessment](https://github.com/davidjurgens/potato-showcase/tree/main/audio/voicemos-quality-assessment) -- Speech synthesis quality ratings

---

## slider

**Description:** Continuous or semi-continuous numeric scale with a draggable handle. Used when fine-grained numeric ratings are needed rather than discrete categories.

**Required fields (one of):**
- `labels`: List of label strings for discrete positions, OR
- `min_value`, `max_value`, `starting_value`: Numeric range and initial position

**Example tasks:**
- [STS Benchmark](https://github.com/davidjurgens/potato-showcase/tree/main/text/semantic-similarity/stsb-sentence-similarity) -- Continuous 0-5 semantic similarity scoring
- [Automated Essay Scoring](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/automated-essay-scoring) -- Holistic essay quality rating
- [Semantic Similarity Template](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/semantic-similarity) -- Reusable slider-based similarity template

---

## span

**Description:** Text span annotation where annotators highlight words or character ranges and assign labels. Used for NER, keyphrase extraction, and other in-text markup.

**Required fields:**
- `labels`: Non-empty list of span label strings

**Example tasks:**
- [WNUT-2017 Emerging Entities](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/wnut2017-emerging-entities) -- Named entity recognition in social media text
- [FAVA Hallucination Spans](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/fava-hallucination-spans) -- Fine-grained hallucination span detection
- [Toxic Spans](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/toxic-spans) -- Character-level toxicity span identification

---

## span_link

**Description:** Relation annotation between two text spans. Annotators first mark entity or event spans, then draw typed links between them to represent relationships such as causation, part-of, or semantic roles.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [MultiTACRED](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/multitacred-multilingual-relations) -- Multilingual relation extraction with 41 relation types
- [CrossRE](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/crossre-cross-domain-relations) -- Cross-domain relation extraction across 6 domains
- [RadGraph-XL](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/radgraph-radiology-relations) -- Radiology entity and relation extraction

---

## select

**Description:** Dropdown selection from a list of options. Similar to radio but rendered as a dropdown menu, useful when the number of options is large and would be unwieldy as radio buttons.

**Required fields:**
- `labels`: Non-empty list of label strings

**Example tasks:**
- [WSD SemEval-2007](https://github.com/davidjurgens/potato-showcase/tree/main/text/word-sense/wsd-semeval2007) -- Word sense disambiguation from sense inventories
- [MS MARCO Passage Ranking](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-retrieval/msmarco-passage-ranking) -- Graded passage relevance selection
- [Financial PhraseBank](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial/financial-phrasebank-sentiment) -- Financial sentiment classification via dropdown

---

## number

**Description:** Numeric input field for entering integer or decimal values. Used for counting, scoring, or any task requiring a precise numeric response.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [SemEval-2018 Event Counting](https://github.com/davidjurgens/potato-showcase/tree/main/semeval/2018/task05-event-counting) -- Counting events and participants in news
- [GPQA Expert QA](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/gpqa-expert-qa) -- Graduate-level science question evaluation
- [BIG-Bench Task Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/big-bench-task-eval) -- Confidence scoring for model outputs

---

## multirate

**Description:** Rate multiple items on the same scale simultaneously. Displays a matrix where rows are items (e.g., model responses, attributes) and columns are rating levels.

**Required fields:**
- `labels`: List of rating level strings
- `options` or `options_from_data`: List of items to rate, or a data field name to pull items from

**Example tasks:**
- [UltraFeedback Multi-Aspect](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/ultrafeedback-multiaspect) -- Rate AI responses on helpfulness, honesty, instruction-following, and truthfulness
- [SemEval Sentiment Multi-Rating](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/semeval-sentiment-multirate) -- Multi-dimensional sentiment rating of tweets
- [RewardBench Reward Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/rewardbench-reward-eval) -- Multi-aspect reward model evaluation

---

## pure_display

**Description:** Display-only element that shows information to the annotator without collecting any input. Used for presenting context, instructions, model cards, or reference material alongside active annotation fields.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [HELM Model Card Display](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/helm-model-card-display) -- Display model performance summaries for review

---

## pairwise

**Description:** Side-by-side comparison of two items where annotators judge which is better, or rate relative quality. Used for preference learning and RLHF data collection.

**Required fields:**
- Optional `labels` (list of >= 2 labels for named choices)
- Optional `mode`: `"binary"` (win/lose/tie) or `"scale"` (graded preference)

**Example tasks:**
- [DPO Preference Data](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/dpo-preference-data) -- Pairwise preference collection for Direct Preference Optimization
- [WildBench LLM Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/wildbench-llm-eval) -- Pairwise LLM output comparison on real-world tasks
- [MT-Bench](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/mtbench-llm-evaluation) -- Multi-turn LLM response quality comparison

---

## bws (Best-Worst Scaling)

**Description:** Best-Worst Scaling (MaxDiff) annotation where annotators select the best and worst items from a set. Produces more reliable rankings than direct rating by reducing scale bias.

**Required fields:**
- Optional `tuple_size`: Number of items shown per comparison (integer >= 2)

**Example tasks:**
- [Chatbot Arena BWS](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/chatbot-arena-pairwise-bws) -- Best-worst scaling of chatbot responses
- [Ruddit Offensiveness BWS](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/ruddit-offensiveness-bws) -- Best-worst scaling of Reddit comment offensiveness (tuple size 4)

---

## image_annotation

**Description:** Spatial annotation on images using drawing tools such as bounding boxes, polygons, freeform regions, landmarks, and brushes. Used for object detection, segmentation, keypoint annotation, and region labeling.

**Required fields:**
- `tools`: List of drawing tools (e.g., `bbox`, `polygon`, `freeform`, `landmark`, `fill`, `eraser`, `brush`)
- `labels`: Non-empty list of label strings for annotated regions

**Example tasks:**
- [RefCOCO Expression Grounding](https://github.com/davidjurgens/potato-showcase/tree/main/image/visual-grounding/refcoco-expression) -- Bounding box grounding of referring expressions
- [ViTPose Keypoint Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/image/human-pose/vitpose-keypoint-annotation) -- Human body keypoint and pose annotation
- [CHART-Infographics Analysis](https://github.com/davidjurgens/potato-showcase/tree/main/multimodal/chartinfo-chart-analysis) -- Chart element detection with bounding boxes

---

## audio_annotation

**Description:** Temporal segment annotation on audio waveforms. Annotators mark time-aligned regions in audio and assign labels, useful for transcription alignment, speaker diarization, and phonetic annotation.

**Required fields:**
- Optional `mode`: `"label"`, `"questions"`, or `"both"`
- If mode is `"label"` or `"both"`: requires `labels`
- If mode is `"questions"` or `"both"`: requires `segment_schemes`

**Example tasks:**
- [CoVoST Speech Translation](https://github.com/davidjurgens/potato-showcase/tree/main/audio/covost-speech-translation) -- Audio segment labeling for speech translation
- [LibriSpeech Transcription](https://github.com/davidjurgens/potato-showcase/tree/main/audio/librispeech-transcription) -- Audio segment classification by content type
- [Speech Commands Recognition](https://github.com/davidjurgens/potato-showcase/tree/main/audio/speech-commands-recognition) -- Keyword boundary annotation in audio clips

---

## video_annotation

**Description:** Temporal segment annotation on video timelines. Annotators mark start/end times of events, actions, or scenes within a video and assign labels to each segment.

**Required fields:**
- Optional `mode`: `"segment"`, `"frame"`, `"keyframe"`, `"tracking"`, or `"combined"`
- Most modes require `labels`

**Example tasks:**
- [Charades-STA Temporal Grounding](https://github.com/davidjurgens/potato-showcase/tree/main/video/temporal-grounding/charades-sta-grounding) -- Ground language descriptions to video segments
- [AVA Atomic Visual Actions](https://github.com/davidjurgens/potato-showcase/tree/main/video/action-recognition/ava-atomic-actions) -- Spatio-temporal action annotation in movie clips
- [Ego4D Episodic Memory](https://github.com/davidjurgens/potato-showcase/tree/main/video/ego4d-episodic-memory) -- Egocentric video activity segmentation and narration

---

## video (display only)

**Description:** Embeds a video player without collecting temporal annotations. Used when annotators need to watch video content before responding with other annotation types (radio, text, etc.).

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [Video-ChatGPT QA Display](https://github.com/davidjurgens/potato-showcase/tree/main/video/video-chatgpt-qa-display) -- Video display for QA evaluation of model outputs
- [TVSum Summarization](https://github.com/davidjurgens/potato-showcase/tree/main/video/summarization/tvsum-summarization) -- Video display for frame-level importance scoring

---

## coreference

**Description:** Coreference chain annotation where annotators link mentions (pronouns, noun phrases, names) that refer to the same real-world entity into clusters. Used for entity and event coreference resolution.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [OntoNotes Coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/ontonotes-coreference-resolution) -- Full coreference resolution on the OntoNotes 5.0 corpus

---

## tree_annotation

**Description:** Hierarchical tree structure annotation where annotators build parent-child relationships between nodes. Used for syntactic parsing, discourse structure, and any task requiring tree-shaped output.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [Universal Dependencies Parsing](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing/ud-dependency-parsing) -- Syntactic dependency tree construction
- [PDTB Discourse Relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse/pdtb-discourse-relations-tree) -- Hierarchical discourse tree annotation
- [RumourEval Verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/rumoureval-verification) -- Thread structure analysis for rumour verification

---

## triage

**Description:** Quick pre-annotation filtering step where annotators flag whether an item needs detailed annotation. Speeds up a pipeline by letting annotators skip irrelevant items before the more expensive schemes run.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [CoNLL-2003 NER with Triage](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/conll2003-ner-triage) -- Triage step before span-based NER annotation
- [Triage Quick Annotation Template](https://github.com/davidjurgens/potato-showcase/tree/main/templates/text/triage-quick-annotation) -- Reusable triage template for any workflow

---

## event_annotation

**Description:** Structured event extraction annotation where annotators identify event triggers, arguments, and roles within text. Used for tasks that mark event structures with typed participants.

**Required fields:**
- No extra required fields beyond standard scheme fields

**Example tasks:**
- [BioNLP Gene Regulation Events](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/bionlp-gene-regulation-events) -- Biomedical event extraction for gene regulation

---

## tiered_annotation

**Description:** Multi-level hierarchical annotation where annotators assign labels at multiple tiers (e.g., topic then subtopic, coarse then fine category). Each tier can have its own label set.

**Required fields:**
- `tiers`: List of tier definitions (each a dict with at least a `name` key)
- `source_field`: The data field to annotate

**Example tasks:**
- [MMLU-Pro Tiered Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/preference-learning/mmlu-pro-tiered-eval) -- Tiered topic and subtopic categorization for multi-subject QA

---

## ranking

**Description:** Rank a set of items from best to worst. Produces a full or partial ordering rather than an absolute score.

**Required fields:**
- `labels`: Non-empty list of label strings (the ranking criterion labels)
- Optional `items_key`: Data field holding the list of items to rank
- Optional `allow_ties`: Whether annotators may assign the same rank to multiple items

**Example tasks:**
- [WMT15 Relative Ranking](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/wmt15-relative-ranking) -- Five-way relative ranking of machine translations with ties allowed

---

## semantic_differential

**Description:** Rating on bipolar adjective scales anchored by opposing terms at each end (e.g., Fake -- Natural). The standard instrument format in psychometrics and human--robot interaction research.

**Required fields:**
- `pairs`: List of bipolar adjective pairs, each with a left and right anchor
- Optional `scale_points`: Number of points on each scale (typically 5 or 7)

**Example tasks:**
- [Godspeed Agent Perception](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/godspeed-agent-perception) -- The Godspeed questionnaire's anthropomorphism, animacy, likeability, perceived intelligence, and perceived safety series

---

## conjoint

**Description:** Discrete-choice conjoint analysis: annotators choose between side-by-side profiles whose attributes are independently randomized, so that each attribute's causal effect on choice can be estimated.

**Required fields:**
- `attributes`: List of profile attributes with their possible levels
- Optional `profiles_per_set`: Number of profiles shown per choice task (default 2)
- Optional `show_none_option`: Whether to offer a "neither" choice

**Example tasks:**
- [Conjoint Candidate/Immigrant Profiles](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/conjoint-candidate-profiles) -- Forced-choice profile comparison plus per-profile rating scales

---

## soft_label

**Description:** Distribute a fixed budget of probability mass across labels instead of picking one. Useful when annotators are uncertain, or when the disagreement itself is the signal you want to keep.

**Required fields:**
- `labels`: Non-empty list of label strings
- Optional `total`: Budget to distribute (e.g., 100)
- Optional `min_per_label`, `show_distribution_chart`

**Example tasks:**
- [ChaosNLI Label Distributions](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference/chaosnli-label-distributions) -- Collective NLI label distributions over entailment/neutral/contradiction

---

## rubric_eval

**Description:** Score a response against a list of named rubric criteria, each on its own scale. Used for fine-grained, skill-decomposed evaluation of model outputs.

**Required fields:**
- `criteria`: List of rubric criteria (name plus description/anchors)
- Optional `scale_points`, `scale_labels`, `show_overall`

**Example tasks:**
- [FLASK Skill-based Rubric Evaluation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/flask-skill-rubric-evaluation) -- Twelve fine-grained alignment skills scored on the paper's 1--5 rubrics

---

## error_span

**Description:** Mark spans of text as errors, assigning each a typed error category and a severity. The standard format for translation and generation quality error analysis.

**Required fields:**
- `error_types`: List (or nested hierarchy) of error categories
- Optional `severities`: Severity levels applied per marked span
- Optional `show_score`, `max_score`: Live quality score derived from marked errors

**Example tasks:**
- [MQM MT Error Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/mqm-mt-error-annotation) -- Full MQM error hierarchy with major/minor/neutral severities
- See also [ESA MT Error Spans](https://github.com/davidjurgens/potato-showcase/tree/main/evaluation/esa-mt-error-spans) for the lighter Error Span Annotation protocol

---

## text_edit

**Description:** Inline editing of a source text with diff tracking. Annotators rewrite rather than label, and the interface records what changed.

**Required fields:**
- `source_field`: The data field holding the text to be edited
- Optional `show_diff`, `show_edit_distance`, `allow_reset`

**Example tasks:**
- [JFLEG Fluency Rewriting](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/jfleg-fluency-rewriting) -- Holistic fluency rewrites of learner sentences plus a fluency rating

---

## hierarchical_multiselect

**Description:** Multi-label selection over a nested taxonomy, with expandable parent/child nodes, search, and optional automatic propagation of selections up or down the hierarchy.

**Required fields:**
- `taxonomy`: Nested label hierarchy
- Optional `auto_select_parent`, `auto_select_children`, `expand_depth`, `show_search`, `max_selections`

**Example tasks:**
- [RCV1 Hierarchical Topic Coding](https://github.com/davidjurgens/potato-showcase/tree/main/text/topic-classification/rcv1-hierarchical-topic-coding) -- Reuters topic hierarchy with the corpus's parent-propagation coding policy

---

## multi_document_event

**Description:** Annotate events that recur across multiple documents, filling structured slots per event and linking mentions to shared cross-document event instances.

**Required fields:**
- `slots`: List of event slot definitions (e.g., action, time, location, participants)
- Optional `allow_annotator_create`: Whether annotators may create new event instances

**Example tasks:**
- [ECB+ Cross-Document Event Coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/ecb-plus-cross-document-events) -- Event and entity mention slots linked across documents in the same topic
- See also [MAVEN-ERE](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/maven-ere-event-coreference) for within-document event relation annotation

---

## speech_transcript

**Description:** Per-segment annotation over a time-aligned transcript: tag speech errors or disfluencies on each segment, optionally supplying a correction, with audio playback per segment.

**Required fields:**
- `segments_key`: Data field holding the aligned transcript segments
- `error_types`: Tag set applied per segment
- Optional `audio_key`, `allow_correction`

**Example tasks:**
- [PodcastFillers Disfluency Tagging](https://github.com/davidjurgens/potato-showcase/tree/main/audio/podcastfillers-disfluency-tagging) -- Filler-word and disfluency tagging over aligned podcast transcripts

---

## temporal_grounding

**Description:** Mark gold time intervals in a video that correspond to a natural-language query, with live IoU feedback against predicted moments.

**Required fields:**
- `video_key`: Data field holding the video source
- `events_key`: Data field holding the query/event definitions to ground

**Example tasks:**
- [QVHighlights Moment Grounding and Saliency](https://github.com/davidjurgens/potato-showcase/tree/main/video/temporal-grounding/qvhighlights-moment-saliency) -- Query-based moment boundaries plus saliency rating

---

## table_grid

**Description:** Table structure annotation over an image: define the row and column grid, then assign each cell a role such as header, data, or empty.

**Required fields:**
- `image_key`: Data field holding the table image
- `rows_key` / `cols_key`: Data fields holding the grid dimensions
- `roles`: Per-cell role label set

**Example tasks:**
- [WTW Wired Table Structure Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/image/wtw-table-structure-annotation) -- Wired table structure recovery in natural scenes

---

## process_reward

**Description:** Per-step reward signals over a reasoning or action trace, used to train and evaluate process reward models. Supports full per-step rating and first-error localization modes.

**Required fields:**
- `steps_key`: Data field holding the ordered list of steps
- Optional `mode`: e.g. per-step rating or `first_error`
- Optional `inline_with_trace`: Attach the controls inline to a chain-of-thought trace display

**Example tasks:**
- [ProcessBench Earliest-Error Identification](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/processbench-math-error-steps) -- Locate the earliest erroneous step in a math solution
- [PRM800K Step Verification](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/prm800k-step-verification) -- Per-step positive/neutral/negative process supervision

---

## gui_trajectory

**Description:** Step-by-step review of a computer-use or GUI agent episode: each step shows a screenshot and the action taken, and annotators judge action correctness and click grounding.

**Required fields:**
- `steps_key`: Data field holding the episode's ordered steps
- `screenshot_key` / `action_key`: Per-step screenshot and action fields
- Optional `coord_space`, `verdict_options`

**Example tasks:**
- [AITW Mobile Trajectory Review](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/aitw-mobile-trajectory-review) -- Android device-control episode review in the Android in the Wild style

---

## tool_call_review

**Description:** Per-tool-call correctness review over an agent dialogue: was the right tool selected, were the arguments right, and was the call made in the right order.

**Required fields:**
- `steps_key`: Data field holding the ordered tool calls
- Optional `verdict_options`: Per-call verdict label set

**Example tasks:**
- [API-Bank Tool Call Review](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/apibank-tool-call-review) -- Per-call review of API calls in tool-augmented assistant dialogues

---

## failure_attribution

**Description:** Attribute a multi-agent system's failure to a responsible agent and a decisive step, with a free-text reason. Localizes blame rather than scoring overall quality.

**Required fields:**
- `steps_key`: Data field holding the ordered trace steps
- `agent_key`: Per-step field naming the acting agent

**Example tasks:**
- [Who&When Multi-Agent Failure Attribution](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/whowhen-failure-attribution) -- Responsible agent, decisive step, and reason for the failure
- See also [MAST Failure Taxonomy](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/mast-failure-taxonomy) for taxonomy-based failure mode labeling

---

## agent_scorecard

**Description:** Per-agent and per-team scorecard over a multi-agent run: rate each agent and the team on named dimensions, and check off which run milestones were reached.

**Required fields:**
- `steps_key` / `agent_key`: Trace steps and the per-step agent field used to derive scorecard rows
- `agent_dimensions` / `team_dimensions`: Dimensions rated per agent and per team
- Optional `scale`, `milestones`

**Example tasks:**
- [MultiAgentBench Collaboration Scorecard](https://github.com/davidjurgens/potato-showcase/tree/main/agentic/multiagentbench-collaboration-scorecard) -- Communication and planning ratings plus milestone checklist
