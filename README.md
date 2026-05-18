<div align="center">

# Matthew Paver

I build software that turns messy information into useful tools. Most of what I work on starts with public web data, scraped pages, or raw CSVs, and ends with a product someone can actually open.

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

## What I'm working on

I'm running **[Inference Brief](https://inferencebrief.co/)**, an AI-news reader I built end-to-end. It collects, scores, summarises, and publishes stories into issues. There's an account system, reading history, bookmarks, and a billing surface behind it.

On the side I run **Happening**, a private system that watches 103 London venue pages and turns them into structured event data. It treats each venue as a configured source with extraction rules, dedupe, and validation, and has a 167-test reliability suite I keep adding to as the venues change shape.

## What I tend to work on

**Products.** Web apps where AI sits inside a real workflow rather than off to the side. Usually Next.js and TypeScript on the front, Python with Postgres or Supabase behind. Inference Brief is the live one; AI Study Companion and QuickSupply are private MVPs.

**Data systems.** Scrapers, pipelines, validation, and the boring infrastructure that makes a daily run trustworthy. Happening is the biggest example. Smart Job Market Intelligence is similar in shape.

**Analytics and ML.** Ranking systems with proper temporal evaluation, schedule-risk apps, dashboards that ship with the data and the methodology. ProjectLens, the Marketing ML Lakehouse, a dating-app recommender, and an HR analytics handoff package.

## Featured builds

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">
    <img src="store/assets/inference-brief.png" alt="Inference Brief product preview" />
  </a>
  <h3>Inference Brief</h3>
  <p>Live AI-news reader. Collection, scoring, summaries, issues, accounts, bookmarks, reading history.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Python</code> <code>Stripe</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=inference">Preview</a> · <a href="https://inferencebrief.co/">Open product</a> · <a href="CASE_STUDIES.md#inference-brief">Case study</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">
    <img src="store/assets/happening-web.png" alt="Happening event ingestion preview" />
  </a>
  <h3>Happening</h3>
  <p>Private venue-event pipeline. 103 sources, dedupe, validation, a 167-test reliability suite, scheduled daily runs.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code> <code>GitHub Actions</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=happening">Preview</a> · <a href="CASE_STUDIES.md#featured-build-happening">Case study</a></p>
</td>
<td width="33%" valign="top">
  <a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">
    <img src="store/assets/quicksupply-dashboard.png" alt="QuickSupply product preview" />
  </a>
  <h3>QuickSupply</h3>
  <p>School cover ops MVP. Three sides of the workflow (school, agency, teacher) with sequential assignment and live status.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>PostgreSQL</code> <code>Drizzle</code> <code>SSE</code></p>
  <p><a href="https://matthewpaver.github.io/MatthewPaver/store/preview.html?app=quicksupply">Preview</a></p>
</td>
</tr>
</table>

## Public repos worth opening

| Repo | What you'll see |
|:---|:---|
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Bronze/silver/gold DuckDB flow, XGBoost training, data-quality checks, Streamlit dashboard. Runs locally end-to-end. |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Schedule-risk Flask app with upload flow, slippage analysis, milestone pressure, and Power BI-ready exports. |
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Implicit-feedback ranking with temporal holdouts and Top-K metrics. Demo data plus a CLI smoke path. |
| [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) | Power BI handoff package: PBIX files, prepared data, screenshots, and stakeholder commentary. |
| [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Embedding retrieval notebook with a deliberate point about similarity not being truth. |
| [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Small technical examples covering DataFrames, Structured Streaming, and JSON event production. |

## How the work is shaped

I run this repository as if it were a small product. There is a written constitution in `.specify/memory/`, a feature spec in `specs/001-portfolio-store-reliability/`, and a deploy-gate validator in `scripts/validate-store.mjs` that checks the catalogue, image dimensions, sitemap coverage, manifest, favicons, JSON-LD, CSP, dark and print stylesheets, and progressive-enhancement contracts. Lighthouse CI gates accessibility and SEO before each deploy.

When I publish a project I try to write it so a reviewer can be running it locally inside a few minutes — README, run command, tests, sample data, a screenshot or two, and notes on what to look at first. The work is meant to be opened, not just admired.

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

## Routes through the work

The [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) is the best place to start — it has every project laid out with a problem statement, stack, status, and a preview. [Case studies](CASE_STUDIES.md) go deeper into the private builds. [Projects.md](Projects.md) is a fuller appendix when you want every repo, public or private. The [CV](CV.pdf) is there for the conventional read.

## Contact

Open to product, data, and automation work. [LinkedIn](https://www.linkedin.com/in/matthew-paver-534262166/) is the easiest way to reach me.

<details>
<summary>Latest public activity</summary>

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
