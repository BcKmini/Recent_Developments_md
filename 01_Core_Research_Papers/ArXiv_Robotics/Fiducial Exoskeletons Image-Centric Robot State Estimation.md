# Fiducial Exoskeletons: Image-Centric Robot State Estimation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.08034)

## 요약
arXiv:2601.08034v1 Announce Type: new
Abstract: We introduce Fiducial Exoskeletons, an image-based reformulation of 3D robot state estimation that replaces cumbersome procedures and motor-centric pipelines with single-image inference. Traditional approaches - especially robot-camera extrinsic estimation - often rely on high-precision actuators and require time-consuming routines such as hand-eye calibration. In contrast, modern learning-based robot control is increasingly trained and deployed from RGB observations on lower-cost hardware.
Our key insight is twofold. First, we cast robot state estimation as 6D pose estimation of each link from a single RGB image: the robot-camera base transform is obtained directly as the estimated base-link pose, and the joint state is recovered via a lightweight global optimization that enforces kinematic consistency with the observed link poses (optionally warm-started with encoder readings). Second, we make per-link 6D pose estimation robust and simple - even without learning - by introducing the fiducial exoskeleton: a lightweight 3D-printed mount with a fiducial marker on each link and known marker-link geometry.
This design yields robust camera-robot extrinsics, per-link SE(3) poses, and joint-angle state from a single image, enabling robust state estimation even on unplugged robots. Demonstrated on a low-cost robot arm, fiducial exoskeletons substantially simplify setup while improving calibration, state accuracy, and downstream 3D control performance. We release code and printable hardware designs to enable further algorithm-hardware co-design.
