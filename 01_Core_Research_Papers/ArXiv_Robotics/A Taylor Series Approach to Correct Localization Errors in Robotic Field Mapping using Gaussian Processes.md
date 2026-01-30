# A Taylor Series Approach to Correct Localization Errors in Robotic Field Mapping using Gaussian Processes

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.20149)

## 요약
arXiv:2601.20149v1 Announce Type: new
Abstract: Gaussian Processes (GPs) are powerful non-parametric Bayesian models for regression of scalar fields, formulated under the assumption that measurement locations are perfectly known and the corresponding field measurements have Gaussian noise. However, many real-world scalar field mapping applications rely on sensor-equipped mobile robots to collect field measurements, where imperfect localization introduces state uncertainty. Such discrepancies between the estimated and true measurement locations degrade GP mean and covariance estimates. To address this challenge, we propose a method for updating the GP models when improved estimates become available. Leveraging the differentiability of the kernel function, a second-order correction algorithm is developed using the precomputed Jacobians and Hessians of the GP mean and covariance functions for real-time refinement based on measurement location discrepancy data. Simulation results demonstrate improved prediction accuracy and computational efficiency compared to full model retraining.
