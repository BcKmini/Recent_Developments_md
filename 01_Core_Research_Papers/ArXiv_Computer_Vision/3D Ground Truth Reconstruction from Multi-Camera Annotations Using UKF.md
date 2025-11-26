# 3D Ground Truth Reconstruction from Multi-Camera Annotations Using UKF

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.17609)

## 요약
arXiv:2511.17609v1 Announce Type: new
Abstract: Accurate 3D ground truth estimation is critical for applications such as autonomous navigation, surveillance, and robotics. This paper introduces a novel method that uses an Unscented Kalman Filter (UKF) to fuse 2D bounding box or pose keypoint ground truth annotations from multiple calibrated cameras into accurate 3D ground truth. By leveraging human-annotated ground-truth 2D, our proposed method, a multi-camera single-object tracking algorithm, transforms 2D image coordinates into robust 3D world coordinates through homography-based projection and UKF-based fusion. Our proposed algorithm processes multi-view data to estimate object positions and shapes while effectively handling challenges such as occlusion. We evaluate our method on the CMC, Wildtrack, and Panoptic datasets, demonstrating high accuracy in 3D localization compared to the available 3D ground truth. Unlike existing approaches that provide only ground-plane information, our method also outputs the full 3D shape of each object. Additionally, the algorithm offers a scalable and fully automatic solution for multi-camera systems using only 2D image annotations.
