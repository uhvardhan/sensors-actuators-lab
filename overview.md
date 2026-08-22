---
layout: page
title: Overview
permalink: /overview/
hide_title: true
---

{% assign c = site.data.course %}

## Course Objectives

<ol>
{% for o in c.objectives %}<li>{{ o }}</li>{% endfor %}
</ol>

## Course Outcomes

On completion of this laboratory, a student will be able to:

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th class="t-num">CO</th><th>Outcome</th></tr></thead>
  <tbody>
  {% for co in c.outcomes %}
    <tr><td class="t-mono">{{ forloop.index }}</td><td>{{ co.text }}</td></tr>
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
