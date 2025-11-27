# WavefrontDiffusion: Dynamic Decoding Schedule or Improved Reasoning

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.19473)

## 요약
arXiv:2511.19473v1 Announce Type: new
Abstract: Diffusion Language Models (DLMs) have shown strong potential for text generation and are becoming a competitive alternative to autoregressive models. The denoising strategy plays an important role in determining the quality of their outputs. Mainstream denoising strategies include Standard Diffusion and BlockDiffusion. Standard Diffusion performs global denoising without restricting the update range, often finalizing incomplete context and causing premature end-of-sequence predictions. BlockDiffusion updates fixed-size blocks in a preset order, but its rigid structure can break apart coherent semantic units and disrupt reasoning. We present WavefrontDiffusion, a dynamic decoding approach that expands a wavefront of active tokens outward from finalized positions. This adaptive process follows the natural flow of semantic structure while keeping computational cost equal to block-based methods. Across four benchmarks in reasoning and code generation, WavefrontDiffusion achieves state-of-the-art performance while producing outputs with higher semantic fidelity, showing the value of adaptive scheduling for more coherent and efficient generation.
