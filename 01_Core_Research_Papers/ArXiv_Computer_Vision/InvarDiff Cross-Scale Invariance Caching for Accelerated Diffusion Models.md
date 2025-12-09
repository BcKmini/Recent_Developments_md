# InvarDiff: Cross-Scale Invariance Caching for Accelerated Diffusion Models

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.05134)

## 요약
arXiv:2512.05134v1 Announce Type: new
Abstract: Diffusion models deliver high-fidelity synthesis but remain slow due to iterative sampling. We empirically observe there exists feature invariance in deterministic sampling, and present InvarDiff, a training-free acceleration method that exploits the relative temporal invariance across timestep-scale and layer-scale. From a few deterministic runs, we compute a per-timestep, per-layer, per-module binary cache plan matrix and use a re-sampling correction to avoid drift when consecutive caches occur. Using quantile-based change metrics, this matrix specifies which module at which step is reused rather than recomputed. The same invariance criterion is applied at the step scale to enable cross-timestep caching, deciding whether an entire step can reuse cached results. During inference, InvarDiff performs step-first and layer-wise caching guided by this matrix. When applied to DiT and FLUX, our approach reduces redundant compute while preserving fidelity. Experiments show that InvarDiff achieves $2$-$3\times$ end-to-end speed-ups with minimal impact on standard quality metrics. Qualitatively, we observe almost no degradation in visual quality compared with full computations.
