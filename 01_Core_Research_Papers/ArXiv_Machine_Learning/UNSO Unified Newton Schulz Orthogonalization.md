# UNSO: Unified Newton Schulz Orthogonalization

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.02500)

## 요약
arXiv:2602.02500v1 Announce Type: new
Abstract: The Newton-Schulz (NS) iteration has gained increasing interest for its role in the Muon optimizer and the Stiefel manifold. However, the conventional NS iteration suffers from inefficiency and instability. Although various improvements have been introduced to NS iteration, they fail to deviate from the conventional iterative paradigm, which could increase computation burden largely due to the matrix products along the long dimension repeatedly. To address this, we consolidate the iterative structure into a unified framework, named Unified Newton-Schulz Orthogonalization (UNSO). To do so, we could avoid a polynomial expansion. Instead, we evaluate the role of each matrix power, remove the insignificant terms, and provide a recommended polynomial with learnable coefficients. These learnable coefficients are then optimized, and achieve an outstanding performance with stable convergence. The code of our method is available: https://github.com/greekinRoma/Unified\_Newton\_Schulz\_Orthogonalization.
