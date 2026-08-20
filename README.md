<p align="center">
  <a href="https://matthewpaver.github.io/">
    <img src="assets/profile-banner.svg" alt="Matthew Paver — automation, data, and AI projects." width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://matthewpaver.github.io/ProjectLens/board-readiness.html"><img src="https://img.shields.io/badge/Project_Evidence_Desk-Prepare_a_board_review-244a67?style=for-the-badge&logoColor=white" alt="Prepare a board review with Project Evidence Desk" /></a>
  <a href="https://matthewpaver.github.io/"><img src="https://img.shields.io/badge/Project_Catalogue-Inspect-8f5d12?style=for-the-badge&logoColor=white" alt="Inspect the project catalogue" /></a>
  <a href="https://www.linkedin.com/in/matthew-paver-534262166/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/MatthewPaver/MatthewPaver/pages.yml?label=Pages%20deploy&style=flat-square&color=0f766e&labelColor=151515" alt="Pages deploy status" />
  <img src="https://img.shields.io/github/last-commit/MatthewPaver/MatthewPaver?label=Last%20commit&style=flat-square&color=8f5d12&labelColor=151515" alt="Last commit" />
</p>

---

**Check the evidence before you approve, send or ship.** I build human-in-the-loop tools for the decisions teams get wrong under pressure — board approvals and AI releases. Try one below; the demos run in your browser on synthetic data.

## Featured products

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/ProjectLens/change-assurance.html">
    <img src="store/assets/projectlens-change-assurance.png" alt="ProjectLens change assurance workspace" />
  </a>
  <h3>ProjectLens <sub>· live</sub></h3>
  <p>Compare a change pack with its schedule before the board meeting: the three largest conflicts, source dates and a recorded board response.</p>
  <p><code>Python</code> <code>Playwright</code> <code>GitHub Pages</code> <code>UK GMPP data</code></p>
  <p><a href="https://matthewpaver.github.io/ProjectLens/change-assurance.html">Use the tool ↗</a> · <a href="https://matthewpaver.github.io/preview.html?app=projectlens">Product notes ↗</a> · <a href="https://github.com/MatthewPaver/ProjectLens">Repo ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/ai-workflow-evaluator/app/">
    <img src="store/assets/output-gate-workbench.png" alt="Output Gate regression check workbench" />
  </a>
  <h3>Output Gate <sub>· live</sub></h3>
  <p>Catch known AI-output regressions before release: required and banned phrases, checked in the browser or CI, no model call needed.</p>
  <p><code>Python</code> <code>GitHub Actions</code> <code>JSON</code></p>
  <p><a href="https://matthewpaver.github.io/ai-workflow-evaluator/app/">Use the tool ↗</a> · <a href="https://matthewpaver.github.io/preview.html?app=ai-evaluator">Product notes ↗</a> · <a href="https://github.com/MatthewPaver/ai-workflow-evaluator">Repo ↗</a></p>
</td>
</tr>
</table>

<sub>Also private / parked: Happening (event ingestion — paused), QuickSupply (school cover MVP). Study demos archived on GitHub Aug 2026.</sub>

## At a glance

| | |
|:---|:---|
| **Role**     | Product engineer |
| **Based**    | London |
| **Focus**    | Human-in-the-loop decision tools, data products, applied AI |
| **Shipping** | ProjectLens · Output Gate |
| **Stack**    | Python · TypeScript · FastAPI · Next.js · Postgres / DuckDB · Playwright · GitHub Actions |
| **Specs**    | [Constitution](.specify/memory/constitution.md) · [Feature spec](specs/001-portfolio-store-reliability/spec.md) · [Validator](scripts/validate-store.mjs) · [Lighthouse CI](.lighthouserc.json) |

## Build pattern

```mermaid
flowchart LR
    A[Messy public data] --> B[Configured ingestion]
    B --> C[Validation & dedupe]
    C --> D[Spec-driven catalogue]
    D --> E[Inspectable product]
    E --> F[Deploy gate · validator + Lighthouse CI]
    F -.->|fail| B
    F -->|pass| G[Shipped]
```

The pattern is practical: collect the messy input, clean it, check it, and turn it into something a person can use. [Project Evidence Desk](https://matthewpaver.github.io/ProjectLens/board-readiness.html) applies that pattern to the evidence before, during and after a project-board decision; the [project catalogue](https://matthewpaver.github.io/) exposes the engineering underneath.

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

## Open these next

<table>
<tr>
<td valign="top" width="50%">

**▸ Runnable applications**

- [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) — Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/marketing-ml-lakehouse?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/marketing-ml-lakehouse?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [ProjectLens](https://github.com/MatthewPaver/ProjectLens) — Browser-local board readiness: reconcile five evidence groups, expose source-linked findings, record human authority and follow approval conditions<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/ProjectLens?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/ProjectLens?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [DecisionGraph](https://github.com/MatthewPaver/DecisionGraph) — Comparable project cases with inspectable retrieval, problem-to-outcome evidence chains and human review
<sub><strong>Repo standard:</strong> run command, tests or checks, demo/sample data where possible, screenshots, architecture notes, and limitations.</sub>

**▸ Analytics handoff**

- [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) — Power BI dashboard package: PBIX files, dashboard previews, methodology PDF, stakeholder commentary<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/hr-performance-dashboards?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/repo-size/MatthewPaver/hr-performance-dashboards?style=flat-square&label=Size&color=0f766e&labelColor=151515" alt="Repo size" /></sub>

</td>
<td valign="top" width="50%">

**▸ Notebook demos and technical examples**

- [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) — Embedding retrieval with a deliberate point about similarity not being truth<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/sentence-similarity-analysis?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/sentence-similarity-analysis?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) — DataFrames, Structured Streaming, JSON event production<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/pyspark-kafka-streaming?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/pyspark-kafka-streaming?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>

</td>
</tr>
</table>

## Credentials

<p>
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/d0dd54bf93df495da5c3e75ee69940fe"><img src="https://img.shields.io/badge/AWS-Cloud_Practitioner-151515?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS Cloud Practitioner" /></a>
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/455c09a58c6c43beb001b21d3ccec2a0"><img src="https://img.shields.io/badge/AWS-AI_Practitioner-151515?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS AI Practitioner" /></a>
  <a href="https://drive.google.com/file/d/15oXe_G86TEiETdC8kGBhbnKoMjVZ5mQQ/view"><img src="https://img.shields.io/badge/Neo4j-Certified-151515?style=flat-square&logo=neo4j&logoColor=white" alt="Neo4j Certified Professional" /></a>
  <a href="https://drive.google.com/file/d/1NgSeIIF49Sqh2DAMY5KQEtnaddSc1Sqw/view"><img src="https://img.shields.io/badge/Hugging_Face-AI_Agents-151515?style=flat-square&logo=huggingface&logoColor=white" alt="Hugging Face AI Agents" /></a>
  <a href="https://drive.google.com/file/d/15lrcn5_Cn4g-kD165xGNLUGUGXtCptk-/view"><img src="https://img.shields.io/badge/UiPath-RPA_Developer-151515?style=flat-square&logo=uipath&logoColor=white" alt="UiPath RPA Developer" /></a>
  <a href="https://drive.google.com/file/d/15yLBx8nzlhn_PwrGoqQbumRG8zRQPC9t/view"><img src="https://img.shields.io/badge/BCS-Diploma_in_IT-151515?style=flat-square&logo=bcs&logoColor=white" alt="BCS Diploma in IT" /></a>
  <a href="CV.pdf"><img src="https://img.shields.io/badge/CV-Open_PDF-151515?style=flat-square&logo=readthedocs&logoColor=white" alt="Open CV PDF" /></a>
</p>

<details>
<summary><strong>Latest public activity</strong> (auto-updated daily)</summary>

<!-- AUTO:ACTIVITY_START -->
## Latest Public Activity (Auto-Updated)

_This section is automatically refreshed by GitHub Actions._

- Last refresh (UTC): 2026-08-20 07:58

| Repo | Last push | What it is |
|:---|:---:|:---|
| [MatthewPaver](https://github.com/MatthewPaver/MatthewPaver) | 2026-08-19 | Portfolio: AI products, data systems, ML, and analytics — every project has a preview,… |
| [MatthewPaver.github.io](https://github.com/MatthewPaver/MatthewPaver.github.io) | 2026-08-11 | Live demos and open-source tools by Matthew Paver |
| [NVG-Crestovian-Analytics](https://github.com/MatthewPaver/NVG-Crestovian-Analytics) | 2026-08-11 | Private take-home assessment submission for authorised reviewers |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | 2026-08-05 | Evidence-bound project change assurance: check the pack, record the human decision, tra… |
| [dating-app-recommendation-system](https://github.com/MatthewPaver/dating-app-recommendation-system) | 2026-08-05 | Swipe-style recommendation system with implicit feedback, temporal holdouts, and Top-K… |
| [sentence-similarity-analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | 2026-08-05 | Sentence-transformer notebook showing embedding similarity, cosine ranking, and retriev… |

<!-- AUTO:ACTIVITY_END -->

</details>

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

<p align="center">
  <sub>Built and maintained by Matthew Paver — <a href="https://github.com/MatthewPaver/MatthewPaver">github.com/MatthewPaver</a></sub>
</p>
