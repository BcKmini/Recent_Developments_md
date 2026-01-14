# Enabling Long FFT Convolutions on Memory-Constrained FPGAs via Chunking

**출처:** [ArXiv_Machine_Learning](https://arxiv.org/abs/2601.06065)

## 요약
arXiv:2601.06065v1 Announce Type: new
Abstract: The need for long-context reasoning has led to alternative neural network architectures besides Transformers and self-attention, a popular model being Hyena, which employs causal 1D-convolutions implemented with FFTs. Long convolutions enable efficient global context mixing, but requirements for intermediate results exceed the 2-3 MB Block RAM capacity of FPGAs. We present a chunked FFT convolution approach enabling 450K length sequence by 450K length filter convolutions on an Alveo U200 FPGA with 2.8 MB BRAM through chunking and overlap-add reconstruction. We find that throughput scales proportionally with chunk size while degrading minimally by 7% for our longest sequences, demonstrating that careful memory management enables deployment of long-context primitives on edge FPGAs without sacrificing performance.
