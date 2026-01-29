# Latent Structural Similarity Networks for Unsupervised Discovery in Multivariate Time Series

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.18803)

## 요약
arXiv:2601.18803v1 Announce Type: new
Abstract: This paper proposes a task-agnostic discovery layer for multivariate time series that constructs a relational hypothesis graph over entities without assuming linearity, stationarity, or a downstream objective. The method learns window-level sequence representations using an unsupervised sequence-to-sequence autoencoder, aggregates these representations into entity-level embeddings, and induces a sparse similarity network by thresholding a latent-space similarity measure. This network is intended as an analyzable abstraction that compresses the pairwise search space and exposes candidate relationships for further investigation, rather than as a model optimized for prediction, trading, or any decision rule. The framework is demonstrated on a challenging real-world dataset of hourly cryptocurrency returns, illustrating how latent similarity induces coherent network structure; a classical econometric relation is also reported as an external diagnostic lens to contextualize discovered edges.
