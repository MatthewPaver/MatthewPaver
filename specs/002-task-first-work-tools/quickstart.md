# Quickstart: Validate the Task-first Store

```bash
npm test
npm run bump
python3 -m http.server 8000
```

Open `http://localhost:8000/store/`.

Check:

1. the three task routes appear before the catalogue;
2. MeetingProof opens the live browser-local tool;
3. ProjectLens opens change assurance;
4. DecisionGraph opens the precedent workflow;
5. the Work tools filter shows MeetingProof, ProjectLens, and DecisionGraph;
6. the same routes remain usable with JavaScript disabled;
7. the layout has no horizontal overflow at 390px.
