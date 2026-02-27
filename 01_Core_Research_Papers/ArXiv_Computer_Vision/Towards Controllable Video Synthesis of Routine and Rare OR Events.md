# Towards Controllable Video Synthesis of Routine and Rare OR Events

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.21365)

## 요약
arXiv:2602.21365v1 Announce Type: new
Abstract: Purpose: Curating large-scale datasets of operating room (OR) workflow, encompassing rare, safety-critical, or atypical events, remains operationally and ethically challenging. This data bottleneck complicates the development of ambient intelligence for detecting, understanding, and mitigating rare or safety-critical events in the OR.
Methods: This work presents an OR video diffusion framework that enables controlled synthesis of rare and safety-critical events. The framework integrates a geometric abstraction module, a conditioning module, and a fine-tuned diffusion model to first transform OR scenes into abstract geometric representations, then condition the synthesis process, and finally generate realistic OR event videos. Using this framework, we also curate a synthetic dataset to train and validate AI models for detecting near-misses of sterile-field violations.
Results: In synthesizing routine OR events, our method outperforms off-the-shelf video diffusion baselines, achieving lower FVD/LPIPS and higher SSIM/PSNR in both in- and out-of-domain datasets. Through qualitative results, we illustrate its ability for controlled video synthesis of counterfactual events. An AI model trained and validated on the generated synthetic data achieved a RECALL of 70.13% in detecting near safety-critical events. Finally, we conduct an ablation study to quantify performance gains from key design choices.
Conclusion: Our solution enables controlled synthesis of routine and rare OR events from abstract geometric representations. Beyond demonstrating its capability to generate rare and safety-critical scenarios, we show its potential to support the development of ambient intelligence models.
