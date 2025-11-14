# Assessing Identity Leakage in Talking Face Generation: Metrics and Evaluation Framework

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2511.08613)

## 요약
arXiv:2511.08613v1 Announce Type: new
Abstract: Inpainting-based talking face generation aims to preserve video details such as pose, lighting, and gestures while modifying only lip motion, often using an identity reference image to maintain speaker consistency. However, this mechanism can introduce lip leaking, where generated lips are influenced by the reference image rather than solely by the driving audio. Such leakage is difficult to detect with standard metrics and conventional test setup. To address this, we propose a systematic evaluation methodology to analyze and quantify lip leakage. Our framework employs three complementary test setups: silent-input generation, mismatched audio-video pairing, and matched audio-video synthesis. We also introduce derived metrics including lip-sync discrepancy and silent-audio-based lip-sync scores. In addition, we study how different identity reference selections affect leakage, providing insights into reference design. The proposed methodology is model-agnostic and establishes a more reliable benchmark for future research in talking face generation.
