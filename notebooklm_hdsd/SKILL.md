---
name: notebooklm_hdsd
description: Tư vấn chiến lược và hướng dẫn sử dụng Google NotebookLM. Kích hoạt khi user nhắc đến NotebookLM, tạo notebook, chunking tài liệu, System Prompt cho NotebookLM, Studio outputs (Audio/Video/Slide/Mindmap/Quiz), xây Knowledge Base doanh nghiệp, hoặc triển khai NotebookLM cho team.
---

# NotebookLM Strategy & Knowledge Orchestrator

## Mục đích

Orchestrator chuyên biệt cho mọi vấn đề liên quan Google NotebookLM — từ tư vấn cơ bản đến triển khai doanh nghiệp. Skill này KHÔNG duplicate nội dung, mà tham chiếu KI + delegate sang workflow/skill khác.

## Phạm vi & Delegation

| Yêu cầu | Xử lý tại |
|----------|-----------|
| Hỏi về NotebookLM, RAG, Grounding | **Skill này** — tham chiếu KI |
| Thiết kế Notebook, chunking, naming | **Skill này** — tham chiếu KI Ch.02-03 |
| Viết System/Chat/Studio Prompt | **Delegate** → workflow `/notebooklm-prompt` |
| List/query/add notebook qua API | **Delegate** → skill `notebooklm-integration` |
| Hướng dẫn Studio outputs | **Skill này** — tham chiếu KI Ch.02, 06-07 |
| Triển khai cho team/DN | **Skill này** — tham chiếu KI Ch.09-14 |

## Tri thức nền (KI Reference)

```
KI: notebooklm_hdsd
├── notebooklm_kb.md      ← 14 chương, 890 dòng (Full knowledge)
└── quick_reference.md     ← 106 dòng (Tra cứu nhanh)
```

**Quy tắc nạp KI:**
- Câu hỏi đơn giản → Nạp `quick_reference.md` là đủ
- Câu hỏi chuyên sâu → Nạp `notebooklm_kb.md` + tìm chương phù hợp
- LUÔN trích dẫn nguồn KI khi trả lời

## IPO Flow

```
INPUT: Yêu cầu user liên quan NotebookLM
  ↓
PROCESS:
  1. Phân loại → 1 trong 5 modules:
     [Tư vấn] [Thiết kế] [Prompt] [Studio] [Deploy]
  2. Nạp KI phù hợp (quick_ref hoặc full kb)
  3. Delegate nếu cần:
     → Viết prompt: gọi /notebooklm-prompt
     → API interaction: gọi notebooklm-integration
  4. Xử lý + trả lời có tham chiếu nguồn
  ↓
OUTPUT: Tư vấn/Hướng dẫn/Kế hoạch (actionable, có bước tiếp theo)
```

## 5 Modules Chi Tiết

### Module 1 — Tư vấn (Consult)

**Khi nào:** User hỏi "NotebookLM là gì?", "So sánh với ChatGPT", "RAG hoạt động thế nào?"

**Quy trình:**
1. Nạp KI → `quick_reference.md` (bản chất kỹ thuật, so sánh)
2. Nếu cần chi tiết → nạp `notebooklm_kb.md` Ch.01
3. Trả lời bằng tiếng Việt, kèm ví dụ thực tế
4. Nêu rõ giới hạn nếu liên quan (cuối `quick_reference.md`)

### Module 2 — Thiết kế Notebook (Design)

**Khi nào:** "Tôi có 50 file PDF, tổ chức thế nào?", "Chunking sao cho tốt?"

**Quy trình:**
1. Nạp KI → Ch.02 (Thiết lập), Ch.03 (Quản lý tài liệu)
2. Hỏi user: loại tài liệu, số lượng, mục đích sử dụng
3. Đề xuất kiến trúc Notebook:
   - Naming convention: `YYYY-MM-DD_[Loại]_[MoTa]_v[XX].[ext]`
   - Chunking strategy: chia theo chương/chủ đề, 10-30 trang/chunk
   - Cấu trúc notebook: theo phòng ban hoặc theo chủ đề
4. Output: Bảng kế hoạch tổ chức Notebook (actionable)

### Module 3 — Prompt (Delegate)

**Khi nào:** "Viết System Prompt cho notebook", "Tạo prompt chat", "Studio prompt"

**Quy trình:**
1. Nhận diện loại prompt cần viết
2. **DELEGATE** → Gọi workflow `/notebooklm-prompt`
3. Thông báo user: "Tôi sẽ sử dụng quy trình `/notebooklm-prompt` để viết prompt cho bạn"

### Module 4 — Studio Outputs

**Khi nào:** "Tạo podcast", "Làm slide", "Tạo quiz", "Mindmap"

**Quy trình:**
1. Xác định loại output trong 9 tính năng Studio:
   Audio | Presentation | Video | Mindmap | Report | Study Guide | Quiz | Infographic | Table
2. Nạp KI → Ch.02 (mục Studio), Ch.06-07 (Sáng tạo nội dung)
3. Hướng dẫn:
   - Chuẩn bị nguồn (bật/tắt nguồn phù hợp)
   - Viết mô tả cho Studio → delegate `/notebooklm-prompt` Bước 3 nếu cần
   - Tips tối ưu output
4. Output: Hướng dẫn bước-by-bước + prompt mẫu

### Module 5 — Triển khai Doanh nghiệp (Deploy)

**Khi nào:** "Deploy NotebookLM cho team", "Xây KB nội bộ", "Đo ROI"

**Quy trình:**
1. Nạp KI → Ch.09-14 (Doanh nghiệp + Triển khai)
2. Áp dụng quy trình 4 bước:
   - **Chuẩn bị:** Chuẩn hóa tài liệu, convert formats
   - **Xây Notebook:** Kiến trúc theo phòng ban/chủ đề
   - **Cấu hình:** System Prompt, test chất lượng
   - **Đo lường:** ROI = thời gian tiết kiệm × chi phí nhân sự
3. Output: Kế hoạch triển khai chi tiết, bao gồm pricing

## Self-Check

Mỗi output phải đạt **5/5:**

- [ ] Tham chiếu KI nguồn (không tự sáng tác kiến thức NotebookLM)
- [ ] Delegate đúng (prompt → workflow, API → skill integration)
- [ ] Hướng dẫn bước-by-bước rõ ràng
- [ ] Nêu rõ giới hạn NotebookLM nếu liên quan
- [ ] Output actionable (user biết bước tiếp theo cụ thể)
