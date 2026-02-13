# Signature-Kernel Based Evaluation Metrics for Robust Probabilistic and Tail-Event Forecasting

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.10182)

## 요약
arXiv:2602.10182v1 Announce Type: new
Abstract: Probabilistic forecasting is increasingly critical across high-stakes domains, from finance and epidemiology to climate science. However, current evaluation frameworks lack a consensus metric and suffer from two critical flaws: they often assume independence across time steps or variables, and they demonstrably lack sensitivity to tail events, the very occurrences that are most pivotal in real-world decision-making. To address these limitations, we propose two kernel-based metrics: the signature maximum mean discrepancy (Sig-MMD) and our novel censored Sig-MMD (CSig-MMD). By leveraging the signature kernel, these metrics capture complex inter-variate and inter-temporal dependencies and remain robust to missing data. Furthermore, CSig-MMD introduces a censoring scheme that prioritizes a forecaster's capability to predict tail events while strictly maintaining properness, a vital property for a good scoring rule. These metrics enable a more reliable evaluation of direct multi-step forecasting, facilitating the development of more robust probabilistic algorithms.
