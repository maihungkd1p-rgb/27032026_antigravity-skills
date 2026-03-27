---
name: docx-official
description: Tạo, chỉnh sửa và phân tích file Word (.docx) - Báo cáo, tài liệu chuyên nghiệp
---

# DOCX Creation, Editing, and Analysis

Skill này giúp bạn tạo, chỉnh sửa, hoặc phân tích file .docx (Word).
File .docx thực chất là một ZIP archive chứa các file XML và resources.

## Workflow Decision Tree

### Đọc/Phân tích Nội dung
- Trích xuất text từ file docx
- Đọc raw XML nếu cần

### Tạo Document Mới
- Sử dụng **docx-js** (JavaScript/TypeScript)
- Tạo từ scratch với formatting đầy đủ

### Chỉnh sửa Document Có Sẵn
- Đọc file hiện tại
- Thêm/sửa/xóa nội dung
- Lưu file mới

## Tạo Document Mới với docx-js

```javascript
const { Document, Packer, Paragraph, TextRun, HeadingLevel } = require('docx');

const doc = new Document({
    sections: [{
        children: [
            new Paragraph({
                text: "Báo cáo Doanh thu Anna Eyewear",
                heading: HeadingLevel.HEADING_1
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Tổng doanh thu: ", bold: true }),
                    new TextRun({ text: "150,000,000 VND" })
                ]
            })
        ]
    }]
});

Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync('baocao.docx', buffer);
});
```

## Cách sử dụng

### Khi nào dùng:
- Tạo báo cáo kinh doanh định kỳ
- Xuất phân tích dữ liệu ra Word
- Chỉnh sửa template có sẵn

### Ví dụ prompt:
```
Dùng skill @docx-official để tạo báo cáo doanh thu tuần này:
- Tiêu đề: "Báo cáo Kinh Doanh Anna Eyewear - Tuần 4"
- Bao gồm: bảng doanh thu 6 cửa hàng, biểu đồ, nhận xét
- Format: heading, bảng, bullet points
```

## Redlining Workflow

Khi review tài liệu với tracked changes:
1. Đọc document gốc
2. Đánh dấu các thay đổi
3. Xuất với revision marks

## Dependencies
- `docx` (npm package)
- `mammoth` (for reading)

## Related Skills
- xlsx-official, pdf-official, pptx-official
