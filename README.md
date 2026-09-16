# getvocari.app

The public Vocari website. Static HTML, CSS and JavaScript on GitHub Pages; no framework, npm dependencies, database or paid service.

## Work and preview
This checkout is separate from Vocari-App. Branch: `codex/website-refresh`. Original deployed `main`: `0bd97021afb41eb514dc9ac721a48f1e9d1c3851`, retained in `safety/live-2026-09-16`. Nothing is pushed or published by the commands below.

```
python3 scripts/build.py
python3 -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173. The server is local only. Do not expose the project-root development server publicly: it can serve repository maintenance material. GitHub Pages excludes source/docs using `_config.yml`.

## Make changes
- Shared layout, metadata and output: `scripts/build.py`.
- Home content: `content/home.html`; shared styles: `home.css`; menu: `home.js`.
- Support/policy landing pages: `content/pages/*.json` + corresponding HTML.
- Catalog source and destinations: `content/products.json`; renderer: `scripts/catalog.py`; styles and progressive filters: `earbuds/`.
- Posts: copy a file in `content/posts/`, use a unique lowercase hyphenated slug, title, description, category, readTime, factual sources, HTML body and review status. `ready-for-review` includes it in local output; `draft` omits it. Nothing is automatically published. Run the generator and review the page before committing. Publication still requires Clay's merge/publish approval.
- The generated HTML is checked in so GitHub Pages does not need Python. Do not edit generated `index.html` files directly. Re-run `python3 scripts/build.py` after source changes.
- When removing/renaming an existing post, explicitly remove the obsolete generated route and sitemap entry with review; the generator intentionally does not delete files silently.

## Review and publishing
Read `docs/REVIEW.md`, `docs/CATALOG.md`, `docs/AFFILIATES.md` and `docs/ASSETS.md` before activation. There is no automatic deploy workflow in this branch. Existing GitHub Pages publishing uses `main` and the custom `CNAME` getvocari.app; GitHub's latest recorded successful deployment is the baseline above. A future authorized merge into the Pages source can publish automatically—do not merge as part of preview work. Confirm Pages settings before publication.

When approved, configure GitHub authentication through its normal browser/device flow (for example GitHub CLI `gh auth login`, if installed). Never put a token in a remote URL, source file, shell history or chat. Push only the review branch until Clay separately approves the merge. Keep the safety branch and baseline commit recoverable.

If a published version needs rollback, propose a revert commit of the approved website changes on `main` and get approval; do not force-push or rewrite history. A local checkpoint is not evidence of headset compatibility.

No analytics is installed. The optional product-click browser event has no network destination or persistence. Affiliate placement reporting uses actual approved network links; see the internal maintenance guide. Documentation is excluded from Pages but this GitHub repository is public, so it must never contain secrets, account IDs beyond public tracking URLs, private contracts or private business metrics.
