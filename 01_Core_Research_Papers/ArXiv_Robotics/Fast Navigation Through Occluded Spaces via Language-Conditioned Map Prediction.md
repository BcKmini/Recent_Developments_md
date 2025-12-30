# Fast Navigation Through Occluded Spaces via Language-Conditioned Map Prediction

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.21398)

## 요약
arXiv:2512.21398v1 Announce Type: new
Abstract: In cluttered environments, motion planners often face a trade-off between safety and speed due to uncertainty caused by occlusions and limited sensor range. In this work, we investigate whether co-pilot instructions can help robots plan more decisively while remaining safe. We introduce PaceForecaster, as an approach that incorporates such co-pilot instructions into local planners. PaceForecaster takes the robot's local sensor footprint (Level-1) and the provided co-pilot instructions as input and predicts (i) a forecasted map with all regions visible from Level-1 (Level-2) and (ii) an instruction-conditioned subgoal within Level-2. The subgoal provides the planner with explicit guidance to exploit the forecasted environment in a goal-directed manner. We integrate PaceForecaster with a Log-MPPI controller and demonstrate that using language-conditioned forecasts and goals improves navigation performance by 36% over a local-map-only baseline while in polygonal environments.
