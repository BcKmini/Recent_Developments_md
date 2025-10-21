# GAZE:Governance-Aware pre-annotation for Zero-shot World Model Environments

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.14992)

## 요약
arXiv:2510.14992v1 Announce Type: new
Abstract: Training robust world models requires large-scale, precisely labeled multimodal datasets, a process historically bottlenecked by slow and expensive manual annotation. We present a production-tested GAZE pipeline that automates the conversion of raw, long-form video into rich, task-ready supervision for world-model training. Our system (i) normalizes proprietary 360-degree formats into standard views and shards them for parallel processing; (ii) applies a suite of AI models (scene understanding, object tracking, audio transcription, PII/NSFW/minor detection) for dense, multimodal pre-annotation; and (iii) consolidates signals into a structured output specification for rapid human validation.
The GAZE workflow demonstrably yields efficiency gains (~19 minutes saved per review hour) and reduces human review volume by >80% through conservative auto-skipping of low-salience segments. By increasing label density and consistency while integrating privacy safeguards and chain-of-custody metadata, our method generates high-fidelity, privacy-aware datasets directly consumable for learning cross-modal dynamics and action-conditioned prediction. We detail our orchestration, model choices, and data dictionary to provide a scalable blueprint for generating high-quality world model training data without sacrificing throughput or governance.
