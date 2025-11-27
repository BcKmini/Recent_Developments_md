# Quantifying Modality Contributions via Disentangling Multimodal Representations

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.19470)

## 요약
arXiv:2511.19470v1 Announce Type: new
Abstract: Quantifying modality contributions in multimodal models remains a challenge, as existing approaches conflate the notion of contribution itself. Prior work relies on accuracy-based approaches, interpreting performance drops after removing a modality as indicative of its influence. However, such outcome-driven metrics fail to distinguish whether a modality is inherently informative or whether its value arises only through interaction with other modalities. This distinction is particularly important in cross-attention architectures, where modalities influence each other's representations. In this work, we propose a framework based on Partial Information Decomposition (PID) that quantifies modality contributions by decomposing predictive information in internal embeddings into unique, redundant, and synergistic components. To enable scalable, inference-only analysis, we develop an algorithm based on the Iterative Proportional Fitting Procedure (IPFP) that computes layer and dataset-level contributions without retraining. This provides a principled, representation-level view of multimodal behavior, offering clearer and more interpretable insights than outcome-based metrics.
