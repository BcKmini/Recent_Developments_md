# The Hessian of tall-skinny networks is easy to invert

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.06096)

## 요약
arXiv:2601.06096v1 Announce Type: new
Abstract: We describe an exact algorithm for solving linear systems $Hx=b$ where $H$ is the Hessian of a deep net. The method computes Hessian-inverse-vector products without storing the Hessian or its inverse in time and storage that scale linearly in the number of layers. Compared to the naive approach of first computing the Hessian, then solving the linear system, which takes storage that's quadratic in the number of parameters and cubically many operations, our Hessian-inverse-vector product method scales roughly like Pearlmutter's algorithm for computing Hessian-vector products.
