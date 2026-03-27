# RAG Quality Assessment Checklist

## Knowledge Item: ________________
## Date: ________________
## Assessor: ________________

---

## 8 Tiêu Chí Đánh Giá (0-10)

| # | Tiêu Chí | Score | Notes |
|---|----------|-------|-------|
| 1 | **Clarity** - Nội dung rõ ràng, parseable? | /10 | |
| 2 | **Structure** - Headers, sections, metadata? | /10 | |
| 3 | **Specificity** - Đủ chi tiết cho specific queries? | /10 | |
| 4 | **Chunking** - Chunk size 2-8KB? | /10 | |
| 5 | **Semantic Coherence** - Mỗi chunk có ý nghĩa độc lập? | /10 | |
| 6 | **Retrieval Fitness** - Keywords, tags đầy đủ? | /10 | |
| 7 | **Format Quality** - Tables/lists render đúng? | /10 | |
| 8 | **Noise Level** - Không có artifacts/noise? | /10 | |

**TOTAL: _____ / 80 = _____%**

---

## Quick Assessment

| Check | Status |
|-------|--------|
| metadata.json exists and valid? | ☐ |
| All artifacts listed in metadata? | ☐ |
| Has overview.md? | ☐ |
| Has qa_pairs.md? | ☐ |
| Chunks < 15KB? | ☐ |
| Front-matter YAML on sections? | ☐ |
| Cross-references defined? | ☐ |

---

## Issues Found

| Issue | Severity | Fix |
|-------|----------|-----|
| | P1/P2/P3 | |
| | | |
| | | |

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 80%+ | ✅ Production Ready |
| 70-79% | ⚠️ Acceptable, minor fixes |
| 60-69% | 🔶 Needs work |
| <60% | 🔴 Not ready, major issues |
