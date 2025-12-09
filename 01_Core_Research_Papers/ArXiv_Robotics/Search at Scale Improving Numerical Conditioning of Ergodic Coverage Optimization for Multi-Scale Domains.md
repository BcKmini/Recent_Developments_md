# Search at Scale: Improving Numerical Conditioning of Ergodic Coverage Optimization for Multi-Scale Domains

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.05229)

## 요약
arXiv:2512.05229v1 Announce Type: new
Abstract: Recent methods in ergodic coverage planning have shown promise as tools that can adapt to a wide range of geometric coverage problems with general constraints, but are highly sensitive to the numerical scaling of the problem space. The underlying challenge is that the optimization formulation becomes brittle and numerically unstable with changing scales, especially under potentially nonlinear constraints that impose dynamic restrictions, due to the kernel-based formulation. This paper proposes to address this problem via the development of a scale-agnostic and adaptive ergodic coverage optimization method based on the maximum mean discrepancy metric (MMD). Our approach allows the optimizer to solve for the scale of differential constraints while annealing the hyperparameters to best suit the problem domain and ensure physical consistency. We also derive a variation of the ergodic metric in the log space, providing additional numerical conditioning without loss of performance. We compare our approach with existing coverage planning methods and demonstrate the utility of our approach on a wide range of coverage problems.
