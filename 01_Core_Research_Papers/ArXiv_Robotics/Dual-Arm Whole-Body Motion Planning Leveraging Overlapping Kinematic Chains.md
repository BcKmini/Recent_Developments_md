# Dual-Arm Whole-Body Motion Planning: Leveraging Overlapping Kinematic Chains

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.08778)

## 요약
arXiv:2511.08778v1 Announce Type: new
Abstract: High degree-of-freedom dual-arm robots are becoming increasingly common due to their morphology enabling them to operate effectively in human environments. However, motion planning in real-time within unknown, changing environments remains a challenge for such robots due to the high dimensionality of the configuration space and the complex collision-avoidance constraints that must be obeyed. In this work, we propose a novel way to alleviate the curse of dimensionality by leveraging the structure imposed by shared joints (e.g. torso joints) in a dual-arm robot. First, we build two dynamic roadmaps (DRM) for each kinematic chain (i.e. left arm + torso, right arm + torso) with specific structure induced by the shared joints. Then, we show that we can leverage this structure to efficiently search through the composition of the two roadmaps and largely sidestep the curse of dimensionality. Finally, we run several experiments in a real-world grocery store with this motion planner on a 19 DoF mobile manipulation robot executing a grocery fulfillment task, achieving 0.4s average planning times with 99.9% success rate across more than 2000 motion plans.
