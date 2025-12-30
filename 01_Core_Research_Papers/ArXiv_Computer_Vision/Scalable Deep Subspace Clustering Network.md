# Scalable Deep Subspace Clustering Network

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.21434)

## 요약
arXiv:2512.21434v1 Announce Type: new
Abstract: Subspace clustering methods face inherent scalability limits due to the $O(n^3)$ cost (with $n$ denoting the number of data samples) of constructing full $n\times n$ affinities and performing spectral decomposition. While deep learning-based approaches improve feature extraction, they maintain this computational bottleneck through exhaustive pairwise similarity computations. We propose SDSNet (Scalable Deep Subspace Network), a deep subspace clustering framework that achieves $\mathcal{O}(n)$ complexity through (1) landmark-based approximation, avoiding full affinity matrices, (2) joint optimization of auto-encoder reconstruction with self-expression objectives, and (3) direct spectral clustering on factorized representations. The framework combines convolutional auto-encoders with subspace-preserving constraints. Experimental results demonstrate that SDSNet achieves comparable clustering quality to state-of-the-art methods with significantly improved computational efficiency.
