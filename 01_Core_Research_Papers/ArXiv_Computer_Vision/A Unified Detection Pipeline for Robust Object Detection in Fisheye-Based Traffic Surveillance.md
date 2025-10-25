# A Unified Detection Pipeline for Robust Object Detection in Fisheye-Based Traffic Surveillance

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.20016)

## 요약
arXiv:2510.20016v1 Announce Type: new
Abstract: Fisheye cameras offer an efficient solution for wide-area traffic surveillance by capturing large fields of view from a single vantage point. However, the strong radial distortion and nonuniform resolution inherent in fisheye imagery introduce substantial challenges for standard object detectors, particularly near image boundaries where object appearance is severely degraded. In this work, we present a detection framework designed to operate robustly under these conditions. Our approach employs a simple yet effective pre and post processing pipeline that enhances detection consistency across the image, especially in regions affected by severe distortion. We train several state-of-the-art detection models on the fisheye traffic imagery and combine their outputs through an ensemble strategy to improve overall detection accuracy. Our method achieves an F1 score of0.6366 on the 2025 AI City Challenge Track 4, placing 8thoverall out of 62 teams. These results demonstrate the effectiveness of our framework in addressing issues inherent to fisheye imagery.
