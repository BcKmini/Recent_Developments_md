# SHARe-KAN: Holographic Vector Quantization for Memory-Bound Inference

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.15742)

## 요약
arXiv:2512.15742v1 Announce Type: new
Abstract: Kolmogorov-Arnold Networks (KANs) face a fundamental memory wall: their learned basis functions create parameter counts that impose extreme bandwidth demands, hindering deployment in memory-constrained environments. We show that Vision KANs exhibit a holographic topology, where information is distributed across the interference of splines rather than localized to specific edges. Consequently, traditional pruning fails (10% sparsity degrades mAP from 85.23% to 45%, a $\sim$40-point drop). To address this, we present SHARe-KAN, a framework utilizing Gain-Shape-Bias Vector Quantization to exploit functional redundancy while preserving the dense topology. Coupled with LUTHAM, a hardware-aware compiler with static memory planning, we achieve $88\times$ runtime memory reduction (1.13 GB $\to$ 12.91 MB) and match uncompressed baseline accuracy on PASCAL VOC. Profiling on NVIDIA Ampere architecture confirms $>90\%$ L2 cache residency, demonstrating that the workload is decoupled from DRAM bandwidth constraints inherent to spline-based architectures.
