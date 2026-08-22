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
      <th>Experiment</th>
      <th>Files</th>
    </tr>
  </thead>
  <tbody>
  {% for w in site.data.schedule %}
    <tr>
      <td class="t-mono">{{ w.week }}</td>
      <td class="t-mono">
        {%- if w.dates and w.dates.size > 0 -%}
          <ul class="bare">{% for d in w.dates %}<li>{{ d }}</li>{% endfor %}</ul>
        {%- else -%}—{%- endif -%}
      </td>
      <td class="t-title">{{ w.session }}</td>
      <td>
        {%- if w.files and w.files.size > 0 -%}
          <ul class="bare">{% for f in w.files %}<li><a href="{{ f.url | relative_url }}">{{ f.name }}</a></li>{% endfor %}</ul>
        {%- else -%}<span class="t-mono">—</span>{%- endif -%}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>
