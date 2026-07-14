# Portfolio App Ideas

These are ideas that fit the current portfolio: automation, data systems, AI quality, and practical workflows. The goal is not to add more projects for the sake of volume. Each idea should make the app store sharper.

## Best Next Builds

| Idea | Why it fits | Portfolio signal | Suggested scope |
|:---|:---|:---|:---|
| Automation Control Tower | Central dashboard for scheduled jobs, failures, retries, owners, and evidence logs. | Strong automation-specialist signal; connects to Happening, QuickSupply, and evaluator work. | One local app with demo jobs, run history, failure reasons, and handoff notes. |
| Data Quality Command Centre | Dataset checks, schema drift, anomaly alerts, freshness checks, and plain-English issue summaries. | Strong enterprise data-engineering signal. | DuckDB-backed demo with failing/passing sample datasets and a quality timeline. |
| Ops Handoff Generator | Converts messy notes, tickets, emails, and status updates into a clean shift/handoff brief. | Very aligned with automation and operational tooling. | Upload/paste notes, classify issues, produce handoff, risk list, and follow-up tasks. |
| Market Signal Monitor | Public demo version of Smart Job Market Intelligence for one narrow sector. | Makes the private job-market system visible without exposing private code. | Use demo data, trend cards, anomaly notes, and weekly brief output. |

## Smaller Useful Builds

| Idea | Why it is useful | Keep it small by |
|:---|:---|:---|
| README Quality Gate | Checks repo READMEs for run command, tests, screenshot, architecture, limitations, and overused phrases. | Running against local repos and producing a markdown report. |
| Screenshot QA Tool | Checks portfolio thumbnails for missing assets, aspect ratio, file size, contrast notes, and preview coverage. | Starting with file checks and a manual review checklist. |
| Source Reliability Scorecard | Tracks crawler/source health, parse failures, freshness, and confidence over time. | Using fixture data rather than a full crawler. |
| Workflow Cost Tracker | Estimates AI/API/job cost per workflow, with budget alerts and run history. | Using seeded events and simple cost rules. |

## What I Would Avoid For Now

- Another generic chat assistant.
- A broad job-board scraper without a narrow decision workflow.
- A large multi-agent demo where the agents do not change the outcome.
- More dashboards unless they have a clear user decision attached.

## Recommended First Choice

Build **Automation Control Tower** next.

It is the clearest extension of the current portfolio because it connects automation, reliability, scheduled jobs, operational handoff, and quality checks. It would make the app store feel less like separate projects and more like a coherent body of work.
