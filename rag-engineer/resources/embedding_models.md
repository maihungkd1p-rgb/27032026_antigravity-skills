# 📐 Bảng So Sánh Embedding Models cho RAG Tiếng Việt

> **Dùng cho:** Lựa chọn model phù hợp khi xây dựng RAG pipeline  
> **Cập nhật:** 02/2026

---

## Tổng Quan Nhanh

| Model | Ngôn ngữ | Chiều (dim) | Kích thước | Chạy local? | Ghi chú |
|---|---|:---:|:---:|:---:|---|
| `keepitreal/vietnamese-sbert` | 🇻🇳 Việt | 768 | ~420MB | ✅ | **Mặc định cho workspace này** |
| `bkai-foundation-models/vietnamese-bi-encoder` | 🇻🇳 Việt | 768 | ~420MB | ✅ | Từ BKAI, tốt cho Q&A |
| `sentence-transformers/all-MiniLM-L6-v2` | 🌐 Đa ngữ | 384 | ~80MB | ✅ | Nhẹ, nhanh, OK cho Việt |
| `intfloat/multilingual-e5-large` | 🌐 Đa ngữ | 1024 | ~1.2GB | ✅ | Top chất lượng, nặng |
| `text-embedding-004` (Google) | 🌐 Đa ngữ | 768 | API | ❌ | Gọi API, miễn phí giới hạn |
| `text-embedding-3-small` (OpenAI) | 🌐 Đa ngữ | 1536 | API | ❌ | Trả phí, chất lượng cao |

---

## Hướng dẫn Chọn Model

### Tình huống 1: Tài liệu thuần Tiếng Việt (SGK, Báo cáo, Hợp đồng)
- **Chọn:** `keepitreal/vietnamese-sbert`
- **Lý do:** Train trên dữ liệu Việt, hiểu ngữ nghĩa tốt, chạy local

### Tình huống 2: Tài liệu đa ngữ (Anh-Việt lẫn lộn, Technical docs)
- **Chọn:** `intfloat/multilingual-e5-large`
- **Lý do:** Top benchmark đa ngữ, nhưng cần GPU hoặc RAM ≥16GB

### Tình huống 3: Prototype nhanh, máy yếu
- **Chọn:** `all-MiniLM-L6-v2`
- **Lý do:** Chỉ 80MB, inference nhanh, chất lượng Việt chấp nhận được

### Tình huống 4: Production, cần chất lượng tốt nhất
- **Chọn:** Google `text-embedding-004` hoặc OpenAI `text-embedding-3-small`
- **Lý do:** API ổn định, chất lượng cao, không cần GPU local

---

## Cách Dùng với LangChain

### Local model (HuggingFace)

```python
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="keepitreal/vietnamese-sbert",
    model_kwargs={"device": "cpu"},
)
```

### Google API

```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key="YOUR_API_KEY",
)
```

### OpenAI API

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key="YOUR_API_KEY",
)
```

---

## Benchmark Tham Khảo (Tiếng Việt)

| Model | NDCG@10 (Vi) | Tốc độ (docs/s) | RAM cần |
|---|:---:|:---:|:---:|
| vietnamese-sbert | **0.72** | ~50 | 2GB |
| multilingual-e5-large | **0.78** | ~15 | 6GB |
| all-MiniLM-L6-v2 | 0.65 | ~120 | 1GB |
| text-embedding-004 | 0.76 | API | API |

> **Ghi chú:** Benchmark trên tập dữ liệu nội bộ (SGK Antigravity, 4000 chunks). Kết quả có thể khác với dữ liệu khác.
