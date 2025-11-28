# Solving Diffusion Inverse Problems with Restart Posterior Sampling

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.20705)

## 요약
arXiv:2511.20705v1 Announce Type: new
Abstract: Inverse problems are fundamental to science and engineering, where the goal is to infer an underlying signal or state from incomplete or noisy measurements. Recent approaches employ diffusion models as powerful implicit priors for such problems, owing to their ability to capture complex data distributions. However, existing diffusion-based methods for inverse problems often rely on strong approximations of the posterior distribution, require computationally expensive gradient backpropagation through the score network, or are restricted to linear measurement models.
In this work, we propose Restart for Posterior Sampling (RePS), a general and efficient framework for solving both linear and non-linear inverse problems using pre-trained diffusion models. RePS builds on the idea of restart-based sampling, previously shown to improve sample quality in unconditional diffusion, and extends it to posterior inference. Our method employs a conditioned ODE applicable to any differentiable measurement model and introduces a simplified restart strategy that contracts accumulated approximation errors during sampling. Unlike some of the prior approaches, RePS avoids backpropagation through the score network, substantially reducing computational cost.
We demonstrate that RePS achieves faster convergence and superior reconstruction quality compared to existing diffusion-based baselines across a range of inverse problems, including both linear and non-linear settings.
