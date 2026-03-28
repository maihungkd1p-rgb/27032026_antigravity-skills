---
name: docx
description: >
  Tạo, chỉnh sửa tài liệu Word (.docx) chuyên nghiệp. Sử dụng khi:
  tạo file word, viết báo cáo, soạn hợp đồng, cẩm nang quy trình,
  xuất markdown sang docx, tạo đề xuất dự án, tài liệu SOP,
  biên bản cuộc họp, thư công văn, export word, create document.
  Word đẹp = Word cấu trúc mạch lạc, đọc không mỏi mắt.
  (Degrees of Freedom: 🟡 Trung bình — nội dung linh hoạt,
  kỹ thuật định dạng theo chuẩn Corporate cứng).
---

# Word Document Skill (`docx`)

## Mục đích
Skill này tồn tại vì file Word không chỉ là văn bản — nó là **sản phẩm giao tiếp chính thức**.
Người nhận file phải mở ra là **hiểu cấu trúc ngay**, **tin tưởng** nội dung,
và **tra cứu** được mà không phải đọc từ đầu đến cuối. Agent sử dụng skill này
để tạo ra các file `.docx` đạt chuẩn trải nghiệm người đọc, không chỉ đúng nội dung.

## Phạm vi
- **Nên dùng khi:** Tạo/sửa/định dạng file .docx; Xuất Markdown sang Word; Soạn báo cáo, hợp đồng, cẩm nang, SOP, đề xuất.
- **Không dùng khi:** Poster/Brochure (dùng PowerPoint/Canva); Tính toán số liệu (dùng Excel); Google Docs (dùng API riêng).

## Tư Duy Trước Khi Tạo File

Trước khi viết 1 dòng code, Agent phải trả lời 3 câu hỏi:

1. **Người dùng đang giải quyết VẤN ĐỀ gì?** Không phải "muốn 1 file Word" — mà là: báo cáo lên cấp trên? ký kết hợp đồng? tra cứu quy trình? truyền thông nội bộ?
2. **Tính năng nào GIÚP ÍCH nhất?** (Xem `references/feature_pairing.md`):
   - Duyệt nhanh → Executive Summary, Heading rõ ràng
   - Tra cứu → Mục lục (TOC), Table, Bullet points
   - Tin tưởng → Nguồn trích dẫn, Số trang, Font chữ chuẩn xác
3. **Tổ hợp nào là ĐỦ?** Chọn 3-5 format tạo giá trị cao nhất, bảo vệ cognitive load của người đọc.

## Nguyên Tắc 4 Lớp

Mọi file Word phải đạt chuẩn trên cả 4 lớp trải nghiệm:

### Lớp 1 — Cấu trúc (Người dùng tra cứu dễ dàng)
- Tài liệu > 2 trang phải có Mục lục (TOC placeholder) ở đầu.
- Phân cấp Heading nghiêm ngặt: `Heading 1` (Chương) → `Heading 2` (Mục) → `Heading 3` (Ý lớn).
- Sang chương mới phải ngắt trang (Page Break).
- Báo cáo phân tích phải có "Executive Summary" đầu tiên.

### Lớp 2 — Thông tin (Người dùng hiểu đúng)
- Không dùng khối text dài quá 5 dòng. Chia nhỏ bằng Bullet points hoặc Numbering.
- Thông tin định lượng (nhiều biến số) phải ưu tiên dùng Bảng (Table), không viết thành câu dài.
- Chú thích nguồn dữ liệu nếu có. Ghi ngày tạo ở cuối tài liệu.
- Với báo cáo phân tích: thêm text "Key Insights" nói rõ **"vậy thì sao?"**.

### Lớp 3 — Trực quan (Người dùng cảm nhận sự chuyên nghiệp)
- Cỡ chữ chuẩn: Body (11pt), H1 (16pt), H2 (14pt).
- Font chữ: Sans-serif cho màn hình (Arial/Calibri), Serif cho in ấn (Times New Roman).
- Bảng (Tables): Header Row có nền màu. Dùng Table Style `Medium Shading 1 Accent 1`.
- Màu Heading: Dark Blue (0, 51, 102) — nhất quán toàn file.

### Lớp 4 — Tương tác (Người dùng thao tác dễ dàng)
- Số trang mặc định ở Footer.
- URL và tham chiếu chéo nên nhúng Hyperlink.
- Ghi nguồn dữ liệu + ngày tạo ở cuối tài liệu (Source Note).

## Quy Trình (IPO Flow)

### Input
- Xác định **data source**: Markdown text? JSON data? File .docx có sẵn? Hay viết từ scratch?
- Hỏi rõ **mục đích**: Báo cáo nội bộ? Hợp đồng đối ngoại? Template nhập liệu? SOP?
- Nhận diện **đối tượng đọc**: CEO (ngắn gọn, Executive Summary)? Team kỹ thuật (chi tiết)? Khách hàng (formal)?

### Process

**Nhánh A — Tạo mới hoặc sửa file .docx:**
1. Import `python-docx`. Tham khảo `scripts/docx_builder.py` nếu cần class `DocxBuilder`.
2. Áp dụng 3 câu hỏi → chọn tổ hợp tính năng phù hợp.
3. Dựng skeleton: Title → TOC placeholder (nếu > 2 trang) → Executive Summary (nếu báo cáo) → Chapters.
4. Đổ nội dung: Paragraph, Bold/Italic, Bullet list, Tables.
5. Format: Table style, Font, Page break giữa chapters.
6. Finalize: Source note + ngày tạo ở cuối.

**Nhánh B — Convert Markdown/CSV sang .docx:**
1. Parse nội dung nguồn (Markdown heading → Word Heading, list → Bullet, table → Table).
2. Áp dụng styling chuẩn Corporate (DocxBuilder `_setup_styles()`).
3. Lưu file với đầy đủ metadata.

### Output
- File lưu tại `03_Outputs/`. Trả đường dẫn tuyệt đối cho user.
- Tên file: không chứa ký tự đặc biệt, dùng gạch dưới thay khoảng trắng.

## Self-Check

Trước khi bàn giao, Agent tự kiểm tra 11 mục:

**Format & Structure:**
- [ ] Tài liệu có phân cấp Heading 1/2/3 rõ ràng không?
- [ ] Có ngắt trang (Page Break) giữa các chương lớn không?
- [ ] Nếu dài > 2 trang, đã thêm không gian cho Mục Lục (TOC placeholder)?
- [ ] Font chữ và kích thước (11pt cho body) đã chuẩn mực?
- [ ] File lưu đúng `.docx` trong `03_Outputs/`?

**Information Quality:**
- [ ] Dữ liệu output có khớp input gốc (không thêm/bớt sai)?
- [ ] Có "wall-of-text" nào > 5 dòng chưa chia nhỏ thành Bullets/Table?
- [ ] Nếu là báo cáo phân tích: đã có Executive Summary?

**Visual & Interaction:**
- [ ] Bảng biểu (Table) có Header Row nổi bật (màu nền)?
- [ ] Đã thêm số trang hoặc chừa không gian footer?
- [ ] Đã ghi nguồn dữ liệu và ngày tạo ở cuối tài liệu?

## Ví dụ

**Ví dụ 1 — Báo cáo kinh doanh:**
> Input: "Tạo báo cáo tháng 3 cho 6 cửa hàng từ data sáng nay"
> Agent hỏi: Báo cáo gửi ai? → CEO → chọn: TOC + Executive Summary + bảng KPI + Page break giữa chương
> Output: Tạo `03_Outputs/Bao_cao_T3_2026.docx` với TOC placeholder, Summary 1 trang, 3 chương chi tiết

**Ví dụ 2 — Xuất tài liệu quy trình:**
> Input: "Chuyển file Markdown quy trình onboarding sang Word cho HR"
> Agent: Nhánh B (Convert) → parse headings/lists → áp styling Corporate → thêm source note
> Output: `03_Outputs/Quy_Trinh_Onboarding_HR.docx` với Heading đúng cấp, Numbered list, Footer số trang

## Tài Nguyên Đi Kèm
- `scripts/docx_builder.py` — Class DocxBuilder (fluent API) + corporate styles. Chạy trực tiếp hoặc tham khảo patterns.
- `references/feature_pairing.md` — Bảng tra cứu: Nhu cầu người dùng → Tính năng Word nên dùng. Đọc khi cần quyết định tổ hợp tính năng.
- `examples/README.md` — Các ví dụ sử dụng DocxBuilder (báo cáo, quy trình, hợp đồng).
