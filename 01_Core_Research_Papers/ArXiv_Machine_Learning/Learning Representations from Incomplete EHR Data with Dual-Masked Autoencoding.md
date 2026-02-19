# Learning Representations from Incomplete EHR Data with Dual-Masked Autoencoding

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.15159)

## 요약
arXiv:2602.15159v1 Announce Type: new
Abstract: Learning from electronic health records (EHRs) time series is challenging due to irregular sam- pling, heterogeneous missingness, and the resulting sparsity of observations. Prior self-supervised meth- ods either impute before learning, represent missingness through a dedicated input signal, or optimize solely for imputation, reducing their capacity to efficiently learn representations that support clinical downstream tasks. We propose the Augmented-Intrinsic Dual-Masked Autoencoder (AID-MAE), which learns directly from incomplete time series by applying an intrinsic missing mask to represent naturally missing values and an augmented mask that hides a subset of observed values for reconstruction during training. AID-MAE processes only the unmasked subset of tokens and consistently outperforms strong baselines, including XGBoost and DuETT, across multiple clinical tasks on two datasets. In addition, the learned embeddings naturally stratify patient cohorts in the representation space.
