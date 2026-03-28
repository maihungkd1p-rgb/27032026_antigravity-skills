---
name: qa-scoring
description: Chấm điểm chất lượng output theo 5 hạng mục có trọng số — score card chuẩn dùng khi thẩm định báo cáo, code, tài liệu. Tự kích hoạt khi phát hiện ngữ cảnh QA/review.
activation: ai_decision
---

# QA Scoring — Kỹ Năng Chấm Điểm Chất Lượng

## Mục Đích
Cung cấp bảng chấm điểm có trọng số để đánh giá chất lượng output một cách nhất quán, tránh đánh giá cảm tính. Skill này tập trung vào **chất lượng sản phẩm** (khác với Workflow `/reality-check` tập trung vào **trình tự kiểm tra**).

## Khi Nào Dùng Skill Này
- Khi Workflow `/reality-check` gọi đến Bước 3 (Quality Audit)
- Khi cần score card chi tiết cho báo cáo, code, hoặc tài liệu
- Khi so sánh chất lượng giữa nhiều phiên bản output
- Khi train/calibrate tiêu chuẩn chất lượng cho nhóm

## Bảng Chấm Điểm (Score Card)

| Hạng mục | Trọng số | Câu hỏi kiểm tra | Thang điểm |
|---|---|---|---|
| **Đầy đủ yêu cầu** | 30% | Output cover bao nhiêu % yêu cầu gốc? Thiếu mục nào critical? | 0-10 |
| **Chính xác dữ liệu** | 25% | Số liệu khớp nguồn? Logic không mâu thuẫn nội tại? Có cross-check? | 0-10 |
| **Trình bày & Format** | 20% | Tuân thủ Rule #8 (Neobrutalism, 🟢🟡🔴)? Dễ đọc? Heading hierarchy? | 0-10 |
| **Tính hành động** | 15% | Có đề xuất cụ thể, khả thi? Có owner? Có deadline? | 0-10 |
| **Tuân thủ IPO** | 10% | Đúng luồng 01→02→03? Input khai báo rõ? Process có trace? | 0-10 |

## Công Thức Tính Điểm

```
Điểm tổng = Σ (Điểm hạng mục × Trọng số)

Ví dụ:
  Đầy đủ:  8/10 × 0.30 = 2.40
  Chính xác: 7/10 × 0.25 = 1.75
  Trình bày: 9/10 × 0.20 = 1.80
  Hành động: 6/10 × 0.15 = 0.90
  IPO:       8/10 × 0.10 = 0.80
  ─────────────────────────
  TỔNG:              7.65/10
```

## Thang Xếp Hạng

| Điểm | Hạng | Trạng thái | Ý nghĩa |
|---|---|---|---|
| 9.0 – 10 | A | 🟢 READY | Xuất sắc, giao ngay |
| 8.0 – 8.9 | B+ | 🟢 READY | Tốt, sửa nhẹ nếu muốn |
| 7.0 – 7.9 | B | 🟡 NEEDS WORK | Khá, cần sửa 1-2 điểm |
| 6.0 – 6.9 | B- | 🟡 NEEDS WORK | Trung bình khá, sửa nhiều |
| 5.0 – 5.9 | C+ | 🟡 NEEDS WORK | Trung bình, viết lại phần lớn |
| < 5.0 | C/D | 🔴 FAILED | Không đạt, làm lại từ đầu |

## Automatic Fail Triggers

Bất kể điểm tổng, output bị FAIL ngay nếu:
- ❌ Vi phạm IPO (output ở sai thư mục, input bị sửa)
- ❌ Số liệu sai factual (sai số >5% so với nguồn)
- ❌ Fantasy claim không có bằng chứng
- ❌ Copy-paste nguyên khối từ nguồn khác không ghi credit

## Output Template

```markdown
## 📊 QA Score Card

| Hạng mục | Điểm | Trọng số | Có trọng số | Ghi chú |
|---|---|---|---|---|
| Đầy đủ yêu cầu | ?/10 | 30% | ? | [Chi tiết] |
| Chính xác dữ liệu | ?/10 | 25% | ? | [Chi tiết] |
| Trình bày & Format | ?/10 | 20% | ? | [Chi tiết] |
| Tính hành động | ?/10 | 15% | ? | [Chi tiết] |
| Tuân thủ IPO | ?/10 | 10% | ? | [Chi tiết] |
| **TỔNG** | | | **?/10** | **Hạng ?** |

**Automatic Fail**: Không / Có — [Lý do]
**Trạng thái**: 🔴 FAILED / 🟡 NEEDS WORK / 🟢 READY
```

## Lưu Ý Quan Trọng
- Skill này **chỉ chấm điểm**, không tự sửa — output sửa do Agent/User thực hiện
- Sau khi sửa, chạy lại scoring để so sánh Before/After
- Sản phẩm tốt thường qua 2-3 iteration — đó là bình thường, không phải thất bại
- Default to NEEDS WORK — vì chuyên nghiệp, không phải vì bi quan

## Related
- Workflow `/reality-check` — SOP 4 bước thẩm định (gọi skill này ở Bước 3)
- Skill `data-storytelling` — Tối ưu "Trình bày & Format"
- Skill `error-handling-patterns` — Xử lý khi phát hiện lỗi
