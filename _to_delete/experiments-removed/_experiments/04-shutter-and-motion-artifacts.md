---
number: 4
title: "Shutter and Motion Artifacts"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-2"]
topics: "Rolling vs global shutter, line readout timing, skew, jello effect"
aim: >-
  Evaluate image sequences from Rolling and Global shutter sources to quantify geometric distortion in dynamic scenes.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A rolling shutter exposes the sensor row by row, so a scene that moves during readout is recorded at slightly different instants down the frame. A vertical pole passing the camera leans; a spinning propeller bends. A global shutter exposes every pixel at once and pays for it in sensor cost and, usually, in noise.

The distortion is not a defect to be filtered out later — it is a timing artefact with a measurable slope, and that slope tells you the readout time of the sensor.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Rolling shutter camera (CSI or USB) and a global shutter camera
- Rotating or linearly translating target with a straight vertical edge
- Controlled lighting to keep exposure short and constant
- Python with OpenCV (or supplied image sequences from both camera types)

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Capture the same moving target with both cameras at matched exposure.
2. Measure the apparent tilt of a known-vertical edge as a function of target speed.
3. Estimate the sensor readout time from the measured skew.
4. Repeat with the camera moving instead of the target and compare the artefacts.

## Deliverables

- Side-by-side frames showing the artefact at two or more speeds
- Skew angle against target velocity, with the fitted readout time
- Short note on which robotic tasks tolerate a rolling shutter and which cannot

## Reading

Szeliski, chapter on image formation and sensing. Camera datasheets for readout timing.
