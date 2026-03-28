---
name: docx-283
description: >
  Tạo, chỉnh sửa tài liệu Word (.docx) chuyên nghiệp (Báo cáo, Hợp đồng, Đề xuất).
  Word đẹp ≠ Word nhiều màu. Word đẹp = Word cấu trúc mạch lạc, đọc không mỏi mắt.
  (Degrees of Freedom: 🟡 Trung bình — nội dung và cấu trúc linh hoạt theo nhu cầu,
  kỹ thuật định dạng tuân thủ chuẩn Corporate layout).
---

# Word Document Skill (`docx-283`)

## Mục đích
Tài liệu Word là **văn bản lưu trữ và truyền đạt thông tin chính thức**. Người đọc cần một văn bản có cấu trúc phân tầng rõ ràng, thông tin dễ tra cứu và hình thức đáng tin cậy. Agent sử dụng skill này để sinh ra các tệp `.docx` không chỉ có chữ, mà có "linh hồn" của một tài liệu quy chuẩn.

## Phạm vi
- **Nên dùng khi:** Tạo báo cáo kinh doanh, hợp đồng, cẩm nang, tài liệu quy trình, hoặc cần xuất Markdown sang Word.
- **Không dùng khi:** Thiết kế Poster/Brochure (dùng PowerPoint/Canva), tính toán số liệu phức tạp (dùng Excel).

## Tư Duy Trước Khi Tạo File (Nhu cầu ⭢ Tính năng)

Đừng chỉ "print text" vào Word. Hãy trả lời 3 câu hỏi trước khi code:

1. **Người dùng cần đọc tài liệu này để làm gì?** (Duyệt nhanh? Tra cứu chi tiết? Hay ký kết?)
2. **Tính năng Word nào giải quyết tốt nhất?** (Xem bảng tra cứu tại `references/feature_pairing.md`):
   - Duyệt nhanh ⭢ Executive Summary, Heading rõ ràng.
   - Tra cứu ⭢ Mục lục (TOC), Table, Bullet points.
   - Tin tưởng ⭢ Nguồn trích dẫn, Chân trang (Số trang), Font chữ chuẩn xác.
3. **Tổ hợp nào là đủ?** Chọn 3-5 format quan trọng bảo vệ "cognitive load" (tải nhận thức) của người đọc.

## Nguyên Tắc 4 Lớp (Đã Thực Tế Hóa cho Python/Docs)

Mọi file Word phải đạt chuẩn trên cả 4 lớp trải nghiệm:

### Lớp 1 — Cấu trúc (Người dùng tra cứu dễ dàng)
- Tài liệu > 2 trang **BẮT BUỘC** có Mục lục (TOC) ở đầu.
- Phân cấp Heading nghiêm ngặt: `Heading 1` (Chương) ⭢ `Heading 2` (Mục) ⭢ `Heading 3` (Ý lớn).
- Sang chương mới phải **Ngắt trang (Page Break)**.
- Luôn có "Executive Summary" (Tóm tắt) nếu đây là báo cáo phân tích.

### Lớp 2 — Thông tin (Người dùng hiểu đúng)
- Không dùng khối text (wall of text) dài quá 5 dòng. Chia nhỏ bằng Bullet points hoặc Numbering.
- Thông tin định lượng (nhiều biến số) **phải ưu tiên dùng Bảng (Table)**, không viết thành câu dài.
- Chú thích rõ ràng nguồn dữ liệu nếu có.

### Lớp 3 — Trực quan (Người dùng cảm nhận sự chuyên nghiệp)
- Cỡ chữ chuẩn: Body (11-12pt), H1 (18pt), H2 (14pt).
- Font chữ: Ưu tiên bộ Sans-serif cho màn hình (Arial/Calibri/Roboto) hoặc Serif cho in ấn (Times New Roman).
- Bố cục bảng (Tables): Phải có Header Row (tô màu nền).

### Lớp 4 — Tương tác (Người dùng thao tác dễ dàng)
- Số trang mặc định ở Footer (ví dụ: "Trang 1/5").
- Các tham chiếu chéo (Cross-reference) hoặc URL ngoại liên kết nên được nhúng Hyperlink.

## Quy Trình (IPO Flow)

### Input
- Định dạng nguồn: Markdown text? JSON data? Hay yêu cầu viết từ scratch?
- Định vị tính chất tài liệu: Nội bộ hay Đối ngoại? Kỹ thuật hay Kinh doanh?

### Process (Thực thi)

1. Import `docx` (sử dụng gói `python-docx`). Hoặc dùng `scripts/docx_builder.py` để dùng wrapper `DocxBuilder` chuẩn hóa.
2. Dựng cấu trúc: 
   - Add Title / Heading 1.
   - Add chữ "TOC Placeholder" (Mục lục sẽ cần update bằng tay khi mở file do hạn chế của thư viện).
3. Đổ nội dung: Sử dụng Paragraph, Bold/Italic, và Tables.
4. Formatting: Thiết lập Table Style (ví dụ: `Medium Shading 1 Accent 1`). Dùng `docx_builder.py` để tiết kiệm code.

### Output
- File lưu tại thư mục `03_Outputs/`. Trả đường dẫn cho user.

## Self-Check (Kiểm tra trước giao hàng)

Agent tự kiểm đếm 8 tiêu chí sau:

- [ ] Tài liệu có phân cấp Heading 1/2/3 rõ ràng không?
- [ ] Các đoạn văn bản dài đã được chia nhỏ thành Bullet points hoặc Table chưa?
- [ ] Có ngắt trang (Page Break) giữa các chương lớn không?
- [ ] Đã thêm số trang (hoặc chừa không gian footer) chưa?
- [ ] Bảng biểu (Table) có Header Row nổi bật chưa?
- [ ] Nếu dài > 2 trang, đã thêm không gian cho Mục Lục (TOC) chưa?
- [ ] File có được lưu đúng định dạng `.docx` trong `03_Outputs/` không?
- [ ] Font chữ và kích thước (11-12pt cho body) đã chuẩn mực chưa?

## Ví dụ
Xem thêm code mẫu tại `examples/README.md`.

## Tài Nguyên Đi Kèm
- `scripts/docx_builder.py` — Wrapper Class (DocxBuilder) giúp viết code tạo Word cực ngắn, chuẩn corporate.
- `references/feature_pairing.md` — Bảng mapping nhu cầu user với tính năng Word (Tương tự Excel).
- `examples/README.md` — Code block mẫu cho Báo cáo dỏm, Hợp đồng, Table layouts.
