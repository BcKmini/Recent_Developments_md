# Learning Deformable Object Manipulation Using Task-Level Iterative Learning Control

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.21302)

## 요약
arXiv:2602.21302v1 Announce Type: new
Abstract: Dynamic manipulation of deformable objects is challenging for humans and robots because they have infinite degrees of freedom and exhibit underactuated dynamics. We introduce a Task-Level Iterative Learning Control method for dynamic manipulation of deformable objects. We demonstrate this method on a non-planar rope manipulation task called the flying knot. Using a single human demonstration and a simplified rope model, the method learns directly on hardware without reliance on large amounts of demonstration data or massive amounts of simulation. At each iteration, the algorithm constructs a local inverse model of the robot and rope by solving a quadratic program to propagate task-space errors into action updates. We evaluate performance across 7 different kinds of ropes, including chain, latex surgical tubing, and braided and twisted ropes, ranging in thicknesses of 7--25mm and densities of 0.013--0.5 kg/m. Learning achieves a 100\% success rate within 10 trials on all ropes. Furthermore, the method can successfully transfer between most rope types in approximately 2--5 trials. https://flying-knots.github.io
