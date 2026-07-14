# Case Studies

Product and engineering notes from selected builds across automation, data, AI, and analytics.

[Back to Profile](README.md) | [Portfolio Store](https://matthewpaver.github.io/MatthewPaver/store/) | [Project Appendix](Projects.md)

Private and professional examples are anonymised. Public builds link to the working product and source.

---

## How To Read These

Start with the project that matches what you want to inspect. Each note covers the problem, decisions, tradeoffs, result, and implementation.

| Case study | Best signal |
|:---|:---|
| [Can England Win It?](#product-case-study-can-england-win-it) | Public product design, explainable simulation, and shareable scenarios |
| [Featured Build: Happening](#featured-build-happening) | Reliable ingestion from fragmented public web sources |
| [AI Study Companion](#ai-study-companion) | Document AI, async jobs, and adaptive learning loops |
| [Smart Job Market Intelligence](#smart-job-market-intelligence) | Repeatable market intelligence product from scraped listings |

---

## Product Case Study: Can England Win It?

**Type:** Live public product

[Open product](https://matthewpaver.github.io/can-england-win-it/) | [Inspect source](https://github.com/MatthewPaver/can-england-win-it)

### Problem

Tournament probabilities usually arrive as a single percentage. That number is hard to question because the assumptions sit somewhere else, if they are published at all. I wanted to make the probability explorable without turning the experience into a spreadsheet.

### Product Decisions

- **Start with three matchday choices.** A short path gets someone to a result quickly. Analyst mode keeps the four detailed controls available without making them the front door.
- **Show the model boundary.** The app labels its ratings and player boosts as illustrative. It describes the result as a scenario, not a forecast or betting claim.
- **Keep the calculation in the browser.** The static build has no account, database, or backend dependency. Anyone can open it from GitHub Pages and run the same model.
- **Make every result repeatable.** A seeded simulation gives the same output for the same inputs. The URL carries the scenario so another person can open and challenge it.
- **Give the result a proper finish.** A full-screen tournament sequence turns the calculation into a product moment, then returns to the probability, range, and assumptions.

### Trade-offs

The team ratings in `src/model.ts` are isolated and replaceable, but they are not a live forecasting feed. The player choice adds an entertainment boost rather than a measured player statistic. Those limits keep the product honest, though they also mean the result cannot claim predictive accuracy.

Ten thousand runs give a stable result while keeping the simulation immediate on a phone or laptop. A seeded generator reduces random variation between visits, which helps sharing and testing, but it also means rerunning an unchanged scenario will not produce a fresh sample.

### Result

The shipped product runs **10,000 tournament simulations** for each scenario, exposes a central estimate and illustrative range, and supports shareable URLs. It has a responsive, keyboard-friendly interface, six simulation tests, and an automated GitHub Pages deployment.

```mermaid
flowchart LR
    A["Matchday choices or analyst controls"] --> B["England rating adjustment"]
    B --> C["Elo-style match probabilities"]
    C --> D["Seeded Monte Carlo tournament"]
    D --> E["Central estimate and model range"]
    E --> F["Result screen and shareable URL"]
```

**Stack:** `React` `TypeScript` `Vite` `Vitest` `GitHub Pages`

---

## Featured Build: Happening

**Problem:** London event data looks simple from the outside, but the source material is messy: venue pages change structure, dates and prices are inconsistent, images go missing, and the same event can appear in more than one place.

**Constraints:** the system needed to handle many public sources without exposing private operational details, stay cheap to run, make failures visible, and let new sources be added without rewriting the pipeline each time.

**Decisions:** I treated each venue as an explicit source configuration, separated crawling from extraction and normalisation, kept SQLite as the reliable local store, and made source quality visible through checks rather than hiding scrape failures in logs.

**Tradeoffs:** deterministic rules are less glamorous than an all-LLM scraper, but they are easier to debug, test, and operate. Playwright is heavier than plain HTTP, but it handles modern venue sites that render useful content client-side.

**Result:** the system maps **103+ venue sources** into structured event data, with dedupe, validation, source-level quality checks, and a **167-test** reliability suite. The important part is not just collecting events; it is knowing when the data path is healthy.

**Stack:** `Python` `Playwright` `SQLite` `Pydantic` `Next.js`

---

## Happening

**Type:** Private system  
**Problem:** Event listings are fragmented across many sites with inconsistent formats and update patterns.  
**Goal:** Build a repeatable daily ingestion system with reliable normalisation and storage.

### What I Built

- Source configuration for **103 venues**
- Multi-strategy crawling with Playwright-backed extraction
- Structured validation using Pydantic-style schemas
- Deduplication and normalisation before SQLite persistence
- Daily automation workflow
- **167-test** suite covering adapters and pipeline reliability

```mermaid
flowchart LR
    A["Venue source configs"] --> B["Crawler strategy"]
    B --> C["Extraction and parsing"]
    C --> D["Validation"]
    D --> E["Deduplication"]
    E --> F["SQLite event store"]
    F --> G["Daily automation"]
    G --> H["Quality checks"]
    H --> A
```

**Engineering signal:** reliability, explicit source behaviour, and safe iteration under test coverage.  
**Stack:** `Python` `Playwright` `SQLite` `Pydantic` `GitHub Actions`

---

## AI Study Companion

**Type:** Private product  
**Problem:** Learners have long documents but weak active-recall workflows.  
**Goal:** Convert documents into flashcards, quizzes, and adaptive study plans.

### What I Built

- PDF, DOCX, and text ingestion paths
- Token-aware chunking before LLM generation
- Flashcard, quiz, and study-plan generation
- SM-2 style spaced-repetition loop
- Async generation jobs
- Auth, tiers, rate limits, billing boundaries, and export paths
- Local or hosted LLM provider support

```mermaid
flowchart LR
    A["Uploaded document"] --> B["Parse text"]
    B --> C["Chunk by token budget"]
    C --> D["Generate cards and quizzes"]
    D --> E["Review session"]
    E --> F["Spaced repetition state"]
    F --> G["Adaptive study plan"]
    G --> E
```

**Engineering signal:** product-grade pipeline design, not just prompt orchestration.  
**Stack:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

---

## Smart Job Market Intelligence

**Type:** Private system  
**Problem:** Job posting data is high-volume, messy, and constantly changing.  
**Goal:** Build a repeatable intelligence product for trends, insights, and alerting.

### What I Built

- Scraping and ingestion layer for listings
- Salary and skill trend analysis
- Posting volume and remote-ratio tracking
- Alerting workflows
- API surface with tier and rate-limit design
- Background processing architecture

```mermaid
flowchart LR
    A["Job listings"] --> B["Scrapers"]
    B --> C["Normalization"]
    C --> D["Postgres"]
    D --> E["Salary and skill analysis"]
    E --> F["Reports and alerts"]
    D --> G["API tier surface"]
```

**Engineering signal:** repeatable data-product architecture over one-off analysis.  
**Stack:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

---

## Public Portfolio Notes

Public repositories back up the same themes:

| Repo | Portfolio role |
|:---|:---|
| [Marketing ML Lakehouse](https://github.com/MatthewPaver/marketing-ml-lakehouse) | Data engineering + ML workflow |
| [ProjectLens](https://github.com/MatthewPaver/ProjectLens) | Analytics application + project-risk reporting |
| [Architexa](https://github.com/MatthewPaver/Architexa) | Model training + image generation + API integration |
| [Dating App Recommendation System](https://github.com/MatthewPaver/dating-app-recommendation-system) | Practical recommendation modelling |
| [Sentence Similarity Analysis](https://github.com/MatthewPaver/sentence-similarity-analysis) | Embedding-based retrieval patterns |
| [PySpark Kafka Streaming](https://github.com/MatthewPaver/pyspark-kafka-streaming) | Streaming data foundations |
