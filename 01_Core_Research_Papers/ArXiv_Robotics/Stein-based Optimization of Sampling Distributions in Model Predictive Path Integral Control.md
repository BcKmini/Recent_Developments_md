# Stein-based Optimization of Sampling Distributions in Model Predictive Path Integral Control

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.02015)

## 요약
arXiv:2511.02015v1 Announce Type: new
Abstract: This paper presents a novel method for Model Predictive Path Integral (MPPI) control that optimizes sample generation towards an optimal trajectory through Stein Variational Gradient Descent (SVGD). MPPI is traditionally reliant on randomly sampled trajectories, often by a Gaussian distribution. The result can lead to sample deprivation, under-representing the space of possible trajectories, and yield suboptimal results. Through introducing SVGD updates in between MPPI environment steps, we present Stein-Optimized Path-Integral Inference (SOPPI), an MPPI/SVGD algorithm that can dynamically update noise distributions at runtime to shape a more optimal representation without an excessive increase in computational requirements. We demonstrate the efficacy of our method systems ranging from a Cart-Pole to a two-dimensional bipedal walking task, indicating improved performance above standard MPPI across a range of hyper-parameters and demonstrate feasibility at lower particle counts. We discuss the applicability of this MPPI/SVGD method to higher degree-of-freedom systems, as well as its potential to new developments in state-of-the-art differentiable simulators.
