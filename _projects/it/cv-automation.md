---
layout: page
title: CV Data-Driven con LaTeX, Lua e GitHub Actions
description: CV e lettera di presentazione bilingue generati da un unico file JSON con LaTeX e Lua. Compilazione e deploy automatizzati tramite GitHub Actions.
subtitle: "LaTeX · Lua · GitHub Actions"
img: assets/img/cv.png
importance: 2
category: Personal
page_id: cv-automation
lang: it
permalink: /projects/cv-automation/
pretty_table: true
toc:
  sidebar: left
---

Un sistema per la generazione automatica del Curriculum Vitae e della lettera di presentazione, disponibili in italiano e in inglese. Costruito su **LaTeX** con la classe `moderncv`, ma ripensato dall'interno: il contenuto è completamente separato dalla presentazione e risiede in un unico file `data.json`.

## Il problema che risolve

Tenere aggiornato un CV in due lingue su file `.tex` separati significa aggiornare ogni dato due volte, in due posti diversi, rischiando disallineamenti. Questo progetto elimina quella ridondanza.

## Come funziona

### Single Source of Truth

Tutto - esperienze, istruzione, competenze, progetti, dati personali - vive in un unico `data.json`. Per aggiornare il CV basta modificare quel file.

### Il bridge Lua ↔ LaTeX

Il file `commons/lua_data_loader.tex` contiene uno script **Lua** che, durante la compilazione con **LuaLaTeX**, legge il JSON e popola dinamicamente le sezioni del documento nella lingua selezionata. Non è un template statico: è codice che gira al momento della compilazione.

### Pipeline CI/CD

Un workflow **GitHub Actions** compila automaticamente tutti e quattro i documenti ad ogni push e li pubblica sul branch `pdf-release`. Da lì, un secondo step li sincronizza direttamente con il repository del sito personale (`eneamanzi.github.io`), mantenendo la versione online sempre aggiornata senza intervento manuale.

```
data.json  →  lua_data_loader.tex  →  LuaLaTeX  →  PDF
                                                      ↓
                                          GitHub Actions deploy
                                                      ↓
                                       eneamanzi.github.io (always up-to-date)
```

## Documenti generati

| Documento | Lingua |
|-----------|--------|
| Curriculum Vitae | Italiano |
| Curriculum Vitae | Inglese |
| Lettera di presentazione | Italiano |
| Lettera di presentazione | Inglese |

## Stack tecnologico

- **Linguaggio di markup:** LaTeX (`moderncv`)
- **Motore di compilazione:** LuaLaTeX
- **Scripting:** Lua
- **Formato dati:** JSON
- **Automazione:** GitHub Actions
- **Build tool:** `latexmk`

[Vedi il repository su GitHub](https://github.com/eneamanzi/Curriculum-Vitae)