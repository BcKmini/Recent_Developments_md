# R$^2$BD: A Reconstruction-Based Method for Generalizable and Efficient Detection of Fake Images

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.08867)

## 요약
arXiv:2601.08867v1 Announce Type: new
Abstract: Recently, reconstruction-based methods have gained attention for AIGC image detection. These methods leverage pre-trained diffusion models to reconstruct inputs and measure residuals for distinguishing real from fake images. Their key advantage lies in reducing reliance on dataset-specific artifacts and improving generalization under distribution shifts. However, they are limited by significant inefficiency due to multi-step inversion and reconstruction, and their reliance on diffusion backbones further limits generalization to other generative paradigms such as GANs.
In this paper, we propose a novel fake image detection framework, called R$^2$BD, built upon two key designs: (1) G-LDM, a unified reconstruction model that simulates the generation behaviors of VAEs, GANs, and diffusion models, thereby broadening the detection scope beyond prior diffusion-only approaches; and (2) a residual bias calculation module that distinguishes real and fake images in a single inference step, which is a significant efficiency improvement over existing methods that typically require 20$+$ steps.
Extensive experiments on the benchmark from 10 public datasets demonstrate that R$^2$BD is over 22$\times$ faster than existing reconstruction-based methods while achieving superior detection accuracy. In cross-dataset evaluations, it outperforms state-of-the-art methods by an average of 13.87\%, showing strong efficiency and generalization across diverse generative methods. The code and dataset used for evaluation are available at https://github.com/QingyuLiu/RRBD.
