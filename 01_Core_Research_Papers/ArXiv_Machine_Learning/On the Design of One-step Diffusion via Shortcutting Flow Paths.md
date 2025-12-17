# On the Design of One-step Diffusion via Shortcutting Flow Paths

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.11831)

## 요약
arXiv:2512.11831v1 Announce Type: new
Abstract: Recent advances in few-step diffusion models have demonstrated their efficiency and effectiveness by shortcutting the probabilistic paths of diffusion models, especially in training one-step diffusion models from scratch (a.k.a. shortcut models). However, their theoretical derivation and practical implementation are often closely coupled, which obscures the design space. To address this, we propose a common design framework for representative shortcut models. This framework provides theoretical justification for their validity and disentangles concrete component-level choices, thereby enabling systematic identification of improvements. With our proposed improvements, the resulting one-step model achieves a new state-of-the-art FID50k of 2.85 on ImageNet-256x256 under the classifier-free guidance setting. Remarkably, the model requires no pre-training, distillation, or curriculum learning. We believe our work lowers the barrier to component-level innovation in shortcut models and facilitates principled exploration of their design space.
