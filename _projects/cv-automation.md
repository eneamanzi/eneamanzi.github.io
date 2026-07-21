---
layout: page
title: Data-Driven CV with LaTeX, Lua & GitHub Actions
description: Bilingual CV and cover letter generated from a single JSON source using LaTeX and Lua. Automated compilation and deployment via GitHub Actions.
subtitle: "LaTeX · Lua · GitHub Actions"
img:
importance: 2
category: Personal
permalink: /projects/cv-automation/
pretty_table: true
toc:
  sidebar: left
---

An automated system for generating a Curriculum Vitae and cover letter in both Italian and English. Built on **LaTeX** with the `moderncv` class, but rethought from the inside: content is fully separated from presentation and lives as a single source of truth under `data/`.

## The Problem It Solves

Keeping a CV up to date in two languages across separate `.tex` files means updating every piece of data twice, in two different places - with the risk of them falling out of sync. Worse, this website's own CV page used to be a *third* copy, maintained by hand and never quite in sync with the PDF. This project eliminates that redundancy entirely.

## How It Works

### Single Source of Truth

Everything - work experience, education, skills, projects, personal info - lives under `data/`, one JSON file per domain (numbered to match render order), with lightweight Markdown (`**bold**`/`*italic*`) for emphasis instead of raw LaTeX. Updating the CV, cover letter, *and* this website's `/cv/` page means editing those files only.

### The Lua ↔ LaTeX Bridge

The file `commons/lua_data_loader.tex` contains a **Lua** script that, during compilation via **LuaLaTeX**, reads the JSON, converts the Markdown emphasis to LaTeX, and dynamically populates the document sections in the selected language. It's not a static template - it's code that runs at compile time.

### The Python ↔ JSON Resume Bridge

`scripts/generate_resume_json.py` reads the same `data/` source and produces a `resume.json` in [JSON Resume](https://jsonresume.org/) format for this website's `/cv/` page, which renders it through a custom **Research** section (added on top of the standard schema) alongside the usual Education/Experience/Publications/Skills.

### CI/CD Pipeline

A **GitHub Actions** workflow automatically compiles all four documents on every push and publishes them to the `pdf-release` branch. From there, further steps sync the CV PDFs and the generated `resume.json` directly to this website repository (`eneamanzi.github.io`), keeping the online version always current with no manual intervention.

```
data/*.json  →  lua_data_loader.tex  →  LuaLaTeX  →  PDF
     │                                                 ↓
     │                                     GitHub Actions deploy
     │                                                 ↓
     └──  generate_resume_json.py  →  resume.json  →  eneamanzi.github.io (always up-to-date)
```

## Generated Documents

| Document         | Language |
| ---------------- | -------- |
| Curriculum Vitae | Italian  |
| Curriculum Vitae | English  |
| Cover Letter     | Italian  |
| Cover Letter     | English  |

## Tech Stack

- **Markup language:** LaTeX (`moderncv`)
- **Compilation engine:** LuaLaTeX
- **Scripting:** Lua, Python
- **Data format:** JSON (custom domain schema + generated JSON Resume)
- **Automation:** GitHub Actions
- **Build tool:** `latexmk`

[View on GitHub](https://github.com/eneamanzi/Curriculum-Vitae)
