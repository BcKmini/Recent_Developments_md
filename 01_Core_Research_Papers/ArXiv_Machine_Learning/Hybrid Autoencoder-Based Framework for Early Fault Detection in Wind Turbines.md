# Hybrid Autoencoder-Based Framework for Early Fault Detection in Wind Turbines

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.15010)

## 요약
arXiv:2510.15010v1 Announce Type: new
Abstract: Wind turbine reliability is critical to the growing renewable energy sector, where early fault detection significantly reduces downtime and maintenance costs. This paper introduces a novel ensemble-based deep learning framework for unsupervised anomaly detection in wind turbines. The method integrates Variational Autoencoders (VAE), LSTM Autoencoders, and Transformer architectures, each capturing different temporal and contextual patterns from high-dimensional SCADA data. A unique feature engineering pipeline extracts temporal, statistical, and frequency-domain indicators, which are then processed by the deep models. Ensemble scoring combines model predictions, followed by adaptive thresholding to detect operational anomalies without requiring labeled fault data. Evaluated on the CARE dataset containing 89 years of real-world turbine data across three wind farms, the proposed method achieves an AUC-ROC of 0.947 and early fault detection up to 48 hours prior to failure. This approach offers significant societal value by enabling predictive maintenance, reducing turbine failures, and enhancing operational efficiency in large-scale wind energy deployments.
