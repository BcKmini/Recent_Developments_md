# A Few-Shot LLM Framework for Extreme Day Classification in Electricity Markets

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.16735)

## 요약
arXiv:2602.16735v1 Announce Type: new
Abstract: This paper proposes a few-shot classification framework based on Large Language Models (LLMs) to predict whether the next day will have spikes in real-time electricity prices. The approach aggregates system state information, including electricity demand, renewable generation, weather forecasts, and recent electricity prices, into a set of statistical features that are formatted as natural-language prompts and fed to an LLM along with general instructions. The model then determines the likelihood that the next day would be a spike day and reports a confidence score. Using historical data from the Texas electricity market, we demonstrate that this few-shot approach achieves performance comparable to supervised machine learning models, such as Support Vector Machines and XGBoost, and outperforms the latter two when limited historical data are available. These findings highlight the potential of LLMs as a data-efficient tool for classifying electricity price spikes in settings with scarce data.
