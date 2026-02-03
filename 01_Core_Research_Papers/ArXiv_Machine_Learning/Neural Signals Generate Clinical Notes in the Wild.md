# Neural Signals Generate Clinical Notes in the Wild

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.22197)

## 요약
arXiv:2601.22197v1 Announce Type: new
Abstract: Generating clinical reports that summarize abnormal patterns, diagnostic findings, and clinical interpretations from long-term EEG recordings remains labor-intensive. We curate a large-scale clinical EEG dataset with $9{,}922$ reports paired with approximately $11{,}000$ hours of EEG recordings from $9{,}048$ patients. We therefore develop CELM, the first clinical EEG-to-Language foundation model capable of summarizing long-duration, variable-length EEG recordings and performing end-to-end clinical report generation at multiple scales, including recording description, background activity, epileptiform abnormalities, events/seizures, and impressions. Experimental results show that, with patient history supervision, our method achieves $70\%$--$95\%$ average relative improvements in standard generation metrics (e.g., ROUGE-1 and METEOR) from $0.2$--$0.3$ to $0.4$--$0.6$. In the zero-shot setting without patient history, CELM attains generation scores in the range of $0.43$--$0.52$, compared to baselines of $0.17$--$0.26$. CELM integrates pretrained EEG foundation models with language models to enable scalable multimodal learning. We release our model and benchmark construction pipeline at [URL].
