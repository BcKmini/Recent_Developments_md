# Lang2Manip: A Tool for LLM-Based Symbolic-to-Geometric Planning for Manipulation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.17062)

## 요약
arXiv:2512.17062v1 Announce Type: new
Abstract: Simulation is essential for developing robotic manipulation systems, particularly for task and motion planning (TAMP), where symbolic reasoning interfaces with geometric, kinematic, and physics-based execution. Recent advances in Large Language Models (LLMs) enable robots to generate symbolic plans from natural language, yet executing these plans in simulation often requires robot-specific engineering or planner-dependent integration. In this work, we present a unified pipeline that connects an LLM-based symbolic planner with the Kautham motion planning framework to achieve generalizable, robot-agnostic symbolic-to-geometric manipulation. Kautham provides ROS-compatible support for a wide range of industrial manipulators and offers geometric, kinodynamic, physics-driven, and constraint-based motion planning under a single interface. Our system converts language instructions into symbolic actions and computes and executes collision-free trajectories using any of Kautham's planners without additional coding. The result is a flexible and scalable tool for language-driven TAMP that is generalized across robots, planning modalities, and manipulation tasks.
