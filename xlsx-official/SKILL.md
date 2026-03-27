---
name: xlsx-official
description: Tạo, chỉnh sửa và phân tích file Excel (.xlsx) - Dữ liệu, công thức, biểu đồ
---

# XLSX Creation, Editing, and Analysis

Skill này giúp bạn tạo, chỉnh sửa, hoặc phân tích file .xlsx (Excel).

## ⚠️ Yêu cầu Quan trọng

**LibreOffice Required for Formula Recalculation**: LibreOffice được sử dụng để tính lại giá trị công thức.

## CRITICAL: Dùng Formulas, KHÔNG Hardcode Values

### ❌ SAI - Hardcoding Calculated Values
```python
# Sai: Tính trước rồi ghi giá trị
total = 100 + 200 + 300
ws['D1'] = total  # 600
```

### ✅ ĐÚNG - Using Excel Formulas
```python
# Đúng: Dùng công thức Excel
ws['D1'] = '=SUM(A1:C1)'
```

## Đọc và Phân tích với Pandas

```python
import pandas as pd

# Đọc file Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Phân tích
summary = df.describe()
total_revenue = df['revenue'].sum()
```

## Tạo Excel với openpyxl

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Fill, Border

wb = Workbook()
ws = wb.active
ws.title = "Doanh Thu"

# Headers
ws['A1'] = "Cửa hàng"
ws['B1'] = "Doanh thu"
ws['A1'].font = Font(bold=True)

# Data
stores = [("NDI", 50000000), ("DDA", 45000000), ("TBI", 55000000)]
for i, (store, revenue) in enumerate(stores, 2):
    ws[f'A{i}'] = store
    ws[f'B{i}'] = revenue

# Formula
ws['B5'] = '=SUM(B2:B4)'

wb.save('baocao.xlsx')
```

## Cách sử dụng

### Khi nào dùng:
- Tạo báo cáo Excel với công thức
- Phân tích dữ liệu từ file Excel
- Tạo biểu đồ từ data

### Ví dụ prompt:
```
Dùng skill @xlsx-official để tạo file Excel báo cáo doanh thu:
- Sheet 1: Bảng doanh thu 6 cửa hàng (NDI, DDA, TBI, HDU, BNI, HBT)
- Sheet 2: Biểu đồ cột so sánh doanh thu
- Có công thức SUM và AVERAGE
```

## Formula Verification Checklist

- [ ] Kiểm tra không có #REF! errors
- [ ] Kiểm tra không có #VALUE! errors
- [ ] Xác nhận formulas cập nhật đúng khi data thay đổi
- [ ] Test với sample data

## Related Skills
- docx-official, analytics-tracking
