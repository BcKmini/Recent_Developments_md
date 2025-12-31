# Joint UAV-UGV Positioning and Trajectory Planning via Meta A3C for Reliable Emergency Communications

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.22187)

## 요약
arXiv:2512.22187v1 Announce Type: new
Abstract: Joint deployment of unmanned aerial vehicles (UAVs) and unmanned ground vehicles (UGVs) has been shown to be an effective method to establish communications in areas affected by disasters. However, ensuring good Quality of Services (QoS) while using as few UAVs as possible also requires optimal positioning and trajectory planning for UAVs and UGVs. This paper proposes a joint UAV-UGV-based positioning and trajectory planning framework for UAVs and UGVs deployment that guarantees optimal QoS for ground users. To model the UGVs' mobility, we introduce a road graph, which directs their movement along valid road segments and adheres to the road network constraints. To solve the sum rate optimization problem, we reformulate the problem as a Markov Decision Process (MDP) and propose a novel asynchronous Advantage Actor Critic (A3C) incorporated with meta-learning for rapid adaptation to new environments and dynamic conditions. Numerical results demonstrate that our proposed Meta-A3C approach outperforms A3C and DDPG, delivering 13.1\% higher throughput and 49\% faster execution while meeting the QoS requirements.
