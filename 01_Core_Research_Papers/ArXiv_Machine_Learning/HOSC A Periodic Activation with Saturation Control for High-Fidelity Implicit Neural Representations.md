# HOSC: A Periodic Activation with Saturation Control for High-Fidelity Implicit Neural Representations

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.07870)

## 요약
arXiv:2601.07870v1 Announce Type: new
Abstract: Periodic activations such as sine preserve high-frequency information in implicit neural representations (INRs) through their oscillatory structure, but often suffer from gradient instability and limited control over multi-scale behavior. We introduce the Hyperbolic Oscillator with Saturation Control (HOSC) activation, $\text{HOSC}(x) = \tanh\bigl(\beta \sin(\omega\_0 x)\bigr)$, which exposes an explicit parameter $\beta$ that controls the Lipschitz bound of the activation by $\beta \omega\_0$. This provides a direct mechanism to tune gradient magnitudes while retaining a periodic carrier. We provide a mathematical analysis and conduct a comprehensive empirical study across images, audio, video, NeRFs, and SDFs using standardized training protocols. Comparative analysis against SIREN, FINER, and related methods shows where HOSC provides substantial benefits and where it achieves competitive parity. Results establish HOSC as a practical periodic activation for INR applications, with domain-specific guidance on hyperparameter selection. For code visit the project page https://hosc-nn.github.io/ .
