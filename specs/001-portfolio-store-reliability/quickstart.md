# Quickstart: Portfolio Store Reliability

## Validate locally

```bash
npm test
```

Expected result:

```text
Validated 13 indexed store entries, 6 shelves, 13 previews, 16 image tags.
```

## Bump cache token after CSS/JS edits

```bash
npm run bump
# or pin an explicit token
npm run bump 20260520-1
```

Updates the `?v=YYYYMMDD-N` suffix on `styles.css` and `preview.js` references across `store/index.html` and `store/preview.html` in one pass.

## Run Lighthouse locally

```bash
npx -y @lhci/cli@0.13.x autorun --config=./.lighthouserc.json
```

Runs against the static directory. Fails the build on accessibility or SEO scores below 0.95.

## Manual browser checks

1. Open `store/index.html` or the GitHub Pages store.
2. Confirm selected work appears first.
3. Open `?filter=ml#project-grid-heading`.
4. Confirm the ML shelf is active and the grid is filtered.
5. Disable JavaScript and reload.
6. Confirm search/sort/filter controls are hidden and project cards remain usable.
7. Open `store/preview.html?app=quicksupply`.
8. Disable JavaScript and reload.
9. Confirm the no-JS preview fallback routes back to the store.
10. Open `store/preview.html?app=does-not-exist` and confirm the unknown-slug fallback appears with a Back-to-store action.

## Deployment check

The GitHub Pages workflow runs `npm test`, injects the commit SHA into the footer, runs Lighthouse CI, then uploads and deploys the artifact. All gates must pass before deploy.
