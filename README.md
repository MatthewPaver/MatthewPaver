# Matthew Paver

I'm an AI solutions architect and hands-on engineer based in London. I build AI systems, automation and data products, from understanding the problem through to release and operation.

I progressed from data analysis through data science into solutions architecture over six years at Projecting Success. My work has included knowledge graphs, AI-assisted workflows, cloud automation, privacy reviews and technical training.

I'm looking for AI engineering and solutions architecture roles where I can combine technical decisions with building and testing the software.

[Explore my portfolio](https://matthewpaver.github.io/) · [CV (PDF)](CV.pdf) · [LinkedIn](https://www.linkedin.com/in/matthew-paver-534262166/)

## Start with these three

| Project | What it helps someone do | What you can inspect |
|:---|:---|:---|
| [ProjectLens](https://matthewpaver.github.io/store/apps/projectlens/) | Find disagreements between a project's written change request and its schedule before a review meeting. | A browser demo with synthetic schedules, source-linked findings and an exportable review record. |
| [QuickSupply](https://matthewpaver.github.io/store/apps/quicksupply/) | Follow a supply-teacher booking from school request through agency assignment to teacher response. | A recorded redesign case study based on an outdated Liverpool booking process, plus public source. It is not a live staffing service. |
| [Marketing ML Lakehouse](https://matthewpaver.github.io/store/apps/lakehouse/) | Turn campaign files into checked reporting tables that another person can rebuild. | A public Python template and a fixed browser sample. Includes a next-day prediction evaluation against a prior-day baseline, with its limits stated: on the 24-row sample it shows no reliable skill over the baseline. |

[All public projects and smaller examples](https://matthewpaver.github.io/work/) · [Case-study notes](CASE_STUDIES.md) · [Repository guide](Projects.md)

## AI work you can question

[PolicyLens](https://github.com/MatthewPaver/iam-policy-auditor) explores AWS permission reachability. Its deterministic checks produce the evidence; optional AI explains that evidence rather than deciding permissions. The public repository includes a local demo and benchmark. The portfolio also documents a newer local change-review extension, with its publication status made explicit.

[RAG Retrieval Gate](https://github.com/MatthewPaver/rag-retrieval-gate) checks whether a change to a RAG system (embedding model, chunking or retriever) still finds the right evidence. It scores labelled questions on the public SciFact benchmark and fails CI when quality drops; on SciFact a small dense model scores below a BM25 baseline (MRR 0.60 vs 0.63), so the gate rejects it.

## How I work

I start with the user's decision and the data available to support it. I build a small end-to-end path, check the output against a simple alternative, and keep the evidence separate from the interpretation. Where a person must make the decision, the interface should make that responsibility clear.

The portfolio separates live demos, recorded prototypes, reusable code and historical work. It also calls out synthetic data and unfinished evaluation. These projects show how I work; they do not imply commercial adoption or measured business results.

**Tools I use:** Python, TypeScript, SQL, AWS, Docker, GitHub Actions, DuckDB, Power BI and LLM APIs. The implementation and limitations are documented with each project.
