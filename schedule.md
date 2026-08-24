---
layout: page
title: Schedule
permalink: /schedule/
hide_title: true
wide: true
---

{%- comment -%}
  Notes / Scripts / Additional resources all render the same way, so they loop
  over the matching list in _data/schedule.yml rather than repeating the markup.
{%- endcomment -%}
{%- assign link_cols = "notes,scripts,resources" | split: "," -%}

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="t-num">Week</th>
      <th>Date</th>
      <th>Experiment</th>
      <th>Notes</th>
      <th>Scripts</th>
      <th>Additional resources</th>
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
      <td class="t-title">
        {%- if w.session and w.session != "" -%}{{ w.session }}
        {%- else -%}<span class="t-mono">—</span>{%- endif -%}
      </td>
      {%- for key in link_cols -%}
      {%- assign items = w[key] -%}
      <td>
        {%- if items and items.size > 0 -%}
          <ul class="bare">{% for f in items %}<li><a href="{{ f.url | relative_url }}">{{ f.name }}</a></li>{% endfor %}</ul>
        {%- else -%}<span class="t-mono">—</span>{%- endif -%}
      </td>
      {%- endfor -%}
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>
