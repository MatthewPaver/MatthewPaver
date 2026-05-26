# Quality Gates

The portfolio is maintained through checks that match the kind of systems it is trying to showcase.

## Store Validator

Run:

```bash
npm test
```

Checks include catalogue rows, shelves, previews, image dimensions, progressive enhancement, metadata, sitemap coverage, and store/preview parity.

## Portfolio Audit

Run:

```bash
npm run audit:portfolio
```

Review passes:

- Research agent: benchmarks against strong profile patterns without copying them.
- README agent: keeps the profile lean and routed.
- README slop detector: flags generic phrases.
- Thumbnail QA agent: checks missing assets, awkward crops, and diagram-heavy cards.
- Catalogue agent: checks store, card, and preview consistency.
- Repo packaging agent: checks whether public projects are shown with confidence.
- Ideas agent: keeps the next-build backlog aligned with the portfolio.
- Karpathy wiki agent: checks source/wiki separation, compiled pages, index, and log.

## Current Known Improvements

- Keep replacing archive-only SVG thumbnails with real screenshots when an archive item becomes front-door work again.
- Add a short demo video only when it explains a workflow better than a still screenshot.
