# Enabling clinical use of foundation models in histopathology

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.22347)

## 요약
arXiv:2602.22347v1 Announce Type: new
Abstract: Foundation models in histopathology are expected to facilitate the development of high-performing and generalisable deep learning systems. However, current models capture not only biologically relevant features, but also pre-analytic and scanner-specific variation that bias the predictions of task-specific models trained from the foundation model features. Here we show that introducing novel robustness losses during training of downstream task-specific models reduces sensitivity to technical variability. A purpose-designed comprehensive experimentation setup with 27,042 WSIs from 6155 patients is used to train thousands of models from the features of eight popular foundation models for computational pathology. In addition to a substantial improvement in robustness, we observe that prediction accuracy improves by focusing on biologically relevant features. Our approach successfully mitigates robustness issues of foundation models for computational pathology without retraining the foundation models themselves, enabling development of robust computational pathology models applicable to real-world data in routine clinical practice.
