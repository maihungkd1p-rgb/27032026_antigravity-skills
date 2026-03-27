# 🧠 Context Engineering cho RAG

> **Nguồn:** AI Engineering Guidebook 2025 (DailyDoseofDS)  
> **Dùng cho:** Tối ưu quality của context trước khi đưa vào LLM

---

## Nguyên tắc cốt lõi

> "RAG workflow là 80% Retrieval và 20% Generation.  
> Good retrieval + weak LLM → vẫn OK.  
> Bad retrieval + best LLM → FAIL."  
> — AI Engineering Guidebook 2025

---

## 4 Giai Đoạn Context Engineering

| # | Giai đoạn | Mô tả | Công cụ |
|---|---|---|---|
| 1 | **Write** | Lưu context ra ngoài context window (memory, state) | Zep, Redis, file system |
| 2 | **Read** | Kéo context vào context window khi cần | RAG, Tool calls, Memory |
| 3 | **Compress** | Giữ chỉ tokens cần thiết, loại bỏ noise | Summarization, REFRAG |
| 4 | **Isolate** | Tách context cho các sub-agent khác nhau | Multi-agent, Sandbox |

---

## 6 Loại Context cho Agent

| # | Loại | Vai trò | Ví dụ trong RAG |
|---|---|---|---|
| 1 | **Instructions** | Ai, tại sao, làm gì | System prompt, SKILL.md |
| 2 | **Examples** | Mẫu đúng/sai | Few-shot examples, templates |
| 3 | **Knowledge** | Domain knowledge | Vector DB chunks, documents |
| 4 | **Memory** | Lịch sử tương tác | Chat history, user preferences |
| 5 | **Tools** | Khả năng mở rộng | Search API, Calculator, Code exec |
| 6 | **Guardrails** | Giới hạn an toàn | Anti-hallucination rules |

---

## Manual RAG vs Agentic Context Engineering

### Manual RAG (truyền thống)
```
Document → Embed → Store → Query → Retrieve → Generate
```
- Chỉ 1 nguồn (vector DB)
- 1 lần retrieve, 1 lần generate
- Không validate, không retry

### Agentic Context Engineering (2025)
```
Query → Agent Rewrite → Multi-Source (Vector DB + Web + API + Memory)
      → Context Filter Agent → Synthesize Agent → Validate → Response
      ↻ Retry loop
```
- Nhiều nguồn (documents, web, API, memory)
- Agent tự quyết source nào phù hợp
- Agent validate trước khi trả
- 3 tầng: **Ingestion** → **Retrieval** → **Generation**

### 3 Tầng Agentic Context Retrieval

**Tầng 1: Ingestion**
- Kết nối nhiều nguồn dữ liệu (ERP, email, drive, web)
- Xử lý từng loại data khác nhau trước khi embed
- Detect changes → real-time sync (không re-embed toàn bộ)

**Tầng 2: Retrieval**
- Query expansion (mở rộng query mơ hồ)
- Route query đến đúng data source
- Hybrid search (semantic + keyword + graph)
- Time-awareness (dữ liệu mới quan trọng hơn cũ)

**Tầng 3: Generation**
- Citation-backed response (trả lời kèm nguồn)
- Agent check relevance trước khi gửi user

---

## REFRAG (Meta AI, 2025) — Context Compression

Vấn đề: Phần lớn chunks retrieved **không hữu ích** cho LLM.

REFRAG giải quyết bằng 3 bước:
1. **Chunk Compression:** Mỗi chunk → 1 compressed embedding (thay vì hàng trăm token)
2. **RL Relevance Policy:** Lightweight policy chọn chunks quan trọng nhất
3. **Selective Expansion:** Chỉ chunks được chọn mới expand về full tokens

**Kết quả:**
- 30x nhanh hơn time-to-first-token
- 16x context window lớn hơn
- Không mất accuracy

---

## CAG (Cache-Augmented Generation)

Chia knowledge thành 2 lớp:
- **Cold data (cache):** Dữ liệu ổn định (SOP, chính sách) → cache vào KV memory
- **Hot data (retrieve):** Dữ liệu thay đổi (bán hàng, tồn kho) → retrieve via RAG

```
Query → Check KV Cache (cold) + Retrieve Vector DB (hot) → Merge → LLM → Response
```

API hỗ trợ: OpenAI Prompt Caching, Anthropic Prompt Caching
