# Explainable Detection of AI-Generated Images with Artifact Localization Using Faster-Than-Lies and Vision-Language Models for Edge Devices

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.23775)

## 요약
arXiv:2510.23775v1 Announce Type: new
Abstract: The increasing realism of AI-generated imagery poses challenges for verifying visual authenticity. We present an explainable image authenticity detection system that combines a lightweight convolutional classifier ("Faster-Than-Lies") with a Vision-Language Model (Qwen2-VL-7B) to classify, localize, and explain artifacts in 32x32 images. Our model achieves 96.5% accuracy on the extended CiFAKE dataset augmented with adversarial perturbations and maintains an inference time of 175ms on 8-core CPUs, enabling deployment on local or edge devices. Using autoencoder-based reconstruction error maps, we generate artifact localization heatmaps, which enhance interpretability for both humans and the VLM. We further categorize 70 visual artifact types into eight semantic groups and demonstrate explainable text generation for each detected anomaly. This work highlights the feasibility of combining visual and linguistic reasoning for interpretable authenticity detection in low-resolution imagery and outlines potential cross-domain applications in forensics, industrial inspection, and social media moderation.
