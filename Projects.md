# Project Index

<div align="center">

Curated view of the systems, products, and experiments I have been building across AI, data, automation, and analytics. Selected by representativeness, not age.

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

<table>
<tr>
<td width="50%" valign="top">

#### Marketing ML Lakehouse

Local-first marketing analytics lakehouse with DuckDB medallion layers, XGBoost forecasting and conversion models, and a Streamlit dashboard for analysis and commentary.

`Python` `DuckDB` `XGBoost` `Streamlit` `Polars`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/marketing-ml-lakehouse)

</td>
<td width="50%" valign="top">

#### ProjectLens

Web app and backend analysis pipeline for project schedules. Surfaces slippage, forecasting issues, milestone risks, and delivery insights from uploaded data.

`Python` `Flask` `pandas` `Analytics` `Forecasting`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/ProjectLens)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### AI Weekly

Public AI newsletter repository and site that curates tools, research, and trends. Complements the more recent Inference Brief product work.

`Python` `GitHub Actions` `RSS` `Jinja2` `Publishing`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/ai-weekly) [![Read Newsletter](https://img.shields.io/badge/Read_Newsletter-00D9FF?style=flat-square)](https://matthewpaver.github.io/ai-weekly/)

</td>
<td width="50%" valign="top">

#### HR Performance Analytics

Power BI dashboards for HR performance reporting and sales analysis, with datasets, documentation, and walkthrough material.

`Power BI` `Excel` `CSV` `Dashboarding` `Documentation`

[![Dashboards](https://img.shields.io/badge/Dashboards-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/hr-performance-dashboards) [![Portfolio](https://img.shields.io/badge/Portfolio-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/hr-performance-portfolio)

</td>
</tr>
</table>

---

### ML and data projects

<table>
<tr>
<td width="50%" valign="top">

#### Architexa

Architectural image generation built with a conditional GAN and exposed through a Flask API. Produces outputs across nine architectural styles.

`Python` `TensorFlow` `Keras` `Flask` `CGAN`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/Architexa) [![Live Site](https://img.shields.io/badge/Live_Site-00D9FF?style=flat-square)](https://architexa.io)

</td>
<td width="50%" valign="top">

#### Dating App Recommendation System

Recommendation engine for swipe-based apps using implicit-feedback matrix factorisation, framed around practical ranking quality and user matching.

`Python` `NumPy` `SciPy` `Recommendation Systems`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/dating-app-recommendation-system)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Sentence Similarity Analysis

NLP project exploring semantic similarity with transformer embeddings and cosine similarity across factual statements.

`Python` `sentence-transformers` `PyTorch` `NLP`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/sentence-similarity-analysis)

</td>
<td width="50%" valign="top">

#### PySpark Kafka Streaming

Streaming examples combining PySpark Structured Streaming with Kafka producers and consumers for real-time processing demos.

`Python` `PySpark` `Kafka` `Streaming`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/pyspark-kafka-streaming)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Netflix Content Analysis

Exploratory data analysis of the Netflix catalogue using pandas, matplotlib, and seaborn, with trend analysis across genre, geography, and release timelines.

`Python` `pandas` `Matplotlib` `Seaborn` `Colab`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/netflix-content-analysis) [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1WsnSnIngH8xNdBNBWeJgJbKD2uMilVdS?usp=sharing)

</td>
<td></td>
</tr>
</table>

---

### Automation and supporting work

<table>
<tr>
<td width="50%" valign="top">

#### Generate Newsletter

Earlier newsletter-generation prototype that scrapes stories and renders HTML issues through a Python pipeline.

`Python` `HTML` `Automation` `Newsletter`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/generate-newsletter)

</td>
<td width="50%" valign="top">

#### Pinterest Image Scraper

Automation utility for collecting Pinterest images with duplicate detection, multithreading, and proxy support.

`Python` `Web Scraping` `Image Processing`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/pinterest-image-scraper)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### University of Liverpool

Coursework and study repository covering the technical foundation behind the later project work: programming, algorithms, databases, distributed systems, and software engineering.

`Python` `Java` `C++` `Haskell` `SQL`

[![View Repo](https://img.shields.io/badge/View_Repo-0078D4?style=flat-square&logo=github&logoColor=white)](https://github.com/MatthewPaver/university-of-liverpool)

</td>
<td></td>
</tr>
</table>

---

<div align="center">

Private systems are summarised even where source is not public. The profile README is the short version — this page is the fuller view.

</div>
