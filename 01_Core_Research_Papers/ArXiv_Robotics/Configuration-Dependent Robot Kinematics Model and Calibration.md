# Configuration-Dependent Robot Kinematics Model and Calibration

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.19962)

## 요약
arXiv:2510.19962v1 Announce Type: new
Abstract: Accurate robot kinematics is essential for precise tool placement in articulated robots, but non-geometric factors can introduce configuration-dependent model discrepancies. This paper presents a configuration-dependent kinematic calibration framework for improving accuracy across the entire workspace. Local Product-of-Exponential (POE) models, selected for their parameterization continuity, are identified at multiple configurations and interpolated into a global model. Inspired by joint gravity load expressions, we employ Fourier basis function interpolation parameterized by the shoulder and elbow joint angles, achieving accuracy comparable to neural network and autoencoder methods but with substantially higher training efficiency. Validation on two 6-DoF industrial robots shows that the proposed approach reduces the maximum positioning error by over 50%, meeting the sub-millimeter accuracy required for cold spray manufacturing. Robots with larger configuration-dependent discrepancies benefit even more. A dual-robot collaborative task demonstrates the framework's practical applicability and repeatability.
