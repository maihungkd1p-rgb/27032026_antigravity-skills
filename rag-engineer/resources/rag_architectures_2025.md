# 🏗️ 8 Kiến Trúc RAG (2025)

> **Nguồn:** AI Engineering Guidebook 2025 (DailyDoseofDS)  
> **Dùng cho:** Agent chọn đúng kiến trúc RAG cho từng use case

---

## Bảng Tóm Tắt 8 Kiến Trúc

| # | Kiến trúc | Mô tả | Khi nào dùng | Độ phức tạp |
|---|---|---|---|:---:|
| 1 | **Naive RAG** | Retrieve bằng similarity → Generate | Query đơn giản, fact-based | ⭐ |
| 2 | **Multimodal RAG** | Xử lý text + image + audio | Cần trả lời kèm hình ảnh | ⭐⭐⭐ |
| 3 | **HyDE** | Tạo hypothetical answer → embed answer (thay vì question) → retrieve | Khi question khác style answer | ⭐⭐ |
| 4 | **Corrective RAG** | Validate kết quả retrieve vs nguồn tin cậy (web search) | Cần accuracy cao, anti-hallucination | ⭐⭐ |
| 5 | **Graph RAG** | Chuyển context thành Knowledge Graph → reasoning | Dữ liệu có quan hệ phức tạp | ⭐⭐⭐ |
| 6 | **Hybrid RAG** | Kết hợp Dense vector + Graph-based trong 1 pipeline | Cần cả text lẫn relational data | ⭐⭐⭐ |
| 7 | **Adaptive RAG** | Agent tự quyết: simple retrieve hay multi-step reasoning | Query đa dạng complexity | ⭐⭐⭐ |
| 8 | **Agentic RAG** | Agent planning + reasoning + memory + multi-source retrieve | Workflow phức tạp, nhiều tool | ⭐⭐⭐⭐ |

---

## Chi Tiết Từng Kiến Trúc

### 1. Naive RAG ⭐
```
Query → Embed → Similarity Search → Top-K chunks → LLM → Response
```
- **Ưu:** Đơn giản, dễ triển khai, chi phí thấp
- **Nhược:** Retrieve 1 lần, không thể retry nếu context sai
- **Dùng khi:** FAQ, tra cứu SOP, Q&A đơn giản

### 2. Multimodal RAG ⭐⭐⭐
```
Text/Image/Audio → Embed (multi-modal) → Cross-modal Retrieve → LLM → Response
```
- **Ưu:** Trả lời kèm hình ảnh, biểu đồ
- **Nhược:** Cần embedding model đa phương thức
- **Dùng khi:** Catalog sản phẩm có ảnh, tài liệu y khoa

### 3. HyDE (Hypothetical Document Embeddings) ⭐⭐
```
Query → LLM tạo Hypothetical Answer → Embed answer → Retrieve → LLM + Context → Response
```
- **Ưu:** Giải quyết vấn đề "question ≠ answer" về semantic
- **Nhược:** Latency tăng (gọi LLM 2 lần), hypothetical có thể hallucinate
- **Dùng khi:** Query dạng câu hỏi phức tạp, retrieval kém với naive RAG

### 4. Corrective RAG ⭐⭐
```
Query → Retrieve → Validate vs Web/Trusted Source → Filter → LLM → Response
```
- **Ưu:** Đảm bảo thông tin chính xác, up-to-date
- **Nhược:** Cần nguồn validate bên ngoài
- **Dùng khi:** Legal docs, medical info, news — mọi lĩnh vực cần accuracy

### 5. Graph RAG ⭐⭐⭐
```
Documents → Extract Entities + Relations → Build Knowledge Graph → Query → Graph Traverse + LLM → Response
```
- **Ưu:** Reasoning trên quan hệ giữa entities
- **Nhược:** Xây dựng KG tốn effort
- **Dùng khi:** Organizational data, chuỗi cung ứng, compliance

### 6. Hybrid RAG ⭐⭐⭐
```
Query → [Dense Vector Search] + [Graph Search] → Merge Results → LLM → Response
```
- **Ưu:** Kết hợp unstructured + structured data
- **Nhược:** Pipeline phức tạp, cần maintain 2 hệ thống
- **Dùng khi:** Enterprise search (text + database + relations)

### 7. Adaptive RAG ⭐⭐⭐
```
Query → Classifier: Simple? → Direct Retrieve
                      Complex? → Decompose → Multi-step Retrieve → Merge → LLM
```
- **Ưu:** Tối ưu compute — query đơn giản không cần multi-step
- **Nhược:** Cần query classifier chính xác
- **Dùng khi:** Hệ thống có đa dạng loại query

### 8. Agentic RAG ⭐⭐⭐⭐
```
Query → Agent Rewrite → Agent Route (Vector DB / Tools / Web)
      → Retrieve → Agent Validate → LLM → Agent Check → Response
      ↻ Loop nếu chưa đủ tốt
```
- **Ưu:** Robust nhất, tự sửa lỗi, multi-source
- **Nhược:** Phức tạp nhất, latency cao, cần tuning agent behavior
- **Dùng khi:** Production-grade AI assistants, complex workflows

---

## Sơ Đồ Chọn Kiến Trúc

```
Dữ liệu của bạn?
├── Chỉ text, query đơn giản → Naive RAG
├── Text + Image/Audio → Multimodal RAG
├── Có quan hệ phức tạp (entities) → Graph RAG
├── Cần accuracy tuyệt đối → Corrective RAG
├── Query đa dạng (đơn giản lẫn phức tạp) → Adaptive RAG
├── Retrieval bằng question embedding kém → HyDE
├── Cần cả text + structured data → Hybrid RAG
└── Hệ thống phức tạp, nhiều tool → Agentic RAG
```

---

## Lộ Trình Phát Triển (cho Workspace này)

| Phase | Kiến trúc | Trạng thái |
|---|---|:---:|
| 1 | Naive RAG (FAISS + vietnamese-sbert) | ✅ Đã triển khai |
| 2 | Hybrid Search (BM25 + Dense) | 📋 Planned |
| 3 | Adaptive RAG (query classifier) | 📋 Future |
| 4 | Agentic RAG (full agent loop) | 📋 Future |
