---
layout: page
title: Academic Career
permalink: /career/
description: "Full academic record from the University of Milan: courses, grades, and credits (CFU) for the Bachelor's and Master's degrees in Cyber Security."
nav: true
nav_order: 6
pretty_table: true
_styles: >
  table[data-toggle="table"] tbody tr:nth-child(even):not(:hover) {
    background-color: color-mix(in srgb, var(--global-divider-color) 35%, transparent);
  }
  .table-responsive {
    margin: 1.1rem 0 1.4rem;
  }
  .table-responsive .af-table-shell {
    margin: 0;
  }
  table[data-toggle="table"] {
    table-layout: fixed;
  }
---

{% for degree in site.data["uni-career"] %}

## {{ degree.university }}

<div class="row mb-4">
  <div class="col-sm-4">
    <strong>Weighted Average:</strong> &nbsp;
    <span class="badge" style="background-color: var(--global-theme-color); color: #fff; font-size: 1rem;">{{ degree.average }}</span>
  </div>
  <div class="col-sm-4">
    <strong>Credits (CFU):</strong> &nbsp;
    <span class="badge" style="background-color: var(--global-theme-color); color: #fff; font-size: 1rem;">{{ degree.cfu }}</span>
  </div>
  <div class="col-sm-4">
    <strong>Status:</strong> &nbsp;
    <span class="badge" style="background-color: var(--global-theme-color); color: #fff; font-size: 1rem;">{{ degree.status }}</span>
  </div>
</div>

<div class="table-responsive">
<table data-toggle="table">
  <thead>
    <tr>
      <th data-field="course" data-sortable="true" style="width: 55%;">Course</th>
      <th data-field="grade" data-sortable="true" data-align="center" data-halign="center" style="width: 15%;">Grade</th>
      <th data-field="cfu" data-sortable="true" data-align="center" data-halign="center" style="width: 10%;">CFU</th>
      <th data-field="date" data-sortable="true" data-align="center" data-halign="center" style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for exam in degree.exams %}
    {% assign d = exam.date | split: "-" %}
    <tr>
      <td>{{ exam.name }}</td>
      <td>{{ exam.grade }}</td>
      <td>{{ exam.cfu }}</td>
      <td>{{ d[2] }}-{{ d[1] }}-{{ d[0] }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
</div>

{% endfor %}
