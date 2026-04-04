---
layout: page
title: Data-Driven CV with LaTeX, Lua & GitHub Actions
description: Bilingual CV and cover letter generated from a single JSON source using LaTeX and Lua. Automated compilation and deployment via GitHub Actions.
subtitle: "LaTeX · Lua · GitHub Actions"
img: assets/img/cv.png 
importance: 2
category: Personal
page_id: cv-automation
lang: en
permalink: /projects/cv-automation/
pretty_table: true
toc:
  sidebar: left
---

An automated system for generating a Curriculum Vitae and cover letter in both Italian and English. Built on **LaTeX** with the `moderncv` class, but rethought from the inside: content is fully separated from presentation and lives in a single `data.json` file.

## The Problem It Solves

Keeping a CV up to date in two languages across separate `.tex` files means updating every piece of data twice, in two different places - with the risk of them falling out of sync. This project eliminates that redundancy entirely.

## How It Works

### Single Source of Truth

Everything - work experience, education, skills, projects, personal info - lives in one `data.json`. Updating the CV means editing that one file.

### The Lua ↔ LaTeX Bridge

The file `commons/lua_data_loader.tex` contains a **Lua** script that, during compilation via **LuaLaTeX**, reads the JSON and dynamically populates the document sections in the selected language. It's not a static template - it's code that runs at compile time.

### CI/CD Pipeline

A **GitHub Actions** workflow automatically compiles all four documents on every push and publishes them to the `pdf-release` branch. From there, a second step syncs them directly to the personal website repository (`eneamanzi.github.io`), keeping the online version always current with no manual intervention.

```
data.json  →  lua_data_loader.tex  →  LuaLaTeX  →  PDF
                                                      ↓
                                          GitHub Actions deploy
                                                      ↓
                                       eneamanzi.github.io (always up-to-date)
```

## Generated Documents

| Document | Language |
|----------|----------|
| Curriculum Vitae | Italian |
| Curriculum Vitae | English |
| Cover Letter | Italian |
| Cover Letter | English |

## Tech Stack

- **Markup language:** LaTeX (`moderncv`)
- **Compilation engine:** LuaLaTeX
- **Scripting:** Lua
- **Data format:** JSON
- **Automation:** GitHub Actions
- **Build tool:** `latexmk`

[View on GitHub](https://github.com/eneamanzi/Curriculum-Vitae)