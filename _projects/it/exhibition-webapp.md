---
layout: page
title: Web App per Galleria d'Arte
description: Web app full-stack per la gestione e l'esposizione di opere d'arte. Backend Node.js/Express, MongoDB e area admin protetta con autenticazione.
img: assets/img/exhibition-webapp.png
importance: 5
category: University
page_id: exhibition-webapp
lang: it
permalink: /projects/exhibition-webapp/
---

# Web App per Galleria d'Arte

Web app full-stack per la gestione e l'esposizione di un catalogo di opere d'arte, sviluppata per il corso di **Programmazione Web e Mobile** (A.A. 2021-2022). L'applicazione distingue due tipologie di utente: il visitatore, che naviga la galleria pubblica, e l'admin, che gestisce il contenuto tramite un pannello protetto.

## Due ruoli, due esperienze

### Utente visitatore (pubblico)

Può sfogliare la galleria delle opere, aprire il dettaglio di ogni quadro con foto e descrizione, e navigare tra le sezioni del sito tramite una barra di navigazione condivisa.

### Utente admin (protetto)

Accede tramite login con password cifrata (**bcrypt**) e gestisce le opere direttamente dal browser: aggiunta con upload dell'immagine, modifica di titolo e descrizione, eliminazione con richiesta di conferma. Tutte le operazioni avvengono senza ricaricare la pagina, tramite chiamate **AJAX** asincrone al server.

## Architettura

Il backend è un server **Node.js/Express** che espone le route REST (GET, POST, PUT, DELETE) e gestisce le sessioni utente. I dati dei quadri - titolo, descrizione, data e percorso immagine - sono archiviati su **MongoDB** tramite schemi **Mongoose**. Il frontend comunica con il server esclusivamente via AJAX, costruendo il DOM dinamicamente in risposta ai dati ricevuti.

```
Browser  →  AJAX GET /getList  →  Express  →  MongoDB  →  JSON response  →  DOM update
```

L'upload delle immagini è gestito da **Multer**, che salva i file sul server e ne memorizza il percorso nel documento MongoDB corrispondente.

## Aspetti tecnici rilevanti

**Autenticazione e sessioni** - il login verifica la password con bcrypt e mantiene lo stato admin tramite `express-session`. Le route dell'area admin sono protette: senza sessione attiva, ogni richiesta viene respinta.

**Componenti condivisi** - navbar e footer sono file HTML separati, caricati dinamicamente via jQuery in tutte le pagine, evitando duplicazioni nel codice.

**Performance** - le immagini statiche sono compresse fino al 75% della dimensione originale e gli script sono posizionati in fondo al body per non bloccare il rendering. Le pagine sono validate tramite il W3C Validator.

## Stack tecnologico

- **Backend:** Node.js, Express, express-session, Multer, bcrypt, Mongoose
- **Database:** MongoDB
- **Frontend:** HTML5, CSS3, JavaScript, AJAX, jQuery, Bootstrap
- **Versioning:** Git / GitHub