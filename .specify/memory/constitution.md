# Portfolio Constitution

Version: 1.2.0
Ratified: 2026-05-17
Amended: 2026-07-20

## Principles

### 1. The store is the product surface

The profile README routes quickly. The store carries the visual proof, project context, previews, and repository paths. New portfolio content must improve the visitor's ability to understand or inspect the work.

### 2. Evidence over decoration

Every project surfaced in the store must have a clear problem, status, proof point, stack, preview route, and visual asset. Decorative sections that do not help a visitor decide what to open should be removed or kept out of the main path.

### 3. Progressive enhancement is mandatory

The store must remain usable in modern Chrome, Safari, Edge, and with JavaScript disabled. JavaScript may improve filtering, sorting, and motion, but links and primary navigation must still resolve as normal HTML.

### 4. Public repos must support inspection

Public projects promoted by the store should be packaged so a reviewer can understand value quickly: README, setup command, validation command, status, limitations, screenshot or architecture asset, and CI where the repo has runnable code.

### 5. Specs and validation stay together

Portfolio changes that affect navigation, catalogue structure, or project presentation must update the relevant spec artifacts and automated validation. CI should catch missing catalogue data, broken progressive-enhancement assumptions, and stale preview coverage before deploy.

### 6. Data parity is enforced by validation

Card content visible on the storefront must reuse the values declared in `store/app-index.csv` (slug, solves, shows, asset, preview, shelf). Preview content must live in `store/previews.json`. The validator fails on drift between CSV, HTML data attributes, JSON, sitemap coverage, and real image dimensions.

### 7. Shipping discipline

The site must be inspectable as a shipped product: canonical URLs, JSON-LD structured data, social meta, robots and sitemap, manifest and favicon set, CSP, print and dark-mode styles. Lighthouse CI gates accessibility and SEO regressions before deploy.

### 8. Start with the work, not the technology

The first portfolio path must begin with a recognisable task or pain point. Frameworks, models, and orchestration tools are supporting evidence, not catalogue categories. A visitor should be able to choose a tool from the situation they are in, understand what data leaves their browser, and know where a human decision is required.

## Quality Gates

- `npm test` must pass before deploy.
- Lighthouse CI accessibility and SEO categories must score ≥ 0.95.
- Store entries must be represented in `store/app-index.csv` with matching card `data-*` attributes.
- Every preview slug must appear in `sitemap.xml` and `store/previews.json`.
- Store shelves must have no-JS fallback links to the project grid.
- Preview pages must have JavaScript and no-JavaScript paths, plus an unknown-slug fallback.
- Spec artifacts must have no unresolved clarification markers.
- After CSS or JavaScript edits, run `npm run bump` to refresh the cache token.
- Task-first tools must state their input, useful output, privacy boundary, and human approval boundary before the stack.

## Governance

This constitution is the decision source for portfolio structure. If a proposed visual or content change conflicts with these principles, update the constitution first or document the exception in the feature plan.
