# Which Quantization Should I Use? A Unified Evaluation of llama.cpp Quantization on Llama-3.1-8B-Instruct

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.14277)

## 요약
arXiv:2601.14277v1 Announce Type: new
Abstract: Quantization is a practical technique for making large language models easier to deploy by reducing the precision used to store and operate on model weights. This can lower memory use and improve runtime feasibility on constrained hardware, which is especially relevant for users running models locally. Quantization in llama.cpp enables large language models to run on commodity hardware, but available formats are often evaluated inconsistently, making it hard to choose among schemes. We present a unified empirical study of the llama.cpp quantization on a single modern model, Llama-3.1-8B-Instruct (FP16, GGUF), covering 3-8 bit K-quant and legacy formats. We evaluate downstream task performance across standard reasoning, knowledge, instruction-following, and truthfulness benchmarks, and also measure perplexity and CPU throughput (prefill/decoding) alongside model size, compression, and quantization time. Ultimately, this work is a practical guide for choosing a llama.cpp quantization scheme, helping readers make informed, context-aware decisions for their intended use and resource budget.
