---
number: 6
title: "Object Detection and Tracking"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-2", "CO-4"]
topics: "Colour and feature segmentation, centroid extraction, frame-to-frame tracking, latency"
aim: >-
  Implement a vision pipeline to extract the spatial coordinates of a target from a live camera feed or a recorded video stream.
status: draft   # change to `released` when the full sheet is published
resources: []
---
Detection answers where the target is in this frame; tracking answers whether it is the same target as last frame. The distinction matters as soon as the scene has two similar objects, or the target leaves the frame and returns.

Whatever pipeline you build here comes back in Experiment 12, where its output becomes a control signal. Measure its latency now — a detector that is accurate but forty milliseconds late will make the closed loop oscillate.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- USB or CSI camera, calibrated in Experiment 5
- Coloured or fiducial target on a movable mount
- Python with OpenCV
- Recorded fallback video of the same target

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Segment the target and extract its centroid in pixel coordinates each frame.
2. Convert centroid to a bearing using the intrinsics from Experiment 5.
3. Add a simple tracker so identity persists across frames and brief occlusions.
4. Measure end-to-end pipeline latency and the frame rate you can sustain.

## Deliverables

- Annotated video or frame sequence showing the tracked centroid
- Plot of target bearing against time for a swept motion
- Measured latency and frame rate, with the bottleneck identified

## Reading

Szeliski, chapters on segmentation and tracking.
