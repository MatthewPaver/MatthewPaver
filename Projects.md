# Project Appendix

Reference map for the systems, products, and experiments I build across AI, data, automation, and analytics.

[Back to Profile](README.md) | [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) | [Case Studies](CASE_STUDIES.md) | [CV](CV.pdf)

For a first look, open the [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/). This page is deliberately more complete and more plain: it is here for comparison, repo links, and status.

All professional examples are intentionally anonymised and focused on engineering patterns rather than internal identifiers.

---

## Best Viewing Route

| Step | Open | Use it for |
|:---|:---|:---|
| 1 | [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) | Fast visual scan of the best work |
| 2 | This appendix | Compare status, signal, and repo links |
| 3 | [Case Studies](CASE_STUDIES.md) | Read the architecture and tradeoff story |
| 4 | Public repos | Inspect runnable code, docs, and outputs |

---

## Portfolio Snapshot

| Project | Status | Best signal | Link |
|:---|:---|:---|:---|
| MeetingProof | Live everyday work tool | Browser-local follow-up, exact source lines, human approval, tested LangGraph reference | [Use live](https://matthewpaver.github.io/MeetingProof/) · [Tutorial](https://matthewpaver.github.io/MeetingProof/tutorials/obsidian-claude-mcp.html) · [Repo](https://github.com/MatthewPaver/MeetingProof) |
| Can England Win It? | Live interactive experiment | 10,000 seeded simulations, explainable assumptions, shareable scenarios | [Play live](https://matthewpaver.github.io/can-england-win-it/) · [Case study](CASE_STUDIES.md#product-case-study-can-england-win-it) · [Repo](https://github.com/MatthewPaver/can-england-win-it) |
| Happening | Private system | 103 configured sources, daily ingestion, 167 tests | [Case study](CASE_STUDIES.md#happening) |
| AI Study Companion | Private product | Document AI + spaced repetition + async jobs | [Case study](CASE_STUDIES.md#ai-study-companion) |
| Smart Job Market Intelligence | Private system | Scraping, trend analysis, alerts, API tiering | [Case study](CASE_STUDIES.md#smart-job-market-intelligence) |
| QuickSupply | Private MVP | Multi-sided scheduling workflow + sequential assignment | Private |
| Operations Platform Prototype | Private prototype | Operations workflow + payment rails + AI triage pattern | Private |
| Marketing ML Lakehouse | Public runnable app | DuckDB medallion layers + XGBoost + Streamlit | [Repo](https://github.com/MatthewPaver/marketing-ml-lakehouse) |
| ProjectLens | Live project assurance | Browser-local XER comparison, three decision blockers, human decision record and approval-condition follow-up | [Use live](https://matthewpaver.github.io/ProjectLens/change-assurance.html) · [Repo](https://github.com/MatthewPaver/ProjectLens) |
| DecisionGraph | Live decision support | 16 comparable cases, inspectable evidence graph and human outcome feedback | [Use live](https://matthewpaver.github.io/DecisionGraph/) · [Repo](https://github.com/MatthewPaver/DecisionGraph) |

---

## Flagship Systems

### Can England Win It? ![Live](https://img.shields.io/badge/Live-0f766e?style=flat-square)

- Interactive World Cup probability game with a short matchday flow and detailed analyst controls.
- Ten thousand seeded simulations, visible assumptions, and a shareable URL for each scenario.
- Static React product with six model tests and automated GitHub Pages deployment.

**Stack:** `React` `TypeScript` `Vite` `Vitest` `GitHub Pages`

[Play live](https://matthewpaver.github.io/can-england-win-it/) | [Case study](CASE_STUDIES.md#product-case-study-can-england-win-it) | [Repo](https://github.com/MatthewPaver/can-england-win-it)

### Happening ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

- Deterministic event-ingestion platform across **103 venues**.
- Multi-strategy crawling, structured extraction, deduplication, and daily automation.
- Reliability-first approach with a **167-test** suite.

**Stack:** `Python` `Playwright` `SQLite` `Pydantic` `GitHub Actions`  
[Case study](CASE_STUDIES.md#happening)

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
| [MeetingProof](https://github.com/MatthewPaver/MeetingProof) | Live work tool | Browser-local product, LangGraph pause/resume, evidence verification, synthetic evaluations and safe MCP tutorial |
| [Can England Win It?](https://github.com/MatthewPaver/can-england-win-it) | Live interactive experiment | React interface, explainable Monte Carlo simulation, URL-based sharing, unit tests |
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Runnable application | Bronze/silver/gold DuckDB flow, model training, Streamlit reporting |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Live project assurance | Browser-local evidence comparison, decision blockers, human authority and approval conditions |
| [DecisionGraph](https://github.com/MatthewPaver/DecisionGraph) | Live decision support | Comparable-case retrieval, evidence graph and problem-to-outcome chain |
| [HR Performance Analytics](https://github.com/MatthewPaver/hr-performance-dashboards) | Dashboard portfolio | Power BI dashboards, datasets, methodology, documentation |
| [AI Weekly](https://github.com/MatthewPaver/ai-weekly) | Archived output | Earlier collection and newsletter interface |

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
