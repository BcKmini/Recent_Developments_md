# Self-Supervised Masked Autoencoders with Dense-Unet for Coronary Calcium Removal in limited CT Data

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.02392)

## 요약
arXiv:2601.02392v1 Announce Type: new
Abstract: Coronary calcification creates blooming artifacts in Computed Tomography Angiography (CTA), severely hampering the diagnosis of lumen stenosis. While Deep Convolutional Neural Networks (DCNNs) like Dense-Unet have shown promise in removing these artifacts via inpainting, they often require large labeled datasets which are scarce in the medical domain. Inspired by recent advancements in Masked Autoencoders (MAE) for 3D point clouds, we propose \textbf{Dense-MAE}, a novel self-supervised learning framework for volumetric medical data. We introduce a pre-training strategy that randomly masks 3D patches of the vessel lumen and trains the Dense-Unet to reconstruct the missing geometry. This forces the encoder to learn high-level latent features of arterial topology without human annotation. Experimental results on clinical CTA datasets demonstrate that initializing the Calcium Removal network with our MAE-based weights significantly improves inpainting accuracy and stenosis estimation compared to training from scratch, specifically in few-shot scenarios.
