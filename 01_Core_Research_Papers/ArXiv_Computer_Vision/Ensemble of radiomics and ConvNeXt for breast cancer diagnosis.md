# Ensemble of radiomics and ConvNeXt for breast cancer diagnosis

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.05373)

## 요약
arXiv:2601.05373v1 Announce Type: new
Abstract: Early diagnosis of breast cancer is crucial for improving survival rates. Radiomics and deep learning (DL) have shown significant potential in assisting radiologists with early cancer detection. This paper aims to critically assess the performance of radiomics, DL, and ensemble techniques in detecting cancer from screening mammograms. Two independent datasets were used: the RSNA 2023 Breast Cancer Detection Challenge (11,913 patients) and a Mexican cohort from the TecSalud dataset (19,400 patients). The ConvNeXtV1-small DL model was trained on the RSNA dataset and validated on the TecSalud dataset, while radiomics models were developed using the TecSalud dataset and validated with a leave-one-year-out approach. The ensemble method consistently combined and calibrated predictions using the same methodology. Results showed that the ensemble approach achieved the highest area under the curve (AUC) of 0.87, compared to 0.83 for ConvNeXtV1-small and 0.80 for radiomics. In conclusion, ensemble methods combining DL and radiomics predictions significantly enhance breast cancer diagnosis from mammograms.
