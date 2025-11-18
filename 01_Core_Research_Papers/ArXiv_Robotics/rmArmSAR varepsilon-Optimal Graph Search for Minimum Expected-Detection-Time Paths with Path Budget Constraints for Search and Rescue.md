# $\rm{A}^{\rm{SAR}}$: $\varepsilon$-Optimal Graph Search for Minimum Expected-Detection-Time Paths with Path Budget Constraints for Search and Rescue

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.10792)

## 요약
arXiv:2511.10792v1 Announce Type: new
Abstract: Searches are conducted to find missing persons and/or objects given uncertain information, imperfect observers and large search areas in Search and Rescue (SAR). In many scenarios, such as Maritime SAR, expected survival times are short and optimal search could increase the likelihood of success. This optimization problem is complex for nontrivial problems given its probabilistic nature.
Stochastic optimization methods search large problems by nondeterministically sampling the space to reduce the effective size of the problem. This has been used in SAR planning to search otherwise intractably large problems but the stochastic nature provides no formal guarantees on the quality of solutions found in finite time.
This paper instead presents $\rm{A}^{\rm{SAR}}$, an $\varepsilon$-optimal search algorithm for SAR planning. It calculates a heuristic to bound the search space and uses graph-search methods to find solutions that are formally guaranteed to be within a user-specified factor, $\varepsilon$, of the optimal solution. It finds better solutions faster than existing optimization approaches in operational simulations. It is also demonstrated with a real-world field trial on Lake Ontario, Canada, where it was used to locate a drifting manikin in only 150s.
