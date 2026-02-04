# MapDream: Task-Driven Map Learning for Vision-Language Navigation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.00222)

## 요약
arXiv:2602.00222v1 Announce Type: new
Abstract: Vision-Language Navigation (VLN) requires agents to follow natural language instructions in partially observed 3D environments, motivating map representations that aggregate spatial context beyond local perception. However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy. We argue that maps should instead be learned representations shaped directly by navigation objectives rather than exhaustive reconstructions. Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird's-eye-view (BEV) image synthesis. The framework jointly learns map generation and action prediction, distilling environmental context into a compact three-channel BEV map that preserves only navigation-critical affordances. Supervised pre-training bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning. Experiments on R2R-CE and RxR-CE achieve state-of-the-art monocular performance, validating task-driven generative map learning.
