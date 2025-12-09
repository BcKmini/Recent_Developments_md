# Variance Matters: Improving Domain Adaptation via Stratified Sampling

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.05226)

## 요약
arXiv:2512.05226v1 Announce Type: new
Abstract: Domain shift remains a key challenge in deploying machine learning models to the real world. Unsupervised domain adaptation (UDA) aims to address this by minimising domain discrepancy during training, but the discrepancy estimates suffer from high variance in stochastic settings, which can stifle the theoretical benefits of the method. This paper proposes Variance-Reduced Domain Adaptation via Stratified Sampling (VaRDASS), the first specialised stochastic variance reduction technique for UDA. We consider two specific discrepancy measures -- correlation alignment and the maximum mean discrepancy (MMD) -- and derive ad hoc stratification objectives for these terms. We then present expected and worst-case error bounds, and prove that our proposed objective for the MMD is theoretically optimal (i.e., minimises the variance) under certain assumptions. Finally, a practical k-means style optimisation algorithm is introduced and analysed. Experiments on three domain shift datasets demonstrate improved discrepancy estimation accuracy and target domain performance.
