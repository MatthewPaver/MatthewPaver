# Research: Portfolio Store Reliability

## Source Reviewed

- GitHub Spec Kit repository: https://github.com/github/spec-kit
- Spec Kit guide: https://github.com/github/spec-kit/blob/main/spec-driven.md

## Relevant Spec Kit Practices Applied

- Treat specifications as source of truth.
- Separate user need/specification from implementation plan.
- Generate explicit tasks from the plan.
- Add validation so documentation and implementation cannot drift silently.
- Use a constitution to record project-level principles.

## Brownfield Adaptation

This repository already existed and had shipped code. Instead of reinitializing the repo with the CLI, the workflow was applied directly:

- Constitution: `.specify/memory/constitution.md`
- Feature spec: `specs/001-portfolio-store-reliability/spec.md`
- Plan: `specs/001-portfolio-store-reliability/plan.md`
- Tasks: `specs/001-portfolio-store-reliability/tasks.md`
- Validation: `scripts/validate-store.mjs`

## Browser Compatibility Notes

- Plain links are the compatibility baseline.
- JavaScript-only controls are hidden when scripts are disabled.
- Preview pages need explicit no-JS fallback because their content is data-driven by `preview.js`.
- The static HTML path is sufficient for Chrome/Safari/Edge because no framework hydration is required.
