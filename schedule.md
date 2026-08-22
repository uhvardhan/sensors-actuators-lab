---
layout: page
title: Schedule
permalink: /schedule/
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
