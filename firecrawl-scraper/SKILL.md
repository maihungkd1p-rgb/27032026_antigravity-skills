---
name: firecrawl-scraper
description: Deep web scraping, screenshots, PDF parsing, và website crawling
---

# Firecrawl Scraper

## Overview

Deep web scraping, screenshots, PDF parsing, và website crawling sử dụng Firecrawl API.

## Khi nào Sử dụng

- Khi cần trích xuất nội dung sâu từ web pages
- Khi cần tương tác với trang (click, scroll, etc.)
- Khi muốn screenshots hoặc parse PDF
- Khi batch scraping nhiều URLs

## Installation

```bash
npx skills add -g BenedictKing/firecrawl-scraper
```

## Cách sử dụng

### Ví dụ prompt:
```
Dùng skill @firecrawl-scraper để:
- Scrape danh sách sản phẩm từ website đối thủ
- Lấy giá và mô tả của từng sản phẩm
- Xuất ra file JSON/CSV
```

### Use cases cho Anna Eyewear:
1. **Competitor Research**: Scrape giá kính từ đối thủ
2. **Market Analysis**: Thu thập reviews khách hàng
3. **Content Curation**: Lấy bài viết về trends kính mắt

## Best Practices

- Configure API keys via environment variables
- Respect robots.txt
- Rate limiting để tránh bị block

## Lưu ý

Bạn đã có skill `social-scraper` tự tạo trước đó. Skill này bổ sung thêm capabilities cho:
- PDF parsing
- Screenshots
- Batch processing

## Related Skills
- context7-auto-research, tavily-web, exa-search
