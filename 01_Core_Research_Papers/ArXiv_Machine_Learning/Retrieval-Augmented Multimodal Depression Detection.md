# Retrieval-Augmented Multimodal Depression Detection

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.01892)

## 요약
arXiv:2511.01892v1 Announce Type: new
Abstract: Multimodal deep learning has shown promise in depression detection by integrating text, audio, and video signals. Recent work leverages sentiment analysis to enhance emotional understanding, yet suffers from high computational cost, domain mismatch, and static knowledge limitations. To address these issues, we propose a novel Retrieval-Augmented Generation (RAG) framework. Given a depression-related text, our method retrieves semantically relevant emotional content from a sentiment dataset and uses a Large Language Model (LLM) to generate an Emotion Prompt as an auxiliary modality. This prompt enriches emotional representation and improves interpretability. Experiments on the AVEC 2019 dataset show our approach achieves state-of-the-art performance with CCC of 0.593 and MAE of 3.95, surpassing previous transfer learning and multi-task learning baselines.
