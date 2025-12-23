# Dion2: A Simple Method to Shrink Matrix in Muon

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.16928)

## 요약
arXiv:2512.16928v1 Announce Type: new
Abstract: The Muon optimizer enjoys strong empirical performance and theoretical grounding. However, the super-linear cost of its orthonormalization step introduces increasing overhead with scale. To alleviate this cost, several works have attempted to reduce the size of the matrix entering the orthonormalization step. We introduce Dion2, a much simpler method for shrinking the matrix involved in Muon's computation compared to prior approaches. At a high level, Dion2 selects a fraction of rows or columns at each iteration and orthonormalizes only those. This sampling procedure makes the update sparse, reducing both computation and communication costs which in turn improves the scalability of Muon.
