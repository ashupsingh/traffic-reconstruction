# Intelligent Traffic Management: methodology

Status: researched reconstruction / proposed evaluation, prepared 23 October 2026. Not a recovered lab notebook.

## Existing account

Building at Vernovate with a target of reducing congestion by 30%. The reduction is a development target, not a measured deployment result. The ITMS project won the JEC Hackathon in February 2025.

The account above comes from the existing portfolio and is not independent verification. Listed stack: Computer Vision, IoT Sensors, ESP, Raspberry Pi. Exact components and versions still need confirmation.

## System architecture

Video/sensor observations -> lane demand -> bounded phase selection -> simulation log

## Proposed engineering workflow

1. Define lane regions and anonymized observation intervals.
2. Estimate queue length and arrival demand; flag occlusion and stale frames.
3. Compare a fixed-time baseline against demand-based timing with minimum/maximum phase duration and clearance constraints.
4. Evaluate identical demand scenarios and report queue delay, throughput and worst-case waiting.

## Evaluation plan, not results

Record: Mean delay; queue length; throughput; pedestrian waiting; false counts. Use explicit units, test conditions, a baseline where relevant, repeated observations and a timestamped log. Report failure cases alongside successes. No numerical result is available from this reconstruction.

## Limitations and claim boundaries

30% is a target, not a measured result. The controller is a simulation proposal, not road-ready signaling software.

## Design questions for an interview

- Explain the input, decision and output paths in the architecture above.
- What concrete fault would invalidate the output, and how would you detect it?
- Which design decision did you personally make, and what evidence do you retain?
- Which part of this proposed workflow differs from what you actually built?

## Research basis

[FHWA adaptive signal validation](https://ops.fhwa.dot.gov/publications/fhwahop13031/index.htm) — consulted 23 October 2026. This source supports the underlying engineering topic, not the historical implementation. Workflow and evaluation proposals above are original analysis for this project.
