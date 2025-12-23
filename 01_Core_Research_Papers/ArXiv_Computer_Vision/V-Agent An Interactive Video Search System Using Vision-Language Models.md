# V-Agent: An Interactive Video Search System Using Vision-Language Models

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.16925)

## 요약
arXiv:2512.16925v1 Announce Type: new
Abstract: We introduce V-Agent, a novel multi-agent platform designed for advanced video search and interactive user-system conversations. By fine-tuning a vision-language model (VLM) with a small video preference dataset and enhancing it with a retrieval vector from an image-text retrieval model, we overcome the limitations of traditional text-based retrieval systems in multimodal scenarios. The VLM-based retrieval model independently embeds video frames and audio transcriptions from an automatic speech recognition (ASR) module into a shared multimodal representation space, enabling V-Agent to interpret both visual and spoken content for context-aware video search. This system consists of three agents-a routing agent, a search agent, and a chat agent-that work collaboratively to address user intents by refining search outputs and communicating with users. The search agent utilizes the VLM-based retrieval model together with an additional re-ranking module to further enhance video retrieval quality. Our proposed framework demonstrates state-of-the-art zero-shot performance on the MultiVENT 2.0 benchmark, highlighting its potential for both academic research and real-world applications.
