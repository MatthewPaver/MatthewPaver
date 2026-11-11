# Portfolio evidence register

Last verified: 11 November 2026

This replaces the 27 July 2026 disposition list. It is a dated register of what the public entrance currently claims, not a scorecard to optimise.

## One public entrance

[matthewpaver.github.io](https://matthewpaver.github.io/) is the store. Profile README and repository About text should match the same For / Job / Evidence / Limits pattern.

## Front door (inspectable prototypes)

| Product | Who for | Measured evidence on the page | Boundary |
|:---|:---|:---|:---|
| RAG Regression Gate | Engineers checking search updates for staff assistants | Saved CLI comparisons; pass means “not worse”, not “answers are good” | Browser is a saved run, not a live re-score |
| Marketing ML Lakehouse | Analysts rebuilding campaign tables | Model does not beat persistence beyond noise on sample data | Synthetic sample; no ad-platform credentials |
| Winchester Buyer Check | First-time buyers planning an offer | HMLR Winchester snapshot + dated GOV.UK rules | Nine homes are made-up; no AI; not advice |
| PolicyLens | Cloud reviewers comparing IAM policy versions | Set 5 **21/30**; false pass `PLH5-A21` (MFA-less trust) published | Not whole-account; Pass ≠ approval |
| ProjectLens | Project reviewers checking updates vs dates | Set 5 **29/40**; contradiction class **3/10** | Misses contradictions; no causation/entitlement |

## Support / case study

| Product | Role |
|:---|:---|
| QuickSupply | Recorded fictional booking prototype, not a live service |
| recommender-eval-lab | Teaching fixture on planted synthetic preferences |
| pyspark-kafka-streaming | Local streaming examples |
| hr-performance-dashboards | AdventureWorks Power BI case study |

## Private (not public proof)

Commercial and personal systems stay private. Public pages must not imply they are live customer products. Do not list private venture names on the homepage.

## Archived names no longer front door

Output Gate, DecisionGraph, Paper Trading, Can England Win It? and similar archived experiments may remain readable where useful. They are not current flagships.

## How to read a card

1. **For** — the person and decision  
2. **Job** — what they give the tool and what comes back  
3. **Evidence** — linked example, measured result, important failure  
4. **Limits** — what is unproved; who decides  
5. **Next** — one accurately labelled action  

## Verification habit

When claims change, update this file’s date, the homepage cards and the repository READMEs in the same change. Seen regression sets and held-out fixtures must not be described as “pending” if the files are in the tree.
