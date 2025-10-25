# Fourier-Based GAN Fingerprint Detection using ResNet50

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.19840)

## 요약
arXiv:2510.19840v1 Announce Type: new
Abstract: The rapid rise of photorealistic images produced from Generative Adversarial Networks (GANs) poses a serious challenge for image forensics and industrial systems requiring reliable content authenticity. This paper uses frequency-domain analysis combined with deep learning to solve the problem of distinguishing StyleGAN-generated images from real ones. Specifically, a two-dimensional Discrete Fourier Transform (2D DFT) was applied to transform images into the Fourier domain, where subtle periodic artifacts become detectable. A ResNet50 neural network is trained on these transformed images to differentiate between real and synthetic ones. The experiments demonstrate that the frequency-domain model achieves a 92.8 percent and an AUC of 0.95, significantly outperforming the equivalent model trained on raw spatial-domain images. These results indicate that the GAN-generated images have unique frequency-domain signatures or "fingerprints". The method proposed highlights the industrial potential of combining signal processing techniques and deep learning to enhance digital forensics and strengthen the trustworthiness of industrial AI systems.
