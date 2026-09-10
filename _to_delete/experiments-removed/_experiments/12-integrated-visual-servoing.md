---
number: 12
title: "Integrated Visual Servoing"
cycle: "Cycle II — Actuators & Control"
cycle_id: act
co: ["CO-4"]
topics: "Perception–action loop, image-based error, proportional control, latency and stability"
aim: >-
  Design a closed-loop system where vision feedback controls an actuated mechanism for target tracking.
status: draft   # change to `released` when the full sheet is published
resources: []
---
This is the experiment the other eleven were preparation for. The camera pipeline from Experiment 6 produces a target bearing; the error between that bearing and the image centre drives a servo or motor from Cycle II; the motion changes what the camera sees, and the loop closes.

Everything you measured earlier now shows up as behaviour. Detection latency becomes phase lag. Camera distortion becomes steady-state offset. Actuator backlash becomes limit cycling around the setpoint. Tuning the gain is straightforward; explaining why the loop misbehaves at the gain above it is the point of the exercise.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Calibrated camera on a pan (and optionally tilt) mount
- Servo or geared DC motor with a driver, from Cycle II
- Movable target, ideally on a repeatable motion fixture
- Python with OpenCV and a serial or GPIO link to the actuator

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Reuse the Experiment 6 pipeline to produce target bearing at a known rate.
2. Compute the image-plane error and map it to an actuator command with a proportional gain.
3. Raise the gain until the loop oscillates; record the gain at which it does.
4. Back off to a stable setting and measure tracking error against target speed.

## Deliverables

- Block diagram of the closed loop with measured latency on each stage
- Step response and the gain at which instability appears
- Tracking error against target velocity, with the dominant limitation identified

## Reading

Szeliski, chapters on tracking. Any standard treatment of visual servoing and proportional control.
