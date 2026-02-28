# Optimizing Neural Network Architecture for Medical Image Segmentation Using Monte Carlo Tree Search

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.22361)

## 요약
arXiv:2602.22361v1 Announce Type: new
Abstract: This paper proposes a novel medical image segmentation framework, MNAS-Unet, which combines Monte Carlo Tree Search (MCTS) and Neural Architecture Search (NAS). MNAS-Unet dynamically explores promising network architectures through MCTS, significantly enhancing the efficiency and accuracy of architecture search. It also optimizes the DownSC and UpSC unit structures, enabling fast and precise model adjustments. Experimental results demonstrate that MNAS-Unet outperforms NAS-Unet and other state-of-the-art models in segmentation accuracy on several medical image datasets, including PROMISE12, Ultrasound Nerve, and CHAOS. Furthermore, compared with NAS-Unet, MNAS-Unet reduces the architecture search budget by 54% (early stopping at 139 epochs versus 300 epochs under the same search setting), while achieving a lightweight model with only 0.6M parameters and lower GPU memory consumption, which further improves its practical applicability. These results suggest that MNAS-Unet can improve search efficiency while maintaining competitive segmentation accuracy under practical resource constraints.
