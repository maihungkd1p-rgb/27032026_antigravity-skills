---
name: rag-engineer
description: Biến Antigravity thành một Kỹ sư Xử lý Tài liệu Thông minh (RAG Engineer). Tự động hóa việc trích xuất PDF, tối ưu hóa text chunking, và xây dựng Vector Database (như FAISS) hiệu quả.
version: 2.0.0
author: Mai Hưng Workspace
tags: [rag, embedding, chunking, knowledge, faiss, pdf, vietnamese]
scope: global
---

# 🚀 SKILL: RAG ENGINEER (KỸ SƯ XỬ LÝ TÀI LIỆU THÔNG MINH)

> **Hợp nhất từ:** `rag` (Knowledge Architect) + `rag-implementation` (Code Engineer) + `rag-engineer` (IPO Rules)
> **Phiên bản:** V2.0 (Merged)

## 1. Mục Đích (Purpose)
Skill này đóng gói toàn bộ năng lực của một RAG Engineer toàn diện. Agent sẽ thành thạo cả 2 vai trò: **(1) Kiến trúc sư dữ liệu** — biết cách trích xuất, làm sạch, chunking và đánh giá chất lượng Knowledge; và **(2) Kỹ sư triển khai** — biết viết code pipeline RAG hoàn chỉnh bằng LangChain/FAISS. Đặc biệt tối ưu cho tài liệu Tiếng Việt và tuân thủ kiến trúc IPO.

## 2. Phạm Vi Ứng Dụng (Scope)
- Trích xuất dữ liệu từ file PDF (đặc biệt PDF Tiếng Việt với bảng biểu).
- Xây dựng Knowledge Items từ tài liệu thô (DOCX, Excel, scan).
- Thiết kế pipeline RAG end-to-end: Ingest → Chunk → Embed → Store → Retrieve → Evaluate.
- Đánh giá chất lượng Knowledge Base (RAG Score).

## 3. Dấu Hiệu Kích Hoạt (When to use)

- Khẩu lệnh tự nhiên (ưu tiên): "Đọc file PDF này cho tôi", "Làm sao để chat với tài liệu này", "Trích xuất nội dung file", "Tạo bộ hỏi đáp từ văn bản này", "Xử lý file tài liệu".
- **Tư vấn RAG (Self-Awareness):** "Có nên dùng RAG không?", "RAG hay Fine-tuning?", "Nên chọn kiến trúc RAG nào?", "Khi nào RAG không phù hợp?"
- Từ khóa thư viện: `pymupdf4llm`, `PyMuPDF`, `FAISS`, `Chroma`, `LangChain`, `LlamaIndex`.
- Kỹ thuật: `MarkdownTextSplitter`, `SemanticChunker`, `Embedding`, `RAG Pipeline`, `Reranking`, `HyDE`, `Agentic RAG`.
- Yêu cầu nghiệp vụ: "Trích xuất PDF", "Làm RAG", "Tìm kiếm ngữ nghĩa", "Đánh giá Knowledge".

### 3.1 Tự Nhận Biết: Khi Nào Dùng RAG (Decision Matrix)

| Dữ liệu mới/nội bộ? | Cần thay đổi hành vi LLM? | → Phương pháp |
|:---:|:---:|---|
| ❌ | ❌ | Prompt Engineering |
| ❌ | ✅ | Fine-tuning / LoRA |
| ✅ | ❌ | **✅ RAG** |
| ✅ | ✅ | **RAG + Fine-tuning (Hybrid)** |

> **Rule:** Khi User hỏi "có nên dùng RAG?", Agent phải đọc `resources/decision_matrix.md` để tư vấn chi tiết.

---

## 4. Tầng 1 — Kiến trúc sư Dữ liệu (Knowledge Architect)

### 4.1 Quy trình 5 bước chuẩn
1. **Convert:** PDF/DOCX → Markdown (Ưu tiên `pymupdf4llm` cho Tiếng Việt).
2. **Structure:** Tạo Knowledge Item (metadata.json + artifacts/).
3. **Chunk:** Chia nhỏ theo semantic boundaries (2-8KB optimal). Dùng `MarkdownTextSplitter` hoặc `MarkdownHeaderTextSplitter`.
4. **Clean:** Loại bỏ noise (page markers, escape sequences, blank lines thừa). Xem script `scripts/clean_pdf_noise.py`.
5. **Assess:** Chấm điểm RAG Score (8 tiêu chí, thang 80 điểm). Xem template `templates/assessment_checklist.md`.

### 4.2 Tiêu chuẩn Chunk Size

| Size | Đánh giá |
|------|----------|
| < 2KB | ⚠️ Quá nhỏ, thiếu context |
| **2-8KB** | ✅ **Optimal** |
| 8-15KB | ⚠️ Chấp nhận được |
| > 15KB | 🔴 Cần split |

### 4.3 Metadata bắt buộc
Mỗi chunk phải kèm: `source` (file gốc), `page_number`, `header` (H1/H2 chứa chunk), `ki_id` (nếu thuộc Knowledge Item).

---

## 5. Tầng 2 — Kỹ sư Triển khai (Implementation Engineer)

### 5.1 Standard Stack (Ưu tiên cho workspace này)
- **PDF Parsing:** `pymupdf4llm` > `pypdf` (giữ Markdown + bảng biểu Tiếng Việt).
- **Chunking:** `MarkdownTextSplitter` (theo cấu trúc Header) > `RecursiveCharacterTextSplitter`.
- **Vector DB:** `FAISS` (local, nhẹ) là mặc định. `Chroma` nếu cần persist.
- **Embeddings:** `keepitreal/vietnamese-sbert` (local) hoặc Google/OpenAI embeddings (API).

### 5.2 Advanced RAG Patterns (Tham khảo khi cần)

- **Hybrid Search:** Kết hợp BM25 (sparse) + Embedding (dense) với trọng số 0.3/0.7.
- **Multi-Query Retrieval:** Tạo nhiều biến thể câu hỏi để tăng recall.
- **Contextual Compression:** Nén document chỉ giữ phần liên quan trước khi trả kết quả.
- **Parent Document Retriever:** Chunk nhỏ để search, trả về chunk lớn để giữ context.
- **Reranking:** Cross-Encoder (`ms-marco-MiniLM-L-6-v2`) hoặc MMR cho diversity.
- **HyDE:** Tạo hypothetical answer → embed answer thay vì question → retrieve chính xác hơn.

### 5.3 8 Kiến Trúc RAG (Guidebook 2025)

| # | Kiến trúc | Khi nào dùng |
|---|---|---|
| 1 | Naive RAG | Query đơn giản, fact-based |
| 2 | Multimodal RAG | Text + Image/Audio |
| 3 | HyDE | Question khác style answer |
| 4 | Corrective RAG | Cần accuracy tuyệt đối |
| 5 | Graph RAG | Dữ liệu có quan hệ phức tạp |
| 6 | Hybrid RAG | Text + structured data |
| 7 | Adaptive RAG | Query đa dạng complexity |
| 8 | Agentic RAG | Multi-source, cần planning |

> **Chi tiết:** Đọc `resources/rag_architectures_2025.md` để xem flowchart và ví dụ từng kiến trúc.

### 5.3 Anti-Hallucination Guardrails
- Prompt RAG phải có dòng: *"If you cannot answer based on the context, say so."*
- Luôn trả kèm `source_documents` để User verify.
- Đánh giá bằng 3 metrics: Relevance (≥0.8), Groundedness (≥0.9), Recall.

---

## 6. Nguyên Tắc Cốt Lõi (Operational Rules)

- **Rule 1: Tách Biệt Pipeline (Separation of Concerns):**
  - Script 1: Extract PDF → Markdown (VD: `extract_pdf_v2.py`).
  - Script 2: Markdown → Chunking → Build FAISS Index (VD: `build_index.py`).
  - Script 3: Load Index → Query → Trả kết quả (VD: `search_index.py`).
- **Rule 2: Xử lý Tiếng Việt ưu tiên:** UTF-8 bắt buộc. Giữ dấu và cấu trúc bảng.
- **Rule 3: Cấu trúc IPO nghiêm ngặt:**
  - `01_Inputs`: File gốc (PDF/DOCX). **Tuyệt đối READ-ONLY.**
  - `02_Process`: Scripts Python + file Markdown trung gian.
  - `03_Outputs`: FAISS index, báo cáo kết quả, RAG Score report.
- **Rule 4: Quality Gate:** Không deploy Knowledge nào có RAG Score < 70%.

## 7. Quy Trình Thực Hiện Chuẩn (Standard Procedure)

1. **Nhận file** → Copy vào `01_Inputs/`.
2. **Trích xuất** → Dùng `pymupdf4llm`, lưu `.md` tại `02_Process/`.
3. **Làm sạch** → Chạy `scripts/clean_pdf_noise.py`.
4. **Chunking** → `MarkdownTextSplitter`, kèm metadata, kiểm tra 2-8KB.
5. **Build Index** → FAISS, lưu index + `.pkl` metadata tại `03_Outputs/`.
6. **Đánh giá** → Chạy queries mẫu, chấm RAG Score theo `templates/assessment_checklist.md`.
7. **Báo cáo** → Xuất kết quả RAG Score + recommedation.

## 8. Mẫu Trả Lời (Response Pattern)
- Khi viết code: `try...except` bắt buộc, comment rõ ràng, giải thích lý do chọn thư viện.
- Khi tư vấn: So sánh bảng Trade-off giữa các options (VD: FAISS vs Chroma).
- Luôn tham chiếu IPO: *"File PDF sẽ được giữ nguyên tại 01_Inputs, script xử lý tại 02_Process..."*

---

## 📁 Tài Nguyên Đi Kèm

| Thư mục | Nội dung |
|---------|----------|
| `scripts/` | `clean_pdf_noise.py`, `concat_knowledge.py` |
| `templates/` | `metadata_template.json`, `assessment_checklist.md`, `qa_pairs_template.md`, `artifact_template.md` |
| `examples/` | `README.md` (ví dụ Knowledge Item), `demo_rag_pipeline.py` (pipeline build+search hoàn chỉnh) |
| `resources/` | `embedding_models.md` (so sánh 6 models), **`decision_matrix.md`** (khi nào dùng RAG), **`rag_architectures_2025.md`** (8 kiến trúc), **`context_engineering.md`** (4 stages + REFRAG + CAG) |

## 📥 IPO Flow

| Giai đoạn | Nội dung |
|-----------|----------|
| **Input** | Raw documents (PDF, DOCX, Excel) + Domain context |
| **Process** | ① Extract → ② Structure KI → ③ Chunk (2-8KB) → ④ Clean → ⑤ Embed → ⑥ Store FAISS → ⑦ RAG Score audit |
| **Output** | FAISS index production-ready (≥70% RAG Score) + metadata + evaluation report |
