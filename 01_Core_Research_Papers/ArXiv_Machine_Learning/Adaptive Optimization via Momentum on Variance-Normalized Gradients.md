# Adaptive Optimization via Momentum on Variance-Normalized Gradients

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.10204)

## 요약
arXiv:2602.10204v1 Announce Type: new
Abstract: We introduce MVN-Grad (Momentum on Variance-Normalized Gradients), an Adam-style optimizer that improves stability and performance by combining two complementary ideas: variance-based normalization and momentum applied after normalization. MVN-Grad scales each coordinate by an exponential moving average of gradient uncertainty and applies momentum to the resulting normalized gradients, eliminating the cross-time coupling between stale momentum and a stochastic normalizer present in standard Adam-type updates. We prove that this decoupling yields strictly smaller one-step conditional update variance than momentum-then-normalize variance methods under standard noise assumptions, and that MVN-Grad is robust to outliers: it has a uniformly bounded response to single gradient spikes.
In low-variance regimes, we further show variance normalization avoids sign-type collapse associated with second-moment scaling and can yield accelerated convergence. Across CIFAR-100 image classification and GPT-style language modeling benchmarks, MVN-Grad matches or outperforms Adam, AdaBelief, and LaProp, delivering smoother training and improved generalization with no added overhead.
