# To Deceive is to Teach? Forging Perceptual Robustness via Adversarial Reinforcement Learning

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.22227)

## 요약
arXiv:2602.22227v1 Announce Type: new
Abstract: Despite their impressive capabilities, Multimodal Large Language Models (MLLMs) exhibit perceptual fragility when confronted with visually complex scenes. This weakness stems from a reliance on finite training datasets, which are prohibitively expensive to scale and impose a ceiling on model robustness. We introduce \textbf{AOT-SFT}, a large-scale adversarial dataset for bootstrapping MLLM robustness. Building on this, we propose \textbf{AOT (Adversarial Opponent Training)}, a self-play framework that forges MLLM robustness by creating its own training data. Our method orchestrates a co-evolution between an image-editing Attacker and a Defender MLLM, where the Attacker generates a diverse and dynamic curriculum of image manipulations, forcing the Defender to adapt and improve. Extensive experiments demonstrate that AOT enhances the Defender's perceptual robustness and reduces hallucinations, establishing a scalable paradigm for training more reliable MLLMs.
