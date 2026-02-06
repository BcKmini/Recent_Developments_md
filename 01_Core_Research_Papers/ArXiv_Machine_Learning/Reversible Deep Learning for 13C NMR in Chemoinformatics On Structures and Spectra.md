# Reversible Deep Learning for 13C NMR in Chemoinformatics: On Structures and Spectra

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.03875)

## 요약
arXiv:2602.03875v1 Announce Type: new
Abstract: We introduce a reversible deep learning model for 13C NMR that uses a single conditional invertible neural network for both directions between molecular structures and spectra. The network is built from i-RevNet style bijective blocks, so the forward map and its inverse are available by construction. We train the model to predict a 128-bit binned spectrum code from a graph-based structure encoding, while the remaining latent dimensions capture residual variability. At inference time, we invert the same trained network to generate structure candidates from a spectrum code, which explicitly represents the one-to-many nature of spectrum-to-structure inference. On a filtered subset, the model is numerically invertible on trained examples, achieves spectrum-code prediction above chance, and produces coarse but meaningful structural signals when inverted on validation spectra. These results demonstrate that invertible architectures can unify spectrum prediction and uncertainty-aware candidate generation within one end-to-end model.
