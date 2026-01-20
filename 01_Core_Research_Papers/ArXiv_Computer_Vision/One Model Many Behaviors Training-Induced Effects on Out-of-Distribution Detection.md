# One Model, Many Behaviors: Training-Induced Effects on Out-of-Distribution Detection

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.10836)

## 요약
arXiv:2601.10836v1 Announce Type: new
Abstract: Out-of-distribution (OOD) detection is crucial for deploying robust and reliable machine-learning systems in open-world settings. Despite steady advances in OOD detectors, their interplay with modern training pipelines that maximize in-distribution (ID) accuracy and generalization remains under-explored. We investigate this link through a comprehensive empirical study. Fixing the architecture to the widely adopted ResNet-50, we benchmark 21 post-hoc, state-of-the-art OOD detection methods across 56 ImageNet-trained models obtained via diverse training strategies and evaluate them on eight OOD test sets. Contrary to the common assumption that higher ID accuracy implies better OOD detection performance, we uncover a non-monotonic relationship: OOD performance initially improves with accuracy but declines once advanced training recipes push accuracy beyond the baseline. Moreover, we observe a strong interdependence between training strategy, detector choice, and resulting OOD performance, indicating that no single method is universally optimal.
