# DC4GS: Directional Consistency-Driven Adaptive Density Control for 3D Gaussian Splatting

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.26921)

## 요약
arXiv:2510.26921v1 Announce Type: new
Abstract: We present a Directional Consistency (DC)-driven Adaptive Density Control (ADC) for 3D Gaussian Splatting (DC4GS). Whereas the conventional ADC bases its primitive splitting on the magnitudes of positional gradients, we further incorporate the DC of the gradients into ADC, and realize it through the angular coherence of the gradients. Our DC better captures local structural complexities in ADC, avoiding redundant splitting. When splitting is required, we again utilize the DC to define optimal split positions so that sub-primitives best align with the local structures than the conventional random placement. As a consequence, our DC4GS greatly reduces the number of primitives (up to 30% in our experiments) than the existing ADC, and also enhances reconstruction fidelity greatly.
