# BLUEPRINT Rebuilding a Legacy: Multimodal Retrieval for Complex Engineering Drawings and Documents

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2602.13345)

## 요약
arXiv:2602.13345v1 Announce Type: new
Abstract: Decades of engineering drawings and technical records remain locked in legacy archives with inconsistent or missing metadata, making retrieval difficult and often manual. We present Blueprint, a layout-aware multimodal retrieval system designed for large-scale engineering repositories. Blueprint detects canonical drawing regions, applies region-restricted VLM-based OCR, normalizes identifiers (e.g., DWG, part, facility), and fuses lexical and dense retrieval with a lightweight region-level reranker. Deployed on ~770k unlabeled files, it automatically produces structured metadata suitable for cross-facility search.
We evaluate Blueprint on a 5k-file benchmark with 350 expert-curated queries using pooled, graded (0/1/2) relevance judgments. Blueprint delivers a 10.1% absolute gain in Success@3 and an 18.9% relative improvement in nDCG@3 over the strongest vision-language baseline}, consistently outperforming across vision, text, and multimodal intents. Oracle ablations reveal substantial headroom under perfect region detection and OCR. We release all queries, runs, annotations, and code to facilitate reproducible evaluation on legacy engineering archives.
