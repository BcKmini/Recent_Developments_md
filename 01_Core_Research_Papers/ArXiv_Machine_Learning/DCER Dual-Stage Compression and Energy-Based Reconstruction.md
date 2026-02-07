# DCER: Dual-Stage Compression and Energy-Based Reconstruction

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.04904)

## 요약
arXiv:2602.04904v1 Announce Type: new
Abstract: Multimodal fusion faces two robustness challenges: noisy inputs degrade representation quality, and missing modalities cause prediction failures. We propose DCER, a
unified framework addressing both challenges through dual-stage compression and energy-based reconstruction. The compression stage operates at two levels:
within-modality frequency transforms (wavelet for audio, DCT for video) remove noise while preserving task-relevant patterns, and cross-modality bottleneck tokens
force genuine integration rather than modality-specific shortcuts. For missing modalities, energy-based reconstruction recovers representations via gradient descent
on a learned energy function, with the final energy providing intrinsic uncertainty quantification (\r{ho} > 0.72 correlation with prediction error). Experiments on
CMU-MOSI, CMU-MOSEI, and CH-SIMS demonstrate state-of-the-art performance across all benchmarks, with a U-shaped robustness pattern favoring multimodal fusion at
both complete and high-missing conditions. The code will be available on Github.
