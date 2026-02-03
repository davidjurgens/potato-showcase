# Image Annotation Tasks

This category contains annotation task designs for computer vision research, including image classification, object detection, semantic segmentation, and domain-specific applications.

## Subcategories

### [Classification](./classification/)
Tasks for image-level classification and tagging.

| Design | Description | Reference |
|--------|-------------|-----------|
| [ms-coco](./classification/ms-coco) | Object detection & instance segmentation (80 categories) | Lin et al., ECCV 2014 |
| [pascal-voc](./classification/pascal-voc) | Object detection with bounding boxes (20 classes) | Everingham et al., IJCV 2010 |
| [imagenet](./classification/imagenet) | Large-scale image classification (1000+ synsets) | Deng et al., CVPR 2009 |
| [cub-200-birds](./classification/cub-200-birds) | Fine-grained bird species classification (200 species) | Wah et al., 2011 |
| [places365](./classification/places365) | Scene classification (365 categories) | Zhou et al., TPAMI 2017 |
| [open-images](./classification/open-images) | Large-scale object detection (600 classes) | Kuznetsova et al., IJCV 2020 |

### [Segmentation](./segmentation/)
Tasks for pixel-level semantic and instance segmentation.

| Design | Description | Reference |
|--------|-------------|-----------|
| [cityscapes](./segmentation/cityscapes) | Urban scene instance segmentation | Cordts et al., CVPR 2016 |
| [ade20k](./segmentation/ade20k) | Semantic segmentation (150 classes) | Zhou et al., CVPR 2017 |
| [lip-human-parsing](./segmentation/lip-human-parsing) | Human body part segmentation (20 parts) | Gong et al., CVPR 2017 |

### [Medical Imaging](./medical/)
Tasks for medical image analysis and clinical applications.

| Design | Description | Reference |
|--------|-------------|-----------|
| [chexpert](./medical/chexpert) | Chest X-ray multi-label classification (14 observations) | Irvin et al., AAAI 2019 |
| [mimic-cxr](./medical/mimic-cxr) | Chest radiograph classification with reports | Johnson et al., Scientific Data 2019 |

### [Autonomous Driving](./driving/)
Tasks for self-driving car perception and scene understanding.

| Design | Description | Reference |
|--------|-------------|-----------|
| [kitti](./driving/kitti) | Road object detection with 3D bounding boxes | Geiger et al., CVPR 2012 |
| [bdd100k](./driving/bdd100k) | Diverse driving scene segmentation | Yu et al., CVPR 2020 |

### [Aerial & Remote Sensing](./aerial/)
Tasks for satellite imagery and aerial photograph analysis.

| Design | Description | Reference |
|--------|-------------|-----------|
| [bigearth-net](./aerial/bigearth-net) | Sentinel-2 land cover classification (43 classes) | Sumbul et al., IGARSS 2019 |
| [xview](./aerial/xview) | Satellite object detection (60 classes) | Lam et al., arXiv 2018 |
| [dota-aerial](./aerial/dota-aerial) | Oriented bounding box detection in aerial images | Xia et al., CVPR 2018 |

### [Specialized Domains](./specialized/)
Tasks for domain-specific image annotation applications.

| Design | Description | Reference |
|--------|-------------|-----------|
| [mvtec-ad](./specialized/mvtec-ad) | Industrial defect detection (15 categories) | Bergmann et al., CVPR 2019 |
| [deepfashion](./specialized/deepfashion) | Fine-grained fashion classification | Liu et al., CVPR 2016 |
| [celeba](./specialized/celeba) | Face attributes classification (40 attributes) | Liu et al., ICCV 2015 |
| [iwildcam](./specialized/iwildcam) | Wildlife camera trap classification | Beery et al., CVPR 2019 |
| [wikiart](./specialized/wikiart) | Artwork style and genre classification | Saleh & Elgammal, 2015 |
| [docbank](./specialized/docbank) | Document layout analysis | Li et al., COLING 2020 |

## Quick Start

```bash
# Navigate to a specific task
cd image/classification/ms-coco

# Run with Potato
potato start config.yaml
```

## Task Count

**Total: 22 image annotation tasks** across 6 subcategories
