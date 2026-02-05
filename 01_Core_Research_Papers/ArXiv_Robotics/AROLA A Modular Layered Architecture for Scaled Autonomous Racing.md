# AROLA: A Modular Layered Architecture for Scaled Autonomous Racing

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.02730)

## 요약
arXiv:2602.02730v1 Announce Type: new
Abstract: Autonomous racing has advanced rapidly, particularly on scaled platforms, and software stacks must evolve accordingly. In this work, AROLA is introduced as a modular, layered software architecture in which fragmented and monolithic designs are reorganized into interchangeable layers and components connected through standardized ROS 2 interfaces. The autonomous-driving pipeline is decomposed into sensing, pre-processing, perception, localization and mapping, planning, behavior, control, and actuation, enabling rapid module replacement and objective benchmarking without reliance on custom message definitions. To support consistent performance evaluation, a Race Monitor framework is introduced as a lightweight system through which lap timing, trajectory quality, and computational load are logged in real time and standardized post-race analyses are generated. AROLA is validated in simulation and on hardware using the RoboRacer platform, including deployment at the 2025 RoboRacer IV25 competition. Together, AROLA and Race Monitor demonstrate that modularity, transparent interfaces, and systematic evaluation can accelerate development and improve reproducibility in scaled autonomous racing.
