---
name: business-data-analyst
description: Performs deep technical analysis on raw business data using Python. Use when user provides datasets (Excel, CSV, Sheets) and asks for correlations, anomalies, or statistical insights.
---

# Business Data Analyst

## When to use this skill
- User uploads raw data files (CSV, Excel) and asks "What does this say?"
- User asks for specific statistical analysis (correlation, regression, forecasting).
- User wants to find "anomalies" or "reasons for decline/growth" in numbers.
- User needs to clean or transform complex datasets.

## Core Principles
1.  **Code First**: Always write and execute Python code to analyze data. Do not guess.
2.  **Verify Data**: Check for missing values, wrong data types, and outliers first.
3.  **Cross-Validation**: Don't rely on one metric. Compare multiple timeframes or dimensions.

## Workflow

### Phase 1: Ingestion & Inspection
```python
# Standard inspection routine
import pandas as pd
df = pd.read_csv('data.csv') # or read_excel
print(df.info())
print(df.head())
print(df.describe())
```
*Goal: Understand structure, types, and data quality.*

### Phase 2: Exploratory Data Analysis (EDA)
- **Trend Analysis**: Group by date/time. `df.groupby('date')['revenue'].sum()`
- **Distribution**: Check histograms of key metrics.
- **Segmentation**: Group by Category, Store, or Region.

### Phase 3: Advanced Analysis (The "Why")
- **Correlation Matrix**:
  ```python
  correlation = df[['revenue', 'marketing_spend', 'traffic']].corr()
  print(correlation)
  ```
- **Anomaly Detection**:
  - Calculate Z-scores or Interquartile Range (IQR) to find outliers.
  - Identify specific dates or entities that deviate standard patterns.

## Output Format
Return findings in a structured Markdown summary:
1.  **Data Health**: "Analyzed X rows. Found Y missing values (filled with 0)."
2.  **Key Statistics**: Mean, Max, Min, Growth Rate.
3.  **Correlations**: "Strong positive correlation between Ad Spend and Traffic (0.85)."
4.  **Anomalies**: "Store A revenue dropped 40% on [Date], unlike other stores."

## Tools & Libraries
- `pandas`: Data manipulation
- `numpy`: Math operations
- `scipy`: Statistical tests (if needed)
- `matplotlib`/`seaborn`: (Optional) Static plotting for internal checks. For final dashboards, hand off to `dashboard-architect`.
