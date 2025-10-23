# CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.17847)

## 요약
arXiv:2510.17847v1 Announce Type: new
Abstract: Multimodal large language models (MLLMs) rely heavily on instruction tuning to align vision and language capabilities, yet the computational cost of training on large-scale datasets remains a major bottleneck. Existing data selection methods aim to mitigate this by selecting important and diverse subsets, but they often suffer from two critical drawbacks: high computational overhead from processing the entire dataset and suboptimal data selection due to separate treatment of importance and diversity.
We introduce CoIDO, a novel dual-objective framework that jointly optimizes data importance and diversity to overcome these challenges. Unlike existing approaches that require costly evaluations across the whole dataset, CoIDO employs a lightweight plug-in scorer. This scorer is trained on just a small random sample of data to learn the distribution of the candidate set, drastically reducing computational demands. By leveraging a homoscedastic uncertainty-based formulation, CoIDO effectively balances importance and diversity during training, enabling efficient and scalable data selection.
In our experiments, we trained the CoIDO scorer using only 20 percent of randomly sampled data. Once trained, CoIDO was applied to the entire dataset to select a 20 percent subset for instruction tuning. On the widely used LLaVA-1.5-7B model across ten downstream tasks, this selected subset achieved an impressive 98.2 percent of the performance of full-data fine-tuning, on average.
