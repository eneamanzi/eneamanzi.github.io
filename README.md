# eneamanzi.github.io

Sito personale di Enea Manzi — [eneamanzi.github.io](https://eneamanzi.github.io) — basato sul tema Jekyll [al-folio](https://github.com/alshedivat/al-folio) (v1.x, architettura "thin starter + gem").

Questo file è la documentazione **personale** del repo: cosa c'è di reale, cosa arriva da altrove, dove guardare per cambiare qualcosa. Il README originale del tema (badge/community/star history di al-folio, non specifico di questo sito) è stato spostato in [`README.al-folio.md`](README.al-folio.md) — utile se cerchi la documentazione generale di al-folio, non per capire questo sito.

## Single Source of Truth: la maggior parte del contenuto non si modifica qui

Il CV, i progetti e le pubblicazioni **non si editano in questo repo**. Vivono nel repo separato [`Curriculum-Vitae`](https://github.com/eneamanzi/Curriculum-Vitae), sotto `data/*.json`, e da lì una CI li genera e li pusha qui automaticamente:

| File in questo repo                           | Generato da                                                                      | Editabile qui?                                                                                             |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `assets/pdf/cv_english.pdf`, `cv_italian.pdf` | `Curriculum-Vitae` → `build-latex.yml`                                           | ❌ mai                                                                                                     |
| `assets/json/resume.json`                     | `Curriculum-Vitae` → `generate_resume_json.py`                                   | ❌ mai                                                                                                     |
| `_data/socials.yml`                           | `Curriculum-Vitae` → `generate_socials_yml.py`                                   | ❌ mai                                                                                                     |
| `_bibliography/papers.bib`                    | `Curriculum-Vitae` → `generate_papers_bib.py`                                    | ❌ mai                                                                                                     |
| `_projects/<id>.md` (scaffold iniziale)       | `Curriculum-Vitae` → `scaffold_project_pages.py` (eseguito dalla CI del repo CV) | ✅ solo per espandere il contenuto _dopo_ la creazione, non i campi `cv_id`/`importance`/`category`        |
| `_data/coauthors.yml`, `_data/venues.yml`     | —                                                                                | ✅ sempre, a mano — sono preferenze di rendering (link/colori), non fatti del CV                           |
| `_pages/about.md`                             | —                                                                                | ✅ sempre, a mano — deliberatamente non generato, anche se condivide fatti col CV (vedi commento nel file) |
| `_config.yml`, immagini, resto del sito       | —                                                                                | ✅ sempre, a mano                                                                                          |

Per aggiungere/modificare un lavoro, un progetto, una pubblicazione, una lingua, una competenza: si fa **nel repo `Curriculum-Vitae`**, non qui. Vedi il suo README per la lista completa di "dove cambiare cosa".

## Cosa è reale e cosa è demo del tema

Pagine attive: `/cv/`, `/projects/`, `/publications/`, `/career/`, home (`/`).
Pagine disattivate (404 reale, tolte dalla navbar): blog, people, repositories, dropdown/submenus, books, teaching — tutte contenuto demo del tema, mai usate. Il perché di ognuna, con le istruzioni esatte per riattivarla in futuro, è in [`CUSTOMIZATIONS.md`](CUSTOMIZATIONS.md) — non ripetuto qui.

## Override locali del tema

`_includes/cv/render.liquid`, `skills.liquid`, `languages.liquid` sono copie locali che sovrascrivono i template dello stesso nome dentro il gem `al_folio_cv` (aggiungono la sezione "Research" e correggono un paio di bug estetici — dettagli nel README di `Curriculum-Vitae`, sezione "Website Integration").

Il file `.al-folio-overrides.yml` registra, per ognuno di questi 3 file, la versione del gem e i checksum al momento in cui l'override è stato "accettato" consapevolmente. Serve da sentinella: il workflow `upgrade-check.yml` (già attivo, gira a ogni push) segnala automaticamente se il gem cambia quel file upstream dopo l'accettazione — un warning non bloccante, visibile nei log/report di quella run.

**Se modifichi uno di questi 3 file**, rigenera il manifest con:

```bash
bundle exec al-folio upgrade overrides accept --all
```

e poi passa il risultato per Prettier (`npx prettier --write .al-folio-overrides.yml`) prima di committare — il gem non produce output già conforme allo stile di questo repo.

## Aggiornare il tema (non è un `git pull`)

Questo sito **non ha nessun legame git con `alshedivat/al-folio`** (creato con "Use this template", non un fork) — non esiste un "pull dall'upstream" da fare. In v1.x il rendering vero non vive in questo repo ma in gem Ruby pubblicati separatamente (`al_folio_core`, `al_folio_cv`, `al_folio_distill`, ecc. — elenco completo in `Gemfile`). Aggiornare il tema significa alzare il numero di versione di un gem ed eseguire `bundle update`/`bundle install` — esattamente come un pacchetto npm o pip, non un merge di file. I tuoi contenuti/config/dati non vengono mai toccati da questo processo.

L'unica eccezione sono i 3 file overriddati sopra: quelli, un aggiornamento del gem non li tocca mai in automatico (la tua copia locale vince sempre) — da qui il bisogno del tripwire `.al-folio-overrides.yml`.

Per il dettaglio su gem/ownership/confini, vedi [`docs/BOUNDARIES.md`](docs/BOUNDARIES.md) (documentazione del tema, generica ma accurata).

## Sviluppo locale

```bash
docker compose up
```

**Attenzione**: Jekyll in modalità `--watch` (quella usata da `docker compose up`) **non ricarica le modifiche a `_config.yml`** — solo il contenuto delle pagine si rigenera al volo. Se cambi `_config.yml` (es. `exclude:`, `scholar:`, qualunque impostazione), serve un riavvio vero:

```bash
docker compose down && docker compose up
```

Salvare il file e aspettare non basta.

Per una build singola (non il server con watch), utile per verificare che tutto compili prima di un push:

```bash
docker compose run --rm jekyll bundle exec jekyll build
```

## CI/CD rilevante

Il repo ha diversi workflow ereditati dal tema (CodeQL, Axe, docker image checks, ecc. — vedi `docs/` per l'elenco completo). Quelli che contano davvero per questo sito:

- **`deploy.yml`** ("Deploy site") — build Jekyll completa e pubblicazione su `gh-pages` a ogni push su `main`.
- **`prettier.yml`** ("Prettier code formatter") — controlla la formattazione di _tutto_ il repo (tranne quanto in `.prettierignore`) a ogni push/PR. Non corregge da solo: se fallisce, genera un diff scaricabile ma serve un tuo commit con la correzione (`npx prettier --write .`).
- **`upgrade-check.yml`** ("Upgrade contract checks") — l'audit del tema descritto sopra; i suoi avvisi sono sempre non bloccanti.
- **`scaffold-projects.yml`** ("Scaffold Project Pages from CV") — reagisce a un push su `resume.json`; nella pratica trova quasi sempre già tutto fatto (la CI del repo CV esegue lo stesso script prima di pushare), resta come rete di sicurezza.
- **`broken-links-site.yml`** ("Check for broken links on site") — controllo reale dei link nel sito buildato, gira dopo ogni deploy riuscito.
- **`update-citations.yml`** ("Update Google Scholar Citations") — aggiorna `_data/citations.yml` da Google Scholar, 3 volte a settimana.

**Nota**: c'è anche un `broken-links.yml` (nome quasi identico al primo) che risulta **sempre "skipped"** nella tab Actions — non è un errore, è un file `if: github.repository == 'alshedivat/al-folio'` residuo del tema originale, disattivato per sempre su questo fork. Il controllo vero è `broken-links-site.yml`, sopra. Se lo vedi sempre skippato, è normale, ignoralo.

I push da `Curriculum-Vitae` arrivano qui già come commit pronti (non c'è un workflow _in questo repo_ che li "riceve" attivamente — è la CI dell'altro repo che fa il checkout di questo e pusha).

## Attenzione a questo (bug reali già risolti)

- **Mai un esempio BibTeX commentato con `%` dentro `_bibliography/papers.bib`**, per quanto sembri innocuo — verificato che fa crashare la build con le versioni attuali del toolchain (`jekyll-scholar`/`bibtex-ruby`). Il generatore nel repo CV non ne produce più; se editi quel file a mano, evita questo pattern. Dettagli completi in `CUSTOMIZATIONS.md` → sezione Publications, punto 7.
- **Non usare azioni GitHub tipo `cpina/github-action-push-to-another-repository`** per push cross-repo verso questo sito — fanno `rm -rf` sulla cartella target prima di copiare, e hanno cancellato per errore diversi file reali in passato. Il pattern sicuro (checkout diretto + `git add` mirato) è quello già in uso nella CI del repo CV.

## Per approfondire

- [`CUSTOMIZATIONS.md`](CUSTOMIZATIONS.md) — log dettagliato di ogni funzionalità del tema disattivata/riattivata, con motivo e istruzioni di rollback.
- README del repo [`Curriculum-Vitae`](https://github.com/eneamanzi/Curriculum-Vitae) — dove e come modificare i dati veri (CV, progetti, pubblicazioni).
- [`docs/README.md`](docs/README.md), [`docs/QUICKSTART.md`](docs/QUICKSTART.md), [`docs/INSTALL.md`](docs/INSTALL.md), [`docs/CUSTOMIZE.md`](docs/CUSTOMIZE.md), [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md), [`docs/FAQ.md`](docs/FAQ.md) — documentazione generica del tema al-folio, utile per capacità non specifiche di questo sito.
- [`AGENTS.md`](AGENTS.md) / [`CLAUDE.md`](CLAUDE.md) / [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — regole per assistenti AI che lavorano su questo repo (es. quando serve l'audit degli override) — utile leggerli prima di far lavorare un agente qui.
