---
number: 11
title: "Brushless DC (BLDC) Speed Control"
cycle: "Cycle II — Actuators & Control"
cycle_id: act
co: ["CO-4"]
topics: "Electronic commutation, Hall feedback, ESC signalling, speed mapping"
aim: >-
  Interface a BLDC motor with an electronic controller to map control signals to angular velocity.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A brushless motor moves commutation from a mechanical contact to a controller, which buys efficiency and lifetime and costs you a piece of electronics that has to know rotor position. Hall sensors give it directly; sensorless controllers infer it from back-EMF and therefore start badly at low speed.

From the outside an ESC looks like a black box that turns a signal into a speed. The mapping is neither linear nor the same at both ends of the range, and characterising it is what lets you close a loop around it later.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- BLDC motor with a matched electronic speed controller
- Signal source for the ESC input (servo-style PWM or equivalent)
- Optical tachometer or the motor's own Hall feedback for speed measurement
- Secured motor mount and current-monitoring supply

<div class="note" markdown="1">
**Before you power anything on.** Run the motor without a propeller or with a guarded load, clamp the mount, and keep hands and cables clear of the rotor.
</div>

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Arm the ESC following its documented sequence and confirm the throttle range.
2. Step the control signal across its range and record steady-state speed and current at each point.
3. Plot signal against angular velocity; identify dead band, linear region and saturation.
4. Measure the time to reach a commanded speed from rest and from an intermediate speed.

## Deliverables

- Control signal against measured RPM, with dead band and saturation marked
- Current draw across the speed range
- Step-response times, with a comment on what limits them

## Reading

de Silva, chapter on brushless and synchronous machines. ESC and motor datasheets.
