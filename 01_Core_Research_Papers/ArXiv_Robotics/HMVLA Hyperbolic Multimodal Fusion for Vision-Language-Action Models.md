# HMVLA: Hyperbolic Multimodal Fusion for Vision-Language-Action Models

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.02533)

## 요약
arXiv:2602.02533v1 Announce Type: new
Abstract: Vision Language Action (VLA) models have recently shown great potential in bridging multimodal perception with robotic control. However, existing methods often rely on direct fine-tuning of pre-trained Vision-Language Models (VLMs), feeding semantic and visual features directly into a policy network without fully addressing the unique semantic alignment challenges in the VLA domain. In this paper, we propose HMVLA, a novel VLA framework that exploits the inherent hierarchical structures in vision and language for comprehensive semantic alignment. Unlike traditional methods that perform alignment in Euclidean space, our HMVLA embeds multimodal features in hyperbolic space, enabling more effective modeling of the hierarchical relationships present in image text data. Furthermore, we introduce a sparsely gated Mixture of Experts (MoE) mechanism tailored for semantic alignment, which enhances multimodal comprehension between images and text while improving efficiency. Extensive experiments demonstrate that HMVLA surpasses baseline methods in both accuracy and generalization. In addition, we validate its robustness by reconstructing datasets to further test cross domain adaptability.
