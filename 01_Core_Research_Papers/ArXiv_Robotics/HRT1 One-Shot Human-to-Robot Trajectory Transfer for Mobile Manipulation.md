# HRT1: One-Shot Human-to-Robot Trajectory Transfer for Mobile Manipulation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.21026)

## 요약
arXiv:2510.21026v1 Announce Type: new
Abstract: We introduce a novel system for human-to-robot trajectory transfer that enables robots to manipulate objects by learning from human demonstration videos. The system consists of four modules. The first module is a data collection module that is designed to collect human demonstration videos from the point of view of a robot using an AR headset. The second module is a video understanding module that detects objects and extracts 3D human-hand trajectories from demonstration videos. The third module transfers a human-hand trajectory into a reference trajectory of a robot end-effector in 3D space. The last module utilizes a trajectory optimization algorithm to solve a trajectory in the robot configuration space that can follow the end-effector trajectory transferred from the human demonstration. Consequently, these modules enable a robot to watch a human demonstration video once and then repeat the same mobile manipulation task in different environments, even when objects are placed differently from the demonstrations. Experiments of different manipulation tasks are conducted on a mobile manipulator to verify the effectiveness of our system
