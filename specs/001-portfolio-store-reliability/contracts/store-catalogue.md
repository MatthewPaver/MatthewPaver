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

Rules:

- `slug` must be unique.
- `shelf` must exist in `store/tags.csv`.
- `preview` must equal `preview.html?app=<slug>`.
- `asset` must exist under `store/`.
- Every non-archive row must have a visible card title in `store/index.html`.
- Every slug must have preview data in `store/preview.js`.

## `store/tags.csv`

Required columns:

- `tag`
- `label`
- `position`

Rules:

- Each tag must have a filter button in `store/index.html`.
- Each tag must have a shelf link using `?filter=<tag>#project-grid-heading`.

## Progressive Enhancement Contract

- `store/index.html` starts with `class="no-js"`.
- Inline head script switches `no-js` to `js-enabled`.
- Search, sort, and filter controls use `js-only`.
- CSS hides `.js-only` in `.no-js` mode.
- `store/preview.html` includes a `<noscript>` fallback.
