# Egocentric Bias in Vision-Language Models

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.15892)

## 요약
arXiv:2602.15892v1 Announce Type: new
Abstract: Visual perspective taking--inferring how the world appears from another's viewpoint--is foundational to social cognition. We introduce FlipSet, a diagnostic benchmark for Level-2 visual perspective taking (L2 VPT) in vision-language models. The task requires simulating 180-degree rotations of 2D character strings from another agent's perspective, isolating spatial transformation from 3D scene complexity. Evaluating 103 VLMs reveals systematic egocentric bias: the vast majority perform below chance, with roughly three-quarters of errors reproducing the camera viewpoint. Control experiments expose a compositional deficit--models achieve high theory-of-mind accuracy and above-chance mental rotation in isolation, yet fail catastrophically when integration is required. This dissociation indicates that current VLMs lack the mechanisms needed to bind social awareness to spatial operations, suggesting fundamental limitations in model-based spatial reasoning. FlipSet provides a cognitively grounded testbed for diagnosing perspective-taking capabilities in multimodal systems.
