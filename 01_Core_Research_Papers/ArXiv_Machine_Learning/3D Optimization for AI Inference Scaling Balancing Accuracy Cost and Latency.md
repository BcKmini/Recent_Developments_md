# 3D Optimization for AI Inference Scaling: Balancing Accuracy, Cost, and Latency

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.18905)

## 요약
arXiv:2510.18905v1 Announce Type: new
Abstract: AI inference scaling is often tuned through 1D heuristics (a fixed reasoning passes) or 2D bivariate trade-offs (e.g., performance vs. compute), which fail to consider cost and latency constraints. We introduce a 3D optimization framework that jointly calibrates accuracy, cost, and latency within a unified decision space, enabling constraints-aware inference scaling. Using Monte Carlo simulations across three representative scenarios and nine simulated large language models, we evaluate four optimization methods to address the 3D multi-objective optimization (MOO) problem. Framing inference scaling in MOO shapes a feasible space that 1D and 2D optimizations fail to capture, enabling environmentadaptive selection of the inference scaling k. Results show that knee-point optimization achieves the best balance, while accuracy-maximization remains favorable when precision is prioritized. The framework establishes a theoretical foundation for deployment-aware inference scaling across diverse operational contexts.
