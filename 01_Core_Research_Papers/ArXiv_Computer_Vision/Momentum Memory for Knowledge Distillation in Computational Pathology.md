# Momentum Memory for Knowledge Distillation in Computational Pathology

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.21395)

## 요약
arXiv:2602.21395v1 Announce Type: new
Abstract: Multimodal learning that integrates genomics and histopathology has shown strong potential in cancer diagnosis, yet its clinical translation is hindered by the limited availability of paired histology-genomics data. Knowledge distillation (KD) offers a practical solution by transferring genomic supervision into histopathology models, enabling accurate inference using histology alone. However, existing KD methods rely on batch-local alignment, which introduces instability due to limited within-batch comparisons and ultimately degrades performance.
To address these limitations, we propose Momentum Memory Knowledge Distillation (MoMKD), a cross-modal distillation framework driven by a momentum-updated memory. This memory aggregates genomic and histopathology information across batches, effectively enlarging the supervisory context available to each mini-batch. Furthermore, we decouple the gradients of the genomics and histology branches, preventing genomic signals from dominating histology feature learning during training and eliminating the modality-gap issue at inference time.
Extensive experiments on the TCGA-BRCA benchmark (HER2, PR, and ODX classification tasks) and an independent in-house testing dataset demonstrate that MoMKD consistently outperforms state-of-the-art MIL and multimodal KD baselines, delivering strong performance and generalization under histology-only inference. Overall, MoMKD establishes a robust and generalizable knowledge distillation paradigm for computational pathology.
