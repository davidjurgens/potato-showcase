# Candidate Datasets to Build Next

Build-next backlog for the **traffic** lens (see `DATASET_DEMAND_PLAYBOOK.md`).
This file is the brainstorm + rationale; nothing here is built yet. Each entry
is a *named proper-noun* people search for, with a real annotation protocol Potato
can reproduce.

> **Honesty note on demand:** our Google Search Console only shows queries we
> already rank for, so it cannot measure demand for datasets we have no page for.
> The "demand" judgments below are reasoned from how widely each dataset is cited,
> taught, and ported — not measured. Validate by seeding a page and re-pulling
> `Queries.csv`/`Pages.csv` next cycle, or spot-check with a keyword tool.

---

## The strongest angle: datasets that get re-annotated in other languages

A dataset whose **annotation protocol is re-run in new languages** is a compounding
traffic magnet. Every localization is a fresh searched proper-noun ("KorQuAD",
"GermanQuAD", "MasakhaNER"), and the searcher is *exactly* the person who needs an
annotation tool — they are about to reproduce the labeling in their language. That
is Potato's pitch. These tasks also tend to be span/linking/structured (high
reproduction value), not single-radio.

Lead with this family. The named variants below are the page titles to create.

### 1. SQuAD family — extractive QA (span selection)  ★ top priority
The SQuAD span-QA protocol is the most-ported annotation task in NLP. Each port is
a high-search proper-noun in its own language community:

- **KorQuAD** (Korean) — very high in-country search
- **FQuAD** (French), **GermanQuAD** (German), **SberQuAD** (Russian)
- **ARCD** / Arabic-SQuAD, **SQuAD-it** (Italian), **JaQuAD** (Japanese)
- **CMRC 2018** (Chinese), **PQuAD** (Persian), **TQuAD** (Turkish)
- Multilingual umbrellas: **XQuAD**, **MLQA**, **TyDiQA**, **MKQA**

Potato fit: `span` over a passage to mark the answer + a question field; optional
"unanswerable" radio (SQuAD 2.0). One reusable config; swap the language data.
We have `squad-extractive-qa` (English) only. **Build:** KorQuAD, GermanQuAD, FQuAD
as named pages + a guide "annotate SQuAD-style QA in your language" that links them.

### 2. Multilingual NER — WikiAnn / Masakha / Universal NER (span)  ★ top priority
NER is the other heavily-ported span task. Named magnets:

- **WikiANN / PAN-X** — NER in 282 languages; the multilingual NER reference
- **MasakhaNER / MasakhaNER 2.0** — 20 African languages; strong, growing "extend
  to your language" brand (Masakhane community)
- **Universal NER (UNER)** — 2024 cross-lingual NER aligned to UD
- Named European: **GermEval** (German), **CoNLL-2002** (Spanish/Dutch)

Potato fit: `span` with PER/ORG/LOC/MISC (or the Masakha tagset). We have
`conll2003-ner-triage`, `wnut2017`, `multiconerii` (MultiCoNER, 12 langs),
`complex-ner`. **Build:** WikiANN/PAN-X and MasakhaNER — distinct named entities,
not covered.

### 3. Universal Dependencies — the archetypal "annotate your language" project  ★
UD is literally a global effort to annotate treebanks in 100+ languages to one
scheme. People search "Universal Dependencies <language>", "<language> treebank",
"UD POS tags". The reproduction story writes itself.

Potato fit: `span_linking` (head→dependent arcs) + UPOS `radio`/`multiselect`.
We have a generic `ud-dependency-parsing` — **elevate** it to a flagship with the
per-language framing, or add Universal POS as a sibling.

### 4. Localized GLUE/SuperGLUE suites — "extend the benchmark to my language"
The GLUE pattern is copied wholesale per language; each suite is a searched name:

- **KLUE** (Korean), **CLUE** (Chinese), **IndoNLU / IndoLEM** (Indonesian)
- **JGLUE** (Japanese), **FLUE** (French), **Russian SuperGLUE**
- **IndicGLUE / IndicXTREME** (Indian languages), **GLUECoS** (Hinglish code-switching)

Potato fit: a suite is several tasks; build an **overview page + one representative
reproducible task** (e.g. KLUE-NLI as `radio`, KLUE-NER as `span`). We have none of
the localized suites. Good brand fit ("Potato to build your language's GLUE").

### 5. Native NLI (XNLI extended)
We have SNLI/MNLI/XNLI. Named native NLIs still searched: **OCNLI** (Chinese),
**IndoNLI**, **FarsTail** (Persian), **JNLI** (Japanese, part of JGLUE), **ANLI**
(adversarial). Lower priority — core NLI is covered; add only the highest-search
native ones. Potato fit: `radio` (entail/neutral/contradiction).

---

## Famous English benchmarks we lack (high general search, weaker i18n angle)

These pull search on the strength of the name alone; some have multilingual ports
via the **Okapi / m-*** multilingual-eval efforts (a secondary i18n hook).

| Dataset | Task / Potato type | Note |
|---|---|---|
| **SST / Stanford Sentiment Treebank** | sentiment, `radio`/`likert` | Canonical; we have generic sentiment but not the named SST. Ported widely. |
| **Jigsaw Toxic Comments** | toxicity, `multiselect` | Kaggle dataset, very high search; multilingual Jigsaw exists. |
| **HellaSwag** | commonsense MCQ, `radio` | High search; multilingual via Okapi/m-HellaSwag. |
| **WinoGrande** | coref/commonsense MCQ, `radio` | High search; WinoX multilingual coref. |
| **PIQA** | physical commonsense MCQ, `radio` | High search. |
| **CommonsenseQA** | MCQ, `radio` | We have `commonsense-qa-explanation`; CSQA proper + **X-CSQA** multilingual. |
| **ARC / OpenBookQA** | science MCQ, `radio` | High search; ARC very cited. |
| **BoolQ** | yes/no QA, `radio` | SuperGLUE; multilingual BoolQ ports. |
| **DROP** | discrete-reasoning QA, `span`/`text` | Cited; rich annotation. |
| **RACE** | reading-comprehension MCQ, `radio` | Heavily used in education NLP. |
| **TruthfulQA** | truthfulness eval, `radio`/`likert` | Very high current search. |

These are easy `radio` reproductions (lower Potato differentiation) — prioritize
under the span/linking i18n tasks above, but several (SST, Jigsaw, HellaSwag,
TruthfulQA) are high enough search to be worth named pages.

---

## Multilingual hate speech / toxicity (localization-heavy)

- **HASOC** (Hindi/German/Marathi/…), **OffensEval / OLID** ports (Arabic, Danish,
  Greek, Turkish), **HatEval** (es/en — also a *buried* re-title of our
  `semeval/2019/task05-hateval`), **NaijaSenti / AfriHate**, **MLMA**.
- Potato fit: `radio`/`multiselect` with the local taxonomy. We have many English
  hate-speech designs; the win is the **named multilingual** ones.

---

## Other multilingual umbrellas (named, searched, mostly structured)

- **XL-Sum**, **WikiLingua** — multilingual summarization (`text`/`span`).
- **MASSIVE**, **MultiATIS++**, **xSID** — multilingual intent + slot filling
  (`radio` + `span`); strong "build your language's voice-assistant data" story.
- **Taxi1500**, **SIB-200** — massively-multilingual topic classification.
- **Universal Proposition Bank**, **multilingual FrameNet** — SRL (`span_linking`).
- **Open Multilingual WordNet** — word sense; we only have `wsd-semeval2007`.

---

## Suggested first batch (when we build)

Ordered by demand × Potato-differentiation × i18n-compounding:

1. **KorQuAD + GermanQuAD + FQuAD** (SQuAD span QA) + the "SQuAD in your language" guide.
2. **MasakhaNER** and **WikiANN/PAN-X** (multilingual NER span).
3. **Universal Dependencies** flagship elevation (`span_linking`).
4. **KLUE** overview + KLUE-NER/NLI representative tasks.
5. Two high-search English names as quick `radio` wins: **SST** and **TruthfulQA**.

Reproduction bar is non-negotiable per the playbook §3–5: source the real
annotation guidelines, verify every fact/URL (HTTP 200, browser UA), and pass
`python -m potato.validate_cli --strict`. Do **not** invent dataset URLs — see
`LINK_CLEANUP_TODO.md` for the mess that creates.
