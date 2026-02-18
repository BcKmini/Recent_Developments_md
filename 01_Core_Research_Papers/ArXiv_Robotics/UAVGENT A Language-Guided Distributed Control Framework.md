# UAVGENT: A Language-Guided Distributed Control Framework

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2602.13212)

## 요약
arXiv:2602.13212v1 Announce Type: new
Abstract: We study language-in-the-loop control for multi-drone systems that execute evolving, high-level missions while retaining formal robustness guarantees at the physical layer. We propose a three-layer architecture in which (i) a human operator issues natural-language instructions, (ii) an LLM-based supervisor periodically interprets, verifies, and corrects the commanded task in the context of the latest state and target estimates, and (iii) a distributed inner-loop controller tracks the resulting reference using only local relative information. We derive a theoretical guarantee that characterizes tracking performance under bounded disturbances and piecewise-smooth references with discrete jumps induced by LLM updates. Overall, our results illustrate how centralized language-based task reasoning can be combined with distributed feedback control to achieve complex behaviors with provable robustness and stability.
