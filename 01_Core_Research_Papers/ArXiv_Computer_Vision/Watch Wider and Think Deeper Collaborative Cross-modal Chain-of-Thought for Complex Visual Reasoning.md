# Watch Wider and Think Deeper: Collaborative Cross-modal Chain-of-Thought for Complex Visual Reasoning

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2601.02422)

## 요약
arXiv:2601.02422v1 Announce Type: new
Abstract: Multi-modal reasoning requires the seamless integration of visual and linguistic cues, yet existing Chain-of-Thought methods suffer from two critical limitations in cross-modal scenarios: (1) over-reliance on single coarse-grained image regions, and (2) semantic fragmentation between successive reasoning steps. To address these issues, we propose the CoCoT (Collaborative Coross-modal Thought) frame- work, built upon two key innovations: a) Dynamic Multi-Region Grounding to adaptively detect the most relevant image regions based on the question, and b) Relation-Aware Reasoning to enable multi-region collaboration by iteratively align- ing visual cues to form a coherent and logical chain of thought. Through this approach, we construct the CoCoT-70K dataset, comprising 74,691 high-quality samples with multi-region annotations and structured reasoning chains. Extensive experiments demonstrate that CoCoT significantly enhances complex visual rea- soning, achieving an average accuracy improvement of 15.4% on LLaVA-1.5 and 4.0% on Qwen2-VL across six challenging benchmarks. The data and code are available at: https://github.com/deer-echo/CoCoT.
