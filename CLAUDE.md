# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git Rules

- **Never** include `Co-Authored-By` lines (or any "co-authored by Claude" variant) in git commit messages.
- CLAUDE.md is untracked — do not commit it.

## Project Overview

This is the **Potato Annotation Showcase** — a curated collection of 121 example annotation task configurations for [Potato](https://github.com/davidjurgens/potato), a lightweight annotation tool for NLP research. It is a resource/configuration repository, not a code project. There is no build system, test suite, or linting.

## Repository Structure

Seven top-level category directories, each containing self-contained task folders:

- **text/** (38 tasks) — NLP annotation (sentiment, NER, hate speech, fact verification, etc.)
- **image/** (22 tasks) — Computer vision (classification, segmentation, medical imaging, etc.)
- **video/** (21 tasks) — Video understanding (action recognition, temporal grounding, summarization)
- **audio/** (4 tasks) — Speech & audio (transcription, diarization, emotion, music genre)
- **preference-learning/** (12 tasks) — RLHF and preference annotation
- **evaluation/** (5 tasks) — AI output evaluation (summarization, translation, QA, captioning)
- **templates/** (19 tasks) — Generic reusable templates for common annotation patterns

## Task Folder Convention

Every task folder contains exactly three files:

1. **metadata.json** — Title, description, author, annotation types, domain tags, complexity level, paper reference with BibTeX, dataset URL, featured flag.
2. **config.yaml** — Potato configuration: annotation schemes (radio, multiselect, span, pairwise, video_annotation), HTML layout templates, keyboard shortcuts, label definitions with tooltips, user/output settings.
3. **sample-data.json** — 8–12 example items demonstrating expected data structure (ID + content fields).

## Key Patterns

- Tasks are fully self-contained — each folder works independently with Potato.
- Annotation types in configs: `radio`, `multiselect`, `span`, `pairwise`, `video_annotation`.
- Most tasks reference published datasets/papers; metadata includes citation BibTeX.
- Templates in `templates/` are meant to be copied and customized for new tasks.
- HTML layout templates inside `config.yaml` support rich multi-modal display (images, video, audio waveforms).
