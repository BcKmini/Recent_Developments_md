# RANSAC Scoring Functions: Analysis and Reality Check

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.19850)

## 요약
arXiv:2512.19850v1 Announce Type: new
Abstract: We revisit the problem of assigning a score (a quality of fit) to candidate geometric models -- one of the key components of RANSAC for robust geometric fitting. In a non-robust setting, the ``gold standard'' scoring function, known as the geometric error, follows from a probabilistic model with Gaussian noises. We extend it to spherical noises. In a robust setting, we consider a mixture with uniformly distributed outliers and show that a threshold-based parameterization leads to a unified view of likelihood-based and robust M-estimators and associated local optimization schemes.
Next we analyze MAGSAC++ which stands out for two reasons. First, it achieves the best results according to existing benchmarks. Second, it makes quite different modeling assumptions and derivation steps. We discovered, however that the derivation does not correspond to sound principles and the resulting score function is in fact numerically equivalent to a simple Gaussian-uniform likelihood, a basic model within the proposed framework.
Finally, we propose an experimental methodology for evaluating scoring functions: assuming either a large validation set, or a small random validation set in expectation. We find that all scoring functions, including using a learned inlier distribution, perform identically. In particular, MAGSAC++ score is found to be neither better performing than simple contenders nor less sensitive to the choice of the threshold hyperparameter.
Our theoretical and experimental analysis thus comprehensively revisit the state-of-the-art, which is critical for any future research seeking to improve the methods or apply them to other robust fitting problems.
