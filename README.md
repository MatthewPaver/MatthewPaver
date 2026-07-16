<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/">
    <img src="assets/profile-banner.svg" alt="Matthew Paver — automation, data, and AI projects." width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/"><img src="https://img.shields.io/badge/Portfolio_Store-Open-0f766e?style=for-the-badge&logoColor=white" alt="Open Portfolio Store" /></a>
  <a href="https://www.linkedin.com/in/matthew-paver-534262166/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/MatthewPaver/MatthewPaver/pages.yml?label=Pages%20deploy&style=flat-square&color=0f766e&labelColor=151515" alt="Pages deploy status" />
  <img src="https://img.shields.io/github/last-commit/MatthewPaver/MatthewPaver?label=Last%20commit&style=flat-square&color=8f5d12&labelColor=151515" alt="Last commit" />
</p>

---

## Featured products

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/can-england-win-it/">
    <img src="store/assets/project-1966-profile.png" alt="Can England Win It simulation result screen" />
  </a>
  <h3>Can England Win It? <sub>· live</sub></h3>
  <p>A playable World Cup probability lab: make three matchday calls and run 10,000 tournament futures.</p>
  <p><code>React</code> <code>TypeScript</code> <code>Vite</code> <code>Vitest</code> <code>Monte Carlo</code></p>
  <p><a href="https://matthewpaver.github.io/can-england-win-it/">Play live ↗</a> · <a href="CASE_STUDIES.md#product-case-study-can-england-win-it">Case study ↗</a> · <a href="https://github.com/MatthewPaver/can-england-win-it">Repo ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">
    <img src="store/assets/happening-web.png" alt="Happening venue ingestion dashboard" />
  </a>
  <h3>Happening <sub>· private</sub></h3>
  <p>Venue pages turned into structured event data, with source configs, scheduled runs, and a 167-test reliability suite.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code> <code>GitHub Actions</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">Preview ↗</a> · <a href="CASE_STUDIES.md#featured-build-happening">Case study ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">
    <img src="store/assets/quicksupply-dashboard.png" alt="QuickSupply cover operations dashboard" />
  </a>
  <h3>QuickSupply <sub>· private MVP</sub></h3>
  <p>A school cover-ops workflow built for three sides: school, agency, teacher. Sequential assignment, compliance checks, live status.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>PostgreSQL</code> <code>Drizzle</code> <code>SSE</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">Preview ↗</a></p>
</td>
</tr>
</table>

## At a glance

| | |
|:---|:---|
| **Role**     | Software engineer and automation specialist |
| **Based**    | London |
| **Focus**    | Automation, data products, AI workflows, analytics tools |
| **Shipping** | Project 1966 (live simulator) · Happening (private venue-ingestion system) · QuickSupply (private MVP) |
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

The pattern is practical: collect the messy input, clean it, check it, and turn it into something you can open. The [portfolio store](https://matthewpaver.github.io/MatthewPaver/store/) follows the same habit: indexed catalogue, validator, Lighthouse CI, no framework, no build step.

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

## Open these next

<table>
<tr>
<td valign="top" width="50%">

**▸ Runnable applications**

- [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) — Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/marketing-ml-lakehouse?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/marketing-ml-lakehouse?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [ProjectLens](https://github.com/MatthewPaver/ProjectLens) — Schedule-risk Flask app: upload, slippage analysis, milestone pressure, Power BI-ready exports<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/ProjectLens?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/ProjectLens?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
<sub><strong>Repo standard:</strong> run command, tests or checks, demo/sample data where possible, screenshots, architecture notes, and limitations.</sub>

**▸ Analytics handoff**

- [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) — Power BI dashboard package: PBIX files, dashboard previews, methodology PDF, stakeholder commentary<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/hr-performance-dashboards?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/repo-size/MatthewPaver/hr-performance-dashboards?style=flat-square&label=Size&color=0f766e&labelColor=151515" alt="Repo size" /></sub>

</td>
<td valign="top" width="50%">

**▸ Notebook demos and technical examples**

- [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) — Implicit-feedback ranking with temporal holdouts and Top-K metrics<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/dating-app-recommendation-system?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/dating-app-recommendation-system?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
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

- Last refresh (UTC): 2026-07-16 09:30

| Repo | Last push | What it is |
|:---|:---:|:---|
| [MatthewPaver.github.io](https://github.com/MatthewPaver/MatthewPaver.github.io) | 2026-07-15 | Live apps, open-source tools and private product pilots by Matthew Paver |
| [MatthewPaver](https://github.com/MatthewPaver/MatthewPaver) | 2026-07-15 | Portfolio: AI products, data systems, ML, and analytics — every project has a preview,… |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | 2026-07-15 | Evidence-bound project change assurance: check the pack, record the human decision, tra… |
| [DecisionGraph](https://github.com/MatthewPaver/DecisionGraph) | 2026-07-15 | Evidence-linked project decision memory and comparable-case retrieval demo |
| [paper-trading-bot](https://github.com/MatthewPaver/paper-trading-bot) | 2026-07-15 | Evidence-first paper-trading research engine with reproducible backtests, risk controls… |
| [happening-open-core](https://github.com/MatthewPaver/happening-open-core) | 2026-07-15 | Evidence-aware event schemas and reproducible source-coverage benchmarks |

<!-- AUTO:ACTIVITY_END -->

</details>

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

<p align="center">
  <sub>Built and maintained by Matthew Paver — <a href="https://github.com/MatthewPaver/MatthewPaver">github.com/MatthewPaver</a></sub>
</p>
