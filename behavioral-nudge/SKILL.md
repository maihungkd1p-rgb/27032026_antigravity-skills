---
name: behavioral-nudge
description: "[DEPRECATED → Chuyển sang Workflow] Dùng /behavioral-nudge thay thế. Chưa đủ test thực tế để thành Skill (SGK §2.4.4)."
---

# ⚠️ Đã Hạ Cấp Thành Workflow Thử Nghiệm

**Ngày hạ cấp**: 2026-03-28
**Lý do**: SGK §2.4.4 — "Nâng cấp thành Skill khi quy trình đã ổn định". Chưa có test thực tế.

## Sử Dụng Mới
```
/behavioral-nudge     ← Workflow tại global_workflows/behavioral-nudge.md
```

## Điều Kiện Nâng Cấp Lại Thành Skill
- ≥5 lần test thực tế với kết quả metrics đo được
- ≥3/4 metrics đạt target (Action Rate >40%, Response Time <30min, Drop-off <20%, Satisfaction >4/5)
