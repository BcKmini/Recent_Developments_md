# Lagged backward-compatible physics-informed neural networks for unsaturated soil consolidation analysis

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.07031)

## 요약
arXiv:2602.07031v1 Announce Type: new
Abstract: This study develops a Lagged Backward-Compatible Physics-Informed Neural Network (LBC-PINN) for simulating and inverting one-dimensional unsaturated soil consolidation under long-term loading. To address the challenges of coupled air and water pressure dissipation across multi-scale time domains, the framework integrates logarithmic time segmentation, lagged compatibility loss enforcement, and segment-wise transfer learning.
In forward analysis, the LBC-PINN with recommended segmentation schemes accurately predicts pore air and pore water pressure evolution. Model predictions are validated against finite element method (FEM) results, with mean absolute errors below 1e-2 for time durations up to 1e10 seconds. A simplified segmentation strategy based on the characteristic air-phase dissipation time improves computational efficiency while preserving predictive accuracy. Sensitivity analyses confirm the robustness of the framework across air-to-water permeability ratios ranging from 1e-3 to 1e3.
