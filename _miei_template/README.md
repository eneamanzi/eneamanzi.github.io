# Archivio Template

Questa cartella NON è processata da Jekyll (è nella lista `exclude` di `_config.yml`).
Contiene scheletri puliti di layout e pagine che potrebbero tornare utili in futuro.

## Struttura

- `layouts/`   → Layout Liquid pronti all'uso (spostarli in `_layouts/` per attivarli)
- `pages/`     → Front matter di riferimento per nuove sezioni del sito
- `projects/`  → Template front matter per nuove schede progetto
- `includes/`  → Include specializzati (es. Distill per post scientifici)

## Come usare un template

1. Copia il file nella cartella di destinazione corretta del progetto attivo
2. Rimuovi i commenti `# TEMPLATE:` dal front matter
3. Compila i campi con i tuoi contenuti reali