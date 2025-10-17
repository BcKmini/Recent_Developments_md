# Deep Edge Filter: Return of the Human-Crafted Layer in Deep Learning

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2510.13865)

## 요약
arXiv:2510.13865v1 Announce Type: new
Abstract: We introduce the Deep Edge Filter, a novel approach that applies high-pass filtering to deep neural network features to improve model generalizability. Our method is motivated by our hypothesis that neural networks encode task-relevant semantic information in high-frequency components while storing domain-specific biases in low-frequency components of deep features. By subtracting low-pass filtered outputs from original features, our approach isolates generalizable representations while preserving architectural integrity. Experimental results across diverse domains such as Vision, Text, 3D, and Audio demonstrate consistent performance improvements regardless of model architecture and data modality. Analysis reveals that our method induces feature sparsification and effectively isolates high-frequency components, providing empirical validation of our core hypothesis. The code is available at https://github.com/dongkwani/DeepEdgeFilter.
