# Feature Specification: Task-first Work Tools

Feature: `002-task-first-work-tools`
Date: 2026-07-20
Status: Implemented

## User Need

A visitor with an ordinary work problem should be able to choose and use the relevant tool without first understanding AI frameworks. Technical reviewers should still be able to inspect how each result is bounded and tested.

## User Stories

### Story 1: Choose from a familiar situation

As a visitor, I can start with “I have meeting notes”, “I have a project change”, or “I need to know what happened last time” and reach the matching live workflow.

Acceptance criteria:

- A task-first section appears before the full catalogue.
- Each route names the input, the useful result, and the human boundary.
- Every primary action works without JavaScript.

### Story 2: Complete a low-level work task

As a person leaving a meeting, I can turn clearly labelled notes into evidence-linked actions, decisions, and questions, review them, and export an approved follow-up.

Acceptance criteria:

- The live MeetingProof tool is linked directly.
- Its portfolio entry identifies browser-local processing and human approval.
- Its tutorial and source repository are available from the preview.

### Story 3: Inspect the engineering

As a technical reviewer, I can see why LangGraph is used, what LangSmith evaluates, and where deterministic code rejects unsupported evidence.

Acceptance criteria:

- Framework names appear as implementation evidence, not as products.
- MeetingProof exposes its graph, synthetic evaluation fixtures, tests, and limitations.
- Ruflo is not presented as part of this product unless multi-agent coordination becomes necessary.

## Requirements

- R1: Add a `work` shelf and no-JavaScript shelf link.
- R2: Add MeetingProof to the CSV, store card, preview data, JSON-LD, and curated ordering.
- R3: Replace the entertainment-led first spotlight with a task-first three-route surface.
- R4: Keep the existing catalogue and project URLs intact.
- R5: Update stale ProjectLens wording to the current browser-local assurance product.
- R6: Validate the new spec artifacts and task-first HTML markers.

## Success Criteria

- SC1: A first-time visitor can identify the correct tool from the problem statement alone.
- SC2: `npm test` validates 14 catalogue entries, 6 shelves, and 14 previews.
- SC3: Desktop and mobile browser QA reaches MeetingProof, ProjectLens, and DecisionGraph from normal links.
- SC4: The live portfolio deploy completes with Lighthouse accessibility and SEO gates.
