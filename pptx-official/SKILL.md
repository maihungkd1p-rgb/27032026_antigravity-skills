---
name: pptx-official
description: Tạo, chỉnh sửa và phân tích file PowerPoint (.pptx) - Bố cục, slide, văn bản, hình ảnh
---

# pptx-official

Kỹ năng này cung cấp hướng dẫn và nguyên tắc để tương tác an toàn với các file PowerPoint (`.pptx`) thông qua Python.

## CÔNG CỤ CHUẨN ĐƯỢC PHÊ DUYỆT
* **python-pptx**: Thư viện Python chính thức được khuyên dùng để tạo và chỉnh sửa file `.pptx`.

## QUY TRÌNH BA BƯỚC BẮT BUỘC

1. **Hiểu rõ yêu cầu & Cấu trúc:** Xác định cần tạo mới hay sửa file cũ. Nắm rõ master slide, layout và placeholders.
2. **Triển khai (python-pptx):** Tiến hành tạo slide, chèn text, hình ảnh hoặc các elements khác.
3. **Lưu & Xác minh:** Lưu file thành `.pptx` và (tuỳ chọn) có thể sử dụng VBScript/comtypes để xuất ra PDF nếu cần preview.

## NGUYÊN TẮC CỐT LÕI
* Tránh chỉnh sửa trực tiếp XML rủi ro cao nếu `python-pptx` chưa hỗ trợ.
* Sử dụng AutoShapes thay vì vẽ thủ công khi có thể.
* Đối với việc đọc nội dung .pptx, hãy tận dụng hàm `shape.has_text_frame` để an toàn trích xuất text.

## VÍ DỤ CƠ BẢN

```python
from pptx import Presentation

# Tạo mới
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "Ví dụ với python-pptx"

prs.save('test.pptx')
```
