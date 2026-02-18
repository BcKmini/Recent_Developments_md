# Directional Concentration Uncertainty: A representational approach to uncertainty quantification for generative models

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.13264)

## 요약
arXiv:2602.13264v1 Announce Type: new
Abstract: In the critical task of making generative models trustworthy and robust, methods for Uncertainty Quantification (UQ) have begun to show encouraging potential. However, many of these methods rely on rigid heuristics that fail to generalize across tasks and modalities. Here, we propose a novel framework for UQ that is highly flexible and approaches or surpasses the performance of prior heuristic methods. We introduce Directional Concentration Uncertainty (DCU), a novel statistical procedure for quantifying the concentration of embeddings based on the von Mises-Fisher (vMF) distribution. Our method captures uncertainty by measuring the geometric dispersion of multiple generated outputs from a language model using continuous embeddings of the generated outputs without any task specific heuristics. In our experiments, we show that DCU matches or exceeds calibration levels of prior works like semantic entropy (Kuhn et al., 2023) and also generalizes well to more complex tasks in multi-modal domains. We present a framework for the wider potential of DCU and its implications for integration into UQ for multi-modal and agentic frameworks.
