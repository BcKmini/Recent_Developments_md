# Motion Planning and Control of an Overactuated 4-Wheel Drive with Constrained Independent Steering

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.19054)

## 요약
arXiv:2510.19054v1 Announce Type: new
Abstract: This paper addresses motion planning and con- trol of an overactuated 4-wheel drive train with independent steering (4WIS) where mechanical constraints prevent the wheels from executing full 360-degree rotations (swerve). The configuration space of such a robot is constrained and contains discontinuities that affect the smoothness of the robot motion. We introduce a mathematical formulation of the steering constraints and derive discontinuity planes that partition the velocity space into regions of smooth and efficient motion. We further design the motion planner for path tracking and ob- stacle avoidance that explicitly accounts for swerve constraints and the velocity transition smoothness. The motion controller uses local feedback to generate actuation from the desired velocity, while properly handling the discontinuity crossing by temporarily stopping the motion and repositioning the wheels. We implement the proposed motion planner as an extension to ROS Navigation package and evaluate the system in simulation and on a physical robot.
