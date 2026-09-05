# Selected case studies

[Profile](README.md) · [Portfolio](https://matthewpaver.github.io/) · [Repository guide](Projects.md)

These are personal public projects, not claims of client deployment. The portfolio pages include the screenshots, recordings, source links and current limitations.

## ProjectLens

**Problem:** A project's written change request can disagree with the schedule it cites. A reviewer needs to find those disagreements and ask for evidence before approving the change.

**My approach:** Compare the schedule evidence first, keep the source dates beside each finding, and let the reviewer record questions and a decision. An optional retrieval route can suggest precedents, but the reviewer must decide whether they are relevant.

**What you can try:** The public Northstar example produces three review blockers, including an unacknowledged 73-day finish-date movement. Inspect the dates and export the review record.

**Boundary:** The bundled schedules are synthetic. Static precedent cards are not live retrieval. A schedule difference does not establish its cause, contractual responsibility or the probability of project failure.

[Read the case](https://matthewpaver.github.io/store/apps/projectlens/) · [Try the review](https://matthewpaver.github.io/ProjectLens/change-assurance.html) · [Source](https://github.com/MatthewPaver/ProjectLens)

## QuickSupply

**Problem:** An outdated Liverpool supply-teacher booking process made it hard to follow a request across school, agency and teacher roles.

**My approach:** Give each role its own view of the same booking. Make the current state and next action visible, including the agency's assignment and the teacher's response.

**What you can inspect:** A recording follows a fictional cover request through the three roles. The public repository contains the prototype's implementation.

**Boundary:** This is a historical product-redesign case study, not a live staffing service or a deployment-ready template. I have not established adoption or time savings. Testing declined offers and last-minute cancellations with actual staff would be the next product test.

[Watch the case study](https://matthewpaver.github.io/store/apps/quicksupply/) · [Source](https://github.com/MatthewPaver/QuickSupply)

## Marketing ML Lakehouse

**Problem:** A marketing report is difficult to trust if nobody can retrace the source files, data checks and transformations behind it.

**My approach:** A local template takes campaign files through table layers in DuckDB, trains an example model and opens a Streamlit dashboard. Keeping the steps rebuildable makes the output easier to inspect and adapt.

**What you can try:** Inspect the fixed public data-quality snapshot, then follow the published Python walkthrough to rebuild the example locally.

**Learning and boundary:** The newer local work uses a future prediction target and compares it with carrying today's value forward. That next-day evaluation and the GA4 adapter are not yet in the public walkthrough. Neither the fixed browser sample nor the earlier model establishes forecasting value for a real advertising account.

[Read the case](https://matthewpaver.github.io/store/apps/lakehouse/) · [Published walkthrough](https://github.com/MatthewPaver/marketing-ml-lakehouse/blob/main/DEMO.md) · [Source](https://github.com/MatthewPaver/marketing-ml-lakehouse)

## Further work

- [PolicyLens](https://matthewpaver.github.io/store/apps/policylens/): separating permission evidence from AI explanation, with explicit limits to the AWS model.
- [Winchester House Hunter](https://matthewpaver.github.io/store/apps/winchester/): an example home shortlist with budget filters, evidence checks and separate historical completed-sale context.
- [HR Performance Analytics](https://matthewpaver.github.io/store/apps/hr/): a historical dashboard and a correction to two unsupported field interpretations. The original exports still need rebuilding.
- [Can England Win It?](https://matthewpaver.github.io/store/apps/england/): a finished interactive simulation showing assumptions and repeatable scenarios, not a sporting forecast.
