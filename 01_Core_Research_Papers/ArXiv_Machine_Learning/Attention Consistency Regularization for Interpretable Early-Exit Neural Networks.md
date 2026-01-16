# Attention Consistency Regularization for Interpretable Early-Exit Neural Networks

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.08891)

## 요약
arXiv:2601.08891v1 Announce Type: new
Abstract: Early-exit neural networks enable adaptive inference by allowing predictions at intermediate layers, reducing computational cost. However, early exits often lack interpretability and may focus on different features than deeper layers, limiting trust and explainability. This paper presents Explanation-Guided Training (EGT), a multi-objective framework that improves interpretability and consistency in early-exit networks through attention-based regularization. EGT introduces an attention consistency loss that aligns early-exit attention maps with the final exit. The framework jointly optimizes classification accuracy and attention consistency through a weighted combination of losses. Experiments on a real-world image classification dataset demonstrate that EGT achieves up to 98.97% overall accuracy (matching baseline performance) with a 1.97x inference speedup through early exits, while improving attention consistency by up to 18.5% compared to baseline models. The proposed method provides more interpretable and consistent explanations across all exit points, making early-exit networks more suitable for explainable AI applications in resource-constrained environments.
