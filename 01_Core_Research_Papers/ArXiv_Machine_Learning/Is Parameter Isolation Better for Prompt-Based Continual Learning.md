# Is Parameter Isolation Better for Prompt-Based Continual Learning?

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.20894)

## 요약
arXiv:2601.20894v1 Announce Type: new
Abstract: Prompt-based continual learning methods effectively mitigate catastrophic forgetting. However, most existing methods assign a fixed set of prompts to each task, completely isolating knowledge across tasks and resulting in suboptimal parameter utilization. To address this, we consider the practical needs of continual learning and propose a prompt-sharing framework. This framework constructs a global prompt pool and introduces a task-aware gated routing mechanism that sparsely activates a subset of prompts to achieve dynamic decoupling and collaborative optimization of task-specific feature representations. Furthermore, we introduce a history-aware modulator that leverages cumulative prompt activation statistics to protect frequently used prompts from excessive updates, thereby mitigating inefficient parameter usage and knowledge forgetting. Extensive analysis and empirical results demonstrate that our approach consistently outperforms existing static allocation strategies in effectiveness and efficiency.
