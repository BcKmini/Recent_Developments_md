# Leveraging Synthetic Priors for Monocular Depth Estimation in Specular Surgical Environments

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.23786)

## 요약
arXiv:2512.23786v1 Announce Type: new
Abstract: Accurate Monocular Depth Estimation (MDE) is critical for robotic surgery but remains fragile in specular, fluid-filled endoscopic environments. Existing self-supervised methods, typically relying on foundation models trained with noisy real-world pseudo-labels, often suffer from boundary collapse on thin surgical tools and transparent surfaces. In this work, we address this by leveraging the high-fidelity synthetic priors of the Depth Anything V2 architecture, which inherently captures precise geometric details of thin structures. We efficiently adapt these priors to the medical domain using Dynamic Vector Low-Rank Adaptation (DV-LORA), minimizing the parameter budget while bridging the synthetic-to-real gap. Additionally, we introduce a physically-stratified evaluation protocol on the SCARED dataset to rigorously quantify performance in high-specularity regimes often masked by aggregate metrics. Our approach establishes a new state-of-the-art, achieving an accuracy (< 1.25) of 98.1% and reducing Squared Relative Error by over 17% compared to established baselines, demonstrating superior robustness in adverse surgical lighting.
