# Project Index

<div align="center">

Curated view of the systems, products, and experiments I have been building across AI, data, automation, and analytics. This is selective rather than exhaustive.

[Back to Profile](https://github.com/MatthewPaver/MatthewPaver)

</div>

---

## Current Systems

These are the projects that best reflect the direction of my recent work. Some are private, but they are included here because they represent the strongest examples of how I build. Details are available on request where appropriate.

<table>
<tr>
<td width="50%" valign="top">

### Happening ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Event ingestion and normalisation platform covering **103 London venues**. Uses multi-strategy crawling, structured extraction, selector learning, deduplication, and daily automation. Built to run reliably rather than just scrape once.

**Highlights:** 103 source configs, SQLite pipeline, daily scheduled runs, 167 tests

**Tech:** `Python` `Playwright` `SQLite` `Pydantic` `GitHub Actions`

</td>
<td width="50%" valign="top">

### AI Study Companion ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Study product that turns documents into flashcards, quizzes, and adaptive study plans. Includes PDF parsing, token-aware chunking, spaced repetition, async generation jobs, billing, and support for local or hosted LLMs.

**Highlights:** document upload pipeline, SM-2 review loop, Stripe billing, voice features, multi-provider LLM support

**Tech:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Inference Brief

AI newsletter platform and reading product. The stack combines a weekly editorial pipeline with a personalised web app, issue archive, bookmarks, reading history, topic preferences, and subscription flows.

**Highlights:** live publication workflow, personalised feed, search, issue archive, automated summarisation and scoring

**Tech:** `Next.js` `TypeScript` `Supabase` `Python` `Stripe`

[![Live Site](https://img.shields.io/badge/Live_Site-00D9FF?style=flat-square)](https://inferencebrief.co/)

</td>
<td width="50%" valign="top">

### Smart Job Market Intelligence ![Private](https://img.shields.io/badge/Private-grey?style=flat-square&logo=lock&logoColor=white)

Job market analytics platform for tracking salary ranges, trending skills, posting volume, remote ratios, and alerting. Framed as a product with API tiers, billing hooks, and recurring analysis jobs.

**Highlights:** scraping plus analytics pipeline, alerting, trend reporting, rate-limited API design

**Tech:** `Python` `FastAPI` `PostgreSQL` `Redis` `Celery`

</td>
</tr>
</table>

---

## Selected Public Repositories

### Production-style applications

#### Marketing ML Lakehouse

Local-first marketing analytics lakehouse with DuckDB medallion layers, XGBoost forecasting and conversion models, and a Streamlit dashboard for analysis and commentary.

`Python` `DuckDB` `XGBoost` `Streamlit` `Polars`

[View Repository](https://github.com/MatthewPaver/marketing-ml-lakehouse)

#### ProjectLens

Web app and backend analysis pipeline for project schedules. Designed to surface slippage, forecasting issues, milestone risks, and delivery insights from uploaded data.

`Python` `Flask` `pandas` `Analytics` `Forecasting`

[View Repository](https://github.com/MatthewPaver/ProjectLens)

#### AI Weekly

Public AI newsletter repository and site that curates tools, research, and trends. Complements the more recent Inference Brief product work.

`Python` `GitHub Actions` `RSS` `Jinja2` `Publishing`

[View Repository](https://github.com/MatthewPaver/ai-weekly) | [Read Newsletter](https://matthewpaver.github.io/ai-weekly/)

#### HR Performance Dashboards

Power BI implementation repo containing dashboard files, datasets, screenshots, and supporting material for HR performance reporting and sales analysis.

`Power BI` `Excel` `CSV` `Dashboarding`

[View Repository](https://github.com/MatthewPaver/hr-performance-dashboards)

#### HR Performance Portfolio

Companion portfolio repo with the write-up, presentation material, and walkthrough content for the HR analytics project.

`Power BI` `Documentation` `Portfolio`

[View Repository](https://github.com/MatthewPaver/hr-performance-portfolio)

---

### ML and data projects

#### Architexa

Architectural image generation project built with a conditional GAN and exposed through a Flask API. Produces outputs across nine architectural styles.

`Python` `TensorFlow` `Keras` `Flask` `CGAN`

[View Repository](https://github.com/MatthewPaver/Architexa) | [Live Site](https://architexa.io)

#### Dating App Recommendation System

Recommendation engine for swipe-based apps using implicit-feedback matrix factorisation, framed around practical ranking quality and user matching.

`Python` `NumPy` `SciPy` `Recommendation Systems`

[View Repository](https://github.com/MatthewPaver/dating-app-recommendation-system)

#### Sentence Similarity Analysis

NLP project exploring semantic similarity with transformer embeddings and cosine similarity across factual statements.

`Python` `sentence-transformers` `PyTorch` `NLP`

[View Repository](https://github.com/MatthewPaver/sentence-similarity-analysis)

#### PySpark Kafka Streaming

Streaming examples that combine PySpark Structured Streaming with Kafka producers and consumers for real-time processing demos.

`Python` `PySpark` `Kafka` `Streaming`

[View Repository](https://github.com/MatthewPaver/pyspark-kafka-streaming)

#### Netflix Content Analysis

Exploratory data analysis of the Netflix catalogue using pandas, matplotlib, and seaborn, with trend analysis across genre, geography, and release timelines.

`Python` `pandas` `Matplotlib` `Seaborn` `Colab`

[View Repository](https://github.com/MatthewPaver/netflix-content-analysis) | [Open in Colab](https://colab.research.google.com/drive/1WsnSnIngH8xNdBNBWeJgJbKD2uMilVdS?usp=sharing)

---

### Automation and supporting work

#### Generate Newsletter

Earlier newsletter-generation prototype that scrapes stories and renders HTML issues through a Python pipeline.

`Python` `HTML` `Automation` `Newsletter`

[View Repository](https://github.com/MatthewPaver/generate-newsletter)

#### Pinterest Image Scraper

Automation utility for collecting Pinterest images with duplicate detection, multithreading, and proxy support.

`Python` `Web Scraping` `Image Processing`

[View Repository](https://github.com/MatthewPaver/pinterest-image-scraper)

#### University of Liverpool

Coursework and study repository covering the technical foundation behind the later project work: programming, algorithms, databases, distributed systems, and software engineering.

`Python` `Java` `C++` `Haskell` `SQL`

[View Repository](https://github.com/MatthewPaver/university-of-liverpool)

---

## Notes

- Selected private systems are summarised here even where source is not public.
- Public repositories are ordered by how representative they feel, not by age.
- The profile README is the short version. This page is the fuller view.
