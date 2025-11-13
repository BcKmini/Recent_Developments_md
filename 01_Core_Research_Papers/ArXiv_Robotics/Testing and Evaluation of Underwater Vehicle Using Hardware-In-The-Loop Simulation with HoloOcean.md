# Testing and Evaluation of Underwater Vehicle Using Hardware-In-The-Loop Simulation with HoloOcean

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.07687)

## 요약
arXiv:2511.07687v1 Announce Type: new
Abstract: Testing marine robotics systems in controlled environments before field tests is challenging, especially when acoustic-based sensors and control surfaces only function properly underwater. Deploying robots in indoor tanks and pools often faces space constraints that complicate testing of control, navigation, and perception algorithms at scale. Recent developments of high-fidelity underwater simulation tools have the potential to address these problems. We demonstrate the utility of the recently released HoloOcean 2.0 simulator with improved dynamics for torpedo AUV vehicles and a new ROS 2 interface. We have successfully demonstrated a Hardware-in-the-Loop (HIL) and Software-in-the-Loop (SIL) setup for testing and evaluating a CougUV torpedo autonomous underwater vehicle (AUV) that was built and developed in our lab. With this HIL and SIL setup, simulations are run in HoloOcean using a ROS 2 bridge such that simulated sensor data is sent to the CougUV (mimicking sensor drivers) and control surface commands are sent back to the simulation, where vehicle dynamics and sensor data are calculated. We compare our simulated results to real-world field trial results.
