# NanoNet: Parameter-Efficient Learning with Label-Scarce Supervision for Lightweight Text Mining Model

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.06093)

## 요약
arXiv:2602.06093v1 Announce Type: new
Abstract: The lightweight semi-supervised learning (LSL) strategy provides an effective approach of conserving labeled samples and minimizing model inference costs. Prior research has effectively applied knowledge transfer learning and co-training regularization from large to small models in LSL. However, such training strategies are computationally intensive and prone to local optima, thereby increasing the difficulty of finding the optimal solution. This has prompted us to investigate the feasibility of integrating three low-cost scenarios for text mining tasks: limited labeled supervision, lightweight fine-tuning, and rapid-inference small models. We propose NanoNet, a novel framework for lightweight text mining that implements parameter-efficient learning with limited supervision. It employs online knowledge distillation to generate multiple small models and enhances their performance through mutual learning regularization. The entire process leverages parameter-efficient learning, reducing training costs and minimizing supervision requirements, ultimately yielding a lightweight model for downstream inference.
