---
layout: page
title: Experiments
permalink: /experiments/
eyebrow: Twelve compulsory experiments
lede: Cycle I builds the perception stack; Cycle II drives it. Each experiment has its own page with aim, apparatus, procedure and deliverables — released as the semester progresses.
---

{% assign exps = site.experiments | sort: "number" %}

<h2 id="cycle-i"><span class="chip chip--sense">I</span>&nbsp; Sensors &amp; Perception</h2>

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="t-num">No.</th>
      <th>Experiment</th>
      <th>What you do</th>
      <th>CO</th>
    </tr>
  </thead>
  <tbody>
  {% for e in exps %}{% if e.cycle_id == "sense" %}
    <tr>
      <td class="t-mono">{{ e.number | prepend: '0' | slice: -2, 2 }}</td>
      <td class="t-title"><a href="{{ e.url | relative_url }}">{{ e.title }}</a></td>
      <td>{{ e.aim }}</td>
      <td class="t-mono">{{ e.co | join: ", " }}</td>
    </tr>
  {% endif %}{% endfor %}
  </tbody>
</table>
</div>

<h2 id="cycle-ii"><span class="chip chip--act">II</span>&nbsp; Actuators &amp; Control</h2>

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="t-num">No.</th>
      <th>Experiment</th>
      <th>What you do</th>
      <th>CO</th>
    </tr>
  </thead>
  <tbody>
  {% for e in exps %}{% if e.cycle_id == "act" %}
    <tr>
      <td class="t-mono">{{ e.number | prepend: '0' | slice: -2, 2 }}</td>
      <td class="t-title"><a href="{{ e.url | relative_url }}">{{ e.title }}</a></td>
      <td>{{ e.aim }}</td>
      <td class="t-mono">{{ e.co | join: ", " }}</td>
    </tr>
  {% endif %}{% endfor %}
  </tbody>
</table>
</div>

## What a submission looks like

Every experiment is assessed on the same four things, whether it ran on live hardware or a
supplied dataset:

- **Setup** — what was connected to what, sample rates, and the conditions the data was taken under.
- **Data** — raw logs kept, not just the processed result. A plot without its underlying data cannot be checked.
- **Analysis** — the number the experiment asks for, with its units and an honest error estimate.
- **Interpretation** — two or three sentences on why the sensor or actuator behaved the way it did.

<div class="note" markdown="1">
**Code.** Push your scripts to a repository and put the link in your record. Notebooks are
fine for analysis; the acquisition code should be a plain script that runs end to end.
</div>
