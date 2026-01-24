# You Need Better Attention Priors

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.15380)

## 요약
arXiv:2601.15380v1 Announce Type: new
Abstract: We generalize the attention mechanism by viewing it through the lens of Entropic Optimal Transport, revealing that standard attention corresponds to a transport problem regularized by an implicit uniform prior. We introduce Generalized Optimal transport Attention with Trainable priors (GOAT), a new attention mechanism that replaces this naive assumption with a learnable, continuous prior. This prior maintains full compatibility with optimized kernels such as FlashAttention. GOAT also provides an EOT-based explanation of attention sinks and materializes a solution for them, avoiding the representational trade-offs of standard attention. Finally, by absorbing spatial information into the core attention computation, GOAT learns an extrapolatable prior that combines the flexibility of learned positional embeddings with the length generalization of fixed encodings.
