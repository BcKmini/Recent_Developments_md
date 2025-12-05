# GOMP: Grasped Object Manifold Projection for Multimodal Imitation Learning of Manipulation

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2512.03347)

## 요약
arXiv:2512.03347v1 Announce Type: new
Abstract: Imitation Learning (IL) holds great potential for learning repetitive manipulation tasks, such as those in industrial assembly. However, its effectiveness is often limited by insufficient trajectory precision due to compounding errors. In this paper, we introduce Grasped Object Manifold Projection (GOMP), an interactive method that mitigates these errors by constraining a non-rigidly grasped object to a lower-dimensional manifold. GOMP assumes a precise task in which a manipulator holds an object that may shift within the grasp in an observable manner and must be mated with a grounded part. Crucially, all GOMP enhancements are learned from the same expert dataset used to train the base IL policy, and are adjusted with an n-arm bandit-based interactive component. We propose a theoretical basis for GOMP's improvement upon the well-known compounding error bound in IL literature. We demonstrate the framework on four precise assembly tasks using tactile feedback, and note that the approach remains modality-agnostic. Data and videos are available at williamvdb.github.io/GOMPsite.
