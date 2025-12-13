# Push Smarter, Not Harder: Hierarchical RL-Diffusion Policy for Efficient Nonprehensile Manipulation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.10099)

## 요약
arXiv:2512.10099v1 Announce Type: new
Abstract: Nonprehensile manipulation, such as pushing objects across cluttered environments, presents a challenging control problem due to complex contact dynamics and long-horizon planning requirements. In this work, we propose HeRD, a hierarchical reinforcement learning-diffusion policy that decomposes pushing tasks into two levels: high-level goal selection and low-level trajectory generation. We employ a high-level reinforcement learning (RL) agent to select intermediate spatial goals, and a low-level goal-conditioned diffusion model to generate feasible, efficient trajectories to reach them.
This architecture combines the long-term reward maximizing behaviour of RL with the generative capabilities of diffusion models. We evaluate our method in a 2D simulation environment and show that it outperforms the state-of-the-art baseline in success rate, path efficiency, and generalization across multiple environment configurations. Our results suggest that hierarchical control with generative low-level planning is a promising direction for scalable, goal-directed nonprehensile manipulation. Code, documentation, and trained models are available: https://github.com/carosteven/HeRD.
