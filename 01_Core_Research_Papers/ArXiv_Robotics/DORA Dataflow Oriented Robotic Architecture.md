# DORA: Dataflow Oriented Robotic Architecture

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.13252)

## 요약
arXiv:2602.13252v1 Announce Type: new
Abstract: Robotic middleware serves as the foundational infrastructure, enabling complex robotic systems to operate in a coordinated and modular manner. In data-intensive robotic applications, especially in industrial scenarios, communication efficiency directly impact system responsiveness, stability, and overall productivity. However, existing robotic middleware exhibit several limitations: (1) they rely heavily on (de)serialization mechanisms, introducing significant overhead for large-sized data; (2) they lack efficient and flexible support for heterogeneous data sizes, particularly in intra-robot communication and Python-based execution environments. To address these challenges, we propose Dataflow-Oriented Robotic Architecture (DORA) that enables explicit data dependency specification and efficient zero-copy data transmission. We implement the proposed framework as an open-source system and evaluate it through extensive experiments in both simulation and real-world robotic environments. Experimental results demonstrate substantial reductions in latency and CPU overhead compared to state-of-the-art middleware.
