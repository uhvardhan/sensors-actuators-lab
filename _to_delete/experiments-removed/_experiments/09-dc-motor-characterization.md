---
number: 9
title: "DC Motor Characterization"
cycle: "Cycle II — Actuators & Control"
cycle_id: act
co: ["CO-4"]
topics: "H-bridge drive, PWM, back-EMF, torque–speed curve, stall current"
aim: >-
  Control a DC motor via an H-Bridge and analyze current consumption under varying load conditions.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A brushed DC motor is close to a straight line: torque falls linearly as speed rises, current tracks torque, and back-EMF is what makes the two meet. The stall point is where all the electrical power goes to heat, which is why a motor that is merely blocked, not broken, still destroys itself in seconds.

An H-bridge lets you set both magnitude and direction. Measuring current while you sweep PWM duty under load is how the torque–speed curve on the datasheet turns into a number you trust.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Brushed DC gearmotor with an encoder or tachometer
- H-bridge driver module rated above the motor's stall current
- Bench supply with current display, or an in-line current sensor
- Adjustable mechanical load (friction brake or prony arrangement)

<div class="note" markdown="1">
**Before you power anything on.** Stall testing draws several times the running current. Keep stalls under a few seconds, fuse the supply, and never leave a stalled motor energised.
</div>

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Drive the motor open-loop across a PWM duty sweep and record no-load speed and current.
2. Apply increasing load at fixed duty; record speed and current at each setting.
3. Plot the torque–speed and current–torque relationships; extract stall current and no-load speed.
4. Verify direction reversal and observe the current transient at reversal.

## Deliverables

- Torque–speed and current–torque plots with the operating region marked
- Measured stall current against the datasheet value
- Note on the thermal limit and how long stall can safely be sustained

## Reading

de Silva, chapter on DC motors and drives. Niku, chapter on actuators.
