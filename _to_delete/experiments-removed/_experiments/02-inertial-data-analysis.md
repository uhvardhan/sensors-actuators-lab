---
number: 2
title: "Inertial Data Analysis"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-1"]
topics: "MEMS accelerometer and gyroscope noise, bias, drift, complementary filtering"
aim: >-
  Characterize noise and bias from an Inertial Measurement Unit (IMU) stream to estimate stable orientation via digital filtering.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A gyroscope measures rate, so orientation from a gyro alone is an integral, and any constant bias becomes an angle that grows linearly with time. An accelerometer measures the gravity vector, which is absolute but useless the moment the sensor accelerates. Each fixes what the other gets wrong, which is why almost every attitude estimate is some form of fusion.

Before fusing anything, you characterise. Log a stationary IMU for several minutes and the bias, the noise density and the slow thermal drift all become visible in the data.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- 6-DOF or 9-DOF MEMS IMU module
- Serial or I²C interface to a host computer
- Level surface and a protractor or indexed rotary fixture
- Python with NumPy, SciPy and Matplotlib (or a supplied IMU log)

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Log at least five minutes of stationary data at a fixed sample rate.
2. Compute per-axis mean (bias) and standard deviation; plot histograms and the Allan deviation if time allows.
3. Integrate raw gyro rate to show unbounded drift in yaw over the same window.
4. Implement a complementary filter fusing accelerometer tilt with gyro rate; tune the crossover.

## Deliverables

- Per-axis bias and noise table for accelerometer and gyroscope
- Drift plot: raw gyro integration against filtered estimate over the same interval
- Chosen filter coefficient with a justification in terms of the measured noise

## Reading

de Silva, chapter on inertial sensing. Any standard treatment of complementary and Kalman filtering for attitude.
