# Compressed Map Priors for 3D Perception

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.00139)

## 요약
arXiv:2601.00139v1 Announce Type: new
Abstract: Human drivers rarely travel where no person has gone before. After all, thousands of drivers use busy city roads every day, and only one can claim to be the first. The same holds for autonomous computer vision systems. The vast majority of the deployment area of an autonomous vision system will have been visited before. Yet, most autonomous vehicle vision systems act as if they are encountering each location for the first time. In this work, we present Compressed Map Priors (CMP), a simple but effective framework to learn spatial priors from historic traversals. The map priors use a binarized hashmap that requires only $32\text{KB}/\text{km}^2$, a $20\times$ reduction compared to the dense storage. Compressed Map Priors easily integrate into leading 3D perception systems at little to no extra computational costs, and lead to a significant and consistent improvement in 3D object detection on the nuScenes dataset across several architectures.
