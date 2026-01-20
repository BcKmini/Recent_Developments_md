# Towards Tensor Network Models for Low-Latency Jet Tagging on FPGAs

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.10801)

## 요약
arXiv:2601.10801v1 Announce Type: new
Abstract: We present a systematic study of Tensor Network (TN) models $\unicode{x2013}$ Matrix Product States (MPS) and Tree Tensor Networks (TTN) $\unicode{x2013}$ for real-time jet tagging in high-energy physics, with a focus on low-latency deployment on Field Programmable Gate Arrays (FPGAs). Motivated by the strict requirements of the HL-LHC Level-1 trigger system, we explore TNs as compact and interpretable alternatives to deep neural networks. Using low-level jet constituent features, our models achieve competitive performance compared to state-of-the-art deep learning classifiers. We investigate post-training quantization to enable hardware-efficient implementations without degrading classification performance or latency. The best-performing models are synthesized to estimate FPGA resource usage, latency, and memory occupancy, demonstrating sub-microsecond latency and supporting the feasibility of online deployment in real-time trigger systems. Overall, this study highlights the potential of TN-based models for fast and resource-efficient inference in low-latency environments.
