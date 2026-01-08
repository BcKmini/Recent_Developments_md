# GEM-Style Constraints for PEFT with Dual Gradient Projection in LoRA

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.02500)

## 요약
arXiv:2601.02500v1 Announce Type: new
Abstract: Full fine-tuning of Large Language Models (LLMs) is computationally costly, motivating Continual Learning (CL) approaches that utilize parameter-efficient adapters. We revisit Gradient Episodic Memory (GEM) within the Low-Rank Adapter (LoRA) subspace and introduce I-GEM: a fixed-budget, GPU-resident dual projected-gradient approximation to GEM's quadratic projection. By constraining non-interference solely within the adapter parameters, I-GEM preserves GEM-like stability with orders-of-magnitude lower mean projection overhead. On a 3-task AG News split with induced domain drift, using GPT-2 (355M) and LoRA ($r=8$), I-GEM matches GEM's average accuracy (within $\sim\!0.04$ pts) and outperforms A-GEM by $\sim\!1.4$ pts. Crucially, it reduces projection time vs.\ GEM by a factor of $\sim\!10^3$. These results suggest that applying GEM constraints in the LoRA subspace is a practical pathway for continual learning at the LLM scale.
