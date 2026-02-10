# MetaSSP: Enhancing Semi-supervised Implicit 3D Reconstruction through Meta-adaptive EMA and SDF-aware Pseudo-label Evaluation

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.06163)

## 요약
arXiv:2602.06163v1 Announce Type: new
Abstract: Implicit SDF-based methods for single-view 3D reconstruction achieve high-quality surfaces but require large labeled datasets, limiting their scalability. We propose MetaSSP, a novel semi-supervised framework that exploits abundant unlabeled images. Our approach introduces gradient-based parameter importance estimation to regularize adaptive EMA updates and an SDF-aware pseudo-label weighting mechanism combining augmentation consistency with SDF variance. Beginning with a 10% supervised warm-up, the unified pipeline jointly refines labeled and unlabeled data. On the Pix3D benchmark, our method reduces Chamfer Distance by approximately 20.61% and increases IoU by around 24.09% compared to existing semi-supervised baselines, setting a new state of the art.
