---
layout: page
title: Resources
permalink: /resources/
eyebrow: Books, tools, datasets
lede: What to read, what to install, and where to get data when the hardware is unavailable.
---

{% assign c = site.data.course %}

## Set this up before week 1

Every experiment analyses its data in Python. Install this once and you will not lose a
session to a broken environment.

```bash
# A dedicated environment keeps the lab isolated from your other projects
conda create -n salab python=3.11
conda activate salab

pip install numpy scipy matplotlib pandas jupyter
pip install opencv-python          # Experiments 4, 5, 6, 12
pip install open3d                 # Experiment 7
pip install pyserial               # Any experiment reading a microcontroller
```

Export the environment when you are done — `conda env export > environment.yml` — and keep
it with your code, so your results stay reproducible on another machine.

<div class="note" markdown="1">
**Working on Windows?** Serial port access and camera backends behave differently. WSL2
does not pass USB devices through by default; run acquisition natively on Windows and do
the analysis wherever you like.
</div>

## Textbooks

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th>Author</th><th>Title</th><th>Used for</th></tr></thead>
  <tbody>
  {% for b in c.textbooks %}
    <tr>
      <td>{{ b.author }}</td>
      <td class="t-title">{{ b.title }}<br><span class="t-mono">{{ b.publisher }}</span></td>
      <td>{{ b.note }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## References

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th>Author</th><th>Title</th><th>Used for</th></tr></thead>
  <tbody>
  {% for b in c.references %}
    <tr>
      <td>{{ b.author }}</td>
      <td class="t-title">{{ b.title }}<br><span class="t-mono">{{ b.publisher }}</span></td>
      <td>{{ b.note }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## Online

<ul>
{% for r in c.online_resources %}
  <li><a href="{{ r.url }}">{{ r.name }}</a></li>
{% endfor %}
</ul>

## Datasets

Where hardware is shared across batches, a recorded dataset stands in so the analysis can
still be done. Links are added here as each experiment is released.

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th class="t-num">Exp</th><th>Dataset</th><th>Contents</th></tr></thead>
  <tbody>
    <tr><td class="t-mono">—</td><td colspan="2">No datasets published yet.</td></tr>
  </tbody>
</table>
</div>

## Related course

This lab runs alongside the theory course **Sensors and Actuators for Robotics
(25PC1RA202)**, which covers the same ground analytically across five units:
proprioceptive sensing, robotic vision, exteroceptive perception and force sensing,
electric actuators and drives, and geared transmission. Where an experiment assumes a
derivation, that is where to find it.
