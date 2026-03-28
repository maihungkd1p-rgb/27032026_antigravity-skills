---
name: excel
description: >
  Tạo, chỉnh sửa, phân tích file Excel (.xlsx) chuyên nghiệp. Sử dụng khi:
  tạo file excel, báo cáo doanh thu, xuất data ra bảng, vẽ biểu đồ excel,
  tạo timeline kế hoạch, phân tích dữ liệu, bảng tổng hợp, ranking cửa hàng.
  Excel đẹp ≠ Excel tô màu. Excel đẹp = Excel người dùng MỞ RA LÀ HIỂU NGAY.
  (Degrees of Freedom: 🟡 Trung bình — chiến lược linh hoạt theo ngữ cảnh,
  kỹ thuật thực thi theo chuẩn cứng).
---

# Excel Skill

## Mục đích
Skill này tồn tại vì file Excel không chỉ là bảng tính — nó là **sản phẩm giao tiếp**.
Người nhận file phải mở ra là **hiểu ngay** thông điệp chính, **tin tưởng** dữ liệu,
và **hành động** được mà không cần hỏi thêm. Agent sử dụng skill này để tạo ra các file
Excel đạt chuẩn trải nghiệm người dùng, không chỉ đúng dữ liệu.

## Phạm vi
- **Nên dùng khi:** Tạo/sửa/định dạng file .xlsx; Đọc & phân tích data từ Excel; Xuất báo cáo, timeline, bảng tổng hợp.
- **Không dùng khi:** File .xls cũ (cần convert trước); Google Sheets (dùng API riêng); Biểu đồ phức tạp cần BI tool.

## Tư Duy Trước Khi Tạo File

Trước khi viết 1 dòng code, Agent phải trả lời 3 câu hỏi:

1. **Người dùng đang giải quyết VẤN ĐỀ gì?** Không phải "muốn 1 file Excel" — mà là: so sánh hiệu suất? theo dõi kế hoạch? báo cáo lên cấp trên? ra quyết định nhanh?
2. **Tính năng nào GIÚP ÍCH nhất?** Chọn từ 6 nhóm giá trị (xem `references/feature_pairing.md`):
   - Hiểu dữ liệu → biểu đồ, data bars, sparklines
   - Tìm điều quan trọng → conditional formatting, pre-sorting, "Key Insights" text
   - Tiết kiệm thời gian → Overview sheet, tóm tắt tính sẵn, freeze panes
   - Sử dụng trực tiếp → bộ lọc, công thức (không hardcode), hyperlinks
   - Tin tưởng dữ liệu → ghi nguồn, ngày tạo, number_format nhất quán
   - Thu insight → cột so sánh Δ/%, xếp hạng, chỉ báo xu hướng ↑↓
3. **Tổ hợp nào PHÙ HỢP kịch bản này?** Không nhồi tất cả tính năng — chọn 3-5 tính năng tạo giá trị cao nhất.

## Nguyên Tắc 4 Lớp

Mọi file Excel phải đạt chuẩn trên cả 4 lớp trải nghiệm:

### Lớp 1 — Cấu trúc (Người dùng tìm thấy ngay)
- Sheet đầu tiên luôn là **"Overview"** nếu có ≥ 3 sheets (tóm tắt + mục lục có hyperlink).
- Bố cục: cột A để trống (width 3) làm lề, hàng 1 để trống, nội dung bắt đầu từ **B2**.
- Giãn cách: 1 hàng trống giữa các phần, 2 hàng trống giữa các bảng.
- Thứ tự sheets: Tổng quát → Cụ thể (Overview → Data → Analysis).

### Lớp 2 — Thông tin (Người dùng hiểu đúng)
- Mọi ô số **phải có number_format** (`#,##0` / `0.0%` / `$#,##0.00`). Cùng cột = cùng format.
- Giá trị thiếu = trống hoặc "N/A", **không bao giờ** = 0 (trừ khi thực sự bằng 0).
- Luôn ghi: nguồn dữ liệu, phạm vi thời gian, ngày tạo file.
- Với báo cáo phân tích: thêm text "Key Insights" nói rõ **"vậy thì sao?"**.

### Lớp 3 — Trực quan (Người dùng cảm nhận chuyên nghiệp)
- **Tắt gridlines** (`ws.sheet_view.showGridLines = False`) cho giao diện sạch.
- Dùng bảng màu Corporate nhất quán (xem `scripts/excel_builder.py` cho ExcelStyles).
- Border mỏng, màu nhạt — tránh border đen đậm.
- Chiều rộng cột tự tính theo nội dung (hàm `auto_column_widths` trong ExcelBuilder).

### Lớp 4 — Tương tác (Người dùng làm việc được)
- **Freeze panes** nếu bảng > 10 dòng (giữ header khi cuộn).
- **Auto-filter** nếu bảng > 20 dòng (người dùng tự lọc).
- **Pre-sort** theo chiều quan trọng nhất (revenue giảm dần, ngày tăng dần).
- Dùng **formulas** khi người dùng có thể cập nhật input; hardcode chỉ khi data là final.

## Quy Trình (IPO Flow)

### Input
- Xác định **data source**: file path, JSON, DataFrame, hay Markdown table?
- Hỏi rõ **mục đích**: báo cáo nội bộ? chia sẻ bên ngoài? template nhập liệu?
- Nhận diện **template cần dùng**: Timeline? Bảng tổng hợp? Báo cáo nhiều sheet?

### Process

**Nhánh A — Tạo hoặc sửa file (.xlsx):**
1. Import `openpyxl`. Tham khảo `scripts/excel_builder.py` nếu cần class ExcelBuilder.
2. Áp dụng 3 câu hỏi → chọn tổ hợp tính năng phù hợp.
3. Lần lượt dựng 4 lớp: Cấu trúc → Thông tin → Trực quan → Tương tác.
4. Chèn formulas (KHÔNG hardcode tính toán).
5. Đặt `number_format` cho MỌI cột số.

**Nhánh B — Đọc & phân tích data (.xlsx):**
1. Import `pandas`. Dùng `pd.read_excel()`.
2. Phân tích theo yêu cầu, xuất kết quả.

### Output
- File lưu tại `03_Outputs/`. Trả đường dẫn tuyệt đối.
- Tên sheet ≤ 31 ký tự, không chứa `\ / * ? : [ ]`.

## Self-Check

Trước khi bàn giao, Agent tự kiểm tra 8 mục:

- [ ] Công thức Excel dưới dạng string (`'=SUM(A1:A10)'`), không hardcode kết quả?
- [ ] Mọi cột số có `number_format` nhất quán?
- [ ] File lưu đúng `03_Outputs/`?
- [ ] Không có nguy cơ `#REF!` hoặc `#VALUE!` do sai dòng/cột?
- [ ] Nếu ≥3 sheets: có sheet Overview với mục lục hyperlink?
- [ ] Nếu bảng >10 dòng: đã freeze panes?
- [ ] Có ghi nguồn dữ liệu và ngày tạo?
- [ ] Gridlines đã tắt (cho file hướng ra bên ngoài)?

## Ví dụ

**Ví dụ 1 — Báo cáo doanh thu:**
> Input: "Tạo báo cáo tháng 3 cho 6 cửa hàng từ raw_data.json"
> Agent hỏi: Báo cáo gửi ai? → CEO → chọn: Overview sheet + pre-sort theo doanh thu + Key Insights text + freeze panes
> Output: Tạo `03_Outputs/Bao_cao_T3_2026.xlsx` với 2 sheets (Overview + Chi tiết)

**Ví dụ 2 — Timeline kế hoạch:**
> Input: "Xuất bảng timeline dự án 2026"
> Agent: dùng `scripts/timeline_builder.py` pattern → tạo file với marker "●", group rows, freeze cột C
> Output: `03_Outputs/Timeline_2026.xlsx`

## Tài Nguyên Đi Kèm
- `scripts/excel_builder.py` — Class ExcelBuilder (fluent API) + ExcelStyles + utility functions. Chạy trực tiếp hoặc tham khảo patterns.
- `scripts/timeline_builder.py` — Hàm `create_timeline_sheet()` chuyên cho bảng kế hoạch theo tháng.
- `references/feature_pairing.md` — Bảng tra cứu: Nhu cầu người dùng → Tính năng Excel nên dùng. Đọc khi cần quyết định tổ hợp tính năng.
- `examples/README.md` — Các ví dụ sử dụng ExcelBuilder (timeline, multi-sheet, custom styling).
