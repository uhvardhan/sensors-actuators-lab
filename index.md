---
layout: home
title: Home
permalink: /
---

This laboratory is the hands-on half of **Sensors and Actuators for Robotics (25PC1RA202)**.
Where the theory course derives the physics, this one puts a sensor on the bench, logs what
it actually reports, and asks how far that differs from the ideal.

Cycle I works outward from the robot's own body: quadrature encoders and wheel odometry,
then MEMS inertial sensors and their bias and drift, then active ranging, then cameras —
shutter behaviour, intrinsic calibration, tracking, depth, and finally 2D LiDAR scans turned
into an occupancy picture of the room.

Cycle II closes the loop. DC motors under load, steppers at micro-stepping resolution,
brushless motors under electronic commutation — and then Experiment 12, where a camera's
output drives an actuator in real time and the two halves of the course meet.

Every experiment is either live hardware or a supplied dataset, so a session is never lost
to a dead sensor. Bring a laptop with the toolchain from the [Resources]({{ '/resources/' | relative_url }})
page already installed.
