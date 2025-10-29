# Proportion and Perspective Control for Flow-Based Image Generation

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.21763)

## 요약
arXiv:2510.21763v1 Announce Type: new
Abstract: While modern text-to-image diffusion models generate high-fidelity images, they offer limited control over the spatial and geometric structure of the output. To address this, we introduce and evaluate two ControlNets specialized for artistic control: (1) a proportion ControlNet that uses bounding boxes to dictate the position and scale of objects, and (2) a perspective ControlNet that employs vanishing lines to control the 3D geometry of the scene. We support the training of these modules with data pipelines that leverage vision-language models for annotation and specialized algorithms for conditioning image synthesis. Our experiments demonstrate that both modules provide effective control but exhibit limitations with complex constraints. Both models are released on HuggingFace: https://huggingface.co/obvious-research
