---
name: Memory
description: >
  Sử dụng skill này khi user nhắc đến các vấn đề về:
  "nhớ dài hạn", "trí nhớ AI", "catastrophic forgetting", "não cá vàng",
  "hay quên", "hỏi xong quên", "hindsight", "nested learning",
  "tổ chức bộ nhớ", "thiết kế bộ nhớ", "bộ nhớ ngoài", "kiến trúc AI Agent",
  "lưu trạng thái", "dữ liệu lịch sử".
  Skill hướng dẫn cách ứng dụng Hindsight (Explicit Memory) 
  và Nested Learning (Implicit Memory) xây dựng bộ nhớ dài hạn cho Agent.
---

# Memory: Kiến trúc Hệ Thống Trí Nhớ Dài Hạn Cho AI Agent

## Mục đích
Skill này được sinh ra để khắc phục nhược điểm "não cá vàng" (Catastrophic Forgetting) của các AI Agent và LLM hiện tại. Nó đúc kết từ hai đột phá cuối năm 2025: **Hindsight** (Vectorize/Virginia Tech) và **Nested Learning** (Google Research).
Sử dụng skill này để thiết kế, tối ưu hóa và tư vấn kiến trúc bộ nhớ cho AI Agent, giúp Agent không chỉ thông minh trong ngắn hạn mà còn nhớ lâu, học liên tục và duy trì tính cách (personality) nhất quán.

## Phạm vi ứng dụng
- **Nên dùng khi:**
  - Thiết kế kiến trúc LLM/Agent cần trí nhớ dài hạn (Long-term Memory).
  - Khắc phục lỗi Agent quên thông tin cũ hoặc thay đổi tính cách đột ngột.
  - Review và nâng cấp System Prompt để cải thiện khả năng thu thập và truy xuất thông tin.
  - Xây dựng hệ thống RAG không chỉ truy xuất Fact mà cần cập nhật cả Opinion/Belief theo thời gian.
- **Không dùng khi:**
  - Tác vụ chỉ cần hỏi đáp một lần (Single-shot QA) không cần lưu trạng thái.
  - Các công việc thao tác file đơn giản không liên quan đến học liên tục (Continual Learning).

## Bộ nguyên tắc cốt lõi

1. **Hiểu rõ giới hạn của RAG Truyền Thống:** RAG thông thường chỉ truy xuất văn bản (fact) nhét vào prompt. Nó yếu ở khả năng suy luận thời gian (temporal reasoning) và không phân biệt được đâu là "Sự thật khách quan" (Fact) đâu là "Quan điểm/Ý kiến chủ quan" (Belief/Opinion).
2. **Áp dụng Hindsight (System 2 - Chậm & Cấu trúc):** Khi thiết kế lớp tương tác với System Prompt hoặc Database của Agent, hãy xây dựng 4 mạng lưu trữ riêng biệt:
   - *World:* Sự thật khách quan.
   - *Experience:* Lịch sử tương tác ngôi thứ nhất.
   - *Observation:* Tóm tắt trung lập về các thực thể (Entity Summary).
   - *Opinion:* Quan điểm, niềm tin (kèm theo mức độ tin cậy "Confidence" và mốc thời gian "Timestamp").
3. **Áp dụng Nested Learning (System 1 - Nhanh & Trực giác):** Khi tư vấn về huấn luyện hoặc chọn Backbone cho Agent, hãy ưu tiên các mô hình có cơ chế học lồng ghép (multi-timescale):
   - *Fast weights (Inner loop):* Cập nhật ngay thông tin mới.
   - *Slow weights (Outer loop):* Củng cố kiến thức dài hạn không làm hỏng tri thức cốt lõi.
4. **Hướng tới Hybrid System:** Kết hợp cả hai! Dùng *Nested Learning* ở tầng Backbone (để tự học liên tục) và *Hindsight* ở tầng Memory Layer (để giao tiếp minh bạch, giải thích được lý do Agent đưa ra quyết định dựa trên Confidence).
5. **Cấu trúc 3 Hoạt Động (R3):** System Prompt của Agent phải thể hiện được 3 việc: **Retain** (Giữ lại & trích xuất dữ kiện), **Recall** (Truy xuất) và **Reflect** (Phản hồi nhất quán theo tính cách).

## Quy trình thực hiện

1. **Bước 1: Phân tích Vấn đề của User**
   - Đọc kỹ yêu cầu (Input) để xem Agent của User đang gặp rủi ro gì (Rối loạn tính cách? Quên dữ kiện cũ? Hay đơn giản là RAG báo lỗi cấu trúc?).
2. **Bước 2: Đối chiếu với Mô hình Hybrid**
   - Xác định xem giải pháp nên can thiệp vào tầng **Backbone** (gợi ý Nested Learning) hay tầng **Memory/System Prompt** (áp dụng 4 lớp mạng của Hindsight).
3. **Bước 3: Tái cấu trúc & Tối ưu**
   - Áp dụng chuẩn R3 (Retain - Recall - Reflect) vào System Prompt hoặc lộ trình hệ thống của User.
   - Dùng cấu trúc thư mục hoặc tư duy phân lớp (World/Experience/Observation/Opinion) nếu User cần ví dụ code/cấu trúc DB.
4. **Bước 4: Đề xuất hành động (Output)**
   - Đưa ra bản thiết kế kiến trúc, hoặc bản System Prompt đã được sửa đổi, giải thích **TẠI SAO** (dựa trên Confidence/Timestamp) lại sửa như vậy.

## Ví dụ

**Đầu vào:** "Review giúp tôi System Prompt của Agent CSKH này xem tại sao nó hay quên thông tin khách hàng, trước đó khách bảo thích màu đỏ, nay nó lại tư vấn màu xanh."

**Đầu ra:** (Agent sử dụng Skill)
1. *Phân tích:* Agent CSKH đang bị rò rỉ bộ nhớ dài hạn, RAG hiện tại không phân tách được Opinion của khách hàng.
2. *Áp dụng Hindsight:* Cần bổ sung Mạng Opinion với Timestamp và Confidence vào System Prompt.
3. *Đề xuất sửa đổi System Prompt:*
   ...
   "Khi tương tác, bạn phải thực hiện 3 bước R3 (Retain, Recall, Reflect).
   - Truy xuất mạng `Opinion`: 'Khách hàng thích màu đỏ (Confidence: 0.9, Timestamp: Ngày hôm qua)'.
   - Nếu có evidence mới: 'Khách hàng vừa mua áo màu xanh (Timestamp: Hôm nay)', hãy giảm Confidence của màu đỏ xuống 0.6 và cập nhật màu xanh lên 0.8. Không được thay đổi tính cách đột ngột..."
   ...
   *Giải thích:* Việc dùng Hindsight chia tách Opinion và dùng cơ chế Confidence decay giúp Agent tư vấn tự nhiên như con người, thay đổi từ từ dựa trên bằng chứng (evidence) mới.
