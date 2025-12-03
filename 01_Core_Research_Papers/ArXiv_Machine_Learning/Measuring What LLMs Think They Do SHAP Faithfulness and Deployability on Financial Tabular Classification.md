# Measuring What LLMs Think They Do: SHAP Faithfulness and Deployability on Financial Tabular Classification

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.00163)

## 요약
arXiv:2512.00163v1 Announce Type: new
Abstract: Large Language Models (LLMs) have attracted significant attention for classification tasks, offering a flexible alternative to trusted classical machine learning models like LightGBM through zero-shot prompting. However, their reliability for structured tabular data remains unclear, particularly in high stakes applications like financial risk assessment. Our study systematically evaluates LLMs and generates their SHAP values on financial classification tasks. Our analysis shows a divergence between LLMs self-explanation of feature impact and their SHAP values, as well as notable differences between LLMs and LightGBM SHAP values. These findings highlight the limitations of LLMs as standalone classifiers for structured financial modeling, but also instill optimism that improved explainability mechanisms coupled with few-shot prompting will make LLMs usable in risk-sensitive domains.
