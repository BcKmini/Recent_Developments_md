# PC-UNet: An Enforcing Poisson Statistics U-Net for Positron Emission Tomography Denoising

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.14995)

## 요약
arXiv:2510.14995v1 Announce Type: new
Abstract: Positron Emission Tomography (PET) is crucial in medicine, but its clinical use is limited due to high signal-to-noise ratio doses increasing radiation exposure. Lowering doses increases Poisson noise, which current denoising methods fail to handle, causing distortions and artifacts. We propose a Poisson Consistent U-Net (PC-UNet) model with a new Poisson Variance and Mean Consistency Loss (PVMC-Loss) that incorporates physical data to improve image fidelity. PVMC-Loss is statistically unbiased in variance and gradient adaptation, acting as a Generalized Method of Moments implementation, offering robustness to minor data mismatches. Tests on PET datasets show PC-UNet improves physical consistency and image fidelity, proving its ability to integrate physical information effectively.
