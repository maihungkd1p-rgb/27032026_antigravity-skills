---
name: viet-chuyen-nghiep
description: Orchestrator tạo nội dung tiếng Việt chuyên nghiệp theo mô hình 4 lớp. Kích hoạt khi có yêu cầu viết tiếng Việt ("Viết bài...", "Tạo nội dung...", "Phân tích..."). Luôn đảm bảo chuẩn tiếng Việt.
---

# Viết Chuyên Nghiệp

Orchestrator tạo nội dung tiếng Việt chuyên nghiệp theo mô hình 4 lớp: Content → Style → Platform → Standards.

## Khi Nào Dùng Skill Này

**Tự động kích hoạt khi:**
- User yêu cầu tạo nội dung tiếng Việt: "Viết bài về...", "Tạo nội dung..."
- User cần phân tích hoặc nghiên cứu: "Phân tích...", "Nghiên cứu..."
- User muốn báo cáo hoặc trình bày: "Làm báo cáo...", "Trình bày..."
- Bất kỳ task viết chuyên nghiệp bằng tiếng Việt nào

---

## Mô Hình 4 Lớp

```
Request từ User
    ↓
┌──────────────────────────────────────────────┐
│ Bước 1: CONTENT — Viết CÁI GÌ? (optional)   │
│ Cần thu thập/xử lý dữ liệu trước khi viết?  │
│ → 01_content/nghien-cuu.md                   │
│ → 01_content/phan-tich.md                    │
│ Bỏ qua nếu đã đủ thông tin                   │
└──────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────┐
│ Bước 2: STYLE — Viết THẾ NÀO? (chọn 1)      │
│ → 02_style/storytelling.md                   │
│ → 02_style/technical-academic.md             │
│ → 02_style/technical.md (Hướng dẫn/Guide)    │
│ → 02_style/data-report.md (Báo cáo số liệu)  │
│ → 02_style/executive.md (Tóm tắt lãnh đạo)   │
└──────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────┐
│ Bước 3: PLATFORM — Hiển thị Ở ĐÂU? (chọn 1) │
│ → 03_platform/facebook.md (plaintext)        │
│ → 03_platform/linkedin.md (professional)     │
│ → 03_platform/docx.md (văn bản hành chính)   │
│ → 03_platform/presentation.md (slide)        │
│ → Markdown/Blog (mặc định, không cần load)   │
└──────────────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────┐
│ Bước 4: STANDARDS — Đạt chuẩn CHƯA? (BẮT BUỘC) │
│ → 04_standards/quy-tac-tieng-viet.md (LUÔN)  │
│ → 04_standards/kiem-chung.md (nếu có claims)  │
└──────────────────────────────────────────────┘
    ↓
Viết Content
```

---

## Phân Tích INPUT: 5 Câu Hỏi Thiết Yếu

Trước khi routing, phân tích request bằng 5 câu hỏi:

| # | Câu hỏi | Quyết định |
|---|---------|-----------|
| 1 | User cung cấp gì? (data thô, ý tưởng, topic?) | Content modules cần load? |
| 2 | Mục đích? (inspire, educate, instruct, inform, brief) | Style module nào? |
| 3 | Độc giả là ai? (công chúng, professionals, technical, executives) | Tone & depth? |
| 4 | Platform? (Facebook, LinkedIn, Docs, Slide) | Platform module nào? |
| 5 | Tone mong muốn? (trang trọng, thoải mái, phân tích, cảm xúc) | Confirm style? |

---

## Routing Rules

### Bước 1: Content (optional)

Load **chỉ khi cần** xử lý dữ liệu trước khi viết:

| Tình huống | Module |
|-----------|--------|
| User cung cấp data phức tạp, cần trích xuất insights | `01_content/phan-tich.md` |
| Topic cần thu thập thông tin, nghiên cứu | `01_content/nghien-cuu.md` |

### Bước 2: Style (chọn 1)

| Mục đích | Tone | Độc giả | Module |
|---------|------|----------|--------|
| Inspire, persuade | Cảm xúc, story | Phổ thông | `02_style/storytelling.md` |
| Educate, document | Chuyên môn, academic | Technical/Students | `02_style/technical-academic.md` |
| Instruct, explain | Rõ ràng, trực tiếp | Mọi level | `02_style/technical.md` |
| Inform, data-driven | Phân tích | Professionals | `02_style/data-report.md` |
| Brief executives | Ngắn gọn, actionable | Decision-makers | `02_style/executive.md` |

### Bước 3: Platform (chọn 1)

| Platform | Module | Ghi chú |
|----------|--------|---------|
| Facebook cá nhân | `03_platform/facebook.md` | Plaintext, ALL CAPS, === |
| LinkedIn | `03_platform/linkedin.md` | Professional, spacing, hashtags |
| Blog/Website | Không cần load | Markdown mặc định |
| DOCX/Word | `03_platform/docx.md` | Format heading, table, font |
| Slide/Presentation | `03_platform/presentation.md` | Slide structure, visual cues |

### Bước 4: Standards (BẮT BUỘC)

**Luôn load:** `04_standards/quy-tac-tieng-viet.md`  
**Load thêm nếu có claims quan trọng:** `04_standards/kiem-chung.md`

---

## Auto-Detect Patterns

| User Nói | Route Đến |
|-----------|-----------|
| "Viết bài blog về..." | storytelling |
| "Viết bài đăng Facebook..." | storytelling + facebook |
| "Viết bài LinkedIn..." | storytelling/technical + linkedin |
| "Chuyển sang dạng FB..." | facebook (format only) |
| "Viết tài liệu kỹ thuật..." | technical-academic / technical |
| "Hướng dẫn sử dụng..." | technical |
| "Viết giáo trình/sách..." | technical-academic |
| "Phân tích data/dữ liệu..." | phan-tich → data-report |
| "Làm báo cáo..." | data-report hoặc executive |
| "Nghiên cứu về..." | nghien-cuu → (chọn style) |
| "Tóm tắt cho sếp..." | executive |
| "Làm slide...", "Thuyết trình..." | presentation |
| "Soạn văn bản...", "Soạn công văn..." | docx |

---

## Sơ Đồ Module

```
viet-chuyen-nghiep/
│
├── SKILL.md                     ← Bạn đang ở đây (Router)
│
├── 01_content/                  ← NỘI DUNG — Thu thập, xử lý
│   ├── nghien-cuu.md            ← Topic → Information [SẴN SÀNG]
│   └── phan-tich.md             ← Data → Insights [SẴN SÀNG]
│
├── 02_style/                    ← TRÌNH BÀY — Phương pháp viết
│   ├── storytelling.md          ← Cảm xúc/Blog [SẴN SÀNG]
│   ├── technical-academic.md    ← Kỹ thuật/Học thuật [SẴN SÀNG]
│   ├── technical.md             ← Hướng dẫn/Guide [SẴN SÀNG]
│   ├── data-report.md           ← Báo cáo dữ liệu [SẴN SÀNG]
│   └── executive.md             ← Tóm tắt lãnh đạo [SẴN SÀNG]
│
├── 03_platform/                 ← NỀN TẢNG — Format theo platform
│   ├── facebook.md              ← Plaintext Facebook [SẴN SÀNG]
│   ├── linkedin.md              ← Professional Networking [SẴN SÀNG]
│   ├── docx.md                  ← Văn bản Word [SẴN SÀNG]
│   └── presentation.md          ← Slide thuyết trình [SẴN SÀNG]
│
└── 04_standards/                ← TIÊU CHUẨN — Rà soát
    ├── quy-tac-tieng-viet.md    ← Quy tắc tiếng Việt [BẮT BUỘC]
    └── kiem-chung.md            ← Kiểm chứng claims [SẴN SÀNG]
```

---

## Checklist Thực Hiện

Với mỗi request tạo nội dung:

- [ ] Phân tích INPUT kỹ lưỡng (trả lời đủ 5 câu hỏi)
- [ ] Xác định có cần content modules không (Bước 1)
- [ ] Chọn style module phù hợp (Bước 2)
- [ ] Xác định platform target (Bước 3)
- [ ] **Load 04_standards/quy-tac-tieng-viet.md** (BẮT BUỘC - không bỏ qua)
- [ ] Load 04_standards/kiem-chung.md nếu có claims
- [ ] Viết content theo guidelines đã load
- [ ] Verify đã tuân thủ tiêu chuẩn

---

**Token Budget:** ~2,000 tokens  
**Vai trò:** Orchestrator/Router  
**Triết lý:** Tách rõ 4 lớp — Content, Style, Platform, Standards  
**Version:** 2.1 (Full Modules)
