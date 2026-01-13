# STResNet & STYOLO : A New Family of Compact Classification and Object Detection Models for MCUs

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.05364)

## 요약
arXiv:2601.05364v1 Announce Type: new
Abstract: Recent advancements in lightweight neural networks have significantly improved the efficiency of deploying deep learning models on edge hardware. However, most existing architectures still trade accuracy for latency, which limits their applicability on microcontroller and neural processing unit based devices. In this work, we introduce two new model families, STResNet for image classification and STYOLO for object detection, jointly optimized for accuracy, efficiency, and memory footprint on resource constrained platforms. The proposed STResNet series, ranging from Nano to Tiny variants, achieves competitive ImageNet 1K accuracy within a four million parameter budget. Specifically, STResNetMilli attains 70.0 percent Top 1 accuracy with only three million parameters, outperforming MobileNetV1 and ShuffleNetV2 at comparable computational complexity. For object detection, STYOLOMicro and STYOLOMilli achieve 30.5 percent and 33.6 percent mean average precision, respectively, on the MS COCO dataset, surpassing YOLOv5n and YOLOX Nano in both accuracy and efficiency. Furthermore, when STResNetMilli is used as a backbone with the Ultralytics training environment.
