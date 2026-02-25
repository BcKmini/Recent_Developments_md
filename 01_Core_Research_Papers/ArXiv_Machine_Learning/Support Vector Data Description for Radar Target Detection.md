# Support Vector Data Description for Radar Target Detection

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.18486)

## 요약
arXiv:2602.18486v1 Announce Type: new
Abstract: Classical radar detection techniques rely on adaptive detectors that estimate the noise covariance matrix from target-free secondary data. While effective in Gaussian environments, these methods degrade in the presence of clutter, which is better modeled by heavy-tailed distributions such as the Complex Elliptically Symmetric (CES) and Compound-Gaussian (CGD) families. Robust covariance estimators like M-estimators or Tyler's estimator address this issue, but still struggle when thermal noise combines with clutter. To overcome these challenges, we investigate the use of Support Vector Data Description (SVDD) and its deep extension, Deep SVDD, for target detection. These one-class learning methods avoid direct noise covariance estimation and are adapted here as CFAR detectors. We propose two novel SVDD-based detection algorithms and demonstrate their effectiveness on simulated radar data.
