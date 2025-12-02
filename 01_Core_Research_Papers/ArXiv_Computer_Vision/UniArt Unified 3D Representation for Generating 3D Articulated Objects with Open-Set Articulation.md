# UniArt: Unified 3D Representation for Generating 3D Articulated Objects with Open-Set Articulation

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.21887)

## 요약
arXiv:2511.21887v1 Announce Type: new
Abstract: Articulated 3D objects play a vital role in realistic simulation and embodied robotics, yet manually constructing such assets remains costly and difficult to scale. In this paper, we present UniArt, a diffusion-based framework that directly synthesizes fully articulated 3D objects from a single image in an end-to-end manner. Unlike prior multi-stage techniques, UniArt establishes a unified latent representation that jointly encodes geometry, texture, part segmentation, and kinematic parameters. We introduce a reversible joint-to-voxel embedding, which spatially aligns articulation features with volumetric geometry, enabling the model to learn coherent motion behaviors alongside structural formation. Furthermore, we formulate articulation type prediction as an open-set problem, removing the need for fixed joint semantics and allowing generalization to novel joint categories and unseen object types. Experiments on the PartNet-Mobility benchmark demonstrate that UniArt achieves state-of-the-art mesh quality and articulation accuracy.
