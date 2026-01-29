# Learning the Pareto Space of Multi-Objective Autonomous Driving: A Modular, Data-Driven Approach

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.18913)

## 요약
arXiv:2601.18913v1 Announce Type: new
Abstract: Balancing safety, efficiency, and interaction is fundamental to designing autonomous driving agents and to understanding autonomous vehicle (AV) behavior in real-world operation. This study introduces an empirical learning framework that derives these trade-offs directly from naturalistic trajectory data. A unified objective space represents each AV timestep through composite scores of safety, efficiency, and interaction. Pareto dominance is applied to identify non-dominated states, forming an empirical frontier that defines the attainable region of balanced performance.
The proposed framework was demonstrated using the Third Generation Simulation (TGSIM) datasets from Foggy Bottom and I-395. Results showed that only 0.23\% of AV driving instances were Pareto-optimal, underscoring the rarity of simultaneous optimization across objectives. Pareto-optimal states showed notably higher mean scores for safety, efficiency, and interaction compared to non-optimal cases, with interaction showing the greatest potential for improvement.
This minimally invasive and modular framework, which requires only kinematic and positional data, can be directly applied beyond the scope of this study to derive and visualize multi-objective learning surfaces
