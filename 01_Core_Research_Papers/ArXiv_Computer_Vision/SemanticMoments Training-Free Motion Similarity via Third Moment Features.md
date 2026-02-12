# SemanticMoments: Training-Free Motion Similarity via Third Moment Features

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.09146)

## 요약
arXiv:2602.09146v1 Announce Type: new
Abstract: Retrieving videos based on semantic motion is a fundamental, yet unsolved, problem. Existing video representation approaches overly rely on static appearance and scene context rather than motion dynamics, a bias inherited from their training data and objectives. Conversely, traditional motion-centric inputs like optical flow lack the semantic grounding needed to understand high-level motion. To demonstrate this inherent bias, we introduce the SimMotion benchmarks, combining controlled synthetic data with a new human-annotated real-world dataset. We show that existing models perform poorly on these benchmarks, often failing to disentangle motion from appearance. To address this gap, we propose SemanticMoments, a simple, training-free method that computes temporal statistics (specifically, higher-order moments) over features from pre-trained semantic models. Across our benchmarks, SemanticMoments consistently outperforms existing RGB, flow, and text-supervised methods. This demonstrates that temporal statistics in a semantic feature space provide a scalable and perceptually grounded foundation for motion-centric video understanding.
