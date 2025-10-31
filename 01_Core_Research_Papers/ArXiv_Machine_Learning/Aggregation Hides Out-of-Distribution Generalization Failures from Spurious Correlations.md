# Aggregation Hides Out-of-Distribution Generalization Failures from Spurious Correlations

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.24884)

## 요약
arXiv:2510.24884v1 Announce Type: new
Abstract: Benchmarks for out-of-distribution (OOD) generalization frequently show a strong positive correlation between in-distribution (ID) and OOD accuracy across models, termed "accuracy-on-the-line." This pattern is often taken to imply that spurious correlations - correlations that improve ID but reduce OOD performance - are rare in practice. We find that this positive correlation is often an artifact of aggregating heterogeneous OOD examples. Using a simple gradient-based method, OODSelect, we identify semantically coherent OOD subsets where accuracy on the line does not hold. Across widely used distribution shift benchmarks, the OODSelect uncovers subsets, sometimes over half of the standard OOD set, where higher ID accuracy predicts lower OOD accuracy. Our findings indicate that aggregate metrics can obscure important failure modes of OOD robustness. We release code and the identified subsets to facilitate further research.
