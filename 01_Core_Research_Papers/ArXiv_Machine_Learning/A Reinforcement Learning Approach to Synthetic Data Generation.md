# A Reinforcement Learning Approach to Synthetic Data Generation

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.21395)

## 요약
arXiv:2512.21395v1 Announce Type: new
Abstract: Synthetic data generation (SDG) is a promising approach for enabling data sharing in biomedical studies while preserving patient privacy. Yet, state-of-the-art generative models often require large datasets and complex training procedures, limiting their applicability in small-sample settings. In this work, we reframe SDG as a reinforcement learning (RL) problem and introduce RLSyn, a novel framework that models the data generator as a stochastic policy over patient records and optimizes it using Proximal Policy Optimization with discriminator-derived rewards, yielding more stable and data-efficient training. We evaluate RLSyn on two biomedical datasets - AI-READI and MIMIC-IV- and benchmark it against state-of-the-art generative adversarial networks (GANs) and diffusion-based methods across extensive privacy, utility, and fidelity evaluations. RL-Syn performs comparably to diffusion models and outperforms GANs on MIMIC-IV, while outperforming both diffusion models and GANs on the smaller AI-READI dataset. These results demonstrate that reinforcement learning provides a principled and effective alternative for synthetic biomedical data generation, particularly in data-scarce regimes.
