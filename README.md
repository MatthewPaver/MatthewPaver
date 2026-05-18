<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/">
    <img src="assets/profile-banner.svg" alt="Matthew Paver — AI products, data systems, and analytics" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/"><img src="https://img.shields.io/badge/Portfolio_Store-Open-0f766e?style=for-the-badge&logoColor=white" alt="Open Portfolio Store" /></a>
  <a href="https://inferencebrief.co/"><img src="https://img.shields.io/badge/Inference_Brief-Live-8f5d12?style=for-the-badge&logoColor=white" alt="Open Inference Brief" /></a>
  <a href="https://www.linkedin.com/in/matthew-paver-534262166/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p>

## At a glance

| | |
|:---|:---|
| **Role**     | Software engineer · AI, data, analytics |
| **Based**    | London |
| **Shipping** | [Inference Brief](https://inferencebrief.co/) (live, paid) · Happening (private venue-ingestion system, 103 sources / 167 tests) |
| **Open to**  | Product, data, and automation roles |
| **Stack**    | Python · TypeScript · FastAPI · Next.js · Postgres / DuckDB · Playwright · GitHub Actions |
| **Specs**    | [Constitution](.specify/memory/constitution.md) · [Feature spec](specs/001-portfolio-store-reliability/spec.md) · [Validator](scripts/validate-store.mjs) · [Lighthouse CI](.lighthouserc.json) |

## Featured builds

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">
    <img src="store/assets/inference-brief.png" alt="Inference Brief product preview" />
  </a>
  <h3>Inference Brief <sub>· <a href="https://inferencebrief.co/">live</a></sub></h3>
  <p>An AI-news reader with paid subscriptions. Source collection, scoring, summaries, issues, bookmarks, and reading history.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Python</code> <code>Stripe</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">Preview ↗</a> · <a href="https://inferencebrief.co/">Open product ↗</a> · <a href="CASE_STUDIES.md#inference-brief">Case study ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">
    <img src="store/assets/happening-web.png" alt="Happening event ingestion preview" />
  </a>
  <h3>Happening <sub>· private</sub></h3>
  <p>A venue-event pipeline that turns 103 inconsistent source pages into structured data. 167-test reliability suite, scheduled daily runs.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code> <code>GitHub Actions</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">Preview ↗</a> · <a href="CASE_STUDIES.md#featured-build-happening">Case study ↗</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">
    <img src="store/assets/quicksupply-dashboard.png" alt="QuickSupply product preview" />
  </a>
  <h3>QuickSupply <sub>· private MVP</sub></h3>
  <p>A school cover-ops workflow built for three sides: school, agency, teacher. Sequential assignment, compliance checks, live status.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>PostgreSQL</code> <code>Drizzle</code> <code>SSE</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">Preview ↗</a></p>
</td>
</tr>
</table>

## Public repos to open

**Runnable applications**

| Repo | What you see when you open it |
|:---|:---|
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard. Runs locally end-to-end. |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Schedule-risk Flask app: upload, slippage analysis, milestone pressure, Power BI-ready exports. |

**Notebook demos and technical examples**

| Repo | What you see when you open it |
|:---|:---|
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Implicit-feedback ranking with temporal holdouts and Top-K metrics. Demo data + CLI smoke path. |
| [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Embedding retrieval with a deliberate point about similarity not being truth. |
| [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Compact examples covering DataFrames, Structured Streaming, JSON event production. |

**Analytics handoff**

| Repo | What you see when you open it |
|:---|:---|
| [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) | Power BI dashboard package: PBIX files, dashboard previews, methodology PDF, stakeholder commentary. |

## How the work is shaped

I run this repository like a small product. There's a written constitution in [`.specify/memory/`](.specify/memory/constitution.md), a feature spec in [`specs/001-portfolio-store-reliability/`](specs/001-portfolio-store-reliability/spec.md), and a deploy-gate validator in [`scripts/validate-store.mjs`](scripts/validate-store.mjs) that checks the catalogue, image dimensions, sitemap coverage, manifest, favicons, JSON-LD, CSP, print stylesheet, and progressive-enhancement contracts. Lighthouse CI gates accessibility and SEO before each deploy.

When I publish a project I write it so a reviewer can be running it locally inside a few minutes — README, run command, tests, sample data, a screenshot, and notes on what to look at first. The work is meant to be opened, not just admired.

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
| The full repo map | [Projects appendix](Projects.md) |
| Background and experience | [CV](CV.pdf) |

<details>
<summary><strong>Latest public activity</strong> (auto-updated daily)</summary>

<!-- AUTO:ACTIVITY_START -->
## Latest Public Activity (Auto-Updated)

_This section is automatically refreshed by GitHub Actions._

- Last refresh (UTC): 2026-05-18 11:12

| Repo | Last push | What it is |
|:---|:---:|:---|
| [hr-performance-dashboards](https://github.com/MatthewPaver/hr-performance-dashboards) | 2026-05-17 | Power BI dashboard handoff package for HR, absence, and sales performance analytics. |
| [MatthewPaver](https://github.com/MatthewPaver/MatthewPaver) | 2026-05-17 | AI and data engineering portfolio: product store, case studies, public repo map, and cr… |
| [marketing-ml-lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | 2026-05-17 | Local DuckDB, XGBoost, and Streamlit analytics pipeline for marketing performance data. |
| [netflix-content-analysis](https://github.com/MatthewPaver/netflix-content-analysis) | 2026-05-17 | Notebook EDA of Netflix title data with country, genre, timeline, and catalog growth an… |
| [sentence-similarity-analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | 2026-05-16 | Sentence-transformer notebook showing embedding similarity, cosine ranking, and retriev… |
| [dating-app-recommendation-system](https://github.com/MatthewPaver/dating-app-recommendation-system) | 2026-05-16 | Swipe-style recommendation system with implicit feedback, temporal holdouts, and Top-K… |

<!-- AUTO:ACTIVITY_END -->

</details>

<p align="center">
  <sub>Hand-built. Spec-driven. Deploy gated. — <a href="https://github.com/MatthewPaver/MatthewPaver">github.com/MatthewPaver</a></sub>
</p>
