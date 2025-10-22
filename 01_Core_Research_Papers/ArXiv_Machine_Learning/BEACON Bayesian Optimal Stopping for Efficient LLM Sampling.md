# BEACON: Bayesian Optimal Stopping for Efficient LLM Sampling

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.15945)

## 요약
arXiv:2510.15945v1 Announce Type: new
Abstract: Sampling multiple responses is a common way to improve LLM output quality, but it comes at the cost of additional computation. The key challenge is deciding when to stop generating new samples to balance accuracy gains against efficiency. To address this, we introduce BEACON (Bayesian Efficient Adaptive Criterion for Optimal N-stopping), a principled adaptive sampling framework grounded in Sequential Search with Bayesian Learning. BEACON sequentially generates responses from the policy LLM, updates posterior belief over reward distributions in real time without further training, and determines when to stop by weighing expected gains against computational cost. Sampling terminates once the marginal utility of further exploration no longer justifies the expense. We establish both theoretical optimality guarantees and practical tractability, and show empirically that BEACON reduces average sampling by up to 80% while maintaining response quality. We further demonstrate BEACON's utility for cost-efficient preference data generation and outline practical extensions, offering actionable insights for future researchers.
