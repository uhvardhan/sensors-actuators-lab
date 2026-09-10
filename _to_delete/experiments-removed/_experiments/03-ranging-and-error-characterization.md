---
number: 3
title: "Ranging and Error Characterization"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-1", "CO-3"]
topics: "Ultrasonic time-of-flight, IR triangulation, beam width, surface dependence"
aim: >-
  Analyze Ultrasonic and Infrared distance data (Live or Logged) to model sensor accuracy and identify technology-specific limitations.
status: draft   # change to `released` when the full sheet is published
resources: []
---
Ultrasonic ranging is time-of-flight through air, so it inherits the temperature dependence of the speed of sound and a beam wide enough that the reading is the nearest thing in a cone, not the thing in front. Infrared triangulation is geometric instead, which makes it sharper laterally but strongly non-linear with distance and easily fooled by dark or specular surfaces.

The point of running both against the same targets is that the failure modes are different, and a robot that carries only one of them is blind in a specific, predictable way.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Ultrasonic ranging module and an IR triangulation sensor
- Microcontroller with serial logging to the host
- Target panels: flat card, cloth, and an angled or specular surface
- Measuring tape or optical rail for ground-truth distance

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Take repeated readings from both sensors at a series of known distances.
2. Plot reported against true distance; fit and report the transfer characteristic for each.
3. Repeat at incident angles away from normal, and with an absorbing target.
4. Identify the usable range and the conditions where each sensor fails outright.

## Deliverables

- Calibration curves with residuals for both sensors
- Table of failure conditions by surface and angle
- One-paragraph recommendation on which sensor suits which robot task

## Reading

de Silva, chapter on proximity and displacement sensing. Siegwart et al., section on range sensors.
