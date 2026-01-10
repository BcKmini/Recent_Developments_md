# Green MLOps: Closed-Loop, Energy-Aware Inference with NVIDIA Triton, FastAPI, and Bio-Inspired Thresholding

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.04250)

## 요약
arXiv:2601.04250v1 Announce Type: new
Abstract: Energy efficiency is a first-order concern in AI deployment, as long-running inference can exceed training in cumulative carbon impact. We propose a bio-inspired framework that maps protein-folding energy basins to inference cost landscapes and controls execution via a decaying, closed-loop threshold. A request is admitted only when the expected utility-to-energy trade-off is favorable (high confidence/utility at low marginal energy and congestion), biasing operation toward the first acceptable local basin rather than pursuing costly global minima. We evaluate DistilBERT and ResNet-18 served through FastAPI with ONNX Runtime and NVIDIA Triton on an RTX 4000 Ada GPU. Our ablation study reveals that the bio-controller reduces processing time by 42% compared to standard open-loop execution (0.50s vs 0.29s on A100 test set), with a minimal accuracy degradation (<0.5%). Furthermore, we establish the efficiency boundaries between lightweight local serving (ORT) and managed batching (Triton). The results connect biophysical energy models to Green MLOps and offer a practical, auditable basis for closed-loop energy-aware inference in production.
