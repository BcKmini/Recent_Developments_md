# Variational Physics-Informed Ansatz for Reconstructing Hidden Interaction Networks from Steady States

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.13708)

## 요약
arXiv:2512.13708v1 Announce Type: new
Abstract: The interaction structure of a complex dynamical system governs its collective behavior, yet existing reconstruction methods struggle with nonlinear, heterogeneous, and higher-order couplings, especially when only steady states are observable. We propose a Variational Physics-Informed Ansatz (VPIA) that infers general interaction operators directly from heterogeneous steady-state data. VPIA embeds the steady-state constraints of the dynamics into a differentiable variational representation and reconstructs the underlying couplings by minimizing a physics-derived steady-state residual, without requiring temporal trajectories, derivative estimation, or supervision. Residual sampling combined with natural-gradient optimization enables scalable learning of large and higher-order networks. Across diverse nonlinear systems, VPIA accurately recovers directed, weighted, and multi-body structures under substantial noise, providing a unified and robust framework for physics-constrained inference of complex interaction networks in settings where only snapshot observations are available.
