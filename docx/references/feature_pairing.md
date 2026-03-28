# Bảng Ghép Nối: Nhu Cầu Người Dùng → Tính Năng Word (DOCX)

Đọc tài liệu này khi bạn chuẩn bị sinh một tệp Word mới. Việc chọn ĐÚNG format quyết định độ chuyên nghiệp (Làm phong phú trực quan không làm tăng tải nhận thức).

---

## 1. Giúp người dùng 「Hiểu Cấu Trúc Nhanh Chóng」

| Tính năng | Khi nào sử dụng | Lưu ý triển khai (với Python) |
|---|---|---|
| Phân cấp Heading 1/2/3 | Xương sống của mọi tài liệu > 1 trang | `doc.add_heading('H1', level=1)` — Tuân thủ trật tự, H1 rồi mới tới H2 |
| Mục lục (TOC) | Tài liệu dài, phức tạp (> 2 trang) | Do hạn chế của gen AI, đặt một đoạn text "[Nhấn Update Table để tạo Mục lục tại đây]" ở trang 2 |
| Tóm tắt (Executive Summary) | Báo cáo kinh doanh, Đề xuất (Proposals) | Đặt ngay sau trang Bìa/TOC. In đậm key insights. |
| Ngắt trang (Page Break) | Kết thúc một Chương (Heading 1) | Luôn ngắt trang trước khi bắt đầu Heading 1 mới để bố cục thoáng |

## 2. Giúp người dùng 「Tìm Điều Quan Trọng」

| Tính năng | Khi nào sử dụng | Lưu ý triển khai (với Python) |
|---|---|---|
| Bullet Points | Liệt kê ý chính (Tránh wall-of-text) | `doc.add_bullet_list(['Ý 1', 'Ý 2'])` |
| Bôi đậm (Bold) | Nhấn mạnh KPIs, Tên riêng, Cảnh báo | Áp dụng trên Run object (`run.bold = True`) |
| Bảng (Tables) | So sánh các thông số, dữ liệu định lượng đa chiều | Thay vì viết: "A có 5, B có 6", hãy tạo bảng 2x2. |

## 3. Giúp người dùng 「Tin Tưởng Nội Dung」

| Tính năng | Khi nào sử dụng | Lưu ý triển khai (với Python) |
|---|---|---|
| Nguồn trích dẫn (Sources) | Mọi biểu đồ, số liệu lấy từ nguồn ngoài | Thêm đoạn *Nguồn cực nhỏ, in nghiêng* cuối bảng |
| Đánh số trang (Pagination) | Tài liệu chuyên nghiệp | Cài đặt trong section footer |
| Mẫu Corporate chuẩn (Styles) | Văn bản đối ngoại hoặc trình ký | Dùng Font: Arial/Calibri, màu Dark Blue cho Heading, Table style: `Medium Shading 1 Accent 1` |

## 4. Tránh Những Ảo Tưởng Này (Limits)

Để bảo vệ môi trường runtime Python-docx, **tuyệt đối không cố gắng sinh mã Code cho các tính năng sau** (trừ khi dùng file Template có sẵn):
- Điền vào "Trường Biểu Mẫu" (Word Forms / Content Controls).
- Tạo SmartArt động (Flowcharts).
- Theo dõi Thay đổi (Track Changes).
- Bình luận (Comments) tự động gán vào Sidebar.
