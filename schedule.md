---
layout: page
title: Schedule
permalink: /schedule/
eyebrow: Semester plan
hide_title: true
---

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="t-num">Week</th>
      <th>Date</th>
      <th>Session</th>
    </tr>
  </thead>
  <tbody>
  {% for w in site.data.schedule %}
    <tr>
      <td class="t-mono">{{ w.week }}</td>
      <td class="t-mono">{% if w.date and w.date != "" %}{{ w.date }}{% else %}—{% endif %}</td>
      <td class="t-title">{{ w.session }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

<div class="note" markdown="1">
**Missed a session?** Experiments must be completed in sequence — Experiment 12 depends on
working code from Experiments 6 and 11. Arrange a make-up slot in the same week rather than
carrying the backlog into the next cycle.
</div>

## Assessment dates

| Assessment | Covers | When |
| --- | --- | --- |
| Lab internal I | Experiments 1–8 (Cycle I) | Week 10 |
| Lab internal II | Experiments 9–12 (Cycle II) | Week 15 |
| Record submission | All twelve experiments | Week 15 |
| Semester end examination | Full syllabus, practical | Week 16 |
