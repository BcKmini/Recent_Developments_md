# Vision Transformers Need More Than Registers

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.22394)

## 요약
arXiv:2602.22394v1 Announce Type: new
Abstract: Vision Transformers (ViTs), when pre-trained on large-scale data, provide general-purpose representations for diverse downstream tasks. However, artifacts in ViTs are widely observed across different supervision paradigms and downstream tasks. Through systematic analysis of artifacts in ViTs, we find that their fundamental mechanisms have yet to be sufficiently elucidated. In this paper, through systematic analysis, we conclude that these artifacts originate from a lazy aggregation behavior: ViT uses semantically irrelevant background patches as shortcuts to represent global semantics, driven by global attention and Coarse-grained semantic supervision. Our solution selectively integrates patch features into the CLS token, reducing the influence of background-dominated shortcuts and consistently improving performance across 12 benchmarks under label-, text-, and self-supervision. We hope this work offers a new perspective on ViT behavior.
