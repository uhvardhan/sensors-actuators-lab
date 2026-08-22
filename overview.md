---
layout: page
title: Overview
permalink: /overview/
eyebrow: Syllabus
lede: Course objectives, outcomes, articulation matrix and assessment breakdown, as approved under the R25 regulation.
---

{% assign c = site.data.course %}

## Course at a glance

<div class="table-scroll" markdown="0">
<table>
  <tbody>
    <tr><th>Course code</th><td class="t-mono">{{ c.code }}</td></tr>
    <tr><th>Programme</th><td>{{ c.programme }}</td></tr>
    <tr><th>Semester</th><td>{{ c.semester }} · {{ c.regulation }} regulation</td></tr>
    <tr><th>L · T/P · C</th><td class="t-mono">{{ c.teaching_scheme.lecture }} · {{ c.teaching_scheme.practical }} · {{ c.teaching_scheme.credits }}</td></tr>
    <tr><th>Prerequisite</th><td>{{ c.prerequisites }}</td></tr>
  </tbody>
</table>
</div>

## Course objectives

<ul>
{% for o in c.objectives %}<li>{{ o }}</li>{% endfor %}
</ul>

## Course outcomes

On completion of this laboratory, a student will be able to:

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th class="t-num">CO</th><th>Outcome</th></tr></thead>
  <tbody>
  {% for co in c.outcomes %}
    <tr><td class="t-mono">{{ co.id }}</td><td>{{ co.text }}</td></tr>
  {% endfor %}
  </tbody>
</table>
</div>

## Articulation matrix

Correlation of course outcomes with programme outcomes and programme specific outcomes.
Mapping levels: **1** slight, **2** moderate, **3** substantial.

<div class="table-scroll matrix" markdown="0">
<table>
  <thead>
    <tr>
      <th>CO</th>
      {% for col in c.articulation.columns %}<th>{{ col }}</th>{% endfor %}
    </tr>
  </thead>
  <tbody>
  {% for row in c.articulation.rows %}
    <tr>
      <td class="t-mono">{{ row.id }}</td>
      {% for v in row.values %}
        {% if v == "" %}<td class="empty">·</td>{% else %}<td>{{ v }}</td>{% endif %}
      {% endfor %}
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## Assessment

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th class="t-num">Code</th><th>Component</th><th class="t-center">Marks</th></tr></thead>
  <tbody>
  {% assign total = 0 %}
  {% for e in c.evaluation %}
    {% assign total = total | plus: e.marks %}
    <tr><td class="t-mono">{{ e.key }}</td><td>{{ e.label }}</td><td class="t-center t-mono">{{ e.marks }}</td></tr>
  {% endfor %}
    <tr><td></td><td class="t-title">Total</td><td class="t-center t-mono">{{ total }}</td></tr>
  </tbody>
</table>
</div>

<div class="note" markdown="1">
**Lab record.** Each experiment needs a written record — aim, setup, observations, plots,
and a short interpretation of what the data says. Records are signed off session by session;
a record submitted in bulk at the end of the semester is not accepted for day-to-day marks.
</div>

## How the two cycles fit together

Cycle I is measurement. Every experiment in it ends with the same question: how wrong is
this reading, and in which direction? Encoder quantisation, IMU bias and random walk,
ultrasonic beam spread, rolling shutter skew, lens distortion, stereo disparity error,
LiDAR angular resolution — each has a characteristic failure mode, and knowing it is what
separates a usable estimate from a plausible-looking one.

Cycle II is command. Motors have their own non-idealities — back-EMF, missed steps,
commutation ripple, backlash in the gear train — and a control loop written without
accounting for them behaves well on paper and badly on a bench. Experiment 12 puts a Cycle I
sensor in the feedback path of a Cycle II actuator, which is the smallest complete robot
you can build.
