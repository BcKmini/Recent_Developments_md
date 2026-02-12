# Enhanced Graph Transformer with Serialized Graph Tokens

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.09065)

## 요약
arXiv:2602.09065v1 Announce Type: new
Abstract: Transformers have demonstrated success in graph learning, particularly for node-level tasks. However, existing methods encounter an information bottleneck when generating graph-level representations. The prevalent single token paradigm fails to fully leverage the inherent strength of self-attention in encoding token sequences, and degenerates into a weighted sum of node signals. To address this issue, we design a novel serialized token paradigm to encapsulate global signals more effectively. Specifically, a graph serialization method is proposed to aggregate node signals into serialized graph tokens, with positional encoding being automatically involved. Then, stacked self-attention layers are applied to encode this token sequence and capture its internal dependencies. Our method can yield more expressive graph representations by modeling complex interactions among multiple graph tokens. Experimental results show that our method achieves state-of-the-art results on several graph-level benchmarks. Ablation studies verify the effectiveness of the proposed modules.
