# Contract: Store Catalogue

## `store/app-index.csv`

Required columns:

- `slug`
- `title`
- `shelf`
- `status`
- `kind`
- `problem`
- `proof`
- `stack`
- `preview`
- `asset`
- `solves`
- `shows`

Rules:

- `slug` must be unique.
- `shelf` must exist in `store/tags.csv`.
- `preview` must equal `preview.html?app=<slug>`.
- `asset` must exist under `store/`.
- Every non-archive row must have a visible card title in `store/index.html`.
- Every row must have a `data-slug`, `data-solves`, and `data-shows` attribute on its `<article class="app-card">` in `store/index.html` matching the CSV values.
- Every slug must have a preview entry in `store/previews.json`.
- Every preview slug must appear in `sitemap.xml`.

## `store/tags.csv`

Required columns:

- `tag`
- `label`
- `position`

Rules:

- Each tag must have a filter button in `store/index.html`.
- Each tag must have a shelf link using `?filter=<tag>#project-grid-heading`.

## `store/previews.json`

JSON object keyed by slug. Each entry must declare `title`, `image`, `imageAlt`, `summary`, `problem`, `points`, `stack`, and at least one `links` entry. Optional `video` for demo media. Used at runtime by `store/preview.js` and validated against `app-index.csv` slug coverage.

## Progressive Enhancement Contract

- `store/index.html` starts with `class="no-js"`.
- Inline head script switches `no-js` to `js-enabled`.
- Search, sort, and filter controls use `js-only`.
- CSS hides `.js-only` in `.no-js` mode.
- `store/preview.html` includes a `<noscript>` fallback.

## SEO + Social Contract

- Both HTML pages declare a `rel="canonical"` URL.
- Both HTML pages declare a CSP meta tag.
- Store HTML embeds JSON-LD `Person`, `WebSite`, and `ItemList` schema.
- Store HTML preloads the LCP image (`project-1966-card.avif`) with `fetchpriority="high"`.
- No more than two `fetchpriority="high"` images per page (preload + LCP).
- `store/preview.js` updates `og:*`, `twitter:*`, and `link[rel="canonical"]` to per-slug values at runtime.
- `og:image` is 1200×630 (`store/assets/og-image.png`).

## Asset Contract

The following assets must exist under repo root:

- `robots.txt` with a `Sitemap:` line pointing to `https://matthewpaver.github.io/MatthewPaver/sitemap.xml`.
- `sitemap.xml` listing the store root and every preview slug URL.
- `store/manifest.webmanifest` with `name` and `icons`.
- `store/assets/favicon.svg` (light) and `store/assets/favicon-dark.svg` (dark variant).
- `store/assets/apple-touch-icon.svg`.
- `store/assets/og-image.png` at 1200×630.

## Image Dimension Contract

Every `<img>` with an explicit `width` and `height` referencing a PNG under `store/assets/` must declare dimensions matching the real PNG dimensions. Validator enforces this.

## Cache Version Contract

`store/index.html` and `store/preview.html` reference `styles.css` and `preview.js` with a shared `?v=YYYYMMDD-N` token. Run `npm run bump` after any CSS or JS change to update both files in one pass.
