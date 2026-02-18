# Inferring Turn-Rate-Limited Engagement Zones with Sacrificial Agents for Safe Trajectory Planning

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.13457)

## 요약
arXiv:2602.13457v1 Announce Type: new
Abstract: This paper presents a learning-based framework for estimating pursuer parameters in turn-rate-limited pursuit-evasion scenarios using sacrificial agents. Each sacrificial agent follows a straight-line trajectory toward an adversary and reports whether it was intercepted or survived. These binary outcomes are related to the pursuer's parameters through a geometric reachable-region (RR) model. Two formulations are introduced: a boundary-interception case, where capture occurs at the RR boundary, and an interior-interception case, which allows capture anywhere within it. The pursuer's parameters are inferred using a gradient-based multi-start optimization with custom loss functions tailored to each case.
Two trajectory-selection strategies are proposed for the sacrificial agents: a geometric heuristic that maximizes the spread of expected interception points, and a Bayesian experimental-design method that maximizes the D-score of the expected Gauss-Newton information matrix, thereby selecting trajectories that yield maximal information gain. Monte Carlo experiments demonstrate accurate parameter recovery with five to twelve sacrificial agents. The learned engagement models are then used to generate safe, time-optimal paths for high-value agents that avoid all feasible pursuer engagement regions.
