# A Framework for Combining Optimization-Based and Analytic Inverse Kinematics

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.05092)

## 요약
arXiv:2602.05092v1 Announce Type: new
Abstract: Analytic and optimization methods for solving inverse kinematics (IK) problems have been deeply studied throughout the history of robotics. The two strategies have complementary strengths and weaknesses, but developing a unified approach to take advantage of both methods has proved challenging. A key challenge faced by optimization approaches is the complicated nonlinear relationship between the joint angles and the end-effector pose. When this must be handled concurrently with additional nonconvex constraints like collision avoidance, optimization IK algorithms may suffer high failure rates. We present a new formulation for optimization IK that uses an analytic IK solution as a change of variables, and is fundamentally easier for optimizers to solve. We test our methodology on three popular solvers, representing three different paradigms for constrained nonlinear optimization. Extensive experimental comparisons demonstrate that our new formulation achieves higher success rates than the old formulation and baseline methods across various challenging IK problems, including collision avoidance, grasp selection, and humanoid stability.
