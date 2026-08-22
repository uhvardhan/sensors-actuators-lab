---
number: 7
title: "Volumetric Depth Interpretation"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-3"]
topics: "Stereo disparity, structured light, time-of-flight, point cloud filtering, plane fitting"
aim: >-
  Process 3D point clouds or depth maps from a vision sensor to extract spatial geometry and distance metrics.
status: draft   # change to `released` when the full sheet is published
resources: []
---
Depth from stereo is disparity scaled by baseline and focal length, so its error grows with the square of range — a fact that decides where a stereo rig is useful and where it is not. Structured light and time-of-flight sensors have flatter error curves but their own pathologies: sunlight, reflective surfaces, multipath.

Turning a depth map into a point cloud is arithmetic. Turning a point cloud into something a robot can act on — a floor plane, an object above it, a graspable extent — is the real work.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Depth camera (stereo, structured light or ToF) or a supplied point cloud dataset
- Scene with a flat floor or table and one or two simple objects at known positions
- Python with Open3D or equivalent point cloud tooling

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Convert the depth map to a point cloud using the camera intrinsics.
2. Downsample and remove statistical outliers; note how much data each step discards.
3. Fit and remove the dominant plane, then cluster what remains into objects.
4. Measure the extent and centroid distance of one object and compare with a tape measurement.

## Deliverables

- Rendered point cloud before and after filtering
- Fitted plane parameters and the segmented object clusters
- Measured object distance and dimensions against ground truth, with error stated

## Reading

Szeliski, chapters on stereo correspondence and depth sensing. Open3D documentation.
