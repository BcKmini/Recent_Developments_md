# Patient foundation model for risk stratification in low-risk overweight patients

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.09079)

## 요약
arXiv:2602.09079v1 Announce Type: new
Abstract: Accurate risk stratification in patients with overweight or obesity is critical for guiding preventive care and allocating high-cost therapies such as GLP-1 receptor agonists. We present PatientTPP, a neural temporal point process (TPP) model trained on over 500,000 real-world clinical trajectories to learn patient representations from sequences of diagnoses, labs, and medications. We extend existing TPP modeling approaches to include static and numeric features and incorporate clinical knowledge for event encoding. PatientTPP representations support downstream prediction tasks, including classification of obesity-associated outcomes in low-risk individuals, even for events not explicitly modeled during training. In health economic evaluation, PatientTPP outperformed body mass index in stratifying patients by future cardiovascular-related healthcare costs, identifying higher-risk patients more efficiently. By modeling both the type and timing of clinical events, PatientTPP offers an interpretable, general-purpose foundation for patient risk modeling with direct applications to obesity-related care and cost targeting.
