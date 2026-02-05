# End-to-end reconstruction of OCT optical properties and speckle-reduced structural intensity via physics-based learning

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.02721)

## 요약
arXiv:2602.02721v1 Announce Type: new
Abstract: Inverse scattering in optical coherence tomography (OCT) seeks to recover both structural images and intrinsic tissue optical properties, including refractive index, scattering coefficient, and anisotropy. This inverse problem is challenging due to attenuation, speckle noise, and strong coupling among parameters. We propose a regularized end-to-end deep learning framework that jointly reconstructs optical parameter maps and speckle-reduced OCT structural intensity for layer visualization. Trained with Monte Carlo-simulated ground truth, our network incorporates a physics-based OCT forward model that generates predicted signals from the estimated parameters, providing physics-consistent supervision for parameter recovery and artifact suppression. Experiments on the synthetic corneal OCT dataset demonstrate robust optical map recovery under noise, improved resolution, and enhanced structural fidelity. This approach enables quantitative multi-parameter tissue characterization and highlights the benefit of combining physics-informed modeling with deep learning for computational OCT.
