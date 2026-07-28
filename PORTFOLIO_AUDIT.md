# Portfolio Audit

Last verified: 27 July 2026

This is the current disposition of the 35 repositories on this account. It
replaces the old generated `100/100` report: a portfolio audit is a judgement
record, not a score to optimise.

## Canonical product store

[matthewpaver.github.io](https://matthewpaver.github.io/) is the one public
entrance. It contains eight flagship products and three protected case studies.
The old `/MatthewPaver/store/` routes are retained only as `noindex` redirects.

### Flagships

| Product | Public handoff | Current boundary |
|:---|:---|:---|
| ProjectLens | Live browser example, source, tests, release | Decision support, not contractual analysis |
| MeetingProof | Live browser example, source, tests, release | Human approval remains mandatory |
| Output Gate | Live browser/CLI example, source, tests, release | Known assertions, not a general truth detector |
| DecisionGraph | Live browser example, source, tests, release | Synthetic cases; no invented organisational history |
| Marketing ML Lakehouse | Runnable local pipeline, source, tests, release | Synthetic sample data; no ad-platform credentials |
| Paper Trading | Reproducible research engine and draft release | Simulation only; no performance promise |
| Winchester Buyer Check | Live private-by-design calculator and release | Illustrative planning, not financial advice |
| Newco Assurance | Protected product boundary and private tested code | Method and customer-sensitive material remain private |

Cadence, QuickSupply and Happening are presented as case studies. They are not
dead-end “apps”: each page explains the problem, evidence, current boundary and
why the operating code is protected.

## Repository disposition

### Keep public and actively maintain

- The eight public-facing tool repositories named above, except the private
  Newco implementation.
- `happening-open-core` as the safe public schema and benchmark boundary.
- `hr-performance-dashboards` as a technical Power BI handoff, not an app.
- `pyspark-kafka-streaming` and `sentence-similarity-analysis` as supporting
  technical evidence. They are intentionally not featured products.
- `MatthewPaver` and `MatthewPaver.github.io` for profile routing and the
  canonical store.

### Keep private

- Commercial product systems: Newco Assurance, Inference Brief, Cadence,
  QuickSupply, full Happening and Winchester House.
- Coursework, private datasets, credentialed pipelines and experiments whose
  data or differentiation should not be redistributed.
- Architexa and the dating recommender: both carry dataset/licensing or
  commercial-boundary concerns that make a public showcase misleading.

### Archived with provenance retained

- `netflix-content-analysis`, `can-england-win-it`, `ai-weekly`,
  `generate-newsletter`, `pinterest-image-scraper`, `portfolio` and
  `hr-performance-portfolio`.
- Archived repositories may remain readable when they explain useful history,
  but they do not appear in the product store and should not receive scheduled
  maintenance workflows.

## Public-data decisions

Public data is useful only when its licence, update cycle and role in the
product are explicit. The best next integrations are:

| Repository | Candidate | Useful for | Guardrail |
|:---|:---|:---|:---|
| ProjectLens / DecisionGraph | [NISTA major-project data](https://www.gov.uk/government/collections/major-projects-data) | External benchmark fixtures for portfolio cost, confidence and delivery patterns | Do not invent task-level schedules, decisions or causality that the source does not contain |
| Winchester House | [HM Land Registry Price Paid Data and UK HPI](https://www.gov.uk/government/publications/hm-land-registry-data/public-data) | Local sale-price context and transparent comparables | Keep the integration private until address-data reuse, attribution and product terms are settled |
| HR Performance Dashboards | [ONS sickness-absence data](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/sicknessabsenceinthelabourmarket) | An external UK benchmark beside internal absence measures | Label population/method changes and never compare unlike periods silently |
| Happening | [London cultural-infrastructure data](https://data.london.gov.uk/) | Venue seed coverage and source-completeness checks | Treat it as a benchmark, not a replacement for current event evidence |

MeetingProof and Output Gate should continue to use synthetic regression cases:
public corpora would add little while making privacy and expected-answer
boundaries harder to explain. Marketing ML Lakehouse should retain a generated
sample by default. Paper Trading should retain hashed, reproducible market-data
provenance and must not package fixture results as real returns.

When one of the candidates is implemented, prefer a small fetch/normalise
script, source URL, licence note, retrieval date and content hash over committing
an opaque bulk download.

## GitHub Actions policy

- Product repositories: lint, tests, build, dependency/security audit and one
  meaningful browser smoke path on pull requests.
- Deployed products: a small scheduled production-health check.
- Data products: scheduled ingestion only where data genuinely changes, plus
  freshness/source-health checks. Generation, deployment and source health
  remain separate when they fail for different reasons.
- Static evidence repositories: validate on change; do not run expensive
  mutation, scrape or browser jobs on a schedule without a maintained threshold
  and an owner.
- Archived repositories: no scheduled workflows.

This keeps Actions as product evidence rather than activity theatre.

## Packaging for non-technical users

- Browser tools are the preferred executable: they need no install and can keep
  sensitive inputs local.
- GitHub Releases provide a stable versioned download for the flagship public
  repositories.
- A desktop executable is worthwhile only where the user needs offline file
  access or a long-running local process. It would add signing, update and
  malware-warning support obligations, so it is not a useful wrapper for every
  notebook, data pipeline or static site.

## Commercial boundary

Do not place the whole portfolio in the public domain. MIT is appropriate for
the small reusable public tools; it does not protect the product name or create
a warranty. Keep customer workflows, private datasets, scoring methods,
credentialed collectors and operating advantages private. Winchester Buyer
Check remains publicly viewable with copyright retained rather than being
silently open-sourced.

GitHub Pages is appropriate for the public static catalogue and browser demos.
Commercial SaaS, authentication, sensitive transactions and paid product
workflows belong on dedicated hosting.

