# Multiclass threshold-based classification and model evaluation

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.21794)

## 요약
arXiv:2511.21794v1 Announce Type: new
Abstract: In this paper, we introduce a threshold-based framework for multiclass classification that generalizes the standard argmax rule. This is done by replacing the probabilistic interpretation of softmax outputs with a geometric one on the multidimensional simplex, where the classification depends on a multidimensional threshold. This change of perspective enables for any trained classification network an \textit{a posteriori} optimization of the classification score by means of threshold tuning, as usually carried out in the binary setting, thus allowing for a further refinement of the prediction capability of any network. Our experiments show indeed that multidimensional threshold tuning yields performance improvements across various networks and datasets. Moreover, we derive a multiclass ROC analysis based on \emph{ROC clouds} -- the attainable (FPR,TPR) operating points induced by a single multiclass threshold -- and summarize them via a \emph{Distance From Point} (DFP) score to $(0,1)$. This yields a coherent alternative to standard One-vs-Rest (OvR) curves and aligns with the observed tuning gains.
