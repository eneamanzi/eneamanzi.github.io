# Customizations Log

Traccia delle funzionalità del template al-folio disattivate durante la personalizzazione del sito, con indicazione di come riattivarle in futuro. Le modifiche sui **dati/contenuti reali** (CV, progetti, about, ecc.) sono documentate nel piano di migrazione, non qui: questo file segue solo i **toggle on/off** di feature del template.

Formato per ogni voce: cosa è stato disattivato, dove, perché, come tornare indietro.

---

## GitHub Actions — "Integration tests" rimosso

- **Cosa**: workflow `.github/workflows/unit-tests.yml` ("Integration tests" nella tab Actions) cancellato per davvero, non solo disattivato.
- **Motivo**: fallisce in modo permanente e non risolvibile su questo sito. Il job `comments-integration-tests` esegue `test/integration_comments.sh`, uno script fornito dal template stesso che verifica la funzionalità Giscus controllando l'esistenza di una pagina di un post del blog di esempio (`/blog/2022/giscus-comments/`). Dato che il blog è disattivato per scelta (cartella `_posts` rinominata, vedi sezione Blog), quella pagina non esiste più e il test fallisce sempre — non testa un problema reale del sito, testa una funzionalità del template (blog + commenti) che abbiamo intenzionalmente spento. Questo workflow, insieme agli altri test/CI presenti nel repo, è pensato per chi sviluppa/mantiene il template al-folio stesso (verificare che tutte le feature del tema funzionino su ogni versione), non per un sito personale che ne usa solo una parte.
- **Per riattivare in futuro**: ricrea il file `.github/workflows/unit-tests.yml` (disponibile nel repo ufficiale del template al-folio v1, o nella cronologia git se il repo è versionato) — ha senso solo se si riattiva anche il blog, altrimenti tornerebbe a fallire allo stesso modo.

---

## CV — solo formato JSON Resume (rendercv rimosso)

Decisione presa perché il CV in PDF è gestito da una repo separata (LaTeX/Lua/GitHub Actions), quindi la pipeline `rendercv` di questo sito (che genera un PDF alternativo da `_data/cv.yml` via Python/Typst) è ridondante — teniamo solo il formato JSON Resume per la vista HTML su `/cv/`.

- **Cosa**: formato CV cambiato da `rendercv` a `jsonresume`.
  - File: `_pages/cv.md` → `cv_format: rendercv` → `cv_format: jsonresume`
  - La pagina `/cv/` ora legge solo da `assets/json/resume.json` (schema JSON Resume), non più da `_data/cv.yml`.
- **Cosa**: rimossi per davvero (non solo disattivati) i file legati esclusivamente alla pipeline rendercv, ormai morta:
  - `_data/cv.yml` — dati duplicati rispetto a `resume.json`, non più letti da nessuna pagina.
  - `assets/rendercv/` (intera cartella: `design.yaml`, `locale.yaml`, `settings.yaml`, `rendercv_output/Albert_Einstein_CV.pdf` — quest'ultimo un placeholder del template mai sostituito).
  - `.github/workflows/render-cv.yml` — il workflow GitHub Actions che rigenerava il PDF da `_data/cv.yml` a ogni push; era anche il workflow che falliva nella CI (schema più rigido di rendercv rispetto a quello che accetta il tema Liquid).
  - Riga `rendercv[full]` in `requirements.txt` (dipendenza Python non più necessaria; `nbconvert` e `scholarly` restano, servono ad altro).
  - Cancellati per davvero e non commentati perché non sono contenuti/esempi del template da preservare come riferimento, ma un'intera pipeline tecnica non più usata.
- **Per riattivare in futuro**: rimetti `cv_format: rendercv` in `_pages/cv.md`, ricrea `_data/cv.yml` (schema rendercv, vedi `assets/json/resume.json` per i dati equivalenti da riportare), ripristina `assets/rendercv/*.yaml` e la riga `rendercv[full]` in `requirements.txt`, e riaggiungi un workflow tipo `render-cv.yml` (consultare la cronologia di questo file o la doc di al-folio v1 per il template originale).

---

## Blog

Aggiornamento: `nav: false` da solo NON basta — la pagina restava comunque generata e raggiungibile su `/blog/` (confermato: `jekyll-sitemap` non rispetta `nav`, quindi la pagina finiva pure in `sitemap.xml`). Percorso corretto verificato online (vedi fonti in fondo): escludere la pagina dalla build ed eliminare la collection `_posts`, che in Jekyll è una collection "hardwired" non disattivabile da config — l'unico modo affidabile è rinominare la cartella.

- **Cosa**: pagina blog (`/blog/`) esclusa completamente dalla build (404 reale, non più in `_site/`).
  - File: `_config.yml`, sezione `exclude:`
  - Modifica: aggiunta la riga `- _pages/blog.md` (stesso pattern già usato dal template per `_pages/about_einstein.md`)
  - Per riattivare: rimuovi la riga `- _pages/blog.md` da `exclude:`.

- **Cosa**: tutti i singoli post di esempio (`/blog/2015/...` ecc.) esclusi dalla build.
  - Cartella: `_posts/` → rinominata in `_posts.disabled/`
  - Motivo: `_posts` è una collection speciale di Jekyll, non escludibile in modo affidabile via `exclude:` in config (verificato: [jekyll/jekyll#5064](https://github.com/jekyll/jekyll/issues/5064), [jekyll/jekyll#7186](https://github.com/jekyll/jekyll/issues/7186)); il workaround riconosciuto dalla community è rinominare/spostare la cartella ([Jekyll Talk](https://talk.jekyllrb.com/t/i-dont-want-posts-on-my-website-how-to-remove-this-default-collection/1605)).
  - Per riattivare: rinomina `_posts.disabled/` in `_posts/`.

- **Cosa**: sezione "Latest Posts" rimossa dalla home page (about).
  - File: `_pages/about.md`
  - Modifica: `latest_posts.enabled: true` → `latest_posts.enabled: false`
  - Per riattivare: rimetti `enabled: true` (ha senso solo se anche `_posts/` è riattivata).

- **Non toccato**: la config `blog_name` / `blog_description` / `permalink` / `pagination` / `related_blog_posts` / `disqus_shortname` / `giscus` / `jekyll-archives` in `_config.yml` è rimasta invariata (inerte finché `_posts/` resta disabilitata).
- **Nota collegata**: `_pages/dropdown.md` (esempio di sottomenu) contiene un link figlio alla pagina blog — non toccato, tornerà coerente da solo se riattivi tutto quanto sopra.
- **Fonti consultate**: [jekyll/jekyll#5064](https://github.com/jekyll/jekyll/issues/5064), [jekyll/jekyll#7186](https://github.com/jekyll/jekyll/issues/7186), [Jekyll Talk – I don't want posts on my website](https://talk.jekyllrb.com/t/i-dont-want-posts-on-my-website-how-to-remove-this-default-collection/1605), [jekyll-sitemap README](https://github.com/jekyll/jekyll-sitemap).

- **Scoperta successiva (dopo verifica in locale)**: nonostante `_pages/blog.md` escluso e `_posts/` rinominata, `/blog/2022/` e `/blog/2024/` continuavano a comparire anche dopo un rebuild pulito (`docker compose down` + `up --build`). Causa: il plugin `al_ext_posts` (in `plugins:`) genera **post sintetici da fonti esterne** ad ogni build, a partire dal blocco `external_sources:` in `_config.yml` (un feed RSS di medium.com + una entry statica del 2024) — totalmente indipendente dalla cartella `_posts/`. Non erano residui di cache, erano rigenerati ogni volta.
  - File: `_config.yml`
  - Modifica: l'intero blocco `external_sources:` è stato **commentato** (non cancellato) con una riga di nota sopra, così resta visibile cosa c'era e perché è disattivato.
  - Per riattivare: decommenta il blocco `external_sources:` (righe subito sopra la nota "Disabled as part of the blog shutdown").

---

## Repositories

- **Cosa**: pagina `/repositories/` (widget statistiche/trophy GitHub via servizi esterni `github-readme-stats.vercel.app` e `github-profile-trophy.vercel.app`) esclusa completamente dalla build (404 reale) e tolta dalla navbar.
  - File: `_pages/repositories.md` → `nav: true` → `nav: false`
  - File: `_config.yml`, sezione `exclude:` → aggiunta la riga `- _pages/repositories.md`
  - Per riattivare: rimuovi la riga da `exclude:` in `_config.yml` e rimetti `nav: true` in `_pages/repositories.md`.
- **Motivo**: a differenza di `_pages/projects.md` (contenuti curati, scritti a mano), questa pagina è un widget auto-generato che pesca dati live da due servizi terzi — poco valore aggiunto rispetto al link GitHub già presente nei social, più una dipendenza esterna evitabile.
- **Non toccato**: `_data/repositories.yml` (ancora con `github_users`/`github_repos` placeholder del template) — inerte finché la pagina resta esclusa, pronto se un giorno la riattivi con i tuoi dati reali.

---

## People

- **Cosa**: pagina `/people/` (layout "profiles", pensata per mostrare i membri di un laboratorio/gruppo di ricerca, non per un portfolio individuale) esclusa completamente dalla build (404 reale) e tolta dalla navbar.
  - File: `_pages/profiles.md` → `nav: true` → `nav: false`
  - File: `_config.yml`, sezione `exclude:` → aggiunta la riga `- _pages/profiles.md`
  - Per riattivare: rimuovi la riga da `exclude:` in `_config.yml` e rimetti `nav: true` in `_pages/profiles.md`.
- **Motivo**: il template mostra due card duplicate che puntano entrambe al placeholder `about_einstein.md` (già escluso di suo) — funzionalità pensata per un sito di gruppo/lab con più persone, non pertinente a un portfolio personale.
- **Non toccato**: `_data/coauthors.yml` — non è collegato a questa pagina, serve al matching dei nomi coautori per le citazioni bibliografiche di `jekyll-scholar` (irrilevante finché non usi `_bibliography/papers.bib` con più autori).

---

## Submenus (dropdown)

- **Cosa**: pagina/voce nav `submenus` (esempio del template per creare un menu a tendina nella navbar, non contenuto vero e proprio) esclusa completamente dalla build (404 reale) e tolta dalla navbar.
  - File: `_pages/dropdown.md` → `nav: true` → `nav: false`
  - File: `_config.yml`, sezione `exclude:` → aggiunta la riga `- _pages/dropdown.md`
  - Per riattivare: rimuovi la riga da `exclude:` in `_config.yml` e rimetti `nav: true` in `_pages/dropdown.md`.
- **Motivo**: è solo la demo della funzionalità "dropdown/submenu" del tema, non contenuto reale. I due link che conteneva (`bookshelf` e `blog`) sono entrambi disattivati/inutilizzati oggi.
- **Predisposta per il futuro**: il file `_pages/dropdown.md` resta com'era (struttura `dropdown: true` + `children:` intatta) apposta, così se un giorno serve un vero menu a tendina (es. un dropdown "CV" con dentro `/cv/` e `/career/`) basta riattivarla e aggiornare la lista `children:` con i link giusti — il link a `blog` andrebbe comunque tolto/sostituito perché quella pagina resta disattivata.

---

## Publications

**Stato: riattivata (2026-07-22)** — c'è una prima pubblicazione vera, generata automaticamente dalla single source of truth del repo `Curriculum-Vitae` (vedi sotto). Caso diverso dagli altri file di questa pagina: qui i dati non si editano a mano nel sito.

- **Cosa**: voce "publications" rimessa in navbar.
  - File: `_pages/publications.md` → `nav: false` → `nav: true`.
  - Per disattivarla di nuovo (es. se si torna a zero pubblicazioni vere): rimetti `nav: false` **e** riaggiungi `- _pages/publications.md` a `exclude:` in `_config.yml` — vedi il punto 7 qui sotto sul perché l'esclusione dalla build è necessaria con bibliografia vuota, non basta il solo `nav: false`.

- **Cosa**: `_bibliography/papers.bib`, `_data/coauthors.yml`, `_data/venues.yml` — **non editarli qui a mano**.
  - `papers.bib` è generato dalla CI del repo `Curriculum-Vitae` (`scripts-website-data/generate_papers_bib.py`) a partire da `data/60-publications.json`, e pushato con lo stesso meccanismo di `resume.json`/`socials.yml` (vedi il README di quel repo). Il campo `bibtex` di ogni pubblicazione lì è il testo di citazione così com'è (scritto a mano finché il paper è "submitted", poi copiato dal publisher una volta indicizzato) — questo script non fa parsing/ricostruzione di BibTeX da campi separati.
  - `_data/coauthors.yml`/`_data/venues.yml` restano invece manutenuti **a mano qui nel sito** (non sono fatti del CV ma preferenze di rendering — a quale URL linkare un coautore, che colore per una venue) — ognuno ha in testa un solo esempio commentato con tutti i parametri possibili, invece delle vecchie voci demo Einstein.
  - Per aggiungere una pubblicazione vera: si fa nel repo CV (`data/60-publications.json`), non qui.
  - **Bug incontrato e risolto durante il test in locale (2 round)**:
    1. Primo tentativo: avvolgere le voci in blocchi `@comment{...}` invece che commentarle riga per riga → crash in build (`BibTeX::ParseError: cite-key missing`), perché il parser Ruby (`bibtex-ruby`) usato da questo sito non gestisce bene `@comment{chiave, campo=valore,...}` con caratteri particolari nelle voci Einstein. Corretto passando al commento riga-per-riga con `%`.
    2. Con la bibliografia completamente commentata, il build continuava comunque a crashare con lo stesso errore. Causa reale: il placeholder `_projects/1_project.md` (template, non toccato prima) conteneva `{% cite einstein1950meaning %}` — con quella chiave non più presente nel file, il percorso "citazione non trovata" di questa versione di `jekyll-scholar` genera internamente una voce BibTeX malformata e crasha, indipendentemente da cosa contenga `papers.bib`.
    - **Fix**: in `_projects/1_project.md`, la citazione live `{% cite einstein1950meaning %}` è stata sostituita con un esempio scritto in chiaro (avvolto in `{% raw %}...{% endraw %}` così Liquid non la esegue) che mostra la sintassi `{% cite your-bibtex-key %}` senza eseguirla — il placeholder resta come riferimento su come si cita, ma non prova più a risolvere una chiave inesistente.
    - Per riattivare una citazione vera: aggiungi una voce reale in `papers.bib` e sostituisci l'esempio in chiaro con un vero tag `{% cite tua-chiave %}` (senza `{% raw %}`) in qualunque pagina/progetto.
    3. Con la citazione neutralizzata, la build crashava comunque — stesso errore, ma stavolta durante il rendering del _layout_ `page.liquid` (gemma `al_folio_core`, non nostro), che per pagine con `related_publications: true` in front matter (es. `_projects/1_project.md`) prova a leggere l'intera bibliografia per un blocco "pubblicazioni correlate".
    - Primo sospetto (sbagliato, poi corretto): le due righe `---`/`---` in cima a `papers.bib`. Rimosse per test, ma il crash è rimasto **identico** — quindi non erano la causa. Le due righe sono state **rimesse** (fanno parte della struttura standard del file anche nel template originale).
    - Causa reale: con la bibliografia completamente vuota (zero citazioni attive in tutto il sito) e almeno una pagina con `related_publications: true`, la funzione interna di `jekyll-scholar` che genera il blocco "pubblicazioni correlate" costruisce una query BibTeX vuota/malformata e crasha — indipendentemente dal contenuto di `papers.bib`. Bug della combinazione "bibliografia vuota + `related_publications: true`" in questa versione della gemma, non un problema nel nostro file.
    - **Fix**: `related_publications: true` → `false` nei due placeholder che lo usavano (`_projects/1_project.md`, `_projects/7_project.md`).
    - **Attenzione per il futuro**: finché `_bibliography/papers.bib` non ha almeno una voce reale attiva, evita di impostare `related_publications: true` su qualunque pagina/progetto — farebbe crashare la build. Per riattivare: rimetti `related_publications: true` solo dopo aver aggiunto almeno una pubblicazione vera e non commentata nel file.
    4. Il fix del punto 2 era stato applicato solo a `_projects/1_project.md`: `_projects/7_project.md` (l'altro placeholder con `related_publications: true`) aveva la **stessa identica riga** `{% cite einstein1950meaning %}` non ancora sistemata, e ha fatto crashare la build allo stesso modo. Per chiudere la questione una volta per tutte è stata fatta una ricerca su tutto il repo per `{% cite`, `{% bibliography` e `related_publications: true`: le uniche occorrenze rimaste attive erano quella in `7_project.md` (sistemata con lo stesso trattamento raw/esempio) e `{% bibliography %}` in `_pages/publications.md` (lasciata: lista tutte le voci reali, con bibliografia vuota dovrebbe semplicemente non mostrare nulla, da confermare al prossimo build). L'occorrenza in `_posts.disabled/2023-07-12-post-bibliography.md` è innocua: quella cartella non è più letta da Jekyll (vedi sezione Blog).
    5. Con tutti i placeholder progetti sistemati, il crash si è ripresentato una terza volta, stavolta su `_pages/about.md` — causa `selected_papers: true` (mai toccato fino a questo punto), che internamente chiama la stessa funzione `cited_entries` andata in crash nei punti 3 e 4. Confermato: il bug è sistemico — qualunque funzione del tema che interroga "citazioni/pubblicazioni già usate nel sito" crasha quando la bibliografia ha zero voci attive, indipendentemente da quale pagina lo scateni. Non è da escludere che esistano altri punti simili in file della gemma `al_folio_core` che non possiamo leggere/modificare direttamente.
    - **Fix scelto**: invece di aggiungere una voce placeholder al bibliografia (opzione scartata), `selected_papers: true` → `false` in `_pages/about.md`.
    - Per riattivare: rimetti `selected_papers: true` in `_pages/about.md` solo dopo aver aggiunto almeno una pubblicazione vera e non commentata in `papers.bib`, marcata con `selected = {true}`.
    - **Nota**: se in futuro compare di nuovo lo stesso errore (`BibTeX::Parser#missing_key` / "cite-key missing") su un'altra pagina, la causa è quasi certamente la stessa: qualche altro front-matter flag che attiva un blocco "pubblicazioni/citazioni" del tema mentre `papers.bib` è ancora vuoto. La soluzione è la stessa: disattivare quel flag specifico finché non c'è almeno una pubblicazione vera nel file.
    6. Puntualmente, il crash si è ripresentato una quarta volta esattamente dove segnalato al punto 4 come rischio non confermato: `{% bibliography %}` in `_pages/publications.md` stessa. A differenza degli altri casi, qui il tag non è un extra della pagina ma il suo unico scopo — con bibliografia a zero voci la pagina non può funzionare, non ha senso tenerla "vuota" perché in realtà crasha la build.
    - **Fix**: `_pages/publications.md` aggiunta a `exclude:` in `_config.yml` — stesso trattamento (esclusione reale, 404) già usato per blog/repositories/profiles/dropdown, invece di continuare a disattivare un flag alla volta senza toccare la build.
    - Per riattivare: rimuovi la riga `- _pages/publications.md` da `exclude:` **solo dopo** aver aggiunto almeno una pubblicazione vera e non commentata in `papers.bib` (altrimenti la pagina torna a crashare la build).
    7. **(2026-07-22, alla riattivazione con la prima pubblicazione vera)** Rimossa l'esclusione e aggiunta una voce reale in `papers.bib` (con sopra, come da punto precedente, l'header di 9 esempi Einstein commentati riga-per-riga con `%`) → la build crashava di nuovo, stesso identico errore delle volte precedenti (`Jekyll::Cache#[]: unhandled exception` propagato da `jekyll-scholar`). Isolato con test mirati (build Docker reali, non supposizioni):
       - Con bibliografia vuota (solo l'header commentato, nessuna voce reale) + pagina riattivata → crash.
       - Con **una sola** voce di esempio commentata (anche solo 6 righe, non l'header intero da 9 voci) + la voce vera → crash identico.
       - Con **zero** righe `%`-commentate che assomigliano a una voce BibTeX (`@tipo{chiave, campo=valore}`), solo un avviso in chiaro + la voce vera → build **pulita**.
       - **Causa reale**: il parser `bibtex-ruby` (6.2.0, via `jekyll-scholar` 7.3.0) in uso oggi in questa immagine Docker **non tratta più in modo sicuro un `%`-commento che ha la forma di una voce BibTeX**, anche se sintatticamente è "solo un commento" — probabilmente una regressione del parser rispetto a quando questo trick fu testato la prima volta (punto 1 sopra). Il messaggio "unhandled exception" è un artefatto del meccanismo di cache interno di Jekyll che maschera il vero errore (`BibTeX::ParseError`) su alcune versioni di Ruby - con Ruby 3.3 il vero errore emerge chiaramente, con la Ruby più recente dell'immagine (4.0.x, non pinnata né qui né nel repo ufficiale al-folio) viene mascherato.
       - **Fix**: tolto qualunque esempio `%`-commentato somigliante a una voce BibTeX da `papers.bib` (generato dallo script del repo CV, vedi sopra) - resta solo un avviso in chiaro senza forma `@tipo{...}`. Il riferimento ai campi possibili (`selected`, `preview`, `bibtex_show`, `doi`, ecc.) è stato spostato qui in `CUSTOMIZATIONS.md` (markdown puro, mai passato dal parser BibTeX, quindi a rischio zero): {selected: true} evidenzia un paper in home (richiede anche `selected_papers: true` in `about.md`); `preview: nome-file.png/gif` mostra un'anteprima; `bibtex_show: true` mostra il BibTeX grezzo espandibile; `doi`/`altmetric`/`dimensions`/`google_scholar_id`/`inspirehep_id` alimentano i badge citazione; `award`/`award_name` mostrano un riconoscimento; `video`/`html`/`url`/`pdf` sono link aggiuntivi; `abbr` è l'etichetta breve della venue (vedi `_data/venues.yml`); `additional_info` aggiunge testo libero (markdown) sotto la voce; `annotation` aggiunge una nota a piè di voce.
       - **Attenzione per il futuro**: non rimettere mai un blocco di esempi BibTeX commentato con `%` direttamente in `papers.bib`, per quanto sembri innocuo — verificato che fa crashare la build con le versioni attuali del toolchain. Se serve un esempio, va nella documentazione (qui), mai nel file `.bib` stesso.

- **Cosa**: dati autore aggiornati nella config di jekyll-scholar (dato vero, non un toggle).
  - File: `_config.yml`, sezione `scholar:`
  - Modifica: `last_name: [Einstein]` → `last_name: [Manzi]`; `first_name: [Albert, A.]` → `first_name: [Enea, E.]` (varianti nome/nome abbreviato, per evidenziare in grassetto l'autore nelle liste); `style: apa` → `style: ieee` (preferenza).
  - Tutti gli altri campi di `scholar:` (`source`, `bibliography`, `bibliography_template`, `bibtex_filters`, `replace_strings`, `join_strings`, `details_dir`, `details_link`, `query`, `group_by`, `group_order`) sono stati rivisti ma **non toccati**: sono impostazioni tecniche/strutturali del tema, corrette di default indipendentemente dal contenuto.

---

## Organizzazione esempi del template (Projects / News / Books)

Introdotto un sistema generale per gestire i contenuti di esempio che vengono con il template (placeholder di progetti, annunci, libri), separato dal caso "pagina intera disattivata" già usato sopra: qui si tratta di **singoli elementi dentro una collection** (`_projects`, `_news`, `_books`), non di pagine.

- **Strumento usato**: `published: false` nel front matter di ogni file — è una funzionalità nativa di Jekyll (non del tema), verificata prima di applicarla: esclude davvero il file dalla build (nessuna pagina generata, 404 reale) **e** lo toglie automaticamente da qualsiasi `site.<collection>` usato dai listati (`site.projects`, `site.news`, `site.books`), senza bisogno di toccare `exclude:` in `_config.yml` per ogni singolo file. Per riattivare un elemento: rimuovi la riga `published: false` (o mettila a `true`).

- **Cosa**: i 9 progetti placeholder del template spostati in una sottocartella dedicata.
  - File: `_projects/1_project.md` … `_projects/9_project.md` → spostati in `_projects/examples/`
  - Motivo dello spostamento in sottocartella: separare visivamente/nella struttura repo "esempi da cui prendere ispirazione" dai progetti veri, che restano nella root di `_projects/`.
  - **Verificato prima di spostare**: i 5 progetti veri (`ftp-client.md`, `ftp-server.md`, `exhibition-webapp.md`, `cv-automation.md`, `k8s-kafka-kong.md`) hanno tutti un `permalink:` scritto a mano nel front matter, quindi il loro URL non dipende dalla cartella in cui si trova il file — spostare o riorganizzare non li rompe. I placeholder invece non hanno un `permalink:` esplicito.
  - **Aggiornamento**: inizialmente disattivati con `published: false` (404 reale). Successivamente, su richiesta esplicita, **riattivati** e raggruppati sotto una categoria dedicata `category: Example` (al posto di `work`/`fun` originali del template), aggiunta anche a `display_categories` in `_pages/projects.md`, così sono di nuovo visibili sulla pagina `/projects/` ma chiaramente separati/etichettati come esempi.
  - **Nota sull'URL**: non avendo un `permalink:` esplicito, ora che sono di nuovo pubblicati il loro URL riflette la sottocartella: `/projects/examples/1_project/` invece del vecchio `/projects/1_project/` — non è un problema (nessun link esterno punta a queste pagine), anzi rende ancora più chiaro che sono pagine di esempio.
  - Per ri-disattivarli in futuro: rimetti `published: false` in ciascun file. Per farne uno vero: cambia `category`, scrivi contenuti reali, e aggiungi un `permalink:` esplicito se vuoi un URL stabile indipendente dalla cartella.
  - **Pulizia doppioni**: analizzando i 9 file è emerso che il _corpo_ della pagina era identico, parola per parola, in tutti e 9 (stessa demo "griglia immagini a 3 colonne") — cambiava solo il front matter, e anche lì con doppioni: `giscus_comments: true` era demo sia in `2_project.md` sia in `8_project.md` (copia esatta), "nessuna immagine" era demo sia in `4_project.md` sia in `6_project.md`, e la demo "con immagine di sfondo" era ripetuta 3 volte (1, 5, 7). Il flag `related_publications: false` su 1 e 7 non dimostrava più nulla di suo dato che è stato disattivato durante la vicenda BibTeX (vedi sezione Publications).
    - **Rimossi** (doppioni, nessuna funzionalità unica persa): `5_project.md`, `6_project.md`, `7_project.md`, `8_project.md`, `9_project.md`.
    - **Tenuti** (uno per ogni funzionalità realmente distinta): `1_project.md` (card con immagine), `2_project.md` (commenti Giscus), `3_project.md` (redirect a sito esterno), `4_project.md` (card senza immagine).
    - Questi 5 file sono stati cancellati per davvero (non commentati/disattivati) perché duplicati byte-per-byte del contenuto già presente in un file tenuto — non c'è nulla di unico da preservare come riferimento.
  - **Stato finale**: dopo averli mostrati per revisione visiva, i 4 esempi rimasti (`1_project.md`, `2_project.md`, `3_project.md`, `4_project.md`) sono stati **rimessi a `published: false`** su richiesta esplicita — restano nel repo come riferimento ma di nuovo esclusi dalla build. `Example` tolto anche da `display_categories` in `_pages/projects.md` (ora solo `[Academic, Personal]`), visto che con gli esempi disattivati la categoria risulterebbe vuota.

- **Cosa**: rimosse le immagini di copertina da tutti e 5 i progetti veri.
  - File: `_projects/ftp-client.md`, `ftp-server.md`, `exhibition-webapp.md`, `cv-automation.md`, `k8s-kafka-kong.md` → campo `img:` svuotato in tutti.
  - Motivo: le immagini originali (icone stile "clip art" colorato, stesso stile in `ftp-client.png`, `ftp.png`, `cv.png`, `exhibition-webapp.png`, più il logo ufficiale Kubernetes in `kubernetes.svg`) non piacevano esteticamente — troppo cartoonesche/vistose rispetto al resto del sito minimale. Valutate alternative (loghi puliti stile Simple Icons per Node.js/LaTeX, icona Font Awesome generica per FTP) ma scartate anche quelle.
  - **File immagine cancellati per davvero** (non più referenziati da nessuna parte, verificato con una ricerca sul repo prima di cancellare): `assets/img/ftp-client.png`, `assets/img/ftp.png`, `assets/img/cv.png`, `assets/img/exhibition-webapp.png`, `assets/img/kubernetes.svg`.
  - Per riattivare: aggiungi un valore a `img:` in uno o più progetti (screenshot reale, logo, o icona) e assicurati che il file immagine esista in `assets/img/`.

- **Cosa**: i 3 annunci placeholder del template spostati e disattivati.
  - File: `_news/announcement_1.md`, `_news/announcement_2.md`, `_news/announcement_3.md` → spostati in `_news/examples/`, con `published: false`.
  - Effetto: la sezione "news" in home (`announcements.enabled: true` in `_pages/about.md`, non toccato) ora mostra "No news so far..." invece dei 3 annunci di esempio — verificato che il tema gestisce il caso vuoto senza errori (non è lo stesso bug della bibliografia: qui c'è un `{% if site.news != blank %}` esplicito nel layout).
  - Per riattivare: togli `published: false` dal singolo annuncio che vuoi mostrare, oppure scrivi un annuncio vero in `_news/` (fuori da `examples/`).

- **Cosa**: il libro placeholder del template spostato e disattivato.
  - File: `_books/the_godfather.md` → spostato in `_books/examples/`, con `published: false`.
  - **Cosa**: pagina `/books/` esclusa completamente dalla build (stesso trattamento reale di blog/repositories/profiles/dropdown/publications/teaching) — prima aveva solo `nav: false`, stesso buco di sicurezza già corretto altrove in questo file.
    - File: `_config.yml`, sezione `exclude:` → aggiunta la riga `- _pages/books.md`
    - Per riattivare: rimuovi la riga da `exclude:` in `_config.yml`, e togli `published: false` da almeno un libro reale in `_books/`.

- **Verifica fatta dopo il cambio** (rebuild completo via `docker compose restart`, necessario perché le modifiche a `_config.yml` non vengono ricaricate automaticamente da Jekyll in modalità `--watch`):
  - `/projects/1_project/` (esempio) → 404 ✅
  - `/projects/ftp-client/` (vero) → 200 ✅, contenuto invariato
  - `/books/` → 404 ✅
  - `/career/`, `/cv/`, home → 200 ✅, nessuna regressione
  - Nessun errore/warning nei log del container dopo il rebuild.

- **Convenzione per il futuro**: qualsiasi nuovo esempio del template che arriva con un aggiornamento (o che troviamo esplorando altre collection) va gestito allo stesso modo — sottocartella `examples/` dentro la sua collection + `published: false`. Non cancellare mai i file placeholder, solo disattivarli così.

---

## Teaching

Caso simile a Publications (nessun contenuto oggi, ma potenzialmente utile in futuro — in questo caso per l'eventuale attività didattica durante il PhD), ma qui la funzionalità **non ha lo stesso rischio di crash**: la pagina non dipende da `papers.bib`/jekyll-scholar, quindi si può applicare fin da subito l'esclusione reale invece di limitarsi al solo `nav: false`.

- **Cosa**: pagina `/teaching/` (corsi insegnati, con calendario Google embeddato e lista corsi da `courses.liquid`) esclusa completamente dalla build (404 reale) e tolta dalla navbar.
  - File: `_pages/teaching.md` → `nav: true` → `nav: false`
  - File: `_config.yml`, sezione `exclude:` → aggiunta la riga `- _pages/teaching.md`
  - Per riattivare: rimuovi la riga da `exclude:` in `_config.yml` e rimetti `nav: true` in `_pages/teaching.md`.
- **Motivo**: nessun corso insegnato ad oggi; la pagina userebbe comunque un `calendar_id='test@gmail.com'` placeholder del template, da sostituire con un calendario reale quando servirà.
- **Non toccato**: il resto del front matter (`calendar: true`, l'include `{% include calendar.liquid calendar_id='test@gmail.com' timezone='Asia/Shanghai' %}`, `{% include courses.liquid %}`) resta invariato, pronto da aggiornare con i dati reali (calendar_id, timezone, ed eventuali file in una futura collection `_teachings/`, che al momento non esiste nel repo) quando la funzionalità servirà davvero.
