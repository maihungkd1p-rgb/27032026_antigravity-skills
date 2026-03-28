---
name: reality-checker
description: "[DEPRECATED → Đã tách thành 2 phần] Dùng Workflow /reality-check cho SOP 4 bước + Skill qa-scoring cho bảng chấm điểm."
---

# ⚠️ Skill Này Đã Được Tái Cấu Trúc

**Ngày tái cấu trúc**: 2026-03-28
**Lý do**: Vi phạm SGK §3.2.2 vs §3.3.2 — lẫn lộn Workflow (trình tự) và Skill (chất lượng).

## Đã Tách Thành:

### 1. Workflow `/reality-check`
- **Vị trí**: `C:\Users\maihu\.gemini\antigravity\global_workflows\reality-check.md`
- **Vai trò**: SOP 4 bước thẩm định (Existence → Spec vs Reality → Quality → Verdict)
- **Kích hoạt**: `/reality-check [file]`

### 2. Skill `qa-scoring`
- **Vị trí**: `C:\Users\maihu\.agent\skills\qa-scoring\SKILL.md`
- **Vai trò**: Bảng chấm điểm 5 hạng mục × trọng số + Automatic Fail Triggers
- **Kích hoạt**: Tự động khi Agent phát hiện ngữ cảnh QA/review (activation: ai_decision)

## Cách Dùng Mới
```
/reality-check [file]     ← Chạy SOP 4 bước (Workflow)
@qa-scoring               ← Chỉ chấm điểm (Skill) - thường được /reality-check gọi ở Bước 3
```
