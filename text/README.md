# Text Annotation Tasks

This category contains annotation task designs for text-based NLP research, including sentiment analysis, named entity recognition, information extraction, and more.

> Run these designs in [Potato](https://www.potatoannotator.com), the open-source annotation tool. See the docs for [radio & multiselect schemes](https://www.potatoannotator.com/docs/annotation-types/radio-multiselect) and [span annotation](https://www.potatoannotator.com/docs/annotation-types/span-annotation) to configure text tasks.

## Subcategories

### [Argumentation Stance](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance)

| Design | Description | Reference |
|--------|-------------|-----------|
| [argument-quality](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/argument-quality) | Multi-dimensional argument quality annotation based on the Wachsmuth et al | Wachsmuth et al., EACL 2017 |
| [argument-reasoning](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/argument-reasoning) | Identify implicit warrants in arguments | Habernal et al., NAACL 2018 |
| [claim-perspectives](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/claim-perspectives) | Annotate diverse perspectives on claims with stance and evidence | Chen et al., NAACL 2019 |
| [rumor-stance](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/rumor-stance) | Classify stance toward rumors in social media threads | Zubiaga et al., COLING 2016 |
| [stance-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/argumentation-stance/stance-detection) | Detect the stance of a text toward a given topic | Allaway & McKeown, EMNLP 2020 |

### [Bias Toxicity](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity)

| Design | Description | Reference |
|--------|-------------|-----------|
| [aya-multilingual-redteaming](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity/aya-multilingual-redteaming) | Multilingual safety red-teaming annotation, following the Aya Red-Teaming dataset from 'The Multilingual… | Aakanksha et al., EMNLP 2024 |
| [bbq-bias-benchmark](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity/bbq-bias-benchmark) | Annotate question-answering examples designed to probe social biases | Parrish et al., Findings of ACL 2022 |
| [toxigen-implicit-hate](https://github.com/davidjurgens/potato-showcase/tree/main/text/bias-toxicity/toxigen-implicit-hate) | Detect and classify implicit hate speech in machine-generated text targeting various demographic groups | Hartvigsen et al., ACL 2022 |

### [Code Annotation](https://github.com/davidjurgens/potato-showcase/tree/main/text/code-annotation)

| Design | Description | Reference |
|--------|-------------|-----------|
| [codereviewer-review](https://github.com/davidjurgens/potato-showcase/tree/main/text/code-annotation/codereviewer-review) | Annotation of code review activities based on the CodeReviewer benchmark | Li et al., FSE 2022 |
| [codexglue-defect-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/code-annotation/codexglue-defect-detection) | Binary defect detection and vulnerability localization for C/C++ code based on the CodeXGLUE benchmark | Lu et al., NeurIPS 2021 |
| [humaneval-code-generation](https://github.com/davidjurgens/potato-showcase/tree/main/text/code-annotation/humaneval-code-generation) | HumanEval is OpenAI's set of 164 hand-written Python problems that test whether generated code runs and… | Chen et al., arXiv 2021 |

### [Commonsense Ethics](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics)

| Design | Description | Reference |
|--------|-------------|-----------|
| [atomic-if-then-reasoning](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/atomic-if-then-reasoning) | ATOMIC is the AAAI 2019 knowledge graph of 877k if-then commonsense inferences over 24,313 PersonX/PersonY… | Sap et al., AAAI 2019 |
| [commonsense-inference](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/commonsense-inference) | Annotate commonsense inferences about events, mental states, and social interactions | Hwang et al., AAAI 2021 |
| [commonsense-qa-explanation](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/commonsense-qa-explanation) | Annotate explanations for commonsense QA with positive and negative properties | Aggarwal et al., ACL 2021 |
| [moral-stories](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/moral-stories) | Annotate moral reasoning in situated narratives | Emelin et al., EMNLP 2021 |
| [power-agency-frames](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/power-agency-frames) | Annotate verbs for implied power and agency of participants | Sap et al., EMNLP 2017 |
| [social-chemistry](https://github.com/davidjurgens/potato-showcase/tree/main/text/commonsense-ethics/social-chemistry) | Annotate rules-of-thumb for social and moral norms | Forbes et al., EMNLP 2020 |

### [Computational Social Science](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science)

| Design | Description | Reference |
|--------|-------------|-----------|
| [conjoint-candidate-profiles](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/conjoint-candidate-profiles) | Choice-based conjoint annotation modeled on the immigrant admission experiment in Hainmueller, Hopkins,… | Hainmueller et al., Political Analysis 2014 |
| [human-values-arguments](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/human-values-arguments) | Identification of human values in arguments based on Kiesel et al | Kiesel et al., ACL 2022 |
| [media-frames-analysis](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/media-frames-analysis) | The Media Frames Corpus labels U.S. news articles on immigration, smoking, and same-sex marriage with 15… | Card et al., ACL 2015 |
| [moral-foundations-tweets](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/moral-foundations-tweets) | Classification of moral foundations in social media discourse, based on Moral Foundations Theory (Johnson… | Johnson & Goldwasser, ACL 2018 |
| [offenseval-target-id](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/offenseval-target-id) | Multi-step offensive language annotation combining offensiveness detection, target type classification,… | Zampieri et al., NAACL 2019 (OLID) |
| [politeness-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/politeness-annotation) | Annotate text for politeness level, speech act type, and optional rewrite suggestions based on the… | Madaan et al., ACL 2020 |
| [ruddit-offensiveness-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/ruddit-offensiveness-bws) | Best-worst scaling annotation of the degree of offensiveness of English Reddit comments, based on Ruddit… | Hada et al., ACL 2021 |
| [rumoureval-verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/rumoureval-verification) | Annotate social media posts for rumour stance classification and thread structure analysis based on the… | Gorrell et al., SemEval 2019 |
| [structured-sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/computational-social-science/structured-sentiment) | Fine-grained structured sentiment annotation identifying opinion holders, targets, and polar expressions… | Barnes et al., SemEval 2022 |

### [Coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference)

| Design | Description | Reference |
|--------|-------------|-----------|
| [corefud-multilingual-coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/corefud-multilingual-coreference) | Multilingual coreference resolution across 17 languages using Universal Dependencies-style annotations | Zabokrtsky et al., CRAC@EMNLP 2023 |
| [ecb-plus-cross-document-events](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/ecb-plus-cross-document-events) | Cross-document event coreference annotation based on the ECB+ corpus (Cybulska and Vossen, LREC 2014) | Cybulska & Vossen, LREC 2014 |
| [legalcore-legal-coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/legalcore-legal-coreference) | Event coreference resolution in legal documents including court opinions, contracts, and statutes | Wei et al., Findings of ACL 2025 |
| [maven-ere-event-coreference](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/maven-ere-event-coreference) | Unified event relation extraction covering coreference, temporal, causal, and subevent relations | Wang et al., EMNLP 2022 |
| [ontonotes-coreference-resolution](https://github.com/davidjurgens/potato-showcase/tree/main/text/coreference/ontonotes-coreference-resolution) | Coreference resolution annotation based on the OntoNotes 5.0 corpus | Pradhan et al., CoNLL 2012 |

### [Cross Lingual](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual)

| Design | Description | Reference |
|--------|-------------|-----------|
| [belebele-reading-comprehension](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/belebele-reading-comprehension) | Belebele is a parallel multiple-choice reading comprehension benchmark covering 122 language variants,… | Bandarkar et al., ACL 2024 |
| [flores-mt-quality](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/flores-mt-quality) | Machine translation quality assessment using the FLORES-101 benchmark | Goyal et al., TACL 2022 |
| [indicnlp-multilingual-sa](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/indicnlp-multilingual-sa) | Multilingual sentiment analysis for Indic languages based on the IndicNLP Suite | Kakwani et al., Findings of EMNLP 2020 |
| [masakhanews-topic-classification](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/masakhanews-topic-classification) | Single-label news topic classification for African-language news articles, following the MasakhaNEWS… | Adelani et al., IJCNLP-AACL 2023 |
| [nusax-indonesian-sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/nusax-indonesian-sentiment) | Three-way sentiment annotation for low-resource Indonesian languages, following the NusaX scheme: the… | Winata et al., EACL 2023 |
| [xcopa-causal-reasoning](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/xcopa-causal-reasoning) | Select the most plausible cause or effect for a given premise, testing causal commonsense reasoning across… | Ponti et al., EMNLP 2020 |
| [xnli-cross-lingual-nli](https://github.com/davidjurgens/potato-showcase/tree/main/text/cross-lingual/xnli-cross-lingual-nli) | Natural language inference annotation for cross-lingual evaluation, based on the XNLI benchmark | Conneau et al., EMNLP 2018 |

### [Dialogue](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue)

| Design | Description | Reference |
|--------|-------------|-----------|
| [annomi-counseling-dialogue](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/annomi-counseling-dialogue) | Annotation of motivational interviewing counselling dialogues based on the AnnoMI dataset | Wu et al., ICASSP 2022 |
| [argscichat-scientific-argumentation](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/argscichat-scientific-argumentation) | Annotation of argumentative dialogues about scientific papers based on the ArgSciChat dataset | Ruggeri et al., ACL 2023 |
| [conversation-quality-attributes](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/conversation-quality-attributes) | A generic dialogue-quality annotation template | Template |
| [diasafety-dialogue-safety](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/diasafety-dialogue-safety) | Safety taxonomy annotation for dialogue systems based on the DiaSafety framework | Sun et al., Findings ACL 2022 |
| [dices-diversity-safety](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/dices-diversity-safety) | Diverse annotator perspectives on conversational AI safety based on the DICES dataset | Aroyo et al., NeurIPS 2023 (Datasets and Benchmarks Track) |
| [meditod-medical-dialogue](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/meditod-medical-dialogue) | Medical history-taking dialogue annotation based on the MediTOD dataset | Saley et al., EMNLP 2024 |
| [swbd-damsl-dialogue-acts](https://github.com/davidjurgens/potato-showcase/tree/main/text/dialogue/swbd-damsl-dialogue-acts) | The Switchboard Dialog Act Corpus tags telephone conversations with the SWBD-DAMSL tagset (Jurafsky,… | Jurafsky et al., 1997 |

### [Discourse](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse)

| Design | Description | Reference |
|--------|-------------|-----------|
| [disrpt-discourse-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse/disrpt-discourse-relations) | Discourse segmentation and relation classification | Braud et al., DISRPT@ACL 2023 |
| [flute-figurative-nli](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse/flute-figurative-nli) | Figurative language understanding via NLI. Annotators classify figurative sentences (sarcasm, simile,… | Chakrabarty et al., EMNLP 2022 |
| [pdtb-discourse-relations-tree](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse/pdtb-discourse-relations-tree) | Discourse relation annotation with tree structure, based on the Penn Discourse TreeBank 2.0 | Prasad et al., LREC 2008 |
| [timeline-temporal-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/discourse/timeline-temporal-relations) | Exhaustive temporal relation annotation between events in text | Alsayyahi & Batista-Navarro, EMNLP 2023 |

### [Domain Specific](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific)

| Design | Description | Reference |
|--------|-------------|-----------|
| [bionlp-gene-regulation-events](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/bionlp-gene-regulation-events) | Biomedical event extraction for gene regulation, based on the BioNLP 2011 Shared Task | Kim et al., ACL Workshop 2011 |
| [chemprot-chemical-protein](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/chemprot-chemical-protein) | Identify chemical and gene/protein entities and classify their interaction types in biomedical text, based… | Krallinger et al., BioCreative VI 2017 |
| [clinical-ner-i2b2](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/clinical-ner-i2b2) | Named entity recognition and assertion classification for clinical notes, based on the i2b2/VA 2010 challenge | Uzuner et al., JAMIA 2011 |
| [lexglue-legal-understanding](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/lexglue-legal-understanding) | LexGLUE is a benchmark of 7 legal NLP datasets in English covering EU and US law | Chalkidis et al., ACL 2022 |
| [maud-legal-merger-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/maud-legal-merger-qa) | Legal document understanding for merger agreements | Wang et al., EMNLP 2023 |
| [mednli-clinical-inference](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/mednli-clinical-inference) | Natural language inference for clinical text | Romanov & Shivade, EMNLP 2018 |
| [multiconerii-complex-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/multiconerii-complex-ner) | Complex and ambiguous named entity recognition across 12 languages | Fetahu et al., SemEval@ACL 2023 |
| [n2c2-sdoh-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/n2c2-sdoh-extraction) | Extract social determinants of health (SDOH) from clinical notes | Lybarger et al., JAMIA 2023 |
| [radqa-radiology-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/domain-specific/radqa-radiology-qa) | RadQA is an extractive QA dataset of physician questions answered by spans in MIMIC-III radiology reports,… | Soni et al., LREC 2022 |

### [Education](https://github.com/davidjurgens/potato-showcase/tree/main/text/education)

| Design | Description | Reference |
|--------|-------------|-----------|
| [automated-essay-scoring](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/automated-essay-scoring) | Holistic and analytic scoring of student essays using a deep-neural approach to automated essay scoring… | Uto, Behaviormetrika 2021 |
| [jfleg-fluency-rewriting](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/jfleg-fluency-rewriting) | Holistic fluency rewriting of learner-English sentences based on the JFLEG corpus (Napoles, Sakaguchi, and… | Napoles et al., EACL 2017 |
| [mathdial-tutoring-dialogue](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/mathdial-tutoring-dialogue) | MathDial is a dataset of 2,861 one-to-one math tutoring dialogues grounded in GSM8K word problems,… | Macina et al., Findings of EMNLP 2023 |
| [student-essay-discourse](https://github.com/davidjurgens/potato-showcase/tree/main/text/education/student-essay-discourse) | Discourse element annotation of student essays based on Song et al | Song et al., EMNLP 2020 |

### [Emotion Sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment)

| Design | Description | Reference |
|--------|-------------|-----------|
| [emotion-cause-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/emotion-cause-extraction) | Extract emotion causes from conversational text based on RECCON. Identify which utterances and specific… | Poria et al., Cognitive Computation 2021 |
| [empathetic-dialogues](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/empathetic-dialogues) | Annotate emotional situations and empathetic responses in conversations | Rashkin et al., ACL 2019 |
| [goemotions](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/goemotions) | Multi-label emotion classification with 27 emotion categories plus neutral, based on the Google Research… | Demszky et al., ACL 2020 |
| [news-emotion-roles](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/news-emotion-roles) | Annotate emotions in news headlines with semantic roles | Bostan et al., LREC 2020 |
| [nrc-affect-intensity-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/nrc-affect-intensity-bws) | Rate individual English words for the INTENSITY of a basic emotion (anger, fear, joy, or sadness) using… | Mohammad, LREC 2018 |
| [nrc-emolex-word-emotion](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/nrc-emolex-word-emotion) | Crowdsourced annotation of a word's associations with eight basic emotions (anger, anticipation, disgust,… | Mohammad & Turney, Computational Intelligence 2013 |
| [nrc-vad-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/nrc-vad-bws) | Rate individual English words on three affective dimensions - valence (pleasant-unpleasant), arousal… | Mohammad, ACL 2018 |
| [rusentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/rusentiment) | 5-class sentiment annotation for social media posts based on RuSentiment | Rogers et al., COLING 2018 |
| [scl-sentiment-composition-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/scl-sentiment-composition-bws) | Rate the sentiment of short phrases using Best-Worst Scaling to study how sentiment composes | Kiritchenko & Mohammad, NAACL 2016 |
| [semeval-emotion-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/semeval-emotion-detection) | Multi-label emotion classification with intensity ratings based on SemEval-2018 Task 1 | Mohammad et al., SemEval 2018 |
| [semeval-sentiment-multirate](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/semeval-sentiment-multirate) | Multi-dimensional sentiment rating of tweets based on SemEval-2017 Task 4 | Rosenthal et al., SemEval 2017 |
| [tweet-emotion-intensity-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/tweet-emotion-intensity-bws) | Rate the intensity (degree) of emotion in tweets using Best-Worst Scaling | Mohammad & Bravo-Marquez, WASSA 2017 |
| [warmth-competence-sentences](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/warmth-competence-sentences) | Sentence-level annotation of social perception along the two fundamental dimensions of social cognition:… | Ayesh et al., 2026 |
| [word-colour-associations](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/word-colour-associations) | Annotate the colour that a word evokes | Mohammad, ACL 2011 (CMCL Workshop) |
| [words-of-warmth-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/words-of-warmth-bws) | Rate individual English words on four social-perception dimensions - warmth, competence, sociability, and… | Mohammad, ACL 2025 |
| [worrywords-anxiety-bws](https://github.com/davidjurgens/potato-showcase/tree/main/text/emotion-sentiment/worrywords-anxiety-bws) | Rate individual English words on the calmness-anxiety dimension using Best-Worst Scaling | Mohammad, EMNLP 2024 |

### [Entity Linking](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking)

| Design | Description | Reference |
|--------|-------------|-----------|
| [aida-conll-entity-disambiguation](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking/aida-conll-entity-disambiguation) | Named entity disambiguation and linking to Wikidata knowledge base based on the AIDA-CoNLL dataset | Hoffart et al., EMNLP 2011 |
| [dwie-document-entity-linking](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking/dwie-document-entity-linking) | Document-level entity mention annotation with knowledge-base linking based on DWIE (Zaporojets, Deleu,… | Zaporojets et al., IPM 2021 |
| [entity-linking-tweets](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking/entity-linking-tweets) | Named entity recognition and entity linking in tweets: annotators identify entity mentions in short, noisy… | N/A (generic showcase design) |
| [medmentions-biomedical](https://github.com/davidjurgens/potato-showcase/tree/main/text/entity-linking/medmentions-biomedical) | Entity mention detection and UMLS concept linking for biomedical text based on MedMentions | Mohan & Li, AKBC 2019 |

### [Explainability](https://github.com/davidjurgens/potato-showcase/tree/main/text/explainability)

| Design | Description | Reference |
|--------|-------------|-----------|
| [nli-explanation](https://github.com/davidjurgens/potato-showcase/tree/main/text/explainability/nli-explanation) | Natural language inference with human explanations | Camburu et al., NeurIPS 2018 |
| [rationale-annotation](https://github.com/davidjurgens/potato-showcase/tree/main/text/explainability/rationale-annotation) | Annotate rationales (evidence spans) that justify classification decisions | DeYoung et al., ACL 2020 |

### [Fact Verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification)

| Design | Description | Reference |
|--------|-------------|-----------|
| [check-covid-fact-checking](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/check-covid-fact-checking) | Fact-checking COVID-19 news claims | Wang et al., Findings ACL 2023 |
| [citation-needed-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/citation-needed-detection) | Sentence-level Citation Needed Detection (CND): given a claim from a Wikipedia article (with surrounding… | Quaremba et al., 2026 |
| [clickbait-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/clickbait-detection) | Classify headlines and social media posts as clickbait or non-clickbait based on the Webis Clickbait Corpus | Potthast et al., ECIR 2016 |
| [deceptive-review-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/deceptive-review-detection) | Distinguish between truthful and deceptive (fake) reviews | Ott et al., ACL 2011 |
| [factscore-atomic-factuality](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/factscore-atomic-factuality) | FActScore breaks LLM-generated text into atomic facts and scores the percentage supported by Wikipedia,… | Min et al., EMNLP 2023 |
| [fava-hallucination-spans](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/fava-hallucination-spans) | Fine-grained hallucination span annotation | Mishra et al., COLM 2024 |
| [propaganda-techniques](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/propaganda-techniques) | Span-level annotation of propaganda techniques in news articles based on SemEval 2020 Task 11 | Da San Martino et al., EMNLP 2019 |
| [scientific-claim-verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/scientific-claim-verification) | SciFact pairs 1,409 expert-written scientific claims with 5,183 research abstracts labeled SUPPORTS,… | Wadden et al., EMNLP 2020 |
| [shroom-hallucination-detection](https://github.com/davidjurgens/potato-showcase/tree/main/text/fact-verification/shroom-hallucination-detection) | Binary hallucination detection in NLG outputs | Mickus et al., SemEval@NAACL 2024 |

### [Financial](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial)

| Design | Description | Reference |
|--------|-------------|-----------|
| [financial-phrasebank-sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial/financial-phrasebank-sentiment) | Financial PhraseBank labels English financial news sentences as positive, negative, or neutral by their… | Malo et al., JASIST 2014 |
| [finbert-headline-sentiment](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial/finbert-headline-sentiment) | Classify sentiment of financial news headlines as positive, negative, or neutral, based on the FinBERT… | Araci, arXiv 2019 |
| [flare-financial-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/financial/flare-financial-ner) | Named entity recognition and document classification for financial texts, based on the FLARE benchmark… | Xie et al., PIXIU (NeurIPS 2023 Datasets & Benchmarks) |

### [Hate Speech Moderation](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation)

| Design | Description | Reference |
|--------|-------------|-----------|
| [afrihate-abusive-language](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/afrihate-abusive-language) | Multilingual content-moderation annotation following the AfriHate scheme, a collection of hate speech and… | Muhammad et al., NAACL 2025 |
| [dynamic-hate-speech](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/dynamic-hate-speech) | Hate speech classification with fine-grained type labels based on the Dynamically Generated Hate Speech… | Vidgen et al., ACL 2021 |
| [hatexplain](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/hatexplain) | Multi-task hate speech annotation with classification (hate/offensive/normal), target community… | Mathew et al., AAAI 2021 |
| [implicit-hate-speech](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/implicit-hate-speech) | Detect and categorize implicit hate speech using a six-category taxonomy | ElSherief et al., EMNLP 2021 |
| [social-bias-frames](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/social-bias-frames) | Annotate social media posts for bias using structured frames | Sap et al., ACL 2020 |
| [toxic-spans](https://github.com/davidjurgens/potato-showcase/tree/main/text/hate-speech-moderation/toxic-spans) | Character-level toxic span annotation based on SemEval-2021 Task 5 | Pavlopoulos et al., SemEval 2021 |

### [Information Extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction)

| Design | Description | Reference |
|--------|-------------|-----------|
| [chemical-disease-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/chemical-disease-relations) | Extract chemical-disease relations from biomedical literature | Li et al., Database 2016 |
| [coreference-resolution](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/coreference-resolution) | Link pronouns and noun phrases to the entities they refer to in text | Pradhan et al., CoNLL 2012 |
| [dialogue-relation-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/dialogue-relation-extraction) | Extract relations between entities in dialogue | Yu et al., ACL 2020 |
| [event-argument-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/event-argument-extraction) | Document-level event argument extraction based on MAVEN-Arg | Wang et al., ACL 2024 |
| [kgbert-knowledge-graph](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/kgbert-knowledge-graph) | Validate knowledge graph triples for correctness and annotate relation types based on the KG-BERT framework | Yao et al., arXiv 2019 |
| [massive-intent-slot-filling](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/massive-intent-slot-filling) | Spoken-language-understanding annotation for virtual assistants, following the MASSIVE scheme: 1M parallel… | FitzGerald et al., ACL 2023 |
| [sdoh-extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/sdoh-extraction) | Event-based extraction of social determinants of health from clinical notes based on the n2c2 2022 Track 2… | Lybarger et al., JAMIA 2023 (n2c2/UW SDOH shared task) |
| [temporal-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-extraction/temporal-relations) | Annotate temporal relations between events and time expressions following TimeML guidelines | UzZaman et al., SemEval 2013 |

### [Information Retrieval](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-retrieval)

| Design | Description | Reference |
|--------|-------------|-----------|
| [msmarco-passage-ranking](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-retrieval/msmarco-passage-ranking) | MS MARCO is a large-scale information retrieval benchmark of 8.8M passages and real Bing queries with… | Nguyen et al., NIPS 2016 Workshop (CoCo@NIPS) |
| [trec-dl-passage-ranking](https://github.com/davidjurgens/potato-showcase/tree/main/text/information-retrieval/trec-dl-passage-ranking) | Annotate query-passage relevance for information retrieval evaluation based on the TREC 2019 Deep Learning… | Craswell et al., TREC/SIGIR 2019 |

### [Named Entity Recognition](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition)

| Design | Description | Reference |
|--------|-------------|-----------|
| [adverse-drug-events](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/adverse-drug-events) | Named entity recognition for adverse drug events from patient-reported experiences, based on the CADEC corpus | Karimi et al., J Biomed Inform 2015 |
| [biomedical-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/biomedical-ner) | Named entity recognition for biomedical text based on the JNLPBA shared task | Collier et al., JNLPBA/BioNLP 2004 |
| [complex-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/complex-ner) | Recognize complex and emerging named entities | Malmasi et al., SemEval 2022 |
| [conll2003-ner-triage](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/conll2003-ner-triage) | Named entity recognition with a triage pre-annotation step, based on the CoNLL-2003 Shared Task (Tjong Kim… | Tjong Kim Sang & De Meulder, CoNLL 2003 |
| [masakhaner-african-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/masakhaner-african-ner) | Span-level named entity recognition for African-language text, following the MasakhaNER 2.0 annotation… | Adelani et al., EMNLP 2022 |
| [wikiann-multilingual-ner](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/wikiann-multilingual-ner) | WikiANN / PAN-X is the multilingual NER dataset covering 282 languages, generated automatically from… | Pan et al., ACL 2017; Rahimi et al., ACL 2019 |
| [wnut2017-emerging-entities](https://github.com/davidjurgens/potato-showcase/tree/main/text/named-entity-recognition/wnut2017-emerging-entities) | WNUT-2017 is a named entity recognition benchmark for novel and rare entities in noisy social media text,… | Derczynski et al., W-NUT@EMNLP 2017 |

### [Natural Language Inference](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference)

| Design | Description | Reference |
|--------|-------------|-----------|
| [chaosnli-label-distributions](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference/chaosnli-label-distributions) | Distributional annotation of Natural Language Inference judgments, based on ChaosNLI (Nie, Zhou, and… | Nie et al., EMNLP 2020 |
| [multinli-genre-nli](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference/multinli-genre-nli) | Natural language inference across multiple genres of text, based on the Multi-Genre NLI corpus | Williams et al., NAACL 2018 |
| [snli-textual-entailment](https://github.com/davidjurgens/potato-showcase/tree/main/text/natural-language-inference/snli-textual-entailment) | SNLI is a corpus of 570k human-written English sentence pairs labeled entailment, contradiction, or neutral | Bowman et al., EMNLP 2015 |

### [Parsing](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing)

| Design | Description | Reference |
|--------|-------------|-----------|
| [masakhapos-african-pos](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing/masakhapos-african-pos) | Token-level part-of-speech tagging for typologically diverse African languages, following the MasakhaPOS… | Dione et al., ACL 2023 |
| [sigmorphon-interlinear-glossing](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing/sigmorphon-interlinear-glossing) | Morpheme-level interlinear glossing, the annotation design behind the SIGMORPHON 2023 Shared Task on… | Ginn et al., SIGMORPHON 2023 |
| [ud-dependency-parsing](https://github.com/davidjurgens/potato-showcase/tree/main/text/parsing/ud-dependency-parsing) | Dependency parsing and POS tagging annotation based on Universal Dependencies v2 | Nivre et al., LREC 2020 |

### [Political Media](https://github.com/davidjurgens/potato-showcase/tree/main/text/political-media)

| Design | Description | Reference |
|--------|-------------|-----------|
| [political-discourse](https://github.com/davidjurgens/potato-showcase/tree/main/text/political-media/political-discourse) | Multi-task annotation of political speeches covering sentiment, polarization, populism, topic… | Sermpezis et al., arXiv 2025 |

### [Question Answering](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering)

| Design | Description | Reference |
|--------|-------------|-----------|
| [natural-questions-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering/natural-questions-qa) | Open-domain question answering over Wikipedia passages, based on Google's Natural Questions dataset | Kwiatkowski et al., TACL 2019 |
| [patient-forum-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering/patient-forum-qa) | Question answering and response classification for patient health forum posts: annotators write or assess… | N/A (generic showcase design) |
| [triviaqa-reading-comprehension](https://github.com/davidjurgens/potato-showcase/tree/main/text/question-answering/triviaqa-reading-comprehension) | Trivia question answering with evidence passages, based on the TriviaQA dataset | Joshi et al., ACL 2017 |

### [Reading Comprehension](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension)

| Design | Description | Reference |
|--------|-------------|-----------|
| [fquad-french-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension/fquad-french-qa) | FQuAD is the French extractive QA dataset from Illuin Technology, built on the SQuAD 1.1 protocol | d'Hoffschmidt et al., arXiv 2020 |
| [germanquad-german-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension/germanquad-german-qa) | GermanQuAD is deepset's German machine reading comprehension dataset (MRQA 2021) | Möller et al., MRQA 2021 |
| [korquad-korean-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension/korquad-korean-qa) | KorQuAD 1.0 is the Korean machine reading comprehension dataset built on the SQuAD 1.0 protocol:… | Lim et al., arXiv 2019 |
| [squad-extractive-qa](https://github.com/davidjurgens/potato-showcase/tree/main/text/reading-comprehension/squad-extractive-qa) | Extractive question answering over Wikipedia passages, based on the Stanford Question Answering Dataset | Rajpurkar et al., EMNLP 2016 |

### [Relation Extraction](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction)

| Design | Description | Reference |
|--------|-------------|-----------|
| [crossre-cross-domain-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/crossre-cross-domain-relations) | Cross-domain relation extraction across 6 domains (news, politics, science, music, literature, AI) | Bassignana & Plank, Findings EMNLP 2022 |
| [multitacred-multilingual-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/multitacred-multilingual-relations) | MultiTACRED machine-translates the TACRED relation extraction dataset into 12 languages, keeping 41 TAC… | Hennig et al., ACL 2023 |
| [radgraph-radiology-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/radgraph-radiology-relations) | Entity and relation extraction from radiology reports | Delbrouck et al., Findings ACL 2024 |
| [redfm-multilingual-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/redfm-multilingual-relations) | Multilingual relation extraction across 7 human-revised languages (Arabic, Chinese, English, French,… | Huguet Cabot et al., ACL 2023 |
| [scier-scientific-entity-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/relation-extraction/scier-scientific-entity-relations) | SciER labels Dataset, Method, and Task entities and 9 relation types across 106 full-text scientific… | Zhang et al., EMNLP 2024 |

### [Semantic Similarity](https://github.com/davidjurgens/potato-showcase/tree/main/text/semantic-similarity)

| Design | Description | Reference |
|--------|-------------|-----------|
| [stsb-sentence-similarity](https://github.com/davidjurgens/potato-showcase/tree/main/text/semantic-similarity/stsb-sentence-similarity) | The STS Benchmark scores 8,628 English sentence pairs for semantic similarity on a 0-5 scale, drawn from… | Cer et al., SemEval 2017 |

### [Tabular](https://github.com/davidjurgens/potato-showcase/tree/main/text/tabular)

| Design | Description | Reference |
|--------|-------------|-----------|
| [feverous-structured-factcheck](https://github.com/davidjurgens/potato-showcase/tree/main/text/tabular/feverous-structured-factcheck) | FEVEROUS is a fact-checking dataset of 87,026 Wikipedia claims with evidence drawn from both sentences and… | Aly et al., NeurIPS 2021 |
| [tabfact-table-verification](https://github.com/davidjurgens/potato-showcase/tree/main/text/tabular/tabfact-table-verification) | Verify textual claims against structured tabular data from Wikipedia | Chen et al., ICLR 2020 |

### [Topic Classification](https://github.com/davidjurgens/potato-showcase/tree/main/text/topic-classification)

| Design | Description | Reference |
|--------|-------------|-----------|
| [rcv1-hierarchical-topic-coding](https://github.com/davidjurgens/potato-showcase/tree/main/text/topic-classification/rcv1-hierarchical-topic-coding) | Hierarchical multi-label Topic coding of newswire stories, based on Reuters Corpus Volume 1 (Lewis, Yang,… | Lewis et al., JMLR 2004 |

### [Word Sense](https://github.com/davidjurgens/potato-showcase/tree/main/text/word-sense)

| Design | Description | Reference |
|--------|-------------|-----------|
| [senserel-meaning-relations](https://github.com/davidjurgens/potato-showcase/tree/main/text/word-sense/senserel-meaning-relations) | Sense-level annotation of semantic relations between pairs of word senses | Cassotti et al., 2026 |
| [wsd-semeval2007](https://github.com/davidjurgens/potato-showcase/tree/main/text/word-sense/wsd-semeval2007) | Word sense disambiguation task based on the SemEval-2007 English lexical sample | Pradhan et al., SemEval 2007 |

## Quick Start

```bash
# Navigate to a specific task
cd text/emotion-sentiment/goemotions

# Run with Potato
potato start config.yaml
```

## Task Count

**Total: 144 text annotation tasks** across 30 subcategories
