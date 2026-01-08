# mHC-GNN: Manifold-Constrained Hyper-Connections for Graph Neural Networks

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.02451)

## 요약
arXiv:2601.02451v1 Announce Type: new
Abstract: Graph Neural Networks (GNNs) suffer from over-smoothing in deep architectures and expressiveness bounded by the 1-Weisfeiler-Leman (1-WL) test. We adapt Manifold-Constrained Hyper-Connections (\mhc)~\citep{xie2025mhc}, recently proposed for Transformers, to graph neural networks. Our method, mHC-GNN, expands node representations across $n$ parallel streams and constrains stream-mixing matrices to the Birkhoff polytope via Sinkhorn-Knopp normalization. We prove that mHC-GNN exhibits exponentially slower over-smoothing (rate $(1-\gamma)^{L/n}$ vs.\ $(1-\gamma)^L$) and can distinguish graphs beyond 1-WL. Experiments on 10 datasets with 4 GNN architectures show consistent improvements. Depth experiments from 2 to 128 layers reveal that standard GNNs collapse to near-random performance beyond 16 layers, while mHC-GNN maintains over 74\% accuracy even at 128 layers, with improvements exceeding 50 percentage points at extreme depths. Ablations confirm that the manifold constraint is essential: removing it causes up to 82\% performance degradation. Code is available at \href{https://github.com/smlab-niser/mhc-gnn}{https://github.com/smlab-niser/mhc-gnn}
