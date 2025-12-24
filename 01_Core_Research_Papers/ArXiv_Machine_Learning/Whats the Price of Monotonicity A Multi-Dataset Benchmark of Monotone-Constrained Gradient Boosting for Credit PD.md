# What's the Price of Monotonicity? A Multi-Dataset Benchmark of Monotone-Constrained Gradient Boosting for Credit PD

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.17945)

## 요약
arXiv:2512.17945v1 Announce Type: new
Abstract: Financial institutions face a trade-off between predictive accuracy and interpretability when deploying machine learning models for credit risk. Monotonicity constraints align model behavior with domain knowledge, but their performance cost - the price of monotonicity - is not well quantified. This paper benchmarks monotone-constrained versus unconstrained gradient boosting models for credit probability of default across five public datasets and three libraries. We define the Price of Monotonicity (PoM) as the relative change in standard performance metrics when moving from unconstrained to constrained models, estimated via paired comparisons with bootstrap uncertainty. In our experiments, PoM in AUC ranges from essentially zero to about 2.9 percent: constraints are almost costless on large datasets (typically less than 0.2 percent, often indistinguishable from zero) and most costly on smaller datasets with extensive constraint coverage (around 2-3 percent). Thus, appropriately specified monotonicity constraints can often deliver interpretability with small accuracy losses, particularly in large-scale credit portfolios.
