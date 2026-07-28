# Feature Specification: Portfolio Store Reliability

Feature: `001-portfolio-store-reliability`
Date: 2026-05-17
Status: Implemented

## User Need

Visitors should be able to open the portfolio store, understand the strongest work, choose a category, inspect project previews, and follow through to public repos or case studies regardless of whether they use Chrome, Safari, Edge, or a browser with JavaScript disabled.

## User Stories

### Story 1: Browse the strongest work

As a recruiter, collaborator, or technical reviewer, I can open the portfolio store and immediately see the strongest projects with plain-English context, status, proof points, stack, and links.

Acceptance criteria:

- The selected-work section appears before the full catalogue.
- Project cards explain what the project solves, not just what technology it uses.
- Public repos expose repo links and confidence signals where true.

### Story 2: Navigate by category

As a visitor, I can choose Products, Data systems, Automation, ML, Analytics, or Archive and land on the relevant project grid.

Acceptance criteria:

- With JavaScript enabled, the shelf applies the matching filter and scrolls to the project grid.
- With JavaScript disabled, shelf links still jump to the project grid using normal HTML anchors.
- The page does not expose internal maintenance files such as catalogue CSVs as primary visitor actions.

### Story 3: Use previews safely

As a visitor, I can open a project preview and understand the problem, role, status, focus, stack, and links.

Acceptance criteria:

- With JavaScript enabled, the preview page renders the selected project.
- With JavaScript disabled, the preview page shows a useful fallback with a route back to the store.
- Preview routes are represented in the catalogue index.

### Story 4: Maintain the store without drift

As the portfolio owner, I can add or update projects without silently breaking category links, preview coverage, no-JS behavior, or deploy quality.

Acceptance criteria:

- Each project in the store has a row in `store/app-index.csv`.
- Each shelf has a row in `store/tags.csv`.
- `npm test` fails if a store entry has no asset, preview, shelf, card title, or preview data.
- `npm test` fails if progressive-enhancement guarantees are removed.
- `npm test` fails if spec artifacts contain unresolved clarification markers.

## Requirements

- R1: The README must remain a routing surface, not a second full store.
- R2: The store must keep project metadata in `store/app-index.csv`.
- R3: The store must keep shelf metadata in `store/tags.csv`.
- R4: Shelf links must use `?filter=<shelf>#project-grid-heading`.
- R5: Search, sort, and filter controls must be hidden when JavaScript is disabled.
- R6: The preview page must include a `<noscript>` fallback.
- R7: Validation must run in GitHub Pages deploy before upload/deploy.
- R8: The implementation must avoid adding a frontend build system unless the static site can no longer meet the requirements.

## Success Criteria

- SC1: `npm test` validates catalogue, preview, no-JS, and spec coverage.
- SC2: GitHub Pages deploy passes after validation.
- SC3: Chrome with JavaScript enabled can load `?filter=ml#project-grid-heading` and show only ML-tagged items.
- SC4: Static/no-JS HTML contains usable shelf links and hides JS-only controls through CSS.
- SC5: No visible store UI exposes internal catalogue maintenance links.
