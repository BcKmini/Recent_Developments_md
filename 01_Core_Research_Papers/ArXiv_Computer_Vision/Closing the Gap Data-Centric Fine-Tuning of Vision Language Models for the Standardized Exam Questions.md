# Closing the Gap: Data-Centric Fine-Tuning of Vision Language Models for the Standardized Exam Questions

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.00042)

## 요약
arXiv:2512.00042v1 Announce Type: new
Abstract: Multimodal reasoning has become a cornerstone of modern AI research. Standardized exam questions offer a uniquely rigorous testbed for such reasoning, providing structured visual contexts and verifiable answers. While recent progress has largely focused on algorithmic advances such as reinforcement learning (e.g., GRPO, DPO), the data centric foundations of vision language reasoning remain less explored.
We show that supervised fine-tuning (SFT) with high-quality data can rival proprietary approaches. To this end, we compile a 161.4 million token multimodal dataset combining textbook question-solution pairs, curriculum aligned diagrams, and contextual materials, and fine-tune Qwen-2.5VL-32B using an optimized reasoning syntax (QMSA). The resulting model achieves 78.6% accuracy, only 1.0% below Gemini 2.0 Flash, on our newly released benchmark YKSUniform, which standardizes 1,854 multimodal exam questions across 309 curriculum topics.
Our results reveal that data composition and representational syntax play a decisive role in multimodal reasoning. This work establishes a data centric framework for advancing open weight vision language models, demonstrating that carefully curated and curriculum-grounded multimodal data can elevate supervised fine-tuning to near state-of-the-art performance.
