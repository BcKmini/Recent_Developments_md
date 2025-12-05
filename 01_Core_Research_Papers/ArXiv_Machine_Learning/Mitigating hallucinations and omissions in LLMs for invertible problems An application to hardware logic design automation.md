# Mitigating hallucinations and omissions in LLMs for invertible problems: An application to hardware logic design automation

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.03053)

## 요약
arXiv:2512.03053v1 Announce Type: new
Abstract: We show for invertible problems that transform data from a source domain (for example, Logic Condition Tables (LCTs)) to a destination domain (for example, Hardware Description Language (HDL) code), an approach of using Large Language Models (LLMs) as a lossless encoder from source to destination followed by as a lossless decoder back to the source, comparable to lossless compression in information theory, can mitigate most of the LLM drawbacks of hallucinations and omissions. Specifically, using LCTs as inputs, we generate the full HDL for a two-dimensional network-on-chip router (13 units, 1500-2000 lines of code) using seven different LLMs, reconstruct the LCTs from the auto-generated HDL, and compare the original and reconstructed LCTs. This approach yields significant productivity improvements, not only confirming correctly generated LLM logic and detecting incorrectly generated LLM logic but also assisting developers in finding design specification errors.
