# Multimodal Annotation Tasks

This category contains annotation task designs that combine text with images, charts, memes, or robotic action spaces — tasks where judgments require reasoning across modalities.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [documentation](https://www.potatoannotator.com/docs) for multimodal display layouts.

## Tasks

| Design | Description | Reference |
|--------|-------------|-----------|
| [chartinfo-chart-analysis](./chartinfo-chart-analysis) | Chart and infographic analysis with structured extraction | Template |
| [hatred-hateful-memes](./hatred-hateful-memes) | Hateful meme detection requiring understanding of both image and text | Hee et al., IJCAI 2023 |
| [mmbench-multimodal-eval](./mmbench-multimodal-eval) | MMBench is a multiple-choice benchmark of about 2,974 questions testing vision-language models across 20… | Liu et al., ECCV 2024 |
| [mmmu-multimodal-understanding](./mmmu-multimodal-understanding) | Multi-discipline multimodal QA requiring college-level understanding | Yue et al., CVPR 2024 |
| [mocheg-multimodal-factcheck](./mocheg-multimodal-factcheck) | Multimodal fact-checking requiring reasoning over both text and images | Yao et al., SIGIR 2023 |
| [rt2-robotic-action-annotation](./rt2-robotic-action-annotation) | Robotic manipulation task evaluation and action segmentation based on RT-2 | Brohan et al., CoRL 2023 |
| [saycan-robot-planning](./saycan-robot-planning) | SayCan grounds a large language model in learned robot skills so a robot can carry out long-horizon… | Ahn et al., CoRL 2022 |
| [scienceqa-multimodal-reasoning](./scienceqa-multimodal-reasoning) | Multimodal science question answering with chain-of-thought reasoning, based on ScienceQA. Annotators… | Lu et al., NeurIPS 2022 |
| [soda-eval-social-dialogue](./soda-eval-social-dialogue) | Evaluate the quality of socially-grounded dialogues generated through social commonsense contextualization | Mendonca et al., Findings of EMNLP 2024 |

## Quick Start

```bash
# Navigate to a specific task
cd multimodal/<task-name>

# Run with Potato
potato start config.yaml
```

## Task Count

**Total: 9 multimodal annotation tasks**
