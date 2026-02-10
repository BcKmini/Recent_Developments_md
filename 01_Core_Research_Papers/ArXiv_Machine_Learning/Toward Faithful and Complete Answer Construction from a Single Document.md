# Toward Faithful and Complete Answer Construction from a Single Document

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.06103)

## 요약
arXiv:2602.06103v1 Announce Type: new
Abstract: Modern large language models (LLMs) are powerful generators driven by statistical next-token prediction. While effective at producing fluent text, this design biases models toward high-probability continuations rather than exhaustive and faithful answers grounded in source content. As a result, directly applying LLMs lacks systematic mechanisms to ensure both completeness (avoiding omissions) and faithfulness (avoiding unsupported content), which fundamentally conflicts with core AI safety principles. To address this limitation, we present EVE, a structured framework for document-grounded reasoning.
Unlike free-form prompting, EVE constrains generation to a structured, verifiable pipeline that decomposes high-rigor reasoning into extraction, validation, and enumeration. Empirically, this design enables consistent and simultaneous improvements in recall, precision, and F1-score: recall and precision increase by up to 24\% and 29\%, respectively, with a corresponding 31\% gain in F1-score. This effectively breaks the long-standing trade-off between coverage and accuracy typical of single-pass LLM generation, while also mitigating generation truncation caused by length limitations. At the same time, we emphasize that EVE exhibits performance saturation due to the inherent ambiguity of natural language, reflecting fundamental limits of language-based reasoning.
