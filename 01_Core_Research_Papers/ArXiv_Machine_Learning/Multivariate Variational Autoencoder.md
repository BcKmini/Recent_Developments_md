# Multivariate Variational Autoencoder

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.07472)

## 요약
arXiv:2511.07472v1 Announce Type: new
Abstract: We present the Multivariate Variational Autoencoder (MVAE), a VAE variant that preserves Gaussian tractability while lifting the diagonal posterior restriction. MVAE factorizes each posterior covariance, where a \emph{global} coupling matrix $\mathbf{C}$ induces dataset-wide latent correlations and \emph{per-sample} diagonal scales modulate local uncertainty. This yields a full-covariance family with analytic KL and an efficient reparameterization via $\mathbf{L}=\mathbf{C}\mathrm{diag}(\boldsymbol{\sigma})$. Across Larochelle-style MNIST variants, Fashion-MNIST, CIFAR-10, and CIFAR-100, MVAE consistently matches or improves reconstruction (MSE~$\downarrow$) and delivers robust gains in calibration (NLL/Brier/ECE~$\downarrow$) and unsupervised structure (NMI/ARI~$\uparrow$) relative to diagonal-covariance VAEs with matched capacity, especially at mid-range latent sizes. Latent-plane visualizations further indicate smoother, more coherent factor traversals and sharper local detail. We release a fully reproducible implementation with training/evaluation scripts and sweep utilities to facilitate fair comparison and reuse.
