# Tasks: Portfolio Store Reliability

## Specification

- [x] T001 Create portfolio constitution.
- [x] T002 Create feature specification for store reliability and browser fallback behavior.
- [x] T003 Create implementation plan with architecture and decision rationale.
- [x] T004 Create quickstart validation guide.
- [x] T005 Create catalogue contract.

## Implementation

- [x] T006 Keep internal catalogue links out of visitor-facing store UI.
- [x] T007 Make shelf links use normal `?filter=<shelf>#project-grid-heading` URLs.
- [x] T008 Add `no-js` / `js-enabled` mode to store page.
- [x] T009 Hide JS-only search, sort, and filter controls when scripts are disabled.
- [x] T010 Add preview page no-JS fallback.
- [x] T011 Bump asset cache versions after compatibility changes.

## Validation

- [x] T012 Validate catalogue rows, shelf rows, assets, cards, and preview data.
- [x] T013 Validate no-JS shelf link requirements.
- [x] T014 Validate preview fallback requirements.
- [x] T015 Validate required spec artifacts exist.
- [x] T016 Validate no unresolved clarification markers remain.
- [x] T017 Run local `npm test`.
- [x] T018 Verify GitHub Pages deploy runs validation before deploy.

## SEO, social, and shipping polish

- [x] T019 Add `robots.txt` and `sitemap.xml` at repo root, covering store + every preview slug.
- [x] T020 Generate a 1200×630 `store/assets/og-image.png` and reference it from OG/Twitter meta with width/height/alt.
- [x] T021 Add `@media (prefers-color-scheme: dark)` palette and explicit overrides for the always-dark featured block and card badge.
- [x] T022 Add `npm run bump` script (`scripts/bump-cache-version.mjs`) to centralise the `?v=` cache token.
- [x] T023 Add JSON-LD `Person`, `WebSite`, and `ItemList` schema to the store page.
- [x] T024 Update `store/preview.js` to set per-slug `og:*`, `twitter:*`, and canonical meta at runtime.
- [x] T025 Drop redundant `fetchpriority="high"` from non-LCP images; preload the LCP image instead.
- [x] T026 Add real favicon set (`favicon.svg`, `favicon-dark.svg`, `apple-touch-icon.svg`) and `manifest.webmanifest`.
- [x] T027 Add `rel="canonical"` to both HTML pages.
- [x] T028 Add a print stylesheet that hides toolbars and expands all cards.
- [x] T029 Add a CSP meta tag scoped to local resources and inline scripts.
- [x] T030 Add `humans.txt`.

## Data and code hygiene

- [x] T031 Remove redundant `store/catalogue.csv` (subset of `app-index.csv`).
- [x] T032 Add `solves` and `shows` columns to `app-index.csv` as the source of truth for card snapshots.
- [x] T033 Mirror `solves`/`shows`/`slug` onto each `<article class="app-card">` via `data-*` attributes.
- [x] T034 Move preview content out of `preview.js` into `store/previews.json`; fetch at runtime.
- [x] T035 Add unknown-slug fallback in `preview.js` with a Back-to-store action.
- [x] T036 Pre-compute the search index in `store/script.js` instead of reading `textContent` on every keystroke.
- [x] T037 Substitute the build SHA into `<a id="build-sha">` in the Pages workflow before upload.

## Validator extensions

- [x] T038 Require new CSV columns (`solves`, `shows`) and assert parity with `data-solves`/`data-shows` on cards.
- [x] T039 Assert PNG declared `width`/`height` matches real PNG dimensions.
- [x] T040 Assert every catalogue slug appears in `sitemap.xml`.
- [x] T041 Assert `robots.txt` points to the actual sitemap URL.
- [x] T042 Assert favicon assets and `manifest.webmanifest` exist.
- [x] T043 Assert CSP, canonical, JSON-LD, preload, and print/dark CSS blocks are present.
- [x] T044 Assert `previews.json` keys cover every catalogue slug.
- [x] T045 Cap `fetchpriority="high"` at two occurrences per page.

## CI

- [x] T046 Add `.lighthouserc.json` with accessibility and SEO error thresholds.
- [x] T047 Run Lighthouse CI as part of the Pages workflow.

## Agent collaboration

- [x] T048 Add lean `CLAUDE.md` with project rules, invariants, and forbidden actions.
