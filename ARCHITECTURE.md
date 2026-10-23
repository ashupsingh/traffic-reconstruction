# Reconstruction architecture

```text
Recorded video / counted vehicles -> lane queue estimates -> bounded timing allocation -> simulation metrics
```

Run recorded traffic scenarios against a fixed-time baseline using the same arrival traces. Measure mean delay, queue length and throughput. The 30% figure remains a target. Do not connect this reconstruction to public signals.

See METHODOLOGY.md for research and evaluation details, and reconstruction/model.py for the executable analytical model.
