# SCALEX: Scalable Concept and Latent Exploration for Diffusion Models

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.13750)

## 요약
arXiv:2511.13750v1 Announce Type: new
Abstract: Image generation models frequently encode social biases, including stereotypes tied to gender, race, and profession. Existing methods for analyzing these biases in diffusion models either focus narrowly on predefined categories or depend on manual interpretation of latent directions. These constraints limit scalability and hinder the discovery of subtle or unanticipated patterns.
We introduce SCALEX, a framework for scalable and automated exploration of diffusion model latent spaces. SCALEX extracts semantically meaningful directions from H-space using only natural language prompts, enabling zero-shot interpretation without retraining or labelling. This allows systematic comparison across arbitrary concepts and large-scale discovery of internal model associations. We show that SCALEX detects gender bias in profession prompts, ranks semantic alignment across identity descriptors, and reveals clustered conceptual structure without supervision. By linking prompts to latent directions directly, SCALEX makes bias analysis in diffusion models more scalable, interpretable, and extensible than prior approaches.
