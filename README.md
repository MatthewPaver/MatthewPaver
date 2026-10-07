# Matthew Paver

I'm an AI solutions architect and hands-on engineer based in London. I build AI systems, automation and data products, from understanding the problem through to release and operation.

I have spent seven years in data and AI. Six of them were at Projecting Success, where I progressed from data analysis through data science into solutions architecture. My work has included knowledge graphs, AI-assisted workflows, cloud automation, privacy reviews and technical training.

I'm looking for AI engineering and solutions architecture roles where I can combine technical decisions with building and testing the software.

[Explore my portfolio](https://matthewpaver.github.io/) · [CV (PDF)](CV.pdf) · [LinkedIn](https://www.linkedin.com/in/matthew-paver-534262166/)

## Start with these three

| Project | What it helps someone do | What you can inspect |
|:---|:---|:---|
| [PolicyLens](https://github.com/MatthewPaver/iam-policy-auditor) | Check whether an AWS IAM change widens who can do what, before it is approved. | Deterministic checks produce cited evidence; optional AI explains that evidence rather than deciding. Includes the change-review workflow, an org-wide demo and an authored benchmark, all runnable locally without an AWS account. |
| [RAG Retrieval Gate](https://github.com/MatthewPaver/rag-retrieval-gate) | Stop a change to a RAG system (embedding model, chunking or retriever) from shipping if it finds the right evidence less often. | Scores labelled questions on the public SciFact benchmark with paired-bootstrap confidence intervals and fails CI on a real drop. It blocks a 12-word chunking change (MRR 0.53 vs 0.63) and passes a hybrid retriever, the only significant gain. [Case study](https://matthewpaver.github.io/work/rag-regression-gate/). |
| [ProjectLens](https://matthewpaver.github.io/store/apps/projectlens/) | Find disagreements between a project's written change request and its schedule before a review meeting. | A browser demo with synthetic schedules, cited precedents from a public corpus, source-linked findings and a human-recorded decision. |

## Also worth a look

| Project | What it helps someone do | What you can inspect |
|:---|:---|:---|
| [QuickSupply](https://matthewpaver.github.io/store/apps/quicksupply/) | Follow a supply-teacher booking from school request through agency assignment to teacher response. | A recorded redesign case study based on an outdated Liverpool booking process, plus public source. It is not a live staffing service. |
| [Marketing ML Lakehouse](https://matthewpaver.github.io/store/apps/lakehouse/) | Turn campaign files into checked reporting tables that another person can rebuild. | A public Python template and a console built from its generated evidence. Its next-day model is compared with a prior-day baseline: on the 24-row holdout it shows no reliable skill yet, and the README says so. |

[All public projects and smaller examples](https://matthewpaver.github.io/work/) · [Case-study notes](CASE_STUDIES.md) · [Repository guide](Projects.md)

## How I work

I start with the user's decision and the data available to support it. I build a small end-to-end path, check the output against a simple alternative, and keep the evidence separate from the interpretation. Where a person must make the decision, the interface should make that responsibility clear.

The portfolio separates live demos, recorded prototypes, reusable code and historical work. It also calls out synthetic data and unfinished evaluation. These projects show how I work; they do not imply commercial adoption or measured business results.

**Tools I use:** Python, TypeScript, SQL, AWS, Docker, GitHub Actions, DuckDB, Power BI and LLM APIs. The implementation and limitations are documented with each project.
