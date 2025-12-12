# DW-KNN: A Transparent Local Classifier Integrating Distance Consistency and Neighbor Reliability

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.08956)

## 요약
arXiv:2512.08956v1 Announce Type: new
Abstract: K-Nearest Neighbors (KNN) is one of the most used ML classifiers. However, if we observe closely, standard distance-weighted KNN and relative variants assume all 'k' neighbors are equally reliable. In heterogeneous feature space, this becomes a limitation that hinders reliability in predicting true levels of the observation.
We propose DW-KNN (Double Weighted KNN), a transparent and robust variant that integrates exponential distance with neighbor validity. This enables instance-level interpretability, suppresses noisy or mislabeled samples, and reduces hyperparameter sensitivity.
Comprehensive evaluation on 9 data-sets helps to demonstrate that DW-KNN achieves 0.8988 accuracy on average. It ranks 2nd among six methods and within 0.2% of the best-performing Ensemble KNN. It also exhibits the lowest cross-validation variance (0.0156), indicating reliable prediction stability. Statistical significance test confirmed ($p < 0.001$) improvement over compactness weighted KNN (+4.09\%) and Kernel weighted KNN (+1.13\%). The method provides a simple yet effective alternative to complex adaptive schemes, particularly valuable for high-stakes applications requiring explainable predictions.
