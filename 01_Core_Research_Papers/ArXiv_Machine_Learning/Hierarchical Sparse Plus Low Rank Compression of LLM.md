# Hierarchical Sparse Plus Low Rank Compression of LLM

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.07839)

## 요약
arXiv:2601.07839v1 Announce Type: new
Abstract: Modern large language models (LLMs) place extraordinary pressure on memory and compute budgets, making principled compression indispensable for both deployment and continued training. We present Hierarchical Sparse Plus Low-Rank (HSS) compression, a two-stage scheme that (i) removes the largest-magnitude weights into a sparse matrix S and (ii) applies a recursive Hierarchically Sparse Separable (HSS) low-rank factorisation to the dense residual matrix. A recursive rank-reducing strategy and a reverse Cuthill-Mckee (RCM) permutation are introduced to align high weights towards the diagonal with the block-diagonal hierarchy, maximising off-diagonal compressibility (because they are touched only once). HSS is hardware-friendly: its matrix-vector multiply reduces to one sparse and a sequence of thin-matrix multiplications and can be trained end-to-end with standard optimisers.
Experiments on LLaMA-7B show that targeting only the self-attention projections (1.6 B parameters of Q, K, and V matrices out of a total 7B parameters) suffices to yield large memory savings while retaining comparable state-of-the-art perplexity scores on test samples of the WikiText dataset. For example, with a 30\% sparsity budget and an outer rank of 512, sHSS-RCM achieves a perplexity of 1.64, outperforming dense baselines and classical sparse-plus-SVD variants, while also achieving significant memory savings.
