# EfficientSAM3: Progressive Hierarchical Distillation for Video Concept Segmentation from SAM1, 2, and 3

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.15833)

## 요약
arXiv:2511.15833v1 Announce Type: new
Abstract: The Segment Anything Model 3 (SAM3) advances visual understanding with Promptable Concept Segmentation (PCS) across images and videos, but its unified architecture (shared vision backbone, DETR-style detector, dense-memory tracker) remains prohibitive for on-device use. We present EfficientSAM3, a family of efficient models built on Progressive Hierarchical Distillation (PHD) that transfers capability from SAM3 to lightweight students in three stages: (1) Encoder Distillation aligns image features via prompt-in-the-loop training on SA-1B; (2) Temporal Memory Distillation replaces dense memory with a compact Perceiver-based module trained on SA-V to compress and retrieve spatiotemporal features efficiently; and (3) End-to-End Fine-Tuning refines the full pipeline on the official SAM3 PCS data to preserve concept-level performance. PHD yields a spectrum of student variants using RepViT, TinyViT, and EfficientViT backbones, enabling on-device concept segmentation and tracking while maintaining high fidelity to teacher behavior. We benchmark on popular VOS datasets, and compare with varies of releated work, achieing strong performance-efficiency trade-offs.
