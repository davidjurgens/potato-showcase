# Video Annotation Tasks

This category contains annotation task designs for video understanding research, including action recognition, temporal localization, video summarization, and scene understanding.

## Subcategories

### [Action Recognition](./action-recognition/)
Tasks for recognizing and classifying actions in video.

| Design | Description | Reference |
|--------|-------------|-----------|
| [ava-atomic-actions](./action-recognition/ava-atomic-actions) | Spatio-temporal atomic action detection (80 classes) | Gu et al., CVPR 2018 |
| [charades-activity-segmentation](./action-recognition/charades-activity-segmentation) | Indoor activity recognition and segmentation | Sigurdsson et al., ECCV 2016 |
| [thumos14-action-localization](./action-recognition/thumos14-action-localization) | Temporal action detection in untrimmed video | Idrees et al., CVPR 2017 |
| [activitynet-temporal-localization](./action-recognition/activitynet-temporal-localization) | Large-scale activity recognition (200 classes) | Caba Heilbron et al., CVPR 2015 |
| [epic-kitchens-egocentric](./action-recognition/epic-kitchens-egocentric) | Egocentric kitchen activity with verb-noun pairs | Damen et al., ECCV 2018 |
| [finegym-action-segments](./action-recognition/finegym-action-segments) | Hierarchical gymnastic action segmentation | Shao et al., CVPR 2020 |
| [breakfast-actions](./action-recognition/breakfast-actions) | Cooking activity recognition and segmentation | Kuehne et al., CVPR 2014 |
| [soccernet-action-spotting](./action-recognition/soccernet-action-spotting) | Soccer event detection and spotting | Giancola et al., CVPR 2018 |

### [Temporal Grounding](./temporal-grounding/)
Tasks for grounding language to video segments.

| Design | Description | Reference |
|--------|-------------|-----------|
| [activitynet-captions](./temporal-grounding/activitynet-captions) | Dense video captioning with temporal segments | Krishna et al., ICCV 2017 |
| [didemo-moment-retrieval](./temporal-grounding/didemo-moment-retrieval) | Natural language moment retrieval | Hendricks et al., ICCV 2017 |
| [charades-sta-grounding](./temporal-grounding/charades-sta-grounding) | Temporal activity localization via language | Gao et al., ICCV 2017 |

### [Video Summarization](./summarization/)
Tasks for creating video summaries and selecting keyframes.

| Design | Description | Reference |
|--------|-------------|-----------|
| [tvsum-summarization](./summarization/tvsum-summarization) | Title-based video summarization (10 categories) | Song et al., CVPR 2015 |
| [summe-summarization](./summarization/summe-summarization) | User video summarization | Gygli et al., ECCV 2014 |
| [youtube-highlights](./summarization/youtube-highlights) | Domain-specific highlight detection | Sun et al., ECCV 2014 |
| [lsmdc-keyframe-selection](./summarization/lsmdc-keyframe-selection) | Movie clip keyframe selection | Rohrbach et al., IJCV 2017 |

### [Boundary Detection](./boundary-detection/)
Tasks for detecting shot and scene boundaries in video.

| Design | Description | Reference |
|--------|-------------|-----------|
| [scene-boundary-detection](./boundary-detection/scene-boundary-detection) | Semantic scene boundary detection | Baraldi et al., CVPR 2015 |
| [shot-boundary-detection](./boundary-detection/shot-boundary-detection) | Shot transition detection | Tang et al., arXiv 2019 |
| [moviescenes-detection](./boundary-detection/moviescenes-detection) | Multi-modal movie scene segmentation | Rao et al., CVPR 2020 |

### [Scene Understanding](./scene-understanding/)
Tasks for understanding scene attributes and context in video.

| Design | Description | Reference |
|--------|-------------|-----------|
| [movienet-scene-classification](./scene-understanding/movienet-scene-classification) | Movie scene attribute classification | Qian et al., ECCV 2020 |

### [Instructional Video](./instructional/)
Tasks for understanding procedural and instructional content.

| Design | Description | Reference |
|--------|-------------|-----------|
| [howto100m-instructional](./instructional/howto100m-instructional) | Instructional video step annotation | Miech et al., ICCV 2019 |
| [youcook2-instructional](./instructional/youcook2-instructional) | Recipe step segmentation and captioning | Zhou et al., AAAI 2018 |

## Quick Start

```bash
# Navigate to a specific task
cd video/action-recognition/ava-atomic-actions

# Run with Potato
potato start config.yaml
```

## Annotation Modes

Video annotation tasks in Potato support several modes:

- **Segment Mode**: Mark temporal segments with start/end times
- **Keyframe Mode**: Select representative frames
- **Tracking Mode**: Track objects across frames
- **Combined Mode**: Multiple annotation types per video

## Task Count

**Total: 21 video annotation tasks** across 6 subcategories
