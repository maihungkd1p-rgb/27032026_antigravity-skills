# Ví dụ: QA Score Card cho Báo cáo Doanh thu Ngày

## 📊 QA Score Card

| Hạng mục | Điểm | Trọng số | Có trọng số | Ghi chú |
|---|---|---|---|---|
| Đầy đủ yêu cầu | 8/10 | 30% | 2.40 | Đủ 6 CH, thiếu phần benchmark vs target |
| Chính xác dữ liệu | 9/10 | 25% | 2.25 | Cross-check 3 số liệu với ERP — khớp |
| Trình bày & Format | 7/10 | 20% | 1.40 | Có 🟢🟡🔴 nhưng thiếu biểu đồ trend |
| Tính hành động | 6/10 | 15% | 0.90 | Có đề xuất nhưng thiếu owner cụ thể |
| Tuân thủ IPO | 10/10 | 10% | 1.00 | Input từ 01_Inputs/ERP_daily.csv, output tại 03_Outputs |
| **TỔNG** | | | **7.95/10** | **Hạng B+** |

**Automatic Fail**: Không
**Trạng thái**: 🟢 READY (sửa nhẹ nếu muốn)

## Ghi Chú Đánh Giá
- Điểm mạnh: Dữ liệu chính xác, IPO tuân thủ tốt
- Cần cải thiện: Thêm biểu đồ trend 7 ngày, gán owner cho mỗi đề xuất
- Ước lượng effort sửa: 15 phút
