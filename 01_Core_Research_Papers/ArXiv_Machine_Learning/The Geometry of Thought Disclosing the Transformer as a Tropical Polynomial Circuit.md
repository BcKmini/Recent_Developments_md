# The Geometry of Thought: Disclosing the Transformer as a Tropical Polynomial Circuit

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.09775)

## 요약
arXiv:2601.09775v1 Announce Type: new
Abstract: We prove that the Transformer self-attention mechanism in the high-confidence regime ($\beta \to \infty$, where $\beta$ is an inverse temperature) operates in the tropical semiring (max-plus algebra). In particular, we show that taking the tropical limit of the softmax attention converts it into a tropical matrix product. This reveals that the Transformer's forward pass is effectively executing a dynamic programming recurrence (specifically, a Bellman-Ford path-finding update) on a latent graph defined by token similarities. Our theoretical result provides a new geometric perspective for chain-of-thought reasoning: it emerges from an inherent shortest-path (or longest-path) algorithm being carried out within the network's computation.
