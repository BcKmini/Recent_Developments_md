# TRELLISWorld: Training-Free World Generation from Object Generators

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2510.23880)

## 요약
arXiv:2510.23880v1 Announce Type: new
Abstract: Text-driven 3D scene generation holds promise for a wide range of applications, from virtual prototyping to AR/VR and simulation. However, existing methods are often constrained to single-object generation, require domain-specific training, or lack support for full 360-degree viewability. In this work, we present a training-free approach to 3D scene synthesis by repurposing general-purpose text-to-3D object diffusion models as modular tile generators. We reformulate scene generation as a multi-tile denoising problem, where overlapping 3D regions are independently generated and seamlessly blended via weighted averaging. This enables scalable synthesis of large, coherent scenes while preserving local semantic control. Our method eliminates the need for scene-level datasets or retraining, relies on minimal heuristics, and inherits the generalization capabilities of object-level priors. We demonstrate that our approach supports diverse scene layouts, efficient generation, and flexible editing, establishing a simple yet powerful foundation for general-purpose, language-driven 3D scene construction.
