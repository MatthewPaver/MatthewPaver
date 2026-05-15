# Project Index

Curated view of the systems, products, and experiments I have been building across AI, data, automation, and analytics. Selected by representativeness, not age.

[Back to Profile](README.md) | [Case Studies](CASE_STUDIES.md)

For a browsable storefront view, open the [Idea Store](https://matthewpaver.github.io/MatthewPaver/store/).

---

## Portfolio Map

| Project | Status | Best signal | Link |
|:---|:---|:---|:---|
| Happening | Private system | 103 configured sources, daily event ingestion, 167 tests | [Case study](CASE_STUDIES.md#happening) |
| Inference Brief | Live product | AI briefing workflow plus personalized reading surface | [Live site](https://inferencebrief.co/) |
| AI Study Companion | Private product | Document AI, spaced repetition, async generation jobs | [Case study](CASE_STUDIES.md#ai-study-companion) |
| Smart Job Market Intelligence | Private system | Scraping, trend analysis, alerts, API-tier thinking | [Case study](CASE_STUDIES.md#smart-job-market-intelligence) |
| QuickSupply | Private MVP | Three-sided scheduling workflow with real-time sequential assignment | Private |
| Cadence | Private prototype | Enterprise block operations, payments, tickets, AI triage, governance docs | Private |
| Marketing ML Lakehouse | Public runnable app | DuckDB medallion layers, XGBoost models, Streamlit dashboard | [Repo](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| ProjectLens | Public runnable app | Schedule risk analysis with Flask and reporting outputs | [Repo](https://github.com/MatthewPaver/ProjectLens) |

---

## Flagship Systems

<table>
<tr>
<td width="50%" valign="top">

### Happening ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Event ingestion and normalisation platform covering **103 London venues**. Uses multi-strategy crawling, structured extraction, selector learning, deduplication, and daily automation. Built to run reliably rather than scrape once.

**Proof points:** 103 source configs, SQLite pipeline, daily scheduled runs, 167 tests

**Tech:** `Python` `Playwright` `SQLite` `Pydantic` `GitHub Actions`

[Case study](CASE_STUDIES.md#happening)

</td>
<td width="50%" valign="top">

### Inference Brief

AI newsletter platform and reading product. The stack combines a weekly editorial pipeline with a personalized web app, issue archive, bookmarks, reading history, topic preferences, and subscription flows.

**Proof points:** live product, personalized feed, issue archive, automated summarization and scoring

**Tech:** `Next.js` `TypeScript` `Supabase` `Python` `Stripe`

[Live site](https://inferencebrief.co/) | [Case study](CASE_STUDIES.md#inference-brief)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### AI Study Companion ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Study product that turns documents into flashcards, quizzes, and adaptive study plans. Includes parsing, token-aware chunking, spaced repetition, async generation jobs, billing boundaries, and support for local or hosted LLMs.

**Proof points:** document upload pipeline, SM-2 review loop, Stripe billing, voice features, multi-provider LLM support

**Tech:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

[Case study](CASE_STUDIES.md#ai-study-companion)

</td>
<td width="50%" valign="top">

### Smart Job Market Intelligence ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Job market analytics platform for tracking salary ranges, trending skills, posting volume, remote ratios, and alerting. Framed as a product with API tiers, billing hooks, and recurring analysis jobs.

**Proof points:** scraping plus analytics pipeline, alerting, trend reporting, rate-limited API design

**Tech:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

[Case study](CASE_STUDIES.md#smart-job-market-intelligence)

</td>
</tr>
</table>

---

## Public Repositories

### Additional Private Product Work

| Project | Status | What to look for |
|:---|:---|:---|
| QuickSupply | MVP application | School, teacher, and agency portals; sequential assignment engine; SSE updates; production hardening notes |
| Cadence | Product strategy prototype | UK block-operations workflows, resident clarity, Faster Payments-first flows, auditable tickets, AI triage, governance docs |

### Product-Style Applications

| Project | Status | What to look for |
|:---|:---|:---|
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Runnable application | Bronze/silver/gold DuckDB flow, model training, Streamlit reporting |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Runnable application | Flask interface, schedule-risk pipeline, Power BI-ready outputs |
| [AI Weekly](https://github.com/MatthewPaver/ai-weekly) | Archived output | Earlier newsletter publishing surface superseded by Inference Brief |
| [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) | Dashboard portfolio | Power BI dashboards, datasets, methodology, documentation |

### ML, Data, and Streaming

| Project | Status | What to look for |
|:---|:---|:---|
| [Architexa](https://github.com/MatthewPaver/Architexa) | Completed portfolio project | Conditional GAN, dataset pipeline, Flask API, trained model assets |
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Notebook project with CLI | Implicit feedback, temporal holdout, top-K recommendation lookup |
| [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Notebook demo | Transformer embeddings, cosine similarity, retrieval caveats |
| [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Technical example | Structured Streaming consumer, Kafka producer, Spark setup |
| [Netflix Content Analysis](https://github.com/MatthewPaver/netflix-content-analysis) | Notebook EDA | Country, genre, and timeline analysis in pandas and seaborn |

### Supporting Work

| Project | Status | What to look for |
|:---|:---|:---|
| [Generate Newsletter](https://github.com/MatthewPaver/generate-newsletter) | Archived prototype | Early collection-to-HTML newsletter pipeline before Inference Brief |
| [Pinterest Image Scraper](https://github.com/MatthewPaver/pinterest-image-scraper) | Archived utility | Image collection helper used as supporting data work for Architexa |
| [University of Liverpool](https://github.com/MatthewPaver/university-of-liverpool) | Coursework archive | Programming, algorithms, databases, distributed systems, software engineering |

---

## Next Improvements

These are the highest-signal upgrades still worth doing:

1. Add screenshots to `marketing-ml-lakehouse` and `Architexa`.
2. Add real `evaluate` and `recommend` CLI output to `dating-app-recommendation-system` after installing dependencies.
3. Update archived repo descriptions if you temporarily unarchive `ai-weekly`, `generate-newsletter`, or `pinterest-image-scraper`.
4. Package private-system screenshots or diagrams where they can be safely shared.

---

Private systems are summarised where source is not public. The profile README is the short version; this page is the structured portfolio map.
