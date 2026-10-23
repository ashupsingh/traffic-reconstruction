# Source entry points

Runnable new implementation: `reconstruction/model.py`; checks: `reconstruction/test_model.py`. This is an analytical/software reconstruction, not device firmware.

## Earlier design notes

# Code and implementation record

## Original source status

Historical portfolio description only; original source, measurements and photographs not supplied.

No original code recovered for this project. Exact pin maps, libraries, timings and circuit values are intentionally not invented.

## Reconstructed pseudocode

This is newly written explanatory pseudocode, not executable firmware and not historical evidence.

```text
update lane demand
reject stale observations
select eligible phase
enforce clearance and maximum wait
log decisions
```

## What is needed before implementation

Confirm actual hardware/software interfaces, units, validation rules and failure states. Follow the separate methodology and its test plan. 30% is a target, not a measured result. The controller is a simulation proposal, not road-ready signaling software.
