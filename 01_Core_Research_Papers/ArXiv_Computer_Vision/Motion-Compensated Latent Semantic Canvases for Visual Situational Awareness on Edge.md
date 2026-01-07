# Motion-Compensated Latent Semantic Canvases for Visual Situational Awareness on Edge

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.00854)

## 요약
arXiv:2601.00854v1 Announce Type: new
Abstract: We propose Motion-Compensated Latent Semantic Canvases (MCLSC) for visual situational awareness on resource-constrained edge devices. The core idea is to maintain persistent semantic metadata in two latent canvases - a slowly accumulating static layer and a rapidly updating dynamic layer - defined in a baseline coordinate frame stabilized from the video stream. Expensive panoptic segmentation (Mask2Former) runs asynchronously and is motion-gated: inference is triggered only when motion indicates new information, while stabilization/motion compensation preserves a consistent coordinate system for latent semantic memory. On prerecorded 480p clips, our prototype reduces segmentation calls by >30x and lowers mean end-to-end processing time by >20x compared to naive per-frame segmentation, while maintaining coherent static/dynamic semantic overlays.
