# Real-Time, Energy-Efficient, Sampling-Based Optimal Control via FPGA Acceleration

**출처:** [ArXiv_Robotics](https://arxiv.org/abs/2601.17231)

## 요약
arXiv:2601.17231v1 Announce Type: new
Abstract: Autonomous mobile robots (AMRs), used for search-and-rescue and remote exploration, require fast and robust planning and control schemes. Sampling-based approaches for Model Predictive Control, especially approaches based on the Model Predictive Path Integral Control (MPPI) algorithm, have recently proven both to be highly effective for such applications and to map naturally to GPUs for hardware acceleration. However, both GPU and CPU implementations of such algorithms can struggle to meet tight energy and latency budgets on battery-constrained AMR platforms that leverage embedded compute. To address this issue, we present an FPGA-optimized MPPI design that exposes fine-grained parallelism and eliminates synchronization bottlenecks via deep pipelining and parallelism across algorithmic stages. This results in an average 3.1x to 7.5x speedup over optimized implementations on an embedded GPU and CPU, respectively, while simultaneously achieving a 2.5x to 5.4x reduction in energy usage. These results demonstrate that FPGA architectures are a promising direction for energy-efficient and high-performance edge robotics.
