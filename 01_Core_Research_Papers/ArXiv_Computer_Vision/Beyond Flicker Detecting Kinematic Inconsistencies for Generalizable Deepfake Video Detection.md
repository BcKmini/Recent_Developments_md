# Beyond Flicker: Detecting Kinematic Inconsistencies for Generalizable Deepfake Video Detection

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2512.04175)

## 요약
arXiv:2512.04175v1 Announce Type: new
Abstract: Generalizing deepfake detection to unseen manipulations remains a key challenge. A recent approach to tackle this issue is to train a network with pristine face images that have been manipulated with hand-crafted artifacts to extract more generalizable clues. While effective for static images, extending this to the video domain is an open issue. Existing methods model temporal artifacts as frame-to-frame instabilities, overlooking a key vulnerability: the violation of natural motion dependencies between different facial regions. In this paper, we propose a synthetic video generation method that creates training data with subtle kinematic inconsistencies. We train an autoencoder to decompose facial landmark configurations into motion bases. By manipulating these bases, we selectively break the natural correlations in facial movements and introduce these artifacts into pristine videos via face morphing. A network trained on our data learns to spot these sophisticated biomechanical flaws, achieving state-of-the-art generalization results on several popular benchmarks.
