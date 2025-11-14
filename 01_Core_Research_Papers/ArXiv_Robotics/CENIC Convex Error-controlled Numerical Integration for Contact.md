# CENIC: Convex Error-controlled Numerical Integration for Contact

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.08771)

## 요약
arXiv:2511.08771v1 Announce Type: new
Abstract: State-of-the-art robotics simulators operate in discrete time. This requires users to choose a time step, which is both critical and challenging: large steps can produce non-physical artifacts, while small steps force the simulation to run slowly. Continuous-time error-controlled integration avoids such issues by automatically adjusting the time step to achieve a desired accuracy. But existing error-controlled integrators struggle with the stiff dynamics of contact, and cannot meet the speed and scalability requirements of modern robotics workflows. We introduce CENIC, a new continuous-time integrator that brings together recent advances in convex time-stepping and error-controlled integration, inheriting benefits from both continuous integration and discrete time-stepping. CENIC runs at fast real-time rates comparable to discrete-time robotics simulators like MuJoCo, Drake and Isaac Sim, while also providing guarantees on accuracy and convergence.
