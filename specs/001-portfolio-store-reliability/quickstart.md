# Quickstart: Portfolio Store Reliability

## Validate locally

```bash
npm test
```

Expected result:

```text
Validated 13 indexed store entries and 6 shelves.
```

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

## Deployment check

The GitHub Pages workflow must pass the `Validate store catalogue` step before artifact upload and deploy.
