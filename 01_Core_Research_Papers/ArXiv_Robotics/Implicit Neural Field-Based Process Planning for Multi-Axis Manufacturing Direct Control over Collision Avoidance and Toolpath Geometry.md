# Implicit Neural Field-Based Process Planning for Multi-Axis Manufacturing: Direct Control over Collision Avoidance and Toolpath Geometry

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.17578)

## 요약
arXiv:2511.17578v1 Announce Type: new
Abstract: Existing curved-layer-based process planning methods for multi-axis manufacturing address collisions only indirectly and generate toolpaths in a post-processing step, leaving toolpath geometry uncontrolled during optimization. We present an implicit neural field-based framework for multi-axis process planning that overcomes these limitations by embedding both layer generation and toolpath design within a single differentiable pipeline. Using sinusoidally activated neural networks to represent layers and toolpaths as implicit fields, our method enables direct evaluation of field values and derivatives at any spatial point, thereby allowing explicit collision avoidance and joint optimization of manufacturing layers and toolpaths. We further investigate how network hyperparameters and objective definitions influence singularity behavior and topology transitions, offering built-in mechanisms for regularization and stability control. The proposed approach is demonstrated on examples in both additive and subtractive manufacturing, validating its generality and effectiveness.
