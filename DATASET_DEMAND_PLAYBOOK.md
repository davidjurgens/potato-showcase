# Demand-Driven Dataset Page Playbook

How to pick, build, and ship showcase pages that turn existing search demand into
traffic for Potato. This is the **traffic** lens on curation; the companion
`.paper-search-strategy.md` is the **coverage** lens (filling annotation-type and
modality gaps). Use this one when the goal is "we already get impressions for a
dataset name — capture the click and show Potato can reproduce it."

Worked example built with this playbook: `text/commonsense-ethics/atomic-if-then-reasoning/` (ATOMIC).

---

## 1. Why this works

Search Console shows the pattern clearly. We pulled every non-brand query with
15+ impressions and aggregated by dataset entity:

| Entity | Impressions | Have a page? |
|---|---|---|
| FineGym | 6,265 | yes (thin → enriched) |
| SoccerNet | 1,233 | yes (thin → enriched) |
| GPQA | 883 | yes |
| DeepFashion | 521 | yes |
| **ATOMIC (PersonX/PersonY)** | **425** | **no → built** |
| SemEval-2019 toponym | 294 | yes |
| SciFact | 253 | partial (not branded "SciFact") |
| MagnaTagATune | 77 | no |

Then we checked page-level impressions (`Pages.csv`) for all 379 existing
designs. The split is stark:

- **286 designs get impressions; 97 get exactly zero.**
- The zero bucket is almost entirely **generic-task pages with no proper noun**:
  all 18 `templates/*` (`sentiment-analysis`, `named-entity-recognition`,
  `fact-verification`), plus generic pages like `automated-essay-scoring`,
  `coreference-resolution`, `machine-translation-eval`, `question-answering`,
  `audio-transcription`.
- The winners are all **named entities** searched by proper noun: finegym,
  soccernet, gpqa, deepfashion, factscore, bdd100k, celeba, doreco, belebele.
- SemEval tasks split on the same line: the ones surfacing a **memorable dataset
  name** win (HaHackathon, ValueEval, code-mixed, toponym); 36 identified only by
  a task number get zero — several of those (e.g. `task05-hateval` → **HatEval**)
  are named datasets buried under a numeric slug.

**The rule:** a page earns impressions iff it surfaces a recognizable dataset
proper-noun with real external search demand. Build named datasets with public
annotation guidelines; never build more generic templates.

---

## 2. Targeting pipeline

### Step 1 — Mine the search log

Export `Queries.csv` and `Pages.csv` from Google Search Console (Search results →
Export). Then:

```python
# Cluster queries by dataset entity, rank by impressions.
import csv, re
rows = [r for r in csv.reader(open('Queries.csv'))][1:]
# group by hand-built keyword → entity map; sum impressions; sort desc.
# Flag any cluster with >150 impressions and 0 clicks as a candidate.
```

```python
# Page-level contrast: which existing designs get zero impressions?
# Aggregate Pages.csv by /showcase/<slug>, diff against the set of metadata.json
# slugs on disk. Slugs absent from Pages.csv have zero impressions.
```

### Step 2 — Sort candidates into three buckets

1. **Gap** — high-impression entity with **no page** (e.g. ATOMIC, MagnaTagATune).
   Highest value: net-new page, net-new traffic.
2. **Buried** — a named page that exists under a generic or numeric title
   (e.g. `scientific-claim-verification` should also rank as **SciFact**;
   `task05-hateval` should surface **HatEval**). Cheapest win: re-title, no new
   files.
3. **Thin** — a named page that ranks but is underbuilt. Enrich the metadata
   (overview, datasetStats, paper/dataset links) the way FineGym/SoccerNet were.

### Step 3 — Filter by feasibility

A candidate is buildable only if its **annotation protocol is public and
faithfully reproducible** in Potato. Require:

- A paper or project page that documents the label set / question wording.
- A task that maps to Potato annotation types (`radio`, `multiselect`, `text`,
  `likert`, `span`, `span_linking`, `pairwise`, `bbox`, `polygon`,
  `video_annotation`).
- A live dataset/paper URL (you will verify it in Step 5).

Prioritize: `impressions × feasibility`. Skip datasets whose annotation is
trivial (no reproduction value) or whose guidelines are not public.

---

## 3. Build — the faithful-reproduction bar

This is the part that protects the brand. The site's whole pitch here is "Potato
reproduces this dataset accurately," so a wrong author or dead link is worse than
no page. Each design is exactly three files (see `CLAUDE.md`):
`metadata.json`, `config.yaml`, `sample-data.json`.

**Source the real annotation guidelines, not the abstract.** Pull the label set,
the exact question wording, and the instructions from the paper's annotation
section, the released annotation interface, or the dataset repo. Copy them; do not
paraphrase. For ATOMIC, that meant the nine dimensions
(xIntent, xReact, oReact, xNeed, xWant, xEffect, oWant, oEffect, xAttr) in their
three families, each elicited as a free-text completion exactly as the MTurk HIT
posed it.

**Reproduce the exact taxonomy.** SoccerNet's 17 v2 classes, SciFact's
SUPPORTS/REFUTES/NEI, ATOMIC's nine relations — counts and names verbatim.

**Write the `config.yaml` header as documentation.** Lead with the citation, the
dataset URL, the relation/label glossary, and explicit reproduction notes (where
the config simplifies the original and how to recover full fidelity — e.g. ATOMIC
pools annotators via `min_annotators_per_instance` to recover its
many-answers-per-event set).

---

## 4. Verify every external fact

The four reference errors we fixed (SciER authors, FineSports/LongEval dead repo
URLs, T2I-CompBench affiliation) all came from writing metadata from memory. Never
do that. Before writing `metadata.json`:

```bash
# Confirm every URL resolves (paper + dataset).
for u in "$PAPER_URL" "$DATASET_URL"; do
  echo "$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 20 "$u")  $u"
done
```

- Authors, affiliation, venue, year → confirm against ACL Anthology / arXiv /
  the proceedings page (WebFetch the abstract page).
- Label counts, dataset size → confirm against the paper body (ar5iv renders
  arXiv math/tables well: `https://ar5iv.labs.arxiv.org/abs/<id>`).
- `datasetUrl` → must be the live canonical repo/project page, HTTP 200.
- `citation` → valid BibTeX with the verified author list.

If a fact cannot be verified, leave it out rather than guess.

---

## 5. Validate the config

```bash
cd ~/Documents/Projects/potato
python3 -m potato.validate_cli --strict <design>/config.yaml   # must be clean
python3 -c "import json; json.load(open('<design>/metadata.json')); \
            json.load(open('<design>/sample-data.json')); print('JSON OK')"
```

Notes learned from the ATOMIC build:
- `--strict` rejects legacy keys much of the corpus still uses
  (`allow_all_users`, `instances_per_annotator`, `annotation_per_instance`).
  Prefer the current keys: `per_annotator_quota: {default: N}` (a **mapping**, not
  an int) and `min_annotators_per_instance: N`.
- Free-text fields are `annotation_type: text` with `textarea: true|false`.
- `sample-data.json`: 8–12 realistic items, each with an `id` and the field named
  by `item_properties.text_key`.

The website renders `config.yaml` and `metadata.json` verbatim as the page's
displayed artifact and JSON-LD — so a clean, accurate config *is* the product.

---

## 6. Ship

```bash
# 1. Showcase repo: commit the design (no Co-Authored-By lines).
cd ~/Documents/Projects/potato-showcase
git add <design> && git commit -m "Add <Dataset> showcase design" && git push

# 2. Website reads showcase data at BUILD time from the GitHub raw CDN.
#    Wait for CDN propagation (~5 min TTL), confirm with curl, then:
cd ~/Documents/Projects/potato-website
rm -rf .next/cache && npm run build      # must succeed before push
git commit --allow-empty -m "Redeploy: pick up <Dataset> showcase page" && git push
npm run indexnow                          # final step after a major content update
```

The website pulls `metadata.json` / `config.yaml` per design via the GitHub Trees
API + `raw.githubusercontent.com`, cached `force-cache` and baked at build. A
stale CDN read is the most common gotcha — confirm the raw URL shows the new
content before building.

---

## 7. Next targets (from the 2026-06 search log)

Ordered by demand × feasibility. ATOMIC (425 impr) is done as the template.

| Target | Impr | Bucket | Note |
|---|---|---|---|
| MagnaTagATune | 77 | gap | 188-tag music auto-tagging; we only have generic `music-genre-classification`. |
| SciFact | 253 | buried | Re-brand `scientific-claim-verification`; surface SUPPORTS/REFUTES/NEI and "SciFact". |
| HatEval | (in SemEval) | buried | `semeval/2019/task05-hateval` → surface "HatEval" in title/slug. |
| Tweet intimacy, suggestion mining | — | buried | Other numeric SemEval slugs hiding named datasets. |
| ATOMIC-2020, SocialIQA, GLUCOSE | — | gap | ATOMIC siblings; one cluster, lifts the commonsense-KG entity set. |

See **`CANDIDATE_DATASETS.md`** for the full build-next backlog — led by the
"datasets re-annotated in other languages" angle (SQuAD ports, multilingual NER,
Universal Dependencies, localized GLUE suites), where each localization is a fresh
searched proper-noun and the searcher is about to reproduce the labeling in their
language. See **`LINK_CLEANUP_TODO.md`** for the dead/fabricated `datasetUrl`s to
repair in a cleanup batch.

When the next batch runs, re-pull `Queries.csv`/`Pages.csv` first — the demand
shifts, and newly-shipped pages move from "gap" to "thin/enrich."
