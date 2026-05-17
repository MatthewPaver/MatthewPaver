<div align="center">

# Matthew Paver

### I turn messy information into useful, inspectable products.

Crawled pages, scraped listings, raw CSVs, schedules — collected, checked, and turned into something a real person can open. AI, data, and product design sitting in one workflow rather than three.

<p>
  <a href="https://matthewpaver.github.io/MatthewPaver/store/">
    <img src="https://img.shields.io/badge/Open-Portfolio_Store-151515?style=for-the-badge&labelColor=0f766e&color=151515" alt="Open Portfolio Store" />
  </a>
  <a href="https://inferencebrief.co/">
    <img src="https://img.shields.io/badge/Live-Inference_Brief-151515?style=for-the-badge&labelColor=8f5d12&color=151515" alt="Open Inference Brief" />
  </a>
  <a href="CASE_STUDIES.md">
    <img src="https://img.shields.io/badge/Read-Case_Studies-151515?style=for-the-badge&labelColor=1d4f91&color=151515" alt="Read Case Studies" />
  </a>
  <a href="CV.pdf">
    <img src="https://img.shields.io/badge/View-CV-151515?style=for-the-badge&labelColor=9f3a2f&color=151515" alt="View CV" />
  </a>
  <a href="https://www.linkedin.com/in/matthew-paver-534262166/">
    <img src="https://img.shields.io/badge/Reach_out-LinkedIn-151515?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a66c2&color=151515" alt="Connect on LinkedIn" />
  </a>
</p>

</div>

---

## Signals at a glance

| Signal | Where it shows up |
|:---|:---|
| **Live product with paying-grade infrastructure** | [Inference Brief](https://inferencebrief.co/) — accounts, bookmarks, history, publishing, billing surface |
| **103+ configured sources · 167-test reliability suite** | Happening — venue ingestion done as a contract, not as one-off scraping |
| **Spec-driven portfolio with deploy gates** | [This repo](specs/001-portfolio-store-reliability/) — Spec Kit constitution, validator, Lighthouse CI |
| **Cross-stack delivery** | Python pipelines · Next.js products · DuckDB / Postgres · Power BI handoffs |

## What I build

<table>
<tr>
<td width="33%" valign="top">

### AI products
End-to-end products where AI sits inside a workflow, not next to it. Source collection, scoring, summaries, publishing, accounts, history, and feedback loops.

Best examples: [Inference Brief](https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference), [AI Study Companion](https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=study), [QuickSupply](https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply)

</td>
<td width="33%" valign="top">

### Data systems
Messy public sources turned into checked, repeatable data with explicit source configs, dedupe, validation, scheduled runs, and source-level quality checks.

Best examples: [Happening](https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening), [Smart Job Market Intelligence](https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=smart-job), [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse)

</td>
<td width="33%" valign="top">

### Analytics &amp; ML
Analytics packaged as tools — upload flows, schedule-risk reports, ranking systems with proper temporal evaluation, dashboard handoffs that come with the data and commentary.

Best examples: [ProjectLens](https://github.com/MatthewPaver/ProjectLens), [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system), [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards)

</td>
</tr>
</table>

## Featured builds

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">
    <img src="store/assets/inference-brief.png" alt="Inference Brief product preview" />
  </a>
  <h3>Inference Brief · <a href="https://inferencebrief.co/">live</a></h3>
  <p><strong>Calm AI reading.</strong> Collects, scores, summarises, and publishes stories into issues. Reader accounts with bookmarks, history, and preferences. Editorial workflow separates judgement from automation.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Python</code> <code>Stripe</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">Preview</a> · <a href="https://inferencebrief.co/">Open product</a> · <a href="CASE_STUDIES.md#inference-brief">Case study</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">
    <img src="store/assets/happening-web.png" alt="Happening event ingestion preview" />
  </a>
  <h3>Happening · private</h3>
  <p><strong>Reliable scraping at scale.</strong> Each venue is a configured data contract: extraction rules, dedupe, validation, regression tests. The hard part is not collecting events — it is knowing when the data path is healthy.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code> <code>GitHub Actions</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">Preview</a> · <a href="CASE_STUDIES.md#featured-build-happening">Case study</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">
    <img src="store/assets/quicksupply-dashboard.png" alt="QuickSupply product preview" />
  </a>
  <h3>QuickSupply · private MVP</h3>
  <p><strong>Three-sided cover ops.</strong> School cover requests, sequential agency assignment, teacher availability, compliance checks, and live status. Operational clarity instead of another spreadsheet.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>PostgreSQL</code> <code>Drizzle</code> <code>SSE</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">Preview</a></p>
</td>
</tr>
</table>

## Public repos worth opening

| Repo | What it shows | Open |
|:---|:---|:---|
| **Marketing ML Lakehouse** | Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard. Run locally end-to-end. | [Open](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| **ProjectLens** | Schedule-risk app: upload, clean, slippage analysis, milestone pressure, Power BI-ready outputs. Tests + upload flow. | [Open](https://github.com/MatthewPaver/ProjectLens) |
| **Dating App Recommendation System** | Implicit-feedback ranking with temporal holdouts and Top-K evaluation. Demo data + CLI smoke path. | [Open](https://github.com/MatthewPaver/dating-app-recommendation-system) |
| **HR Performance Analytics** | Power BI handoff package: PBIX files, prepared data, screenshots, stakeholder commentary. | [Open](https://github.com/MatthewPaver/hr-performance-dashboards) |
| **Sentence Similarity Analysis** | Embedding retrieval demo with deliberate caveats about similarity ≠ truth. | [Open](https://github.com/MatthewPaver/sentence-similarity-analysis) |
| **PySpark Kafka Streaming** | Compact technical examples covering DataFrames, Structured Streaming, JSON event production. | [Open](https://github.com/MatthewPaver/pyspark-kafka-streaming) |

## How I work

- **Spec-first.** This repo runs on a Spec Kit constitution, feature spec, validator, and Lighthouse CI gates. Drift between CSV, HTML, JSON, sitemap, and assets is impossible by design.
- **Evidence over decoration.** Every project on the [store](https://matthewpaver.github.io/MatthewPaver/store/) declares its problem, proof point, stack, status, and preview path. No decorative cards.
- **Progressive enhancement.** Every link works without JavaScript. JS only enhances filtering, sorting, motion, and per-slug preview rendering.
- **Reliability over cleverness.** Determinism beats elegance when the system has to run unattended. Happening is 103+ source configs and 167 tests for that reason.
- **Inspectable handoffs.** Public repos ship with run instructions, tests, sample data, and notes on what to look at first.

## Credentials

<table>
<tr>
<td width="22%" valign="top"><strong>Cloud</strong></td>
<td width="78%" valign="top">
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/d0dd54bf93df495da5c3e75ee69940fe"><img src="https://img.shields.io/badge/AWS-Cloud_Practitioner-151515?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS Certified Cloud Practitioner" /></a>
</td>
</tr>
<tr>
<td valign="top"><strong>AI &amp; data</strong></td>
<td valign="top">
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/455c09a58c6c43beb001b21d3ccec2a0"><img src="https://img.shields.io/badge/AWS-AI_Practitioner-151515?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS Certified AI Practitioner" /></a>
  <a href="https://drive.google.com/file/d/15oXe_G86TEiETdC8kGBhbnKoMjVZ5mQQ/view"><img src="https://img.shields.io/badge/Neo4j-Certified_Professional-151515?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j Certified Professional" /></a>
  <a href="https://drive.google.com/file/d/1NgSeIIF49Sqh2DAMY5KQEtnaddSc1Sqw/view"><img src="https://img.shields.io/badge/Hugging_Face-AI_Agents-151515?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face AI Agents Course" /></a>
</td>
</tr>
<tr>
<td valign="top"><strong>Automation</strong></td>
<td valign="top">
  <a href="https://drive.google.com/file/d/15lrcn5_Cn4g-kD165xGNLUGUGXtCptk-/view"><img src="https://img.shields.io/badge/UiPath-RPA_Developer-151515?style=for-the-badge&logo=uipath&logoColor=white" alt="UiPath RPA Developer Advanced" /></a>
</td>
</tr>
<tr>
<td valign="top"><strong>Professional IT</strong></td>
<td valign="top">
  <a href="https://drive.google.com/file/d/15yLBx8nzlhn_PwrGoqQbumRG8zRQPC9t/view"><img src="https://img.shields.io/badge/BCS-Diploma_in_IT-151515?style=for-the-badge&logo=bcs&logoColor=white" alt="BCS Diploma in IT" /></a>
  <a href="https://drive.google.com/file/d/160nzem63oIEv3EF9mCU9NGWwwA4NMdMZ/view"><img src="https://img.shields.io/badge/BCS-Certificate_in_IT-151515?style=for-the-badge&logo=bcs&logoColor=white" alt="BCS Certificate in IT" /></a>
</td>
</tr>
</table>

## Stack I reach for

<p>
  <img src="https://img.shields.io/badge/Python-151515?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-151515?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/FastAPI-151515?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Next.js-151515?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/DuckDB-151515?style=for-the-badge&logo=duckdb&logoColor=white" alt="DuckDB" />
  <img src="https://img.shields.io/badge/PostgreSQL-151515?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Supabase-151515?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
  <img src="https://img.shields.io/badge/Playwright-151515?style=for-the-badge&logo=playwright&logoColor=white" alt="Playwright" />
  <img src="https://img.shields.io/badge/GCP-151515?style=for-the-badge&logo=googlecloud&logoColor=white" alt="GCP" />
  <img src="https://img.shields.io/badge/Power_BI-151515?style=for-the-badge&logo=powerbi&logoColor=white" alt="Power BI" />
</p>

## How to read this

| If you want | Open |
|:---|:---|
| The best visual overview | [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) |
| A live, paying-grade product | [Inference Brief](https://inferencebrief.co/) |
| Architecture &amp; tradeoff stories | [Case Studies](CASE_STUDIES.md) |
| Full repo + project map | [Projects appendix](Projects.md) |
| Background &amp; experience | [CV](CV.pdf) |

The store is the front door — a hand-coded static site with a Spec Kit governance layer, validator, Lighthouse CI, and progressive-enhancement contract. The [`specs/`](specs/001-portfolio-store-reliability/) directory shows how the work is governed; [`scripts/validate-store.mjs`](scripts/validate-store.mjs) is the deploy gate.

## Contact

Open to AI/data product work, automation systems, and operational tooling. Best place to reach me is [LinkedIn](https://www.linkedin.com/in/matthew-paver-534262166/).

<details>
<summary>Latest public activity</summary>

<!-- AUTO:ACTIVITY_START -->
## Latest Public Activity (Auto-Updated)

_This section is automatically refreshed by GitHub Actions._

- Last refresh (UTC): 2026-05-16 09:03

| Repo | Last push | What it is |
|:---|:---:|:---|
| [MatthewPaver](https://github.com/MatthewPaver/MatthewPaver) | 2026-05-16 | AI and data engineering portfolio showcasing production-minded AI products, automation… |
| [ai-weekly](https://github.com/MatthewPaver/ai-weekly) | 2026-05-15 | Archived AI newsletter output superseded by Inference Brief. |
| [generate-newsletter](https://github.com/MatthewPaver/generate-newsletter) | 2026-05-15 | Archived newsletter-generation prototype for collecting articles and rendering HTML out… |
| [pinterest-image-scraper](https://github.com/MatthewPaver/pinterest-image-scraper) | 2026-05-15 | Archived Pinterest image collection utility with duplicate detection, originally used t… |
| [pyspark-kafka-streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | 2026-05-15 | Compact PySpark and Kafka technical examples covering DataFrames, Structured Streaming,… |
| [netflix-content-analysis](https://github.com/MatthewPaver/netflix-content-analysis) | 2026-05-15 | Notebook EDA of Netflix title data with country, genre, timeline, and catalog growth an… |

<!-- AUTO:ACTIVITY_END -->

</details>
