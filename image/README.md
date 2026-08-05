# Image Annotation Tasks

This category contains annotation task designs for computer vision research, including image classification, object detection, semantic segmentation, and domain-specific applications.

> Run these designs in [Potato](https://www.potatoannotator.com). See the [image annotation documentation](https://www.potatoannotator.com/docs/annotation-types/image-annotation) to configure bounding boxes, keypoints, and classification.

## Subcategories

### [Aerial & Remote Sensing](./aerial/)
Tasks for satellite imagery and aerial photograph analysis.

| Design | Description | Reference |
|--------|-------------|-----------|
| [bigearth-net](./aerial/bigearth-net) | Sentinel-2 land cover classification (43 classes) | Sumbul et al., IGARSS 2019 |
| [dota-aerial](./aerial/dota-aerial) | Oriented bounding box detection in aerial images | Xia et al., CVPR 2018 |
| [xview](./aerial/xview) | Satellite object detection (60 classes) | Lam et al., arXiv 2018 |

### [Classification](./classification/)
Tasks for image-level classification and tagging.

| Design | Description | Reference |
|--------|-------------|-----------|
| [cub-200-birds](./classification/cub-200-birds) | Fine-grained bird species classification (200 species) | Wah et al., 2011 |
| [imagenet](./classification/imagenet) | Large-scale image classification (1000+ synsets) | Deng et al., CVPR 2009 |
| [ms-coco](./classification/ms-coco) | Object detection & instance segmentation (80 categories) | Lin et al., ECCV 2014 |
| [open-images](./classification/open-images) | Large-scale object detection (600 classes) | Kuznetsova et al., IJCV 2020 |
| [pascal-voc](./classification/pascal-voc) | Object detection with bounding boxes (20 classes) | Everingham et al., IJCV 2010 |
| [places365](./classification/places365) | Scene classification (365 categories) | Zhou et al., TPAMI 2017 |

### [Doclaynet Document Layout](./doclaynet-document-layout/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [doclaynet-document-layout](./doclaynet-document-layout) | Document layout analysis with bounding box annotations | Pfitzmann et al., KDD 2022 |

### [Autonomous Driving](./driving/)
Tasks for self-driving car perception and scene understanding.

| Design | Description | Reference |
|--------|-------------|-----------|
| [bdd100k](./driving/bdd100k) | Diverse driving scene segmentation | Yu et al., CVPR 2020 |
| [kitti](./driving/kitti) | Road object detection with 3D bounding boxes | Geiger et al., CVPR 2012 |

### [Flair Aerial Land Use](./flair-aerial-land-use/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [flair-aerial-land-use](./flair-aerial-land-use) | Land use and land cover classification from high-resolution aerial imagery | Garioud et al., NeurIPS 2023 |

### [Generation Eval](./generation-eval/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [t2i-compbench](./generation-eval/t2i-compbench) | T2I-CompBench is a 6,000-prompt benchmark for compositional text-to-image generation | Huang et al., NeurIPS 2023 |

### [Human Pose](./human-pose/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [vitpose-keypoint-annotation](./human-pose/vitpose-keypoint-annotation) | Annotate human body keypoints and classify pose categories in images | Template |

### [Medical Imaging](./medical/)
Tasks for medical image analysis and clinical applications.

| Design | Description | Reference |
|--------|-------------|-----------|
| [camelyon-pathology](./medical/camelyon-pathology) | Pathology slide annotation for breast cancer metastasis detection | Ehteshami Bejnordi et al., JAMA 2017 |
| [chexpert](./medical/chexpert) | Chest X-ray multi-label classification (14 observations) | Irvin et al., AAAI 2019 |
| [mimic-cxr](./medical/mimic-cxr) | Chest radiograph classification with reports | Johnson et al., Scientific Data 2019 |

### [Omnidocbench Document Parsing](./omnidocbench-document-parsing/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [omnidocbench-document-parsing](./omnidocbench-document-parsing) | Comprehensive document parsing annotation covering layout detection, text recognition, table structure,… | Ouyang et al., CVPR 2025 |

### [Sa1B Segment Anything](./sa1b-segment-anything/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [sa1b-segment-anything](./sa1b-segment-anything) | Interactive image segmentation annotation | Kirillov et al., ICCV 2023 |

### [Segmentation](./segmentation/)
Tasks for pixel-level semantic and instance segmentation.

| Design | Description | Reference |
|--------|-------------|-----------|
| [ade20k](./segmentation/ade20k) | Semantic segmentation (150 classes) | Zhou et al., CVPR 2017 |
| [cityscapes](./segmentation/cityscapes) | Urban scene instance segmentation | Cordts et al., CVPR 2016 |
| [lip-human-parsing](./segmentation/lip-human-parsing) | Human body part segmentation (20 parts) | Gong et al., CVPR 2017 |

### [Specialized Domains](./specialized/)
Tasks for domain-specific image annotation applications.

| Design | Description | Reference |
|--------|-------------|-----------|
| [celeba](./specialized/celeba) | Face attributes classification (40 attributes) | Liu et al., ICCV 2015 |
| [deepfashion](./specialized/deepfashion) | Fine-grained fashion classification | Liu et al., CVPR 2016 |
| [docbank](./specialized/docbank) | Document layout analysis | Li et al., COLING 2020 |
| [iwildcam](./specialized/iwildcam) | Wildlife camera trap classification | Beery et al., CVPR 2019 |
| [mvtec-ad](./specialized/mvtec-ad) | Industrial defect detection (15 categories) | Bergmann et al., CVPR 2019 |
| [wikiart](./specialized/wikiart) | Artwork style and genre classification | Saleh & Elgammal, 2015 |

### [Visual Grounding](./visual-grounding/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [refcoco-expression](./visual-grounding/refcoco-expression) | Visual grounding task where annotators draw bounding boxes around objects referred to by natural language… | Yu et al., ECCV 2016 |

### [Visual Qa](./visual-qa/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [textvqa-reading-in-images](./visual-qa/textvqa-reading-in-images) | TextVQA is a visual question answering dataset where reading scene text in the image is needed to answer | Singh et al., CVPR 2019 |
| [vqav2-visual-question-answering](./visual-qa/vqav2-visual-question-answering) | VQA v2.0 is a balanced visual question answering benchmark of open-ended questions over COCO images, with… | Goyal et al., CVPR 2017 |

### [Wtw Table Structure Annotation](./wtw-table-structure-annotation/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [wtw-table-structure-annotation](./wtw-table-structure-annotation) | Cell-grid structure annotation for photographed and scanned wired tables, based on the WTW (Wired Table in… | Long et al., ICCV 2021 |

### [Xbd Building Damage](./xbd-building-damage/)

| Design | Description | Reference |
|--------|-------------|-----------|
| [xbd-building-damage](./xbd-building-damage) | Building damage assessment from pre- and post-disaster satellite imagery | Gupta et al., CVPR Workshops 2019 |

## Quick Start

```bash
# Navigate to a specific task
cd image/classification/ms-coco

# Run with Potato
potato start config.yaml
```

## Task Count

**Total: 34 image annotation tasks** across 16 subcategories
