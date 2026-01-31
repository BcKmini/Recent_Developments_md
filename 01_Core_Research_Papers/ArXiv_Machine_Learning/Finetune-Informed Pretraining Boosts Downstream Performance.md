# Finetune-Informed Pretraining Boosts Downstream Performance

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.20884)

## 요약
arXiv:2601.20884v1 Announce Type: new
Abstract: Multimodal pretraining is effective for building general-purpose representations, but in many practical deployments, only one modality is heavily used during downstream fine-tuning. Standard pretraining strategies treat all modalities uniformly, which can lead to under-optimized representations for the modality that actually matters. We propose Finetune-Informed Pretraining (FIP), a model-agnostic method that biases representation learning toward a designated target modality needed at fine-tuning time. FIP combines higher masking difficulty, stronger loss weighting, and increased decoder capacity for the target modality, without modifying the shared encoder or requiring additional supervision. When applied to masked modeling on constellation diagrams for wireless signals, FIP consistently improves downstream fine-tuned performance with no extra data or compute. FIP is simple to implement, architecture-compatible, and broadly applicable across multimodal masked modeling pipelines.
