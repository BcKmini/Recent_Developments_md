# CulinaryCut-VLAP: A Vision-Language-Action-Physics Framework for Food Cutting via a Force-Aware Material Point Method

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.06451)

## 요약
arXiv:2601.06451v1 Announce Type: new
Abstract: Food cutting is a highly practical yet underexplored application at the intersection of vision and robotic manipulation. The task remains challenging because interactions between the knife and deformable materials are highly nonlinear and often entail large deformations, frequent contact, and topological change, which in turn hinder stable and safe large-scale data collection.
To address these challenges, we propose a unified framework that couples a vision-language-action (VLA) dataset with a physically realistic cutting simulator built on the material point method (MPM). Our simulator adopts MLS-MPM as its computational core, reducing numerical dissipation and energy drift while preserving rotational and shear responses even under topology-changing cuts. During cutting, forces and stress distributions are estimated from impulse exchanges between particles and the grid, enabling stable tracking of transient contact forces and energy transfer.
We also provide a benchmark dataset that integrates diverse cutting trajectories, multi-view visual observations, and fine-grained language instructions, together with force--torque and tool--pose labels to provide physically consistent training signals.
These components realize a learning--evaluation loop that respects the core physics of cutting and establishes a safe, reproducible, and scalable foundation for advancing VLA models in deformable object manipulation.
