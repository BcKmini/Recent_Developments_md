# The Double-Edged Nature of the Rashomon Set for Trustworthy Machine Learning

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.21799)

## 요약
arXiv:2511.21799v1 Announce Type: new
Abstract: Real-world machine learning (ML) pipelines rarely produce a single model; instead, they produce a Rashomon set of many near-optimal ones. We show that this multiplicity reshapes key aspects of trustworthiness. At the individual-model level, sparse interpretable models tend to preserve privacy but are fragile to adversarial attacks. In contrast, the diversity within a large Rashomon set enables reactive robustness: even when an attack breaks one model, others often remain accurate. Rashomon sets are also stable under small distribution shifts. However, this same diversity increases information leakage, as disclosing more near-optimal models provides an attacker with progressively richer views of the training data. Through theoretical analysis and empirical studies of sparse decision trees and linear models, we characterize this robustness-privacy trade-off and highlight the dual role of Rashomon sets as both a resource and a risk for trustworthy ML.
