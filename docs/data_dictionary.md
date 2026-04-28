# Data Dictionary

## Dataset Summary

| Item | Details |
|---|---|
| Dataset | Online Retail |
| Source | UCI Machine Learning Repository |
| File | Online Retail.xlsx |
| Granularity | One row per product per transaction |
| Raw rows | 541,909 |
| Cleaned rows | 531,522 |

## Original Columns

| Column | Type | Description | Cleaning Applied |
|---|---|---|---|
| InvoiceNo | string | Transaction ID. Starts with C = cancellation | Used to flag IsCancelled |
| StockCode | string | Product code | No changes |
| Description | string | Product name | Filled nulls with Unknown, removed junk entries |
| Quantity | int | Units per line item | Dropped corrupt negatives (non-cancellation rows) |
| InvoiceDate | datetime | Date and time of transaction | Parsed to extract time-based features |
| UnitPrice | float | Price per unit in GBP | Dropped zero/negative price rows |
| CustomerID | string | Customer identifier | Filled 135k nulls with Guest |
| Country | string | Customer country | No changes |

## Derived Columns

| Column | Logic | Purpose |
|---|---|---|
| TotalRevenue | Quantity × UnitPrice | Revenue per line item |
| IsCancelled | InvoiceNo starts with C | Cancellation flag for KPI |
| InvoiceYearMonth | YYYY-MM from date | Monthly trend grouping |
| MonthName | Month name from date | Readable month label |
| MonthNumber | Month number 1-12 | Correct sorting in Tableau |
| Year | Year from date | Year-over-year comparison |
| Quarter | Q1-Q4 from date | Quarterly breakdown |
| DayOfWeek | Day name from date | Weekly pattern analysis |
| Hour | Hour 0-23 from date | Hourly pattern analysis |
| TimeOfDay | Morning/Afternoon/Evening/Night | Shopping window buckets |
| IsUK | UK or International | Geographic segmentation |
| BasketSize | Small/Medium/Large by invoice total | Order tier analysis |
| ItemsPerOrder | Total quantity per invoice | Basket depth |
| AvgOrderValue | Total spend / order count per customer | Customer spend metric |
| IsRepeatCustomer | Repeat / One-Time / Guest | Retention analysis |
| Recency | Days since last purchase | RFM dimension |
| Frequency | Unique orders per customer | RFM dimension |
| Monetary | Total spend per customer | RFM dimension |
| RFM_Score | R+F+M scores combined | Customer health score |
| CustomerSegment | Champion/Loyal/At Risk/Lost etc | Business segment label |

## Data Quality Notes

- 135,080 rows had no CustomerID. Kept as Guest to preserve revenue data.
- 5,268 exact duplicate rows removed.
- 8,807 cancellation rows flagged but kept for cancellation rate KPI.
- 2,620 system/internal rows removed (postage, fees, manual entries).
- 2,517 rows with zero or negative price removed.
- Dataset covers Dec 2010 to Dec 2011 only.
