# Prototype-Guided Non-Exemplar Continual Learning for Cross-subject EEG Decoding

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2511.20696)

## 요약
arXiv:2511.20696v1 Announce Type: new
Abstract: Due to the significant variability in electroencephalogram (EEG) signals across individuals, knowledge acquired from previous subjects is often overwritten as new subjects are introduced in continual EEG decoding task. Current works mainly rely on storing the historical data of seen subjects as a replay buffer to prevent forgetting. However, privacy concerns or memory constraints make keeping such data impractical. Instead, we propose a Prototype-guided Non-Exemplar Continual Learning (ProNECL)framework that preserves prior knowledge without accessing any historical EEG samples. ProNECL constructs class-level prototypes to summarize discriminative representations from each subject and incrementally aligns new feature spaces with the global prototype memory through cross-subject feature alignment and knowledge distillation. Validated on the BCI Competition IV 2a and 2b datasets, our framework effectively balances knowledge retention and adaptability, achieving superior performance in cross-subject continual EEG decoding tasks.
