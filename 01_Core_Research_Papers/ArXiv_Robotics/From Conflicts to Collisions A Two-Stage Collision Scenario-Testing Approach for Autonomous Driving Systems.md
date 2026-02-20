# From Conflicts to Collisions: A Two-Stage Collision Scenario-Testing Approach for Autonomous Driving Systems

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.15837)

## 요약
arXiv:2602.15837v1 Announce Type: new
Abstract: Autonomous driving systems (ADS) are safety-critical and require rigorous testing before public deployment. Simulation-based scenario testing provides a safe and cost-effective alternative to extensive on-road trials, enabling efficient evaluation of ADS under diverse and high-risk conditions. However, existing approaches mainly evaluates the scenarios based on their proximity to collisions and focus on scenarios already close to collision, leaving many other hazardous situations unexplored. To bridge this, we introduce a collision-related concept of conflict as an intermediate search target and propose a two-stage scenario testing framework that first searches for conflicts and then mutates these conflict scenarios to induce actual collisions. Evaluated on Baidu Apollo, our approach reveals up to 12 distinct collision types in a single run, doubling the diversity discovered by state-of-the-art baselines while requiring fewer simulations thanks to conflict-targeted mutations. These results show that using conflicts as intermediate objectives broadens the search horizon and significantly improves the efficiency and effectiveness of ADS safety evaluation.
