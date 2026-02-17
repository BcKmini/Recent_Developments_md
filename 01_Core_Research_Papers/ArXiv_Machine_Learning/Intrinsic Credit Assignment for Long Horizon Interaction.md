# Intrinsic Credit Assignment for Long Horizon Interaction

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.12342)

## 요약
arXiv:2602.12342v1 Announce Type: new
Abstract: How can we train agents to navigate uncertainty over long horizons? In this work, we propose {\Delta}Belief-RL, which leverages a language model's own intrinsic beliefs to reward intermediate progress. Our method utilizes the change in the probability an agent assigns to the target solution for credit assignment. By training on synthetic interaction data, {\Delta}Belief-RL teaches information-seeking capabilities that consistently outperform purely outcome-based rewards for Reinforcement Learning, with improvements generalizing to out-of-distribution applications ranging from customer service to personalization. Notably, the performance continues to improve as we scale test-time interactions beyond the training horizon, with interaction-efficiency increasing even on Pass@k metrics. Overall, our work introduces a scalable training strategy for navigating uncertainty over a long-horizon, by enabling credit assignment to intermediate actions via intrinsic {\Delta}Belief rewards.
