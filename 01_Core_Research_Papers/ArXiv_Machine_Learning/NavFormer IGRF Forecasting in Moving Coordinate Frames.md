# NavFormer: IGRF Forecasting in Moving Coordinate Frames

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.18800)

## 요약
arXiv:2601.18800v1 Announce Type: new
Abstract: Triad magnetometer components change with sensor attitude even when the IGRF total intensity target stays invariant. NavFormer forecasts this invariant target with rotation invariant scalar features and a Canonical SPD module that stabilizes the spectrum of window level second moments of the triads without sign discontinuities. The module builds a canonical frame from a Gram matrix per window and applies state dependent spectral scaling in the original coordinates. Experiments across five flights show lower error than strong baselines in standard training, few shot training, and zero shot transfer. The code is available at: https://anonymous.4open.science/r/NavFormer-Robust-IGRF-Forecasting-for-Autonomous-Navigators-0765
