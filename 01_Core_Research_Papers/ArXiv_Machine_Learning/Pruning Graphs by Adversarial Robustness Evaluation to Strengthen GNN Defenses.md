# Pruning Graphs by Adversarial Robustness Evaluation to Strengthen GNN Defenses

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.22128)

## 요약
arXiv:2512.22128v1 Announce Type: new
Abstract: Graph Neural Networks (GNNs) have emerged as a dominant paradigm for learning on graph-structured data, thanks to their ability to jointly exploit node features and relational information encoded in the graph topology. This joint modeling, however, also introduces a critical weakness: perturbations or noise in either the structure or the features can be amplified through message passing, making GNNs highly vulnerable to adversarial attacks and spurious connections. In this work, we introduce a pruning framework that leverages adversarial robustness evaluation to explicitly identify and remove fragile or detrimental components of the graph. By using robustness scores as guidance, our method selectively prunes edges that are most likely to degrade model reliability, thereby yielding cleaner and more resilient graph representations. We instantiate this framework on three representative GNN architectures and conduct extensive experiments on benchmarks. The experimental results show that our approach can significantly enhance the defense capability of GNNs in the high-perturbation regime.
