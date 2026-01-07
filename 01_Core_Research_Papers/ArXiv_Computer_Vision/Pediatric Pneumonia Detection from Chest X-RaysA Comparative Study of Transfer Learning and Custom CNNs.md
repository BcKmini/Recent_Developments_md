# Pediatric Pneumonia Detection from Chest X-Rays:A Comparative Study of Transfer Learning and Custom CNNs

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.00837)

## 요약
arXiv:2601.00837v1 Announce Type: new
Abstract: Pneumonia is a leading cause of mortality in children under five, with over 700,000 deaths annually. Accurate diagnosis from chest X-rays is limited by radiologist availability and variability.
Objective: This study compares custom CNNs trained from scratch with transfer learning (ResNet50, DenseNet121, EfficientNet-B0) for pediatric pneumonia detection, evaluating frozen-backbone and fine-tuning regimes.
Methods: A dataset of 5,216 pediatric chest X-rays was split 80/10/10 for training, validation, and testing. Seven models were trained and assessed using accuracy, F1-score, and AUC. Grad-CAM visualizations provided explainability.
Results: Fine-tuned ResNet50 achieved the best performance: 99.43\% accuracy, 99.61\% F1-score, and 99.93\% AUC, with only 3 misclassifications. Fine-tuning outperformed frozen-backbone models by 5.5 percentage points on average. Grad-CAM confirmed clinically relevant lung regions guided predictions.
Conclusions: Transfer learning with fine-tuning substantially outperforms CNNs trained from scratch for pediatric pneumonia detection, showing near-perfect accuracy. This system has strong potential as a screening tool in resource-limited settings. Future work should validate these findings on multi-center and adult datasets.
Keywords: Pneumonia detection, deep learning, transfer learning, CNN, chest X-ray, pediatric diagnosis, ResNet, DenseNet, EfficientNet, Grad-CAM.
