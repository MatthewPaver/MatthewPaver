<div align="center">

# Matthew Paver

### AI products, data systems, automation, and analytics apps

I build practical systems around messy inputs: crawled websites, scraped listings, raw CSVs, notes, schedules, dashboards, and recommendation data. The pattern is usually the same: collect it, clean it, test it, package it, and make it useful through a product or workflow someone can actually open.

<a href="https://matthewpaver.github.io/MatthewPaver/store/">
  <img src="https://img.shields.io/badge/Idea_Store-D9A441?style=for-the-badge" alt="Idea Store" />
</a>
<a href="https://inferencebrief.co/">
  <img src="https://img.shields.io/badge/Live_Product-Inference_Brief-00D9FF?style=for-the-badge" alt="Inference Brief" />
</a>
<a href="CASE_STUDIES.md">
  <img src="https://img.shields.io/badge/Case_Studies-0F766E?style=for-the-badge" alt="Case Studies" />
</a>
<a href="Projects.md">
  <img src="https://img.shields.io/badge/Project_Index-181717?style=for-the-badge&logo=github&logoColor=white" alt="Project Index" />
</a>
<a href="CV.pdf">
  <img src="https://img.shields.io/badge/CV-0078D4?style=for-the-badge&logo=readthedocs&logoColor=white" alt="CV" />
</a>
<a href="https://www.linkedin.com/in/matthew-paver-534262166/">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>

<br />

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

</div>

---

## Snapshot

<table>
<tr>
<td width="25%" valign="top">
  <h3>Live product</h3>
  <p><a href="https://inferencebrief.co/"><strong>Inference Brief</strong></a></p>
  <p>AI news product with publishing, accounts, bookmarks, history, preferences, and a working reader experience.</p>
</td>
<td width="25%" valign="top">
  <h3>Strongest private system</h3>
  <p><a href="CASE_STUDIES.md#happening"><strong>Happening</strong></a></p>
  <p>103+ London venue sources turned into structured event data with crawling, dedupe, checks, and tests.</p>
</td>
<td width="25%" valign="top">
  <h3>Best public data app</h3>
  <p><a href="https://github.com/MatthewPaver/marketing-ml-lakehouse"><strong>Marketing ML Lakehouse</strong></a></p>
  <p>DuckDB lakehouse, data quality checks, XGBoost training, and a Streamlit dashboard.</p>
</td>
<td width="25%" valign="top">
  <h3>Largest public ML dataset</h3>
  <p><a href="https://github.com/MatthewPaver/dating-app-recommendation-system"><strong>3.4M+ interactions</strong></a></p>
  <p>Recommendation-system project with temporal evaluation and Top-K metrics.</p>
</td>
</tr>
</table>

---

## Featured Shelf

<table>
<tr>
<td width="33%" valign="top">
  <a href="https://inferencebrief.co/">
    <img src="store/assets/inference-brief.png" alt="Inference Brief screenshot" />
  </a>
  <h3>Inference Brief</h3>
  <p>Live AI news reader. Collects stories, scores them, writes short briefings, publishes issues, and gives readers bookmarks, history, and preferences.</p>
  <p><code>Next.js</code> <code>TypeScript</code> <code>Supabase</code> <code>Python</code> <code>Stripe</code></p>
</td>
<td width="33%" valign="top">
  <a href="CASE_STUDIES.md#happening">
    <img src="store/assets/happening-pipeline.svg" alt="Happening ingestion pipeline visual" />
  </a>
  <h3>Happening</h3>
  <p>Private ingestion platform. Turns venue websites into clean London event data with adapters, extraction rules, dedupe, scheduled checks, and operational tests.</p>
  <p><code>Python</code> <code>Playwright</code> <code>SQLite</code> <code>Pydantic</code></p>
</td>
<td width="33%" valign="top">
  <a href="https://github.com/MatthewPaver/marketing-ml-lakehouse">
    <img src="store/assets/marketing-lakehouse.svg" alt="Marketing ML Lakehouse workflow visual" />
  </a>
  <h3>Marketing ML Lakehouse</h3>
  <p>Runnable public data app. Loads raw marketing CSVs into DuckDB, builds quality-checked tables, trains models, and serves a dashboard.</p>
  <p><code>Python</code> <code>DuckDB</code> <code>XGBoost</code> <code>Streamlit</code></p>
</td>
</tr>
</table>

---

## What I Build

| Mode | What that means | Examples |
|:---|:---|:---|
| **AI products** | AI is part of a real workflow, not just a prompt demo | [Inference Brief](https://inferencebrief.co/), [AI Study Companion](CASE_STUDIES.md#ai-study-companion) |
| **Data pipelines** | Messy sources become clean, repeatable datasets | [Happening](CASE_STUDIES.md#happening), [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| **Automation** | Jobs run on a schedule and leave evidence behind | Happening checks, newsletter tools, scrape monitors |
| **Analytics apps** | Analysis is packaged into an interface people can use | [ProjectLens](https://github.com/MatthewPaver/ProjectLens), HR dashboards |
| **ML projects** | Ranking, embeddings, forecasting, and generation | recommender systems, Architexa, sentence similarity |

---

## Project Map

| Project | Type | What it does | Stack |
|:---|:---|:---|:---|
| [Inference Brief](https://inferencebrief.co/) | Live product | Collects AI stories, scores them, writes briefings, publishes issues, and gives readers bookmarks/history/preferences | `Next.js` `TypeScript` `Supabase` `Python` `Stripe` |
| [Happening](CASE_STUDIES.md#happening) | Private system | Turns 103+ London venue websites into clean event data with crawling, extraction, dedupe, checks, and tests | `Python` `Playwright` `SQLite` `Pydantic` |
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Public repo | Runnable DuckDB lakehouse with model training, quality checks, and Streamlit reporting | `Python` `DuckDB` `XGBoost` `Streamlit` |
| [AI Study Companion](CASE_STUDIES.md#ai-study-companion) | Private product | Upload notes, generate flashcards/quizzes/study plans, and review with spaced repetition | `FastAPI` `PostgreSQL` `Redis` `Celery` |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Public repo | Upload project schedule data and spot slippage, milestone pressure, and reporting issues | `Python` `Flask` `pandas` |
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Public repo | Implicit-feedback recommender with 3.4M+ interactions, temporal evaluation, and Top-K metrics | `Python` `NumPy` `SciPy` |
| QuickSupply | Private MVP | Scheduling MVP for schools, teachers, and agency staff with sequential assignment and live status updates | `Next.js` `TypeScript` `PostgreSQL` `SSE` |
| Operations Platform Prototype | Private prototype | Resident requests, service-charge visibility, ticket audit trails, payments, and AI triage | `Next.js` `TypeScript` `Payments` |

<details>
<summary>More public repos</summary>

| Repo | What to look at |
|:---|:---|
| [Architexa](https://github.com/MatthewPaver/Architexa) | Conditional GAN, image-generation API, dataset pipeline |
| [sentence-similarity-analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Sentence-transformer embeddings and cosine similarity caveats |
| [pyspark-kafka-streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Compact Kafka and PySpark streaming examples |
| [hr-performance-dashboards](https://github.com/MatthewPaver/hr-performance-dashboards) | Power BI dashboards, prepared CSVs, screenshots, and stakeholder notes |

</details>

---

## How I Think About Projects

```mermaid
flowchart LR
    A["Messy input"] --> B["Collect"]
    B --> C["Clean + validate"]
    C --> D["Store"]
    D --> E["Model / analyse / rank"]
    E --> F["Interface / report / workflow"]
    F --> G["Tests + feedback"]
    G --> C
```

The part I care about is the whole loop: not just the model, not just the dashboard, not just the script. The work is strongest when the data path is repeatable, the output is easy to inspect, and failures are visible.

---

## Current Focus

<table>
<tr>
<td width="33%" valign="top">
  <h3>Productising AI work</h3>
  <p>Turning AI workflows into usable apps with accounts, state, background jobs, and a clear user path.</p>
</td>
<td width="33%" valign="top">
  <h3>Reliable data systems</h3>
  <p>Building pipelines with checks, fixtures, test coverage, and enough observability to trust scheduled runs.</p>
</td>
<td width="33%" valign="top">
  <h3>Showing private work safely</h3>
  <p>Using anonymised case studies, diagrams, and screenshots when the strongest systems cannot be public.</p>
</td>
</tr>
</table>

---

## Credentials

<table>
<tr>
<td width="20%" align="center">
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/455c09a58c6c43beb001b21d3ccec2a0">
    <img src="https://img.shields.io/badge/AWS-AI_Practitioner-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS Certified AI Practitioner" />
  </a>
</td>
<td width="20%" align="center">
  <a href="https://cp.certmetrics.com/amazon/en/public/verify/credential/d0dd54bf93df495da5c3e75ee69940fe">
    <img src="https://img.shields.io/badge/AWS-Cloud_Practitioner-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS Certified Cloud Practitioner" />
  </a>
</td>
<td width="20%" align="center">
  <a href="https://drive.google.com/file/d/15oXe_G86TEiETdC8kGBhbnKoMjVZ5mQQ/view">
    <img src="https://img.shields.io/badge/Neo4j-Certified_Professional-008CC1?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j Certified Professional" />
  </a>
</td>
<td width="20%" align="center">
  <a href="https://drive.google.com/file/d/15lrcn5_Cn4g-kD165xGNLUGUGXtCptk-/view">
    <img src="https://img.shields.io/badge/UiPath-RPA_Developer-FA4616?style=for-the-badge&logo=uipath&logoColor=white" alt="UiPath RPA Developer Advanced" />
  </a>
</td>
<td width="20%" align="center">
  <a href="https://drive.google.com/file/d/15yLBx8nzlhn_PwrGoqQbumRG8zRQPC9t/view">
    <img src="https://img.shields.io/badge/BCS-Diploma_in_IT-234B9B?style=for-the-badge&logo=bcs&logoColor=white" alt="BCS Diploma in IT" />
  </a>
</td>
</tr>
</table>

<details>
<summary>More credentials</summary>

| Certification | Issued By |
|:---|:---|
| [Hugging Face AI Agents Course](https://drive.google.com/file/d/1NgSeIIF49Sqh2DAMY5KQEtnaddSc1Sqw/view) | Hugging Face |
| [BCS Certificate in IT](https://drive.google.com/file/d/160nzem63oIEv3EF9mCU9NGWwwA4NMdMZ/view) | BCS |

</details>

---

<div align="center">

The visual version is the [Idea Store](https://matthewpaver.github.io/MatthewPaver/store/): a browsable shelf of live products, private systems, public repos, and earlier prototypes.

<a href="https://matthewpaver.github.io/MatthewPaver/store/">
  <img src="https://img.shields.io/badge/Open_the_Idea_Store-D9A441?style=for-the-badge" alt="Open the Idea Store" />
</a>
<a href="https://www.linkedin.com/in/matthew-paver-534262166/">
  <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>

</div>
