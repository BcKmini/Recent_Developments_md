# Optimistic Reinforcement Learning-Based Skill Insertions for Task and Motion Planning

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.14065)

## 요약
arXiv:2510.14065v1 Announce Type: new
Abstract: Task and motion planning (TAMP) for robotics manipulation necessitates long-horizon reasoning involving versatile actions and skills. While deterministic actions can be crafted by sampling or optimizing with certain constraints, planning actions with uncertainty, i.e., probabilistic actions, remains a challenge for TAMP. On the contrary, Reinforcement Learning (RL) excels in acquiring versatile, yet short-horizon, manipulation skills that are robust with uncertainties. In this letter, we design a method that integrates RL skills into TAMP pipelines. Besides the policy, a RL skill is defined with data-driven logical components that enable the skill to be deployed by symbolic planning. A plan refinement sub-routine is designed to further tackle the inevitable effect uncertainties. In the experiments, we compare our method with baseline hierarchical planning from both TAMP and RL fields and illustrate the strength of the method. The results show that by embedding RL skills, we extend the capability of TAMP to domains with probabilistic skills, and improve the planning efficiency compared to the previous methods.
