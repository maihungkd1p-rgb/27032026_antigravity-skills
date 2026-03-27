# 🧭 Decision Matrix: Khi Nào Dùng RAG?

> **Nguồn:** AI Engineering Guidebook 2025 (DailyDoseofDS)  
> **Dùng cho:** Agent tự nhận biết khi nào RAG phù hợp, khi nào KHÔNG nên dùng RAG

---

## Ma Trận Quyết Định (2 trục)

| | Ít External Knowledge | Nhiều External Knowledge |
|---|---|---|
| **Ít Adaptation** | ➡️ **Prompt Engineering** | ➡️ **RAG** |
| **Nhiều Adaptation** | ➡️ **Fine-tuning** | ➡️ **RAG + Fine-tuning (Hybrid)** |

### Giải thích 2 trục:
- **External Knowledge:** LLM có cần tham khảo dữ liệu mới / nội bộ không?
- **Adaptation:** LLM có cần thay đổi hành vi, văn phong, từ vựng chuyên ngành không?

---

## ✅ Dùng RAG khi:

1. **Dữ liệu nội bộ / riêng tư:** KPI công ty, hợp đồng, SOP nội bộ, sách chưa công khai
2. **Dữ liệu thay đổi liên tục:** Giá sản phẩm, tồn kho, tin tức, khuyến mãi tháng
3. **Cần trích nguồn (citation):** Trả kết quả kèm "lấy từ trang X, đoạn Y"
4. **Không muốn train lại model:** Chỉ cần "nạp thêm kiến thức"
5. **Vocabulary + Style giữ nguyên:** Không cần LLM nói kiểu khác

## ❌ KHÔNG dùng RAG khi:

1. **Chỉ cần thay đổi format output:** → Prompt Engineering đủ
2. **Cần LLM nói giọng chuyên ngành:** (VD: y khoa, pháp lý) → Fine-tuning
3. **Muốn tóm tắt toàn bộ tài liệu:** RAG chỉ lấy top-K chunks, không thấy toàn bộ → Dùng Long Context hoặc Map-Reduce
4. **Query quá mơ hồ:** "Kể cho tôi mọi thứ" → RAG similarity search không hiệu quả
5. **Dữ liệu có cấu trúc quan hệ phức tạp:** Cây gia phả, mạng lưới nhân sự → Graph RAG hoặc SQL

---

## 🔀 Cây Quyết Định cho Agent

```
User có yêu cầu mới?
├── Cần dữ liệu mới / nội bộ?
│   ├── CÓ → Dữ liệu thay đổi thường xuyên?
│   │   ├── CÓ → ✅ RAG (vector DB + real-time sync)
│   │   └── KHÔNG → Dữ liệu ổn định?
│   │       ├── CÓ, lượng nhỏ → CAG (Cache-Augmented) hoặc Long Context
│   │       └── CÓ, lượng lớn → ✅ RAG
│   └── KHÔNG → Cần thay đổi hành vi/giọng?
│       ├── CÓ → Fine-tuning hoặc LoRA
│       └── KHÔNG → Prompt Engineering đủ
└── Cần reasoning phức tạp, nhiều nguồn?
    ├── CÓ → Agentic RAG (Agent quyết định retrieve)
    └── KHÔNG → Naive RAG đủ
```

---

## So Sánh 3 Phương Pháp

| Tiêu chí | Prompt Engineering | RAG | Fine-tuning |
|---|---|---|---|
| **Thay đổi model?** | ❌ Không | ❌ Không | ✅ Có (train weights) |
| **Cần data mới?** | ❌ | ✅ Vector DB | ✅ Training data |
| **Chi phí** | 💚 Thấp | 💛 Trung bình | 🔴 Cao |
| **Tốc độ setup** | ⚡ Phút | 🕐 Giờ | 🕐 Ngày/Tuần |
| **Khi nào dùng** | Task đơn giản | Tra cứu knowledge | Thay đổi hành vi |
| **Hạn chế** | Giới hạn context | Chỉ top-K, không summarize | Tốn GPU, data quality |

---

## Ví Dụ Thực Tế (Chuỗi Kính Mắt)

| Tình huống | Phương pháp |
|---|---|
| "Chính sách bảo hành mắt kính của Anna là gì?" | ✅ RAG (tra SOP nội bộ) |
| "Viết email marketing giọng trẻ trung cho Gen Z" | Fine-tuning hoặc Prompt |
| "Tóm tắt toàn bộ SGK Antigravity" | ❌ Không dùng RAG → Long Context |
| "Sản phẩm nào bán chạy nhất tháng này?" | ✅ RAG (nạp data bán hàng) |
| "So sánh gọng Titanium X1 vs K2 dựa trên spec" | ✅ RAG (nạp catalog SP) |
| "Tại sao doanh thu Q.7 giảm?" | Agentic RAG (cần nhiều nguồn) |
