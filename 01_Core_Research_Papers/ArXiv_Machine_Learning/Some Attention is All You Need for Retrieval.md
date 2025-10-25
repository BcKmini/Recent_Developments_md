# Some Attention is All You Need for Retrieval

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.19861)

## 요약
arXiv:2510.19861v1 Announce Type: new
Abstract: We demonstrate complete functional segregation in hybrid SSM-Transformer architectures: retrieval depends exclusively on self-attention layers. Across RecurrentGemma-2B/9B and Jamba-Mini-1.6, attention ablation causes catastrophic retrieval failure (0% accuracy), while SSM layers show no compensatory mechanisms even with improved prompting. Conversely, sparsifying attention to just 15% of heads maintains near-perfect retrieval while preserving 84% MMLU performance, suggesting self-attention specializes primarily for retrieval tasks. We identify precise mechanistic requirements for retrieval: needle tokens must be exposed during generation and sufficient context must be available during prefill or generation. This strict functional specialization challenges assumptions about redundancy in hybrid architectures and suggests these models operate as specialized modules rather than integrated systems, with immediate implications for architecture optimization and interpretability.
