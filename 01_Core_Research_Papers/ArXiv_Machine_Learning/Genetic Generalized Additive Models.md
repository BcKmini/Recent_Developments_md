# Genetic Generalized Additive Models

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.15877)

## 요약
arXiv:2602.15877v1 Announce Type: new
Abstract: Generalized Additive Models (GAMs) balance predictive accuracy and interpretability, but manually configuring their structure is challenging. We propose using the multi-objective genetic algorithm NSGA-II to automatically optimize GAMs, jointly minimizing prediction error (RMSE) and a Complexity Penalty that captures sparsity, smoothness, and uncertainty. Experiments on the California Housing dataset show that NSGA-II discovers GAMs that outperform baseline LinearGAMs in accuracy or match performance with substantially lower complexity. The resulting models are simpler, smoother, and exhibit narrower confidence intervals, enhancing interpretability. This framework provides a general approach for automated optimization of transparent, high-performing models. The code can be found at https://github.com/KaaustaaubShankar/GeneticAdditiveModels.
