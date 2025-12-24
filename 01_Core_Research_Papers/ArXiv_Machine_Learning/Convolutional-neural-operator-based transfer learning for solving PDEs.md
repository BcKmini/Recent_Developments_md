# Convolutional-neural-operator-based transfer learning for solving PDEs

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.17969)

## 요약
arXiv:2512.17969v1 Announce Type: new
Abstract: Convolutional neural operator is a CNN-based architecture recently proposed to enforce structure-preserving continuous-discrete equivalence and enable the genuine, alias-free learning of solution operators of PDEs. This neural operator was demonstrated to outperform for certain cases some baseline models such as DeepONet, Fourier neural operator, and Galerkin transformer in terms of surrogate accuracy. The convolutional neural operator, however, seems not to be validated for few-shot learning. We extend the model to few-shot learning scenarios by first pre-training a convolutional neural operator using a source dataset and then adjusting the parameters of the trained neural operator using only a small target dataset. We investigate three strategies for adjusting the parameters of a trained neural operator, including fine-tuning, low-rank adaption, and neuron linear transformation, and find that the neuron linear transformation strategy enjoys the highest surrogate accuracy in solving PDEs such as Kuramoto-Sivashinsky equation, Brusselator diffusion-reaction system, and Navier-Stokes equations.
