# Portfolio di Enea Manzi

Questo è il repository del mio sito web personale e portfolio professionale.

**Sito Live:** [https://eneamanzi.github.io](https://eneamanzi.github.io)

## Tecnologia

* **Framework:** [Jekyll Static Site Generator](https://jekyllrb.com/)
* **Tema:** [al-folio](https://github.com/alshedivat/al-folio) (versione alleggerita per portfolio professionale)
* **Hosting:** GitHub Pages
* **Gestione:** Docker (per sviluppo locale)

## Sviluppo Locale

Per eseguire il sito in locale assicurati di avere Docker installato, poi usa questi comandi:

1.  **Costruisci l'immagine** (necessario la prima volta o dopo modifiche al `Gemfile`):
    ```bash
    docker compose build
    ```

2.  **Avvia il server**:
    ```bash
    docker compose up
    ```

Il sito sarà disponibile su: `http://localhost:8080`

## Licenza

Il codice sorgente di questo sito è basato sul tema [al-folio](https://github.com/alshedivat/al-folio), distribuito sotto [MIT License](https://github.com/eneamanzi/eneamanzi.github.io/blob/main/LICENSE).
I contenuti personali del sito (testi, progetti, immagini personali) sono © Enea Manzi.