# Hierarchical Informative Path Planning via Graph Guidance and Trajectory Optimization

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.17227)

## 요약
arXiv:2601.17227v1 Announce Type: new
Abstract: We study informative path planning (IPP) with travel budgets in cluttered environments, where an agent collects measurements of a latent field modeled as a Gaussian process (GP) to reduce uncertainty at target locations. Graph-based solvers provide global guarantees but assume pre-selected measurement locations, while continuous trajectory optimization supports path-based sensing but is computationally intensive and sensitive to initialization in obstacle-dense settings. We propose a hierarchical framework with three stages: (i) graph-based global planning, (ii) segment-wise budget allocation using geometric and kernel bounds, and (iii) spline-based refinement of each segment with hard constraints and obstacle pruning. By combining global guidance with local refinement, our method achieves lower posterior uncertainty than graph-only and continuous baselines, while running faster than continuous-space solvers (up to 9x faster than gradient-based methods and 20x faster than black-box optimizers) across synthetic cluttered environments and Arctic datasets.
