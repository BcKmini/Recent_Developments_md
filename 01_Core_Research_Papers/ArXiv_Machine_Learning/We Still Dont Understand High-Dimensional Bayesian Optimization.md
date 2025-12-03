# We Still Don't Understand High-Dimensional Bayesian Optimization

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.00170)

## 요약
arXiv:2512.00170v1 Announce Type: new
Abstract: High-dimensional spaces have challenged Bayesian optimization (BO). Existing methods aim to overcome this so-called curse of dimensionality by carefully encoding structural assumptions, from locality to sparsity to smoothness, into the optimization procedure. Surprisingly, we demonstrate that these approaches are outperformed by arguably the simplest method imaginable: Bayesian linear regression. After applying a geometric transformation to avoid boundary-seeking behavior, Gaussian processes with linear kernels match state-of-the-art performance on tasks with 60- to 6,000-dimensional search spaces. Linear models offer numerous advantages over their non-parametric counterparts: they afford closed-form sampling and their computation scales linearly with data, a fact we exploit on molecular optimization tasks with > 20,000 observations. Coupled with empirical analyses, our results suggest the need to depart from past intuitions about BO methods in high-dimensional spaces.
