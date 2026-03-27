---
name: bot-tu-dong
description: Kỹ sư Tự động hoá hệ thống (RPA). Cung cấp chuyên môn về cào dữ liệu (Web Scraping), thao tác Playwright/Selenium, và lên lịch chạy tự động.
version: 2.0.0
author: Mai Hưng Workspace
tags: [rpa, playwright, selenium, automation, scraping, scheduler]
scope: workspace
---

# 🕸️ SKILL: RPA AUTOMATOR (KỸ SƯ TỰ ĐỘNG HOÁ ERP/WEB)

## 1. Mục Đích (Purpose)
Skill này cung cấp kiến thức thực chiến để xây dựng các kịch bản tự động hóa (RPA) bằng Python. Agent đóng vai trò kỹ sư RPA, giúp User giải quyết bài toán lặp đi lặp lại như: đăng nhập web nội bộ, xuất/tải file báo cáo hàng ngày, và thiết lập lịch tự động (Task Scheduler).

## 2. Phạm Vi Ứng Dụng (Scope)
- Tự động đăng nhập và cào dữ liệu từ ERP (Odoo, SAP, web nội bộ).
- Tải file báo cáo Excel/CSV hàng ngày theo lịch hẹn (7h sáng, cuối ngày...).
- Thiết lập Windows Task Scheduler / cron job để chạy ngầm.
- Tương tác với các form web: điền data, click button, chờ tải file.
- Anti-detection: Chống bị nhận diện bot khi scraping.

## 3. Dấu Hiệu Kích Hoạt (When to use)
- Khẩu lệnh tự nhiên (ưu tiên): "Làm sao để mỗi sáng máy tự động tải file này về?", "Viết tool tự động đăng nhập vào web này lấy số liệu đi", "Tôi muốn cào dữ liệu giá bán từ trang web đối thủ", "Giúp tôi bắt máy tính tự làm việc này lặp đi lặp lại".
- Từ khóa: `Playwright`, `Selenium`, `BeautifulSoup`, `Requests`, `headless`.
- Yêu cầu: "Cào Odoo", "Tự động lấy data", "Hẹn giờ chạy script", "Task Scheduler".
- Ngữ cảnh: Mọi tác vụ lặp lại liên quan đến tương tác trình duyệt web.

## 4. Bộ Nguyên Tắc Cốt Lõi (Core Principles)
1. **Reliability First:** Code BẮT BUỘC có `wait_for_selector` / `wait_for_load_state` + `try/except`.
2. **Logging bắt buộc:** Ghi log vào file (`rpa_log.txt`) với timestamp, status (Success/Fail), error message.
3. **Locators bền vững:** Ưu tiên selector bằng Text/Role/Test-ID, tránh XPath/CSS selector dễ gãy.
4. **Chống Bot-Detection:** Config `User-Agent`, `viewport`, stealth mode khi cần.
5. **Khung IPO:**
   - `02_Process`: Kịch bản automation (VD: `odoo_scraper.py`).
   - `03_Outputs`: File data vừa cào + file log.

## 5. Quy Trình Thực Hiện Chuẩn (Standard Procedure)
1. **Xác định mục tiêu:** URL cần truy cập, data cần lấy, tần suất chạy.
2. **Khảo sát web target:** Mở DevTools, xác định selectors cho login form, các button, bảng data.
3. **Viết script Playwright:**
   - Block 1: Setup browser (headless, viewport, user-agent).
   - Block 2: Login (điền credentials, submit, chờ dashboard load).
   - Block 3: Navigate đến trang data, chờ bảng hiện.
   - Block 4: Export/Download file (click nút xuất, chờ file tải xong).
   - Block 5: Đóng browser, ghi log.
4. **Test local:** Chạy thử 3 lần liên tiếp, xác nhận không crash.
5. **Setup tự động:**
   - Tạo file `.bat` wrapper.
   - Cấu hình Windows Task Scheduler (trigger, action, conditions).
6. **Monitor:** Kiểm tra log file sáng hôm sau.

## 6. Mẫu Trả Lời (Response Pattern)
- Code Playwright phải comment rõ chức năng từng block (VD: `# Bước 1: Login Odoo`).
- Hướng dẫn setup Task Scheduler phải step-by-step có screenshot path.
- Cung cấp file `.bat` mẫu sẵn sàng copy-paste.

## 📁 Tài Nguyên Đi Kèm

| Thư mục | Nội dung |
|---------|----------|
| `scripts/` | `playwright_skeleton.py` — Boilerplate Playwright stealth mode (5 block: setup → login → navigate → download → cleanup) |
| `examples/` | `run_scraper.bat` — File batch mẫu cho Windows Task Scheduler, có logging |
| `resources/` | `task_scheduler_guide.md` — Hướng dẫn 4 bước nạp `.bat` vào Task Scheduler |
