# Implementation Plan: Task-first Work Tools

## Structure

The store remains static HTML, CSS, and JavaScript. A new server-free task chooser sits after the hero and before the catalogue. It routes to three independently useful products:

1. MeetingProof for meeting follow-up;
2. ProjectLens for change readiness;
3. DecisionGraph for comparable project precedent.

MeetingProof is the first “everyday workbench” release. Its public experience is browser-local; its separate repository contains the tested LangGraph reference implementation and LangSmith-ready synthetic evaluation set.

## Boundaries

- No framework becomes a visitor-facing category.
- The portfolio does not imply that the browser demo sends notes to a model.
- The three products remain separate because they solve different jobs and have different approval moments.
- DecisionGraph supports ProjectLens but remains independently inspectable.
- Ruflo is deferred until a workflow genuinely needs multiple agents or parallel coordination.

## Validation

- Extend the store validator for feature 002 artifacts and task-first markers.
- Run the catalogue parity gate.
- Test links and layouts in desktop and narrow browser viewports.
- Verify the GitHub Pages deployment and live routes.
