# Reducing Text Bias in Synthetically Generated MCQAs for VLMs in Autonomous Driving

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.17677)

## 요약
arXiv:2602.17677v1 Announce Type: new
Abstract: Multiple Choice Question Answering (MCQA) benchmarks are an established standard for measuring Vision Language Model (VLM) performance in driving tasks. However, we observe the known phenomenon that synthetically generated MCQAs are highly susceptible to hidden textual cues that allow models to exploit linguistic patterns rather than visual context. Our results show that a VLM fine-tuned on such data can achieve accuracy comparable to human-validated benchmarks even without visual input. Our proposed method reduces blind accuracy from +66.9% above random to +2.9%, eliminating the vast majority of exploitable textual shortcuts. By decoupling the correct answer from linguistic artifacts and employing a curriculum learning strategy, we force the model to rely on visual grounding, ensuring that performance accurately reflects perceptual understanding.
