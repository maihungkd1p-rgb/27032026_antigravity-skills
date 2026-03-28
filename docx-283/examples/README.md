# Hướng Dẫn Sử Dụng & Ví Dụ (docx-283)

Đây là các ví dụ về cách Agent dùng script `docx_builder.py` để sinh ra các tài liệu Word chuyên nghiệp.

## 1. Mẫu Báo cáo Kinh Nghiệm (General Report)

```python
from docx_builder import DocxBuilder

# Khởi tạo bản dựng
builder = DocxBuilder("Báo Cáo Hoạt Động Tháng 3")

# Dành riêng trang đầu cho Mục lục (TOC)
builder.add_toc_placeholder()

# Bắt đầu nội dung với Heading 1 (sẽ tự nhảy qua trang mới do TOC Placeholder)
builder.add_heading("1. Tóm tắt Thực thi (Executive Summary)", level=1)
builder.add_paragraph("Tháng 3 đánh dấu sự tăng trưởng ở hầu hết các kênh. Tuy vậy, chúng ta cần lưu ý đến sự phình to của quỹ lương.", bold=True)

# Thông tin dạng Lists (Thay vì text liên tục)
builder.add_heading("2. Các Điểm Nổi Bật", level=1)
builder.add_bullet_list([
    "Doanh thu tổng đạt 120% KPI ngành hàng.",
    "Khách hàng VIP tăng trưởng 12%.",
    "Gia hạn mặt bằng tại CS2 đã hoàn tất sớm."
])

# Bỏ qua dòng trắng bằng Paragraph rỗng
builder.add_paragraph("")

# Sử dụng dữ liệu định lượng bằng bảng (Tables)
builder.add_heading("3. Ngân Sách Phân Tích", level=1)
builder.add_paragraph("Dưới đây là chi tiết ngân sách đã giải ngân:")

headers = ["Khoản MụC", "Dự Kiến (Tr)", "Giải Ngân", "Tình Trạng"]
data = [
    ["Chạy Facebook Ads", "50", "48", "Tốt"],
    ["Chi phí vận hành kho", "20", "25", "Vượt ngân sách"],
    ["Thưởng nhân viên", "15", "15", "Đạt"]
]
builder.add_table(headers, data)

# Lưu kết quả
builder.save("03_Outputs/Bao_cao_HD_T3_2026.docx")
```

## 2. Lịch Trình, Quy Trình (Process Manuals)

```python
from docx_builder import DocxBuilder

doc = DocxBuilder("Quy Trình Chào Đón Nhân Sự Mới")

doc.add_heading("I. Tại sao chúng ta cần quy trình này?", level=1)
doc.add_paragraph("Để nhân sự hòa nhập văn hóa Anna Eyewear nhanh chóng nhất.", italic=True)

doc.add_page_break()

doc.add_heading("II. Các bước thực hiện", level=1)
doc.add_numbered_list([
    "Ngày 1: Tham gia Orientation, cấu hình tài khoản Email/Slack.",
    "Ngày 2: Xuống cửa hàng trải nghiệm thực tế vị trí Giao dịch viên.",
    "Ngày 3: Nhận Buddy và làm bài Test hội nhập."
])

doc.save("03_Outputs/Quy_Trinh_Welcome_$#$.docx")
```
