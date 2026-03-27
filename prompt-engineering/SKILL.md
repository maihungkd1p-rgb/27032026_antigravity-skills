---
name: prompt-engineering
description: Kỹ thuật viết prompt nâng cao để tối ưu hiệu suất LLM
---

# Prompt Engineering Patterns

Kỹ thuật prompt engineering nâng cao để tối đa hóa performance, reliability, và controllability của LLM.

## Core Capabilities

### 1. Few-Shot Learning
Cung cấp examples để LLM học pattern:

```
Ví dụ 1:
Input: "Kính râm Anna"
Output: "Kính râm thời trang Anna Eyewear - Bảo vệ mắt, tỏa sáng phong cách"

Ví dụ 2:
Input: "Gọng kính titan"
Output: "Gọng kính titan cao cấp - Siêu nhẹ, siêu bền, phong cách"

Bây giờ hãy viết cho:
Input: "Tròng kính chống ánh sáng xanh"
Output: ?
```

### 2. Chain-of-Thought Prompting
Yêu cầu LLM explain reasoning:

```
Hãy phân tích từng bước:
1. Đầu tiên, xác định vấn đề chính
2. Sau đó, liệt kê các giải pháp có thể
3. Cuối cùng, chọn giải pháp tốt nhất và giải thích lý do
```

### 3. Prompt Optimization
- **Rõ ràng**: Tránh mơ hồ
- **Cụ thể**: Định nghĩa output format
- **Có cấu trúc**: Dùng sections, numbering

### 4. Template Systems
Tạo templates có thể reuse:

```
## Role
Bạn là [ROLE]

## Context
[CONTEXT]

## Task
[TASK]

## Output Format
[FORMAT]

## Constraints
[CONSTRAINTS]
```

### 5. System Prompt Design
- Định nghĩa persona rõ ràng
- Set boundaries
- Define tone và style

## Key Patterns

### Progressive Disclosure
Không dump tất cả info ngay — reveal dần theo context

### Instruction Hierarchy
1. Role definition
2. Context
3. Task
4. Format
5. Examples
6. Constraints

### Error Recovery
```
Nếu không chắc chắn về [X], hãy:
- Hỏi clarification
- Đưa ra best guess với reasoning
- Liệt kê assumptions
```

## Cách sử dụng

### Khi nào dùng:
- Tối ưu prompts hiện tại
- Giải quyết output không consistent
- Tạo template cho tasks lặp lại

### Ví dụ prompt:
```
Dùng skill @prompt-engineering để:
- Tối ưu prompt viết báo cáo doanh thu hàng ngày
- Đảm bảo output consistent format
- Thêm error handling cho missing data
```

## Best Practices

1. **Start simple, iterate** - Không over-engineer ngay
2. **Test with edge cases** - Thử các input khó
3. **Version control prompts** - Lưu lại các versions
4. **Measure outcomes** - Track quality over time

## Common Pitfalls

❌ **Prompts quá dài** → LLM bỏ qua instructions
❌ **Thiếu examples** → Output inconsistent
❌ **Không define format** → Output khó parse
❌ **Conflicting instructions** → LLM confused

## Related Skills
- rag-engineer, llm-app-patterns, context-window-management
