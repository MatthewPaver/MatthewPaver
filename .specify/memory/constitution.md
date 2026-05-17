# Portfolio Constitution

Version: 1.0.0
Ratified: 2026-05-17

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

## Quality Gates

- `npm test` must pass before deploy.
- Store entries must be represented in `store/app-index.csv`.
- Store shelves must have no-JS fallback links to the project grid.
- Preview pages must have JavaScript and no-JavaScript paths.
- Spec artifacts must have no unresolved clarification markers.

## Governance

This constitution is the decision source for portfolio structure. If a proposed visual or content change conflicts with these principles, update the constitution first or document the exception in the feature plan.
