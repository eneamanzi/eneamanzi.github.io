---
layout: page
title: Carriera Accademica
lang: it
permalink: /carriera/
page_id: career
description: "Carriera accademica di Enea Manzi in Cyber Security e Sicurezza dei Sistemi e delle Reti all'Università degli Studi di Milano. Media ponderata: 28.92 (Triennale) e 29.23 (Magistrale, in corso)."
nav: true
nav_order: 5
---

<div class="career">
  {% for degree in site.data.it["uni-career"] %}
    <h3 class="category mt-5">{{ degree.university }}</h3>
    
    <div class="row mb-4">
      <div class="col-sm-4">
        <strong>Media Ponderata:</strong> <br>
        <span class="badge badge-pill badge-primary" style="font-size: 1rem;">{{ degree.average }}</span>
      </div>
      <div class="col-sm-4">
        <strong>CFU Acquisiti:</strong> <br>
        <span class="badge badge-pill badge-secondary" style="font-size: 1rem;">{{ degree.cfu }}</span>
      </div>
      <div class="col-sm-4">
        <strong>Stato:</strong> <br>
        <span class="badge badge-pill badge-success" style="font-size: 1rem;">{{ degree.status }}</span>
      </div>
    </div>

    <table class="table table-sm table-borderless table-responsive-md mt-3">
      <thead class="thead-light">
        <tr>
          <th style="width: 50%">Esame</th>
          <th class="text-center" style="width: 20%">Voto</th>
          <th class="text-center" style="width: 10%">CFU</th>
          <th class="text-right" style="width: 20%">Data</th>
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