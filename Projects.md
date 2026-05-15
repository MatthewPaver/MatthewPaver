# Project Index

Focused view of the systems, products, and experiments I build across AI, data, automation, and analytics.

[Back to Profile](README.md) | [Idea Store](https://matthewpaver.github.io/MatthewPaver/store/) | [Case Studies](CASE_STUDIES.md) | [Showcase Roadmap](SHOWCASE_ROADMAP.md) | [CV Evidence Log](CV_EVIDENCE_LOG.md)

For a browsable storefront view, open the [Idea Store](https://matthewpaver.github.io/MatthewPaver/store/).

All professional examples are intentionally anonymised and focused on engineering patterns rather than internal identifiers.

---

## Best Viewing Route

| Step | Open | Use it for |
|:---|:---|:---|
| 1 | [Idea Store](https://matthewpaver.github.io/MatthewPaver/store/) | Fast visual scan of the best work |
| 2 | This index | Compare status, signal, and repo links |
| 3 | [Case Studies](CASE_STUDIES.md) | Read the architecture and tradeoff story |
| 4 | Public repos | Inspect runnable code, docs, and outputs |

---

## Portfolio Snapshot

| Project | Status | Best signal | Link |
|:---|:---|:---|:---|
| Happening | Private system | 103 configured sources, daily ingestion, 167 tests | [Case study](CASE_STUDIES.md#happening) |
| Inference Brief | Live product | Editorial workflow + personalised reading product | [Live site](https://inferencebrief.co/) |
| AI Study Companion | Private product | Document AI + spaced repetition + async jobs | [Case study](CASE_STUDIES.md#ai-study-companion) |
| Smart Job Market Intelligence | Private system | Scraping, trend analysis, alerts, API tiering | [Case study](CASE_STUDIES.md#smart-job-market-intelligence) |
| QuickSupply | Private MVP | Multi-sided scheduling workflow + sequential assignment | Private |
| Operations Platform Prototype | Private prototype | Operations workflow + payment rails + AI triage pattern | Private |
| Marketing ML Lakehouse | Public runnable app | DuckDB medallion layers + XGBoost + Streamlit | [Repo](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| ProjectLens | Public runnable app | Schedule risk analysis + reporting outputs | [Repo](https://github.com/MatthewPaver/ProjectLens) |

---

## Flagship Systems

### Happening ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

- Deterministic event-ingestion platform across **103 venues**.
- Multi-strategy crawling, structured extraction, deduplication, and daily automation.
- Reliability-first approach with a **167-test** suite.

**Stack:** `Python` `Playwright` `SQLite` `Pydantic` `GitHub Actions`  
[Case study](CASE_STUDIES.md#happening)

### Inference Brief

- AI newsletter workflow plus personalised reading surface.
- Collection, filtering, scoring, summarisation, publishing, and subscription flows.
- Product includes bookmarks, reading history, and issue archive.

**Stack:** `Next.js` `TypeScript` `Supabase` `Python` `Stripe`  
[Live site](https://inferencebrief.co/) | [Case study](CASE_STUDIES.md#inference-brief)

### AI Study Companion ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

- Document-to-learning pipeline for flashcards, quizzes, and adaptive plans.
- Token-aware chunking, async generation jobs, and persistent review loops.
- Product boundaries include auth, tiers, rate limits, and export paths.

**Stack:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`  
[Case study](CASE_STUDIES.md#ai-study-companion)

### Smart Job Market Intelligence ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

- Job data ingestion and analytics system with trend and alerting workflows.
- Tracks salary ranges, skills, posting volume, and remote ratios.
- Built as a repeatable product surface rather than one-off analysis.

**Stack:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`  
[Case study](CASE_STUDIES.md#smart-job-market-intelligence)

---

## Public Repositories

### Product-Style Applications

| Project | Status | What to look for |
|:---|:---|:---|
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Runnable application | Bronze/silver/gold DuckDB flow, model training, Streamlit reporting |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Runnable application | Flask interface, schedule-risk pipeline, reporting outputs |
| [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) | Dashboard portfolio | Power BI dashboards, datasets, methodology, documentation |
| [AI Weekly](https://github.com/MatthewPaver/ai-weekly) | Archived output | Earlier newsletter surface later superseded by Inference Brief |

### ML, Data, and Streaming

| Project | Status | What to look for |
|:---|:---|:---|
| [Architexa](https://github.com/MatthewPaver/Architexa) | Completed portfolio project | Conditional GAN, dataset pipeline, Flask API |
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Notebook + CLI | Implicit feedback, temporal holdout, top-K recommendations |
| [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Notebook demo | Embeddings + cosine retrieval |
| [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Technical example | Structured Streaming consumer + Kafka producer |
| [Netflix Content Analysis](https://github.com/MatthewPaver/netflix-content-analysis) | Notebook EDA | Country, genre, and timeline analysis |

### Supporting Work

| Project | Status | What to look for |
|:---|:---|:---|
| [Generate Newsletter](https://github.com/MatthewPaver/generate-newsletter) | Archived prototype | Early collection-to-HTML newsletter pipeline |
| [Pinterest Image Scraper](https://github.com/MatthewPaver/pinterest-image-scraper) | Archived utility | Image collection helper tooling |
| [University of Liverpool](https://github.com/MatthewPaver/university-of-liverpool) | Coursework archive | Core CS and software engineering modules |

---

## Operational Stack (Cross-Project)

`Python` `TypeScript` `FastAPI` `n8n` `PostgreSQL` `Redis` `DuckDB` `Firebase` `GCP` `GitHub Actions` `Docker` `Supabase`

---

## Next Improvements

1. Add screenshots to `marketing-ml-lakehouse` and `Architexa`.
2. Add real `evaluate` and `recommend` CLI output to `dating-app-recommendation-system`.
3. Keep archived repo descriptions explicit about what replaced them.
4. Publish more private-system diagrams only when they are safe to share.
