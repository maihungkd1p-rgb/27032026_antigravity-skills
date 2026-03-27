---
name: dashboard-architect
description: Visualizes data and creates interactive reports/dashboards. Use when user wants charts, graphs, or a designated "Report" or "Dashboard". Replaces static data storytelling.
---

# Dashboard Architect

## When to use this skill
- User asks for a "Dashboard", "Chart", or "Visualization".
- User wants to present data to a boss or team.
- User needs to "see" the data interactively.
- Supersedes `data-storytelling` for complex visualization needs.

## Core Principles
1.  **Interactivity**: Prefer interactive tools (Streamlit, HTML/Plotly) over static images when possible.
2.  **Narrative (3C)**: Visuals must support a story. Context -> Conflict -> Conclusion.
3.  **Aesthetics**: Use clean, modern color palettes. Avoid default "Excel-style" charts.

## Workflow

### Option A: Quick Static Report (Markdown + Images)
*Best for simple chat responses.*
1.  Generate charts using Python (`matplotlib`/`seaborn`).
2.  Save as images.
3.  Embed in Markdown report following the **3C Framework** (Context, Conflict, Conclusion).

### Option B: Interactive Dashboard (Streamlit)
*Best for deep dives and client presentations.*
1.  **Structure**:
    - Sidebar: Filters (Date Range, Store, Category).
    - Header: Key Metrics (Big Number Cards with delta).
    - Main: Charts (Line for trends, Bar for comparison).
    - Data Table: Detailed view at the bottom.
2.  **Implementation**:
    - Write a `dashboard.py` file using `streamlit`.
    - Functionality: Load data, apply filters, render Plotly charts.
    - **Instruction**: Tell user to run `streamlit run dashboard.py`.

### Option C: Web-based Report (HTML/JS)
*Best for portable, single-file reports.*
1.  Generate a self-contained HTML file using `plotly.io.to_html` or Chart.js.
2.  Inject CSS for "Premium Design" (as per web app guidelines).

## Visualization Rules
- **Time Series**: Line chart or Area chart.
- **Categorical**: Bar chart (Horizontal for long labels).
- **Composition**: Donut chart (max 5 segments) or Treemap.
- **Correlation**: Scatter plot.

## Report Structure (The 3C Integration)
Even in a dashboard, include text sections:
- **Context**: "Dashboard hiển thị dữ liệu từ ngày X đến Y."
- **Conflict**: Highlight metrics in RED if they are below target.
- **Conclusion**: "Dựa trên biểu đồ, đề xuất tăng ngân sách nhóm A."
