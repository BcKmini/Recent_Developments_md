# Probing Knowledge Holes in Unlearned LLMs

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.00030)

## 요약
arXiv:2511.00030v1 Announce Type: new
Abstract: Machine unlearning has emerged as a prevalent technical solution for selectively removing unwanted knowledge absorbed during pre-training, without requiring full retraining. While recent unlearning techniques can effectively remove undesirable content without severely compromising performance on standard benchmarks, we find that they may inadvertently create ``knowledge holes'' -- unintended losses of benign knowledge that standard benchmarks fail to capture. To probe where unlearned models reveal knowledge holes, we propose a test case generation framework that explores both immediate neighbors of unlearned content and broader areas of potential failures. Our evaluation demonstrates significant hidden costs of unlearning: up to 98.7\% of the test cases yield irrelevant or nonsensical responses from unlearned models, despite being answerable by the pretrained model. These findings necessitate rethinking the conventional approach to evaluating knowledge preservation in unlearning, moving beyond standard, static benchmarks.
