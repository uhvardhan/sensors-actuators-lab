---
number: 8
title: "Planar Environment Mapping"
cycle: "Cycle I — Sensors & Perception"
cycle_id: sense
co: ["CO-3"]
topics: "2D LiDAR scans, polar plots, angular resolution, obstacle extraction"
aim: >-
  Analyze 2D LiDAR scan data (Live or ROS bag) to generate polar plots and identify obstacles in a 2D plane.
status: draft   # change to `released` when the full sheet is published
resources: []
---
A 2D LiDAR returns a range for each angular step in a plane. That is a strong constraint on the world — but only in that plane, which is why a scanner mounted at ankle height cheerfully reports a clear path under a table.

Angular resolution sets how far away two objects can be and still be distinguished. Work out that separation for your scanner at three metres and you will understand most of what obstacle-avoidance code has to cope with.

## Apparatus

Indicative — confirm against the bench allocation for your batch.

- 2D spinning LiDAR module, or a recorded scan log / ROS bag
- Room or arena with measurable wall positions and a few obstacles
- Python with NumPy and Matplotlib

## Procedure

The full sheet with parameter values and observation tables is released before the session. In outline:

1. Parse the scan into ranges and bearings; handle invalid and out-of-range returns explicitly.
2. Render a polar plot and a Cartesian occupancy view of a single scan.
3. Segment the scan into line features (walls) and clusters (obstacles).
4. Compare extracted wall positions against tape measurements of the room.

## Deliverables

- Polar and Cartesian plots of one scan, with invalid returns marked
- List of detected obstacles with bearing, range and angular width
- Angular resolution figure and the resulting minimum separable object spacing at 3 m

## Reading

Siegwart et al., section on laser range finders. de Silva, chapter on optical sensing.
