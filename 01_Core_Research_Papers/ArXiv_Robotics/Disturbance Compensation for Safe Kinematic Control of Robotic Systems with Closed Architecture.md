# Disturbance Compensation for Safe Kinematic Control of Robotic Systems with Closed Architecture

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.05292)

## 요약
arXiv:2512.05292v1 Announce Type: new
Abstract: In commercial robotic systems, it is common to encounter a closed inner-loop torque controller that is not user-modifiable. However, the outer-loop controller, which sends kinematic commands such as position or velocity for the inner-loop controller to track, is typically exposed to users. In this work, we focus on the development of an easily integrated add-on at the outer-loop layer by combining disturbance rejection control and robust control barrier function for high-performance tracking and safe control of the whole dynamic system of an industrial manipulator. This is particularly beneficial when 1) the inner-loop controller is imperfect, unmodifiable, and uncertain; and 2) the dynamic model exhibits significant uncertainty. Stability analysis, formal safety guarantee proof, and hardware experiments with a PUMA robotic manipulator are presented. Our solution demonstrates superior performance in terms of simplicity of implementation, robustness, tracking precision, and safety compared to the state of the art. Video: https://youtu.be/zw1tanvrV8Q
