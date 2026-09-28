---
layout: page
title: Schedule
permalink: /schedule/
hide_title: true
wide: true
---

{%- comment -%}
  Files (notes + scripts) and Additional resources render the same way, so they
  loop over the matching lists in _data/schedule.yml rather than repeating the markup.
{%- endcomment -%}
{%- assign link_cols = "notes+scripts,resources" | split: "," -%}

<div class="table-scroll" markdown="0">
<table>
  <thead>
    <tr>
      <th class="t-num">Week</th>
      <th>Date</th>
      <th>Experiment</th>
      <th>Files</th>
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
      {%- for group in link_cols -%}
      {%- assign keys = group | split: "+" -%}
      {%- assign items = "" | split: "" -%}
      {%- for key in keys -%}{%- if w[key] -%}{%- assign items = items | concat: w[key] -%}{%- endif -%}{%- endfor -%}
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
