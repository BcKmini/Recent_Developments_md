# Tree-Preconditioned Differentiable Optimization and Axioms as Layers

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.06036)

## 요약
arXiv:2601.06036v1 Announce Type: new
Abstract: This paper introduces a differentiable framework that embeds the axiomatic structure of Random Utility Models (RUM) directly into deep neural networks. Although projecting empirical choice data onto the RUM polytope is NP-hard in general, we uncover an isomorphism between RUM consistency and flow conservation on the Boolean lattice. Leveraging this combinatorial structure, we derive a novel Tree-Preconditioned Conjugate Gradient solver. By exploiting the spanning tree of the constraint graph, our preconditioner effectively "whitens" the ill-conditioned Hessian spectrum induced by the Interior Point Method barrier, achieving superlinear convergence and scaling to problem sizes previously deemed unsolvable. We further formulate the projection as a differentiable layer via the Implicit Function Theorem, where the exact Jacobian propagates geometric constraints during backpropagation. Empirical results demonstrate that this "Axioms-as-Layers" paradigm eliminates the structural overfitting inherent in penalty-based methods, enabling models that are jointly trainable, provably rational, and capable of generalizing from sparse data regimes where standard approximations fail.
