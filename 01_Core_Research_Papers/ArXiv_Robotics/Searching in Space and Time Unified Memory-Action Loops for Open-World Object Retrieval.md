# Searching in Space and Time: Unified Memory-Action Loops for Open-World Object Retrieval

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.14004)

## 요약
arXiv:2511.14004v1 Announce Type: new
Abstract: Service robots must retrieve objects in dynamic, open-world settings where requests may reference attributes ("the red mug"), spatial context ("the mug on the table"), or past states ("the mug that was here yesterday"). Existing approaches capture only parts of this problem: scene graphs capture spatial relations but ignore temporal grounding, temporal reasoning methods model dynamics but do not support embodied interaction, and dynamic scene graphs handle both but remain closed-world with fixed vocabularies. We present STAR (SpatioTemporal Active Retrieval), a framework that unifies memory queries and embodied actions within a single decision loop. STAR leverages non-parametric long-term memory and a working memory to support efficient recall, and uses a vision-language model to select either temporal or spatial actions at each step. We introduce STARBench, a benchmark of spatiotemporal object search tasks across simulated and real environments. Experiments in STARBench and on a Tiago robot show that STAR consistently outperforms scene-graph and memory-only baselines, demonstrating the benefits of treating search in time and search in space as a unified problem.
