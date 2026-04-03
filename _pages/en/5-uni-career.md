---
layout: page
title: Academic Career
lang: en
permalink: /career/
page_id: career
description: My academic journey, coursework, and grades.
nav: true
nav_order: 5
---

<div class="career">
  {% for degree in site.data.en["uni-career"] %}
    <h3 class="category mt-5">{{ degree.university }}</h3>
    
    <div class="row mb-4">
      <div class="col-sm-4">
        <strong>Weighted Average:</strong> <br>
        <span class="badge badge-pill badge-primary" style="font-size: 1rem;">{{ degree.average }}</span>
      </div>
      <div class="col-sm-4">
        <strong>Credits (CFU):</strong> <br>
        <span class="badge badge-pill badge-secondary" style="font-size: 1rem;">{{ degree.cfu }}</span>
      </div>
      <div class="col-sm-4">
        <strong>Status:</strong> <br>
        <span class="badge badge-pill badge-success" style="font-size: 1rem;">{{ degree.status }}</span>
      </div>
    </div>

    <table class="table table-sm table-borderless table-responsive-md mt-3">
      <thead class="thead-light">
        <tr>
          <th style="width: 50%">Course</th>
          <th class="text-center" style="width: 20%">Grade</th>
          <th class="text-center" style="width: 10%">CFU</th>
          <th class="text-right" style="width: 20%">Date</th>
        </tr>
      </thead>
      <tbody>
        {% for exam in degree.exams %}
          <tr>
            <td>{{ exam.name }}</td>
            <td class="text-center"><b>{{ exam.grade }}</b></td>
            <td class="text-center">{{ exam.cfu }}</td>
            <td class="text-right text-muted">{{ exam.date }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
    <hr>
  {% endfor %}
</div>