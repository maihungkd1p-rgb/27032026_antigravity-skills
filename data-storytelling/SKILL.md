---
name: data-storytelling
description: Transforms raw data into compelling business narratives using the 3C framework (Context-Conflict-Conclusion). Use when the user asks to create reports, analyze business data, or generate insights from spreadsheets.
---

# Data Storytelling (3C Framework)

## When to use this skill
- User provides raw data (CSV, Excel, JSON) and asks for analysis
- User requests a "business report" or "executive summary"
- User mentions "3C framework" or "data storytelling"
- User wants to present data to stakeholders

## The 3C Framework

### 1. Context (Bối cảnh)
- **What**: Current state, baseline metrics, time period
- **Why it matters**: Set expectations before revealing findings
- **Format**: 2-3 sentences or a quick KPI summary table

### 2. Conflict (Mâu thuẫn/Vấn đề)
- **What**: Gap between expected and actual, anomalies, problems
- **Why it matters**: Creates tension, highlights where to focus
- **Format**: Bullet points with specific numbers, charts if applicable

### 3. Conclusion (Kết luận/Hành động)
- **What**: Recommendations, next steps, action items
- **Why it matters**: Gives stakeholders clear direction
- **Format**: Numbered action items with owners and deadlines

## Workflow

### Step 1: Data Ingestion
```
1. Identify data source (file path, pasted table, or API)
2. Load and inspect first 10 rows
3. Identify key columns and metrics
```

### Step 2: Context Analysis
```
1. Calculate summary statistics (mean, median, totals)
2. Identify time period covered
3. Compare to targets or historical benchmarks
```

### Step 3: Conflict Discovery
```
1. Find outliers (values > 2 standard deviations)
2. Identify negative trends or missed targets
3. Highlight top/bottom performers
```

### Step 4: Conclusion Formation
```
1. Prioritize issues by impact
2. Propose 2-3 actionable recommendations
3. Assign urgency levels (immediate, this week, this month)
```

## Output Template

```markdown
# [Report Title]
*Báo cáo ngày [DATE] | Kỳ phân tích: [PERIOD]*

## 📊 Tổng quan (Context)
[Summary table or KPIs]

## ⚠️ Điểm nóng (Conflict)
- **Issue 1**: [Description with numbers]
- **Issue 2**: [Description with numbers]

## ✅ Đề xuất (Conclusion)
1. [Action 1] - Ưu tiên: Cao
2. [Action 2] - Ưu tiên: Trung bình
3. [Action 3] - Ưu tiên: Thấp
```

## Visualization Guidelines
- Use tables for comparing <10 items
- Use bar charts for categorical comparisons
- Use line charts for time series
- Always label axes and include units

## Language
- Default to Vietnamese for Anna Eyewear reports
- Use simple, non-technical language for store-level reports
- Use English for technical/developer audiences
