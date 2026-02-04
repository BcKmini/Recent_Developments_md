# HYPE-EDIT-1: Benchmark for Measuring Reliability in Frontier Image Editing Models

**출처:** [ArXiv_Computer_Vision](https://arxiv.org/abs/2602.00105)

## 요약
arXiv:2602.00105v1 Announce Type: new
Abstract: Public demos of image editing models are typically best-case samples; real workflows pay for retries and review time. We introduce HYPE-EDIT-1, a 100-task benchmark of reference-based marketing/design edits with binary pass/fail judging. For each task we generate 10 independent outputs to estimate per-attempt pass rate, pass@10, expected attempts under a retry cap, and an effective cost per successful edit that combines model price with human review time. We release 50 public tasks and maintain a 50-task held-out private split for server-side evaluation, plus a standardized JSON schema and tooling for VLM and human-based judging. Across the evaluated models, per-attempt pass rates span 34-83 percent and effective cost per success spans USD 0.66-1.42. Models that have low per-image pricing are more expensive when you consider the total effective cost of retries and human reviews.
