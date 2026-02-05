# SVD-ViT: Does SVD Make Vision Transformers Attend More to the Foreground?

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.02765)

## 요약
arXiv:2602.02765v1 Announce Type: new
Abstract: Vision Transformers (ViT) have been established as large-scale foundation models. However, because self-attention operates globally, they lack an explicit mechanism to distinguish foreground from background. As a result, ViT may learn unnecessary background features and artifacts, leading to degraded classification performance. To address this issue, we propose SVD-ViT, which leverages singular value decomposition (SVD) to prioritize the learning of foreground features. SVD-ViT consists of three components-\textbf{SPC module}, \textbf{SSVA}, and \textbf{ID-RSVD}-and suppresses task-irrelevant factors such as background noise and artifacts by extracting and aggregating singular vectors that capture object foreground information. Experimental results demonstrate that our method improves classification accuracy and effectively learns informative foreground representations while reducing the impact of background noise.
