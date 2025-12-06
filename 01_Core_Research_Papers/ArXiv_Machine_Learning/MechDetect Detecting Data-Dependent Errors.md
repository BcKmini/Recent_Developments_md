# MechDetect: Detecting Data-Dependent Errors

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.04138)

## 요약
arXiv:2512.04138v1 Announce Type: new
Abstract: Data quality monitoring is a core challenge in modern information processing systems. While many approaches to detect data errors or shifts have been proposed, few studies investigate the mechanisms governing error generation. We argue that knowing how errors were generated can be key to tracing and fixing them. In this study, we build on existing work in the statistics literature on missing values and propose MechDetect, a simple algorithm to investigate error generation mechanisms. Given a tabular data set and a corresponding error mask, the algorithm estimates whether or not the errors depend on the data using machine learning models. Our work extends established approaches to detect mechanisms underlying missing values and can be readily applied to other error types, provided that an error mask is available. We demonstrate the effectiveness of MechDetect in experiments on established benchmark datasets.
