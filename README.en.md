**English version** | [Versione italiana](README.md)
# Enea Manzi's Portfolio

This is the repository for my personal website and professional portfolio.

**Live Site:** [https://eneamanzi.github.io](https://eneamanzi.github.io)

## Technology

* **Framework:** [Jekyll Static Site Generator](https://jekyllrb.com/)
* **Theme:** [al-folio](https://github.com/alshedivat/al-folio) (lightweight version for professional portfolio)
* **Hosting:** GitHub Pages
* **Management:** Docker (for local development)

## Local Development

To run the site locally, make sure you have Docker installed, then use these commands:

1.  **Build the image** (required the first time or after changes to the `Gemfile`):
```bash
    docker compose build
```

2.  **Start the server**:
```bash
    docker compose up
```

The site will be available at: `http://localhost:8080`

## License

The source code of this site is based on the [al-folio](https://github.com/alshedivat/al-folio) theme, distributed under the [MIT License](https://github.com/eneamanzi/eneamanzi.github.io/blob/main/LICENSE).
Personal site content (texts, projects, personal images) are © Enea Manzi.