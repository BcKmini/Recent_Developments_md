# R3G: A Reasoning--Retrieval--Reranking Framework for Vision-Centric Answer Generation

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.00104)

## 요약
arXiv:2602.00104v1 Announce Type: new
Abstract: Vision-centric retrieval for VQA requires retrieving images to supply missing visual cues and integrating them into the reasoning process. However, selecting the right images and integrating them effectively into the model's reasoning remains challenging.To address this challenge, we propose R3G, a modular Reasoning-Retrieval-Reranking framework.It first produces a brief reasoning plan that specifies the required visual cues, then adopts a two-stage strategy, with coarse retrieval followed by fine-grained reranking, to select evidence images.On MRAG-Bench, R3G improves accuracy across six MLLM backbones and nine sub-scenarios, achieving state-of-the-art overall performance. Ablations show that sufficiency-aware reranking and reasoning steps are complementary, helping the model both choose the right images and use them well. We release code and data at https://github.com/czh24/R3G.
