---
number: 10
title: "Stepper Motor Precision & Resonance"
cycle: "Cycle II — Actuators & Control"
cycle_id: act
co: ["CO-4"]
topics: "Unipolar and bipolar drive, micro-stepping, step loss, mid-band resonance"
aim: >-
  Interface a stepper motor with a micro-stepping driver to analyze motion smoothness and vibration.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A stepper holds position without feedback, which makes it the cheapest form of precision — right up to the moment it loses steps, after which it is confidently wrong and has no way of knowing. Micro-stepping smooths the motion and cuts audible noise, but the incremental torque per micro-step falls, so positioning accuracy does not improve nearly as much as the step count suggests.

Mid-band resonance is the interesting failure: at a particular step rate the rotor oscillates in step with its own excitation and the motor stalls at a speed it passes through easily when accelerating.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Bipolar stepper motor and a micro-stepping driver with selectable division
- Controller capable of generating a clean step/direction pulse train
- Graduated dial, laser pointer arm or accelerometer for measuring position and vibration
- Bench supply with current limit

<div class="note" markdown="1">
**Before you power anything on.** Never disconnect a stepper from an energised driver — the inductive transient can destroy the output stage.
</div>

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Set the driver current limit correctly for the motor before applying any load.
2. Command a known number of full steps and measure the actual angle travelled.
3. Repeat at 1/2, 1/4, 1/8 and 1/16 micro-stepping; compare smoothness and positioning error.
4. Sweep step rate slowly upward and identify the speed at which resonance or step loss begins.

## Deliverables

- Commanded against measured angle across micro-stepping settings
- Vibration or audible-noise observation at each division
- Identified resonance band and the maximum reliable step rate

## Reading

de Silva, chapter on stepper motors. Driver datasheet for current setting and decay modes.
