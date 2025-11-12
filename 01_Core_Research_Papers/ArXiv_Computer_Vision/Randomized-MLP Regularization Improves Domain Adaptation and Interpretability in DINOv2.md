# Randomized-MLP Regularization Improves Domain Adaptation and Interpretability in DINOv2

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.05509)

## 요약
arXiv:2511.05509v1 Announce Type: new
Abstract: Vision Transformers (ViTs), such as DINOv2, achieve strong performance across domains but often repurpose low-informative patch tokens in ways that reduce the interpretability of attention and feature maps. This challenge is especially evident in medical imaging, where domain shifts can degrade both performance and transparency. In this paper, we introduce Randomized-MLP (RMLP) regularization, a contrastive learning-based method that encourages more semantically aligned representations. We use RMLPs when fine-tuning DINOv2 to both medical and natural image modalities, showing that it improves or maintains downstream performance while producing more interpretable attention maps. We also provide a mathematical analysis of RMLPs, offering insights into its role in enhancing ViT-based models and advancing our understanding of contrastive learning.
