# Matthew Paver

I’m an AI solutions architect in London. I build **checks people can inspect before they decide**: cited evidence beside the answer, measured results that include failures, and a person making the call.

Since November 2025 I have been an Automation & AI Consultant at Ciklum, placed at Trustpilot. Before that I spent six years at Projecting Success, from data analysis through data science into solutions architecture.

[Explore my portfolio](https://matthewpaver.github.io/) · [CV (PDF)](CV.pdf) · [LinkedIn](https://www.linkedin.com/in/matthew-paver-534262166/) · [Evidence register](PORTFOLIO_AUDIT.md)

## Start with these three

Each card follows the same pattern: who it is for, the job, the evidence (including misses) and the limit. None is client or employer work.

| Project | For / Job | Evidence | Look |
|:---|:---|:---|:---|
| **PolicyLens** | Cloud engineers reviewing a proposed AWS IAM change. Compare two policy versions; get newly allowed access with source lines. | Set 5 **21/30**; wrongly passed MFA-less role trust (`PLH5-A21`). Browser also shows real AWS-2021-007. | [Open the example](https://matthewpaver.github.io/iam-policy-auditor/)<br>[Evidence and limits](https://github.com/MatthewPaver/iam-policy-auditor/blob/main/docs/EVIDENCE-AND-LIMITS.md)<br>[Code](https://github.com/MatthewPaver/iam-policy-auditor) |
| **ProjectLens** | Project reviewers checking whether a written update agrees with reported dates. Compare schedules and the update; record questions. | Set 5 **29/40**; contradiction recall **3/10**. Card uses public GMPP data; walkthrough is made-up. | [Open the example](https://matthewpaver.github.io/ProjectLens/change-assurance.html)<br>[Cases](https://github.com/MatthewPaver/ProjectLens/tree/main/bench/real-cases)<br>[Code](https://github.com/MatthewPaver/ProjectLens) |
| **RAG Regression Gate** | Engineers checking whether a search update still finds the right policy. | Browser shows a **saved CLI run**, not a fresh score on your docs. Pass means “not worse”, not “answers are good”. | [Inspect a saved run](https://matthewpaver.github.io/demos/rag-gate/)<br>[Case study](https://matthewpaver.github.io/work/rag-regression-gate/)<br>[Code](https://github.com/MatthewPaver/rag-retrieval-gate) |

## Also worth a look

| Project | What it helps someone do | See it |
|:---|:---|:---|
| **QuickSupply** | Follow a school’s cover request through agency to teacher. Recorded prototype, not a live service. | [Watch the walkthrough](https://matthewpaver.github.io/preview.html?app=quicksupply)<br>[Code](https://github.com/MatthewPaver/QuickSupply) |
| **Marketing ML Lakehouse** | Rebuild campaign tables and test a next-day forecast against “tomorrow looks like today”. On the sample it does not beat that baseline, and the page says so. | [Open the data checks](https://matthewpaver.github.io/marketing-ml-lakehouse/)<br>[Code](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| **Winchester Buyer Check** | First-time-buyer planning aid with dated GOV.UK rules and a real HMLR snapshot. Nine homes are made-up; no AI. | [Open the shortlist](https://matthewpaver.github.io/winchester-buyer-check/)<br>[Code](https://github.com/MatthewPaver/winchester-buyer-check) |

[All public projects](https://matthewpaver.github.io/work/) · [Case-study notes](CASE_STUDIES.md) · [Repository guide](Projects.md)

## How I work

I start with the decision someone needs to make, then test the part most likely to mislead them. I keep the source beside the answer, compare against a simple baseline and publish misses with the headline scores.

These are personal prototypes. Each one says what it does not do.

**Tools I use:** Python, TypeScript, SQL, AWS, Docker, GitHub Actions, DuckDB, Power BI and LLM APIs.
