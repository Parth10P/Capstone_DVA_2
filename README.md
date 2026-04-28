> Newton School of Technology | Data Visualization & Analytics
> Capstone 2 — Industry Simulation

---

| Field | Details |
|---|---|
| **Project Title** | Online Retail Sales Analytics |
| **Team Name** | Phantom |
| **Sector** | Retail & E-commerce |
| **Team ID** | _Fill in_ |
| **Section** | _Fill in_ |
| **Faculty Mentor** | _Fill in_ |
| **Institute** | Newton School of Technology |
| **Submission Date** | _Fill in_ |

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead & Tableau | Parth Patel | `Parth10P` |
| Data Sourcing Lead | Harikrushn Patel | `harikrushnpatel` |
| ETL & Cleaning Lead | Khush Chaudhari | `handle` |
| EDA Lead | AN Pavan Sai | `handle` |
| Statistical Analysis Lead | Aryaman Jyoti | `handle` |

---

## Business Problem

The UK-based online retailer sells unique gift-ware across 38 countries. The business lacks clear visibility into which customer segments are most valuable, where cancellations are hurting revenue, and which international markets deserve more marketing investment.

**Core Business Question**

> How can we identify the highest-value customer segments, reduce cancellation losses, and optimize inventory and marketing spend to grow annual revenue?

**Decision Supported**

> Operations and marketing teams can use this analysis to prioritize stock replenishment, run targeted re-engagement campaigns, and allocate ad spend to the most profitable markets.

---

## Dataset

| Attribute | Details |
|---|---|
| Source | UCI Machine Learning Repository |
| Link | https://archive.ics.uci.edu/dataset/352/online+retail |
| Rows | 541,909 raw → 531,522 after cleaning |
| Columns | 8 original → 28 after feature engineering |
| Period | December 2010 to December 2011 |
| Format | Excel (.xlsx) |

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for full column definitions.

---

## KPI Framework

| KPI | Formula |
|---|---|
| Total Revenue | SUM(TotalRevenue) where IsCancelled = False |
| Avg Order Value | Total Revenue / Unique InvoiceNo count |
| Cancellation Rate | COUNT(IsCancelled=True) / COUNT(all rows) × 100 |
| Repeat Customer Rate | COUNT(Repeat customers) / COUNT(all customers) |
| RFM Score | R + F + M scores combined (1-4 each) |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| Dashboard URL | _Fill in after publishing_ |
| Filters | Year, Quarter, Country, CustomerSegment, BasketSize |

Screenshots in [`tableau/screenshots/`](tableau/screenshots/)
Links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md)

---

## Key Insights

1. Total revenue: £10.27M from 531,522 transactions
2. UK accounts for ~83% of all revenue
3. November 2011 was the peak revenue month
4. Champions and Loyal Customers drive disproportionate revenue
5. Cancellation rate is 1.66% — small but measurable revenue loss
6. Thursday is the highest-revenue weekday
7. Afternoon (12–5 PM) is the peak shopping window
8. Large basket orders (> £200) generate outsized revenue per transaction

---

## Recommendations

| # | Recommendation | Expected Impact |
|---|---|---|
| 1 | Pre-October inventory build-up for peak season | +10–15% peak revenue |
| 2 | Win-back email campaign for At-Risk customers | Recover 5–10% churned revenue |
| 3 | Increase ad spend in top 5 non-UK markets | +8–12% international revenue |
| 4 | Thursday afternoon flash sale notifications | +5–8% conversion rate |
| 5 | Loyalty tier for Large basket customers | +15% repeat large orders |

---

## Repository Structure

```
Capstone_DVA_2/
├── README.md
├── data/
│   ├── raw/                  # original unedited dataset
│   └── processed/            # cleaned output + tableau CSVs
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py
├── tableau/
│   ├── dashboard_links.md
│   └── screenshots/
├── reports/
│   ├── README.md
│   ├── project_report_template.md
│   └── presentation_outline.md
└── docs/
    └── data_dictionary.md
```

---

## Contribution Matrix

| Member | Dataset & Sourcing | ETL & Cleaning | EDA | Statistical Analysis | Tableau Dashboard | Report & PPT |
|---|---|---|---|---|---|---|
| Harikrushn Patel | Owner | Support | Support | Support | Support | Support |
| Khush Chaudhari | Support | Owner | Support | Support | Support | Support |
| AN Pavan Sai | Support | Support | Owner | Support | Support | Support |
| Aryaman Jyoti | Support | Support | Support | Owner | Support | Support |
| Parth Patel | Support | Support | Support | Support | Owner | Owner |

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*