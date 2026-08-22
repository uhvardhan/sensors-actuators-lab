---
number: 5
title: "Geometric Camera Calibration"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-2"]
topics: "Pinhole model, intrinsic matrix, radial and tangential distortion, reprojection error"
aim: >-
  Utilize a dataset of calibration patterns to determine intrinsic parameters and rectify lens-induced distortions.
status: draft   # change to `released` when the full sheet is published
resources: []
---
Every metric thing you later ask a camera to do — measure a distance, estimate a pose, triangulate depth — assumes you know the focal lengths, the principal point and how the lens bends straight lines. Calibration recovers those from images of a pattern whose geometry you already know.

Reprojection error is the honest scorecard. A sub-pixel mean with well-spread pattern poses means the model fits; a low error from twenty nearly identical views means very little.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- Camera under test with fixed focus and fixed zoom
- Rigid, flat checkerboard or ChArUco target with known square size
- Even, diffuse lighting
- Python with OpenCV (or a supplied calibration image set)

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Capture 15–25 views of the target spanning tilt, roll and depth across the whole frame.
2. Detect corners to sub-pixel accuracy and run the calibration.
3. Report the intrinsic matrix and distortion coefficients with per-image reprojection error.
4. Undistort a test image and verify that known-straight lines come out straight.

## Deliverables

- Intrinsic matrix and distortion coefficients, with units stated
- Per-image reprojection error plot and the overall RMS
- Before-and-after undistortion pair with the straightness check marked

## Reading

Szeliski, chapters on image formation and geometric calibration. OpenCV calibration tutorial.
