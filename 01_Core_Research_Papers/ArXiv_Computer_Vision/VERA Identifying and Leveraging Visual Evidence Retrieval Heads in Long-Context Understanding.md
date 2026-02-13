# VERA: Identifying and Leveraging Visual Evidence Retrieval Heads in Long-Context Understanding

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.10146)

## 요약
arXiv:2602.10146v1 Announce Type: new
Abstract: While Vision-Language Models (VLMs) have shown promise in textual understanding, they face significant challenges when handling long context and complex reasoning tasks. In this paper, we dissect the internal mechanisms governing long-context processing in VLMs to understand their performance bottlenecks. Through the lens of attention analysis, we identify specific Visual Evidence Retrieval (VER) Heads - a sparse, dynamic set of attention heads critical for locating visual cues during reasoning, distinct from static OCR heads. We demonstrate that these heads are causal to model performance; masking them leads to significant degradation. Leveraging this discovery, we propose VERA (Visual Evidence Retrieval Augmentation), a training-free framework that detects model uncertainty (i.e., entropy) to trigger the explicit verbalization of visual evidence attended by VER heads. Comprehensive experiments demonstrate that VERA significantly improves long-context understanding of open-source VLMs: it yields an average relative improvement of 21.3% on Qwen3-VL-8B-Instruct and 20.1% on GLM-4.1V-Thinking across five benchmarks.
