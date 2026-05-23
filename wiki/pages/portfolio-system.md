# Portfolio System

The portfolio has three public layers and one maintenance layer.

## Public Layers

- `README.md` is the quick route: best work, links, credentials, and where to go next.
- `store/index.html` is the visual catalogue: cards, shelves, previews, and product-style browsing.
- `store/preview.html` plus `store/previews.json` gives each project a focused app-store-style detail page.

## Maintenance Layer

- `scripts/validate-store.mjs` checks catalogue integrity, preview coverage, image dimensions, SEO basics, and progressive enhancement.
- `tools/portfolio-audit/portfolio-audit.mjs` runs review passes for README clarity, thumbnail quality, catalogue consistency, repo packaging, app ideas, and wiki-pattern structure.
- `PORTFOLIO_AUDIT.md` is the latest compiled report.

## Useful Principle

The README should route quickly. The store should do most of the showing. The wiki should preserve context for future maintenance.
