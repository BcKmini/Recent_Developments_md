# Online Learning-Enhanced High Order Adaptive Safety Control

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.19651)

## 요약
arXiv:2511.19651v1 Announce Type: new
Abstract: Control barrier functions (CBFs) are an effective model-based tool to formally certify the safety of a system. With the growing complexity of modern control problems, CBFs have received increasing attention in both optimization-based and learning-based control communities as a safety filter, owing to their provable guarantees. However, success in transferring these guarantees to real-world systems is critically tied to model accuracy. For example, payloads or wind disturbances can significantly influence the dynamics of an aerial vehicle and invalidate the safety guarantee. In this work, we propose an efficient yet flexible online learning-enhanced high-order adaptive control barrier function using Neural ODEs. Our approach improves the safety of a CBF-certified system on the fly, even under complex time-varying model perturbations. In particular, we deploy our hybrid adaptive CBF controller on a 38g nano quadrotor, keeping a safe distance from the obstacle, against 18km/h wind.
