# R2BC: Multi-Agent Imitation Learning from Single-Agent Demonstrations

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2510.18085)

## 요약
arXiv:2510.18085v1 Announce Type: new
Abstract: Imitation Learning (IL) is a natural way for humans to teach robots, particularly when high-quality demonstrations are easy to obtain. While IL has been widely applied to single-robot settings, relatively few studies have addressed the extension of these methods to multi-agent systems, especially in settings where a single human must provide demonstrations to a team of collaborating robots. In this paper, we introduce and study Round-Robin Behavior Cloning (R2BC), a method that enables a single human operator to effectively train multi-robot systems through sequential, single-agent demonstrations. Our approach allows the human to teleoperate one agent at a time and incrementally teach multi-agent behavior to the entire system, without requiring demonstrations in the joint multi-agent action space. We show that R2BC methods match, and in some cases surpass, the performance of an oracle behavior cloning approach trained on privileged synchronized demonstrations across four multi-agent simulated tasks. Finally, we deploy R2BC on two physical robot tasks trained using real human demonstrations.
