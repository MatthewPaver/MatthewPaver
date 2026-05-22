<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/">
    <img src="assets/profile-banner.svg" alt="Matthew Paver — I build AI products and the data systems behind them." width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/"><img src="https://img.shields.io/badge/Portfolio_Store-Open-0f766e?style=for-the-badge&logoColor=white" alt="Open Portfolio Store" /></a>
  <a href="https://inferencebrief.co/"><img src="https://img.shields.io/badge/Inference_Brief-Live-8f5d12?style=for-the-badge&logoColor=white" alt="Open Inference Brief" /></a>
  <a href="https://www.linkedin.com/in/matthew-paver-534262166/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/MatthewPaver/MatthewPaver/pages.yml?label=Pages%20deploy&style=flat-square&color=0f766e&labelColor=151515" alt="Pages deploy status" />
  <img src="https://img.shields.io/github/last-commit/MatthewPaver/MatthewPaver?label=Last%20commit&style=flat-square&color=8f5d12&labelColor=151515" alt="Last commit" />
  <img src="https://img.shields.io/badge/Projects-14-151515?style=flat-square&labelColor=151515&color=0f766e" alt="14 projects" />
  <img src="https://img.shields.io/badge/Live_paid_product-1-151515?style=flat-square&labelColor=151515&color=16a34a" alt="1 live paid product" />
  <img src="https://img.shields.io/badge/Configured_sources-103-151515?style=flat-square&labelColor=151515&color=8f5d12" alt="103 configured sources" />
  <img src="https://img.shields.io/badge/Reliability_tests-167-151515?style=flat-square&labelColor=151515&color=9f3a2f" alt="167 reliability tests" />
</p>

---

## Featured products

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">
    <img src="store/assets/inference-preview.gif" alt="Inference Brief — live demo" />
  </a>
  <h3>Inference Brief <sub>· <a href="https://inferencebrief.co/">live</a></sub></h3>
  <p>An AI-news reader with paid subscriptions. Source collection, scoring, summaries, issues, bookmarks, and reading history.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Python</code> <code>Stripe</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">Preview ↗</a> · <a href="https://inferencebrief.co/">Open product ↗</a> · <a href="CASE_STUDIES.md#inference-brief">Case study ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">
    <img src="store/assets/happening-preview.gif" alt="Happening — venue ingestion demo" />
  </a>
  <h3>Happening <sub>· private</sub></h3>
  <p>Turns 103 inconsistent venue pages into structured event data. 167-test reliability suite, scheduled daily runs.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code> <code>GitHub Actions</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">Preview ↗</a> · <a href="CASE_STUDIES.md#featured-build-happening">Case study ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">
    <img src="store/assets/quicksupply-preview.gif" alt="QuickSupply — cover ops demo" />
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
| **Role**     | Software engineer · AI, data, analytics |
| **Based**    | London |
| **Shipping** | [Inference Brief](https://inferencebrief.co/) (live, paid) · Happening (private venue-ingestion system) |
| **Open to**  | Product, data, and automation roles |
| **Stack**    | Python · TypeScript · FastAPI · Next.js · Postgres / DuckDB · Playwright · GitHub Actions |
| **Specs**    | [Constitution](.specify/memory/constitution.md) · [Feature spec](specs/001-portfolio-store-reliability/spec.md) · [Validator](scripts/validate-store.mjs) · [Lighthouse CI](.lighthouserc.json) |

## How the work flows

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

Every project I publish has this shape: a configured input, an explicit check, an artifact that can be opened, and a deploy gate that refuses drift. The [portfolio store](https://matthewpaver.github.io/MatthewPaver/store/) runs on that loop — Spec Kit constitution, validator, Lighthouse CI gates, no framework, no build system.

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

## Open these next

<table>
<tr>
<td valign="top" width="50%">

**▸ Runnable applications**

- [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) — Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/marketing-ml-lakehouse?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/marketing-ml-lakehouse?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [ProjectLens](https://github.com/MatthewPaver/ProjectLens) — Schedule-risk Flask app: upload, slippage analysis, milestone pressure, Power BI-ready exports<br/><sub><img src="https://img.shields.io/github/last-commit/MatthewPaver/ProjectLens?style=flat-square&label=Last%20commit&color=8f5d12&labelColor=151515" alt="Last commit" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/ProjectLens?style=flat-square&color=0f766e&labelColor=151515" alt="Top language" /></sub>
- [AI Workflow Evaluator](https://github.com/MatthewPaver/ai-workflow-evaluator) — Runnable quality gate for LLM outputs: accuracy, grounding, hallucination risk, latency, cost, review · [demo](https://matthewpaver.github.io/ai-workflow-evaluator/app/)<br/><sub><img src="https://img.shields.io/github/actions/workflow/status/MatthewPaver/ai-workflow-evaluator/validate.yml?style=flat-square&label=CI&color=0f766e&labelColor=151515" alt="AI Workflow Evaluator CI" /> <img src="https://img.shields.io/github/languages/top/MatthewPaver/ai-workflow-evaluator?style=flat-square&color=8f5d12&labelColor=151515" alt="Top language" /></sub>

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

## Latest shipping

| When | What |
|:---|:---|
| **2026-05** | AI Workflow Evaluator — local quality gate for LLM outputs with dashboard, tests, and CI |
| **2026-05** | Spec-driven portfolio governance: constitution, validator, Lighthouse CI, JSON-LD, manifest, CSP, custom OG card |
| **2026-04** | Inference Brief — accounts, paid subscriptions, bookmarks, reading history |
| **2026-03** | Happening — 167-test reliability suite, 103 venue source configs |
| **2026-02** | QuickSupply MVP — three-sided workflow, sequential assignment, live SSE status |

## GitHub signals

<p>
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img src="https://github-readme-stats.vercel.app/api?username=MatthewPaver&show_icons=true&hide_border=false&bg_color=fbfaf7&title_color=0f766e&text_color=151515&icon_color=8f5d12&border_color=d8d2c8&include_all_commits=true&count_private=false" alt="GitHub stats" height="170" />
  </a>
  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MatthewPaver&layout=compact&hide_border=false&bg_color=fbfaf7&title_color=0f766e&text_color=151515&border_color=d8d2c8&langs_count=8&hide=hcl" alt="Top languages" height="170" />
  </a>
</p>

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

## Routes through the work

| If you want | Open |
|:---|:---|
| The best visual overview | [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) |
| A live paid product | [Inference Brief](https://inferencebrief.co/) |
| Architecture and tradeoff stories | [Case Studies](CASE_STUDIES.md) |
| A piece of writing with an opinion | [What a 167-test scraping suite actually catches](writing/what-a-scraping-suite-catches.md) |
| The full repo map | [Projects appendix](Projects.md) |
| Background and experience | [CV](CV.pdf) |

<details>
<summary><strong>Latest public activity</strong> (auto-updated daily)</summary>

<!-- AUTO:ACTIVITY_START -->
## Latest Public Activity (Auto-Updated)

_This section is automatically refreshed by GitHub Actions._

- Last refresh (UTC): 2026-05-21 10:50

| Repo | Last push | What it is |
|:---|:---:|:---|
| [MatthewPaver](https://github.com/MatthewPaver/MatthewPaver) | 2026-05-20 | Portfolio: AI products, data systems, ML, and analytics — every project has a preview,… |
| [hr-performance-dashboards](https://github.com/MatthewPaver/hr-performance-dashboards) | 2026-05-17 | Power BI dashboard handoff package for HR, absence, and sales performance analytics. |
| [marketing-ml-lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | 2026-05-17 | Local DuckDB, XGBoost, and Streamlit analytics pipeline for marketing performance data. |
| [netflix-content-analysis](https://github.com/MatthewPaver/netflix-content-analysis) | 2026-05-17 | Notebook EDA of Netflix title data with country, genre, timeline, and catalog growth an… |
| [sentence-similarity-analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | 2026-05-16 | Sentence-transformer notebook showing embedding similarity, cosine ranking, and retriev… |
| [dating-app-recommendation-system](https://github.com/MatthewPaver/dating-app-recommendation-system) | 2026-05-16 | Swipe-style recommendation system with implicit feedback, temporal holdouts, and Top-K… |

<!-- AUTO:ACTIVITY_END -->

</details>

<p align="center"><img src="assets/mp-rule.svg" alt="" width="320" height="32" /></p>

<p align="center">
  <sub>Hand-built. Spec-driven. Deploy gated. — <a href="https://github.com/MatthewPaver/MatthewPaver">github.com/MatthewPaver</a></sub>
</p>
