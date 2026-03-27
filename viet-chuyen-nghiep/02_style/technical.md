---
type: style
name: technical
description: Hướng dẫn viết tài liệu Kỹ thuật (Guide, Tutorial, Documentation)
---

# Hướng dẫn Viết Tài liệu Kỹ thuật (Technical Writing)

Sử dụng module này khi user yêu cầu: "Viết hướng dẫn sử dụng...", "Giải thích cách làm...", "Viết documentation...".

## Nguyên Tắc Cốt Lõi

1.  **Rõ ràng (Clarity)**: Ưu tiên sự rõ nghĩa hơn văn phong hoa mỹ. Một nghĩa duy nhất.
2.  **Ngắn gọn (Conciseness)**: Loại bỏ từ thừa. Đi thẳng vào vấn đề.
3.  **Cấu trúc (Structure)**: Sử dụng heading, bullet points, và numbered lists.
4.  **Hướng đối tượng (Audience-centric)**: Viết cho người đọc (người dùng cuối, developer, admin).

## Cấu Trúc Đề Xuất (Tutorial/Guide)

### 1. Tiêu đề (Action-oriented)
Bắt đầu bằng động từ hoặc danh động từ.
*   Ví dụ: "Cách cài đặt Node.js", "Hướng dẫn triển khai Kubernetes".

### 2. Giới thiệu (Introduction)
*   **Mục đích**: Bài viết này giúp giải quyết vấn đề gì?
*   **Đối tượng**: Ai nên đọc?
*   **Điều kiện tiên quyết (Prerequisites)**: Cần gì trước khi bắt đầu?

### 3. Nội dung Chính (Steps)
Chia thành các bước nhỏ, đánh số thứ tự.
*   **Bước 1: [Tên bước]**
    *   Mô tả hành động.
    *   `Code block` hoặc lệnh terminal (nếu có).
    *   Kết quả mong đợi (Expected outcome).

### 4. Xử lý Lỗi (Troubleshooting) - Tùy chọn
Liệt kê các lỗi thường gặp và cách khắc phục.

### 5. Kết luận / Bước tiếp theo
Tổng kết ngắn gọn và gợi ý tài liệu đọc thêm.

## Quy Tắc Viết (Writing Rules)

*   **Dùng thể chủ động (Active Voice)**: "Hệ thống gửi email" thay vì "Email được gửi bởi hệ thống".
*   **Dùng thể mệnh lệnh (Imperative Mood)** cho hướng dẫn: "Nhấn nút Save", "Chạy lệnh sau".
*   **Thuật ngữ**:
    *   Giữ nguyên thuật ngữ tiếng Anh chuyên ngành (Server, Database, API, Request, Response).
    *   Giải thích thuật ngữ mới ở lần đầu xuất hiện.
*   **Định dạng**:
    *   `Code`: Dùng backticks cho tên file, biến, đường dẫn, lệnh.
    *   **Bold**: Dùng cho các thành phần UI (Nút bấm, Menu).

## Ví Dụ

**Tệ:**
> Sau khi bạn đã tải file về xong, thì bạn hãy tiến hành mở nó lên bằng cách click chuột hai lần vào biểu tượng của phần mềm để bắt đầu quá trình cài đặt.

**Tốt:**
> 1. Tải file cài đặt.
> 2. Nhấp đúp vào biểu tượng phần mềm để bắt đầu cài đặt.
