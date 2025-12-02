# Adaptive Parameter Optimization for Robust Remote Photoplethysmography

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.21903)

## 요약
arXiv:2511.21903v1 Announce Type: new
Abstract: Remote photoplethysmography (rPPG) enables contactless vital sign monitoring using standard RGB cameras. However, existing methods rely on fixed parameters optimized for particular lighting conditions and camera setups, limiting adaptability to diverse deployment environments. This paper introduces the Projection-based Robust Signal Mixing (PRISM) algorithm, a training-free method that jointly optimizes photometric detrending and color mixing through online parameter adaptation based on signal quality assessment. PRISM achieves state-of-the-art performance among unsupervised methods, with MAE of 0.77 bpm on PURE and 0.66 bpm on UBFC-rPPG, and accuracy of 97.3\% and 97.5\% respectively at a 5 bpm threshold. Statistical analysis confirms PRISM performs equivalently to leading supervised methods ($p > 0.2$), while maintaining real-time CPU performance without training. This validates that adaptive time series optimization significantly improves rPPG across diverse conditions.
