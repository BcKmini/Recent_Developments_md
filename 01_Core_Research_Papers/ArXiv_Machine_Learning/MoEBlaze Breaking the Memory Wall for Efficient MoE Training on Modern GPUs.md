# MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.05296)

## 요약
arXiv:2601.05296v1 Announce Type: new
Abstract: The pervasive "memory wall" bottleneck is significantly amplified in modern large-scale Mixture-of-Experts (MoE) architectures. MoE's inherent architectural sparsity leads to sparse arithmetic compute and also introduces substantial activation memory overheads -- driven by large token routing buffers and the need to materialize and buffer intermediate tensors. This memory pressure limits the maximum batch size and sequence length that can fit on GPUs, and also results in excessive data movements that hinders performance and efficient model scaling. We present MoEBlaze, a memory-efficient MoE training framework that addresses these issues through a co-designed system approach: (i) an end-to-end token dispatch and MoE training method with optimized data structures to eliminate intermediate buffers and activation materializing, and (ii) co-designed kernels with smart activation checkpoint to mitigate memory footprint while simultaneously achieving better performance. We demonstrate that MoEBlaze can achieve over 4x speedups and over 50% memory savings compared to existing MoE frameworks.
