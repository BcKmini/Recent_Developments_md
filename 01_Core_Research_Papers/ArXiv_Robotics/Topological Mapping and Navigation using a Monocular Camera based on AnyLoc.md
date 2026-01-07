# Topological Mapping and Navigation using a Monocular Camera based on AnyLoc

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.01067)

## 요약
arXiv:2601.01067v1 Announce Type: new
Abstract: This paper proposes a method for topological mapping and navigation using a monocular camera. Based on AnyLoc, keyframes are converted into descriptors to construct topological relationships, enabling loop detection and map building. Unlike metric maps, topological maps simplify path planning and navigation by representing environments with key nodes instead of precise coordinates. Actions for visual navigation are determined by comparing segmented images with the image associated with target nodes. The system relies solely on a monocular camera, ensuring fast map building and navigation using key nodes. Experiments show effective loop detection and navigation in real and simulation environments without pre-training. Compared to a ResNet-based method, this approach improves success rates by 60.2% on average while reducing time and space costs, offering a lightweight solution for robot and human navigation in various scenarios.
