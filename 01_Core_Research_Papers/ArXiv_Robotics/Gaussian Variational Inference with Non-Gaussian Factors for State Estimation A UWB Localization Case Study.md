# Gaussian Variational Inference with Non-Gaussian Factors for State Estimation: A UWB Localization Case Study

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.19855)

## 요약
arXiv:2512.19855v1 Announce Type: new
Abstract: This letter extends the exactly sparse Gaussian variational inference (ESGVI) algorithm for state estimation in two complementary directions. First, ESGVI is generalized to operate on matrix Lie groups, enabling the estimation of states with orientation components while respecting the underlying group structure. Second, factors are introduced to accommodate heavy-tailed and skewed noise distributions, as commonly encountered in ultra-wideband (UWB) localization due to non-line-of-sight (NLOS) and multipath effects. Both extensions are shown to integrate naturally within the ESGVI framework while preserving its sparse and derivative-free structure. The proposed approach is validated in a UWB localization experiment with NLOS-rich measurements, demonstrating improved accuracy and comparable consistency. Finally, a Python implementation within a factor-graph-based estimation framework is made open-source (https://github.com/decargroup/gvi\_ws) to support broader research use.
