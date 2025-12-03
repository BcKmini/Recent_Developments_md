# Faster Verified Explanations for Neural Networks

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2512.00164)

## 요약
arXiv:2512.00164v1 Announce Type: new
Abstract: Verified explanations are a theoretically-principled way to explain the decisions taken by neural networks, which are otherwise black-box in nature. However, these techniques face significant scalability challenges, as they require multiple calls to neural network verifiers, each of them with an exponential worst-case complexity. We present FaVeX, a novel algorithm to compute verified explanations. FaVeX accelerates the computation by dynamically combining batch and sequential processing of input features, and by reusing information from previous queries, both when proving invariances with respect to certain input features, and when searching for feature assignments altering the prediction. Furthermore, we present a novel and hierarchical definition of verified explanations, termed verifier-optimal robust explanations, that explicitly factors the incompleteness of network verifiers within the explanation. Our comprehensive experimental evaluation demonstrates the superior scalability of both FaVeX, and of verifier-optimal robust explanations, which together can produce meaningful formal explanation on networks with hundreds of thousands of non-linear activations.
