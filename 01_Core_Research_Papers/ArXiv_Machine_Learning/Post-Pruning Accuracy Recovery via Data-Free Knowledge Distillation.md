# Post-Pruning Accuracy Recovery via Data-Free Knowledge Distillation

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.20702)

## 요약
arXiv:2511.20702v1 Announce Type: new
Abstract: Model pruning is a widely adopted technique to reduce the computational complexity and memory footprint of Deep Neural Networks (DNNs). However, global unstructured pruning often leads to significant degradation in accuracy, typically necessitating fine-tuning on the original training dataset to recover performance. In privacy-sensitive domains such as healthcare or finance, access to the original training data is often restricted post-deployment due to regulations (e.g., GDPR, HIPAA). This paper proposes a Data-Free Knowledge Distillation framework to bridge the gap between model compression and data privacy. We utilize DeepInversion to synthesize privacy-preserving ``dream'' images from the pre-trained teacher model by inverting Batch Normalization (BN) statistics. These synthetic images serve as a transfer set to distill knowledge from the original teacher to the pruned student network. Experimental results on CIFAR-10 across various architectures (ResNet, MobileNet, VGG) demonstrate that our method significantly recovers accuracy lost during pruning without accessing a single real data point.
