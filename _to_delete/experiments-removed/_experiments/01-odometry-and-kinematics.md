---
number: 1
title: "Odometry and Kinematics"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-1"]
topics: "Quadrature decoding, tick-to-distance calibration, differential-drive odometry"
aim: >-
  Process quadrature encoder data from a live sensor or dataset to estimate the displacement and velocity of a robotic platform.
status: draft   # change to `released` when the full sheet is published
resources: []
---
An incremental encoder gives you edges, not position. Two channels in quadrature let you recover direction as well as magnitude, and counting all four edge transitions per cycle gives four times the raw resolution for free. Everything downstream — the wheel radius you assume, the track width, the counts per revolution — turns those edges into metres, and an error in any one of them integrates without bound.

This experiment is where you find out how quickly dead reckoning drifts. Drive a known path, compare the odometry estimate against a tape-measured ground truth, and quantify the gap.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Differential-drive platform with quadrature encoders on both wheels
- Microcontroller or single-board computer for edge counting
- Measuring tape and marked floor track
- Python with NumPy and Matplotlib (or a supplied encoder log)

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Decode channel A and B into signed counts; verify direction reversal is detected correctly.
2. Calibrate counts per metre by driving a measured straight line several times.
3. Integrate wheel velocities into a pose estimate over a square or figure-of-eight path.
4. Compare final estimated pose against measured pose and report the closure error.

## Deliverables

- Plot of estimated trajectory against the commanded path
- Counts-per-metre calibration figure with spread across trials
- Closure error in metres and degrees, with a note on which term dominates

## Reading

de Silva, chapter on motion transducers. Siegwart et al., section on wheeled odometry and its error model.
