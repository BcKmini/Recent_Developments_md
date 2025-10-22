# VAR-SLAM: Visual Adaptive and Robust SLAM for Dynamic Environments

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.16205)

## 요약
arXiv:2510.16205v1 Announce Type: new
Abstract: Visual SLAM in dynamic environments remains challenging, as several existing methods rely on semantic filtering that only handles known object classes, or use fixed robust kernels that cannot adapt to unknown moving objects, leading to degraded accuracy when they appear in the scene. We present VAR-SLAM (Visual Adaptive and Robust SLAM), an ORB-SLAM3-based system that combines a lightweight semantic keypoint filter to deal with known moving objects, with Barron's adaptive robust loss to handle unknown ones. The shape parameter of the robust kernel is estimated online from residuals, allowing the system to automatically adjust between Gaussian and heavy-tailed behavior. We evaluate VAR-SLAM on the TUM RGB-D, Bonn RGB-D Dynamic, and OpenLORIS datasets, which include both known and unknown moving objects. Results show improved trajectory accuracy and robustness over state-of-the-art baselines, achieving up to 25% lower ATE RMSE than NGD-SLAM on challenging sequences, while maintaining performance at 27 FPS on average.
