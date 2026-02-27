# CableRobotGraphSim: A Graph Neural Network for Modeling Partially Observable Cable-Driven Robot Dynamics

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.21331)

## 요약
arXiv:2602.21331v1 Announce Type: new
Abstract: General-purpose simulators have accelerated the development of robots. Traditional simulators based on first-principles, however, typically require full-state observability or depend on parameter search for system identification. This work presents \texttt{CableRobotGraphSim}, a novel Graph Neural Network (GNN) model for cable-driven robots that aims to address shortcomings of prior simulation solutions. By representing cable-driven robots as graphs, with the rigid-bodies as nodes and the cables and contacts as edges, this model can quickly and accurately match the properties of other simulation models and real robots, while ingesting only partially observable inputs. Accompanying the GNN model is a sim-and-real co-training procedure that promotes generalization and robustness to noisy real data. This model is further integrated with a Model Predictive Path Integral (MPPI) controller for closed-loop navigation, which showcases the model's speed and accuracy.
