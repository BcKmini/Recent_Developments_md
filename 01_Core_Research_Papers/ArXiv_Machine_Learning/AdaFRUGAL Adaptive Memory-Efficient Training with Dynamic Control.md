# AdaFRUGAL: Adaptive Memory-Efficient Training with Dynamic Control

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.11568)

## 요약
arXiv:2601.11568v1 Announce Type: new
Abstract: Training Large Language Models (LLMs) is highly memory-intensive due to optimizer state overhead. The FRUGAL framework mitigates this with gradient splitting, but its static hyperparameters -- the subspace ratio ($\rho$) and update frequency ($T$) -- require costly manual tuning, limiting adaptability. We present AdaFRUGAL, which automates this process by introducing two dynamic controls: (i) a linear decay for $\rho$ to progressively reduce memory, and (ii) a loss-aware schedule for $T$ to lower computational overhead. Experiments across large-scale pre-training (English C4, Vietnamese VietVault) and fine-tuning (GLUE) demonstrate that AdaFRUGAL achieves a compelling trade-off. It maintains competitive performance against AdamW and static FRUGAL while significantly reducing both GPU memory and training time, offering a more practical, autonomous solution for resource-constrained LLM training.
