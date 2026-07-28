# CLAUDE.md

Project rules for AI agents working in this repository. Keep this file under 200 lines.

## What this repo is

A hand-built static portfolio site served by GitHub Pages. The store at `store/` is the front door. Profile README is a routing surface. Case studies and project appendix live in markdown files at root.

## Hard rules

1. **No build system, no bundler, no framework.** HTML, CSS, JavaScript only. If a task seems to need a build step, the answer is to rethink the task.
2. **`npm test` must pass before every commit.** The validator (`scripts/validate-store.mjs`) is the deploy gate. It checks catalogue rows, shelves, preview data, progressive enhancement, image dimensions, sitemap coverage, robots.txt, manifest, favicons, CSP, JSON-LD, and spec artifacts.
3. **Progressive enhancement is mandatory.** Every link must work without JavaScript. JS only enhances filtering, sorting, motion, and preview rendering.
4. **Spec Kit is the source of truth.** `.specify/memory/constitution.md` records principles; `specs/001-portfolio-store-reliability/` records the active feature spec, plan, tasks, contract. Update these alongside any structural change.
5. **Never bypass `--no-verify`, `--force`, or `--no-gpg-sign`.** Investigate failures, do not skip them.

## Catalogue invariants

- Every project on the store has a row in `store/app-index.csv` with all required columns: `slug,title,shelf,status,kind,problem,proof,stack,repo,preview,asset,solves,shows`.
- Every project has a card in `store/index.html` with matching `data-slug`, `data-solves`, `data-shows` attributes.
- Every project has an entry in `store/previews.json` keyed by slug.
- Every project has a row in `sitemap.xml` for its preview URL.
- Shelf tag must exist in `store/tags.csv`.
- Preview URL is always `preview.html?app=<slug>`.
- After CSS or JS edits, run `npm run bump` to refresh the `?v=YYYYMMDD-N` cache token in both HTML files.

## Design language

Follows the impeccable design language by hand (no skill installed):

- Typography: Charter (serif headings) + Avenir Next/Segoe UI (body). No Inter.
- Colour: tinted neutrals (warm cream `--bg`, near-black `--ink`), teal accent. No pure `#000`, no purple/blue gradients.
- Motion: custom cubic-bezier easings, no bounce or elastic curves. `prefers-reduced-motion` is respected.
- Layout: 1160px shell, editorial grid, sharp borders (`border-radius: 0` is the default).
- Dark mode: full `@media (prefers-color-scheme: dark)` palette with explicit overrides for the always-dark `.featured-build` block and the `.app-card::before` badge.
- Status pills: semantic ink colours per category.

## File layout

- `store/index.html` — main storefront, JSON-LD, CSP, OG meta, preload LCP.
- `store/preview.html` — preview shell with `<noscript>` fallback.
- `store/preview.js` — fetches `previews.json`, renders per-slug page, updates social meta, handles unknown slugs.
- `store/script.js` — store interactions, pre-computed search index, filter/sort/URL state.
- `store/previews.json` — preview content per slug.
- `store/app-index.csv` — catalogue source of truth.
- `store/tags.csv` — shelf source of truth.
- `store/manifest.webmanifest` — PWA manifest.
- `store/assets/` — screenshots, thumbnails, favicons, OG image.
- `scripts/validate-store.mjs` — single deploy gate.
- `scripts/bump-cache-version.mjs` — cache token bumper (`npm run bump`).
- `.lighthouserc.json` — Lighthouse CI assertions for a11y, SEO, perf, best practices.
- `.github/workflows/pages.yml` — deploy workflow: validate → inject build SHA → Lighthouse CI → upload → deploy.
- `.github/workflows/refresh-profile.yml` — daily README refresh.

## Common commands

```bash
npm test                    # validate everything
npm run bump                # bump cache token to today's next serial
npm run bump 20260601-1     # bump to explicit token
```

## What not to do

- Do not add a frontend framework, bundler, or build step.
- Do not introduce a runtime dependency unless the validator can replace it with something simpler.
- Do not skip `npm test` failures. The validator catches drift between CSV, HTML, JSON, and assets on purpose.
- Do not commit personal credentials or `.claude/settings.local.json` (already gitignored).
- Do not change the URL contract `preview.html?app=<slug>` — sitemap, JSON-LD, and external links depend on it.
- Do not add `[NEEDS CLARIFICATION]` markers to spec files without resolving them in the same change. The validator fails on stale markers.
- Do not edit auto-generated profile activity block in `README.md` (between `<!-- AUTO:ACTIVITY_START -->` markers). The daily workflow rewrites it.

## When in doubt

Read `.specify/memory/constitution.md` and `specs/001-portfolio-store-reliability/spec.md`. If a proposed change conflicts with either, update the spec first or document the exception in the plan.
