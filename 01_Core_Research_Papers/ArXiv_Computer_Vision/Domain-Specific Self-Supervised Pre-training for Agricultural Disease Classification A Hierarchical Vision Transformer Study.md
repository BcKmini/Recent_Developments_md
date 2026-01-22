# Domain-Specific Self-Supervised Pre-training for Agricultural Disease Classification: A Hierarchical Vision Transformer Study

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.11612)

## 요약
arXiv:2601.11612v1 Announce Type: new
Abstract: We investigate the impact of domain-specific self-supervised pre-training on agricultural disease classification using hierarchical vision transformers. Our key finding is that SimCLR pre-training on just 3,000 unlabeled agricultural images provides a +4.57% accuracy improvement--exceeding the +3.70% gain from hierarchical architecture design. Critically, we show this SSL benefit is architecture-agnostic: applying the same pre-training to Swin-Base yields +4.08%, to ViT-Base +4.20%, confirming practitioners should prioritize domain data collection over architectural choices. Using HierarchicalViT (HVT), a Swin-style hierarchical transformer, we evaluate on three datasets: Cotton Leaf Disease (7 classes, 90.24%), PlantVillage (38 classes, 96.3%), and PlantDoc (27 classes, 87.1%). At matched parameter counts, HVT-Base (78M) achieves 88.91% vs. Swin-Base (88M) at 87.23%, a +1.68% improvement. For deployment reliability, we report calibration analysis showing HVT achieves 3.56% ECE (1.52% after temperature scaling). Code: https://github.com/w2sg-arnav/HierarchicalViT
