# NULLBUS: Multimodal Mixed-Supervision for Breast Ultrasound Segmentation via Nullable Global-Local Prompts

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.20783)

## 요약
arXiv:2512.20783v1 Announce Type: new
Abstract: Breast ultrasound (BUS) segmentation provides lesion boundaries essential for computer-aided diagnosis and treatment planning. While promptable methods can improve segmentation performance and tumor delineation when text or spatial prompts are available, many public BUS datasets lack reliable metadata or reports, constraining training to small multimodal subsets and reducing robustness. We propose NullBUS, a multimodal mixed-supervision framework that learns from images with and without prompts in a single model. To handle missing text, we introduce nullable prompts, implemented as learnable null embeddings with presence masks, enabling fallback to image-only evidence when metadata are absent and the use of text when present. Evaluated on a unified pool of three public BUS datasets, NullBUS achieves a mean IoU of 0.8568 and a mean Dice of 0.9103, demonstrating state-of-the-art performance under mixed prompt availability.
