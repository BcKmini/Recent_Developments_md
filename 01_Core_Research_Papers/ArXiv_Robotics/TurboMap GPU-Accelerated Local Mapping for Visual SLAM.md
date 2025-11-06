# TurboMap: GPU-Accelerated Local Mapping for Visual SLAM

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2511.02036)

## 요약
arXiv:2511.02036v1 Announce Type: new
Abstract: This paper presents TurboMap, a GPU-accelerated and CPU-optimized local mapping module for visual SLAM systems. We identify key performance bottlenecks in the local mapping process for visual SLAM and address them through targeted GPU and CPU optimizations. Specifically, we offload map point triangulation and fusion to the GPU, accelerate redundant keyframe culling on the CPU, and integrate a GPU-accelerated solver to speed up local bundle adjustment. Our implementation is built on top of ORB-SLAM3 and leverages CUDA for GPU programming. The experimental results show that TurboMap achieves an average speedup of 1.3x in the EuRoC dataset and 1.6x in the TUM-VI dataset in the local mapping module, on both desktop and embedded platforms, while maintaining the accuracy of the original system.
