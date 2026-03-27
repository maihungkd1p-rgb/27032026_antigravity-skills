# 🕐 Hướng Dẫn Cài Windows Task Scheduler cho RPA

> **Mục tiêu:** Máy tính tự động chạy script Python mỗi sáng 7h  
> **Yêu cầu:** Windows 10/11, Python đã cài, file `.bat` đã test OK

---

## Bước 1: Chuẩn bị file `.bat`

Sử dụng mẫu `examples/run_scraper.bat`. Sửa 3 dòng cấu hình:

```bat
SET PYTHON_PATH=python
SET SCRIPT_PATH=D:\path\to\your_script.py
SET LOG_PATH=D:\path\to\rpa_log.txt
```

**Test:** Double-click file `.bat` → nếu script chạy OK → tiếp Bước 2.

---

## Bước 2: Mở Task Scheduler

1. Nhấn `Win + R` → gõ `taskschd.msc` → Enter
2. Ở panel bên phải, click **Create Basic Task...**

---

## Bước 3: Cấu hình Task

### Tab General
- **Name:** `RPA_Daily_Scraper`
- **Description:** `Tự động cào dữ liệu Odoo mỗi sáng 7h`
- ✅ Tick: **Run whether user is logged on or not**
- ✅ Tick: **Run with highest privileges**

### Tab Triggers
- Click **New...**
- **Begin the task:** On a schedule
- **Settings:** Daily
- **Start:** `07:00:00`
- **Recur every:** `1` days

### Tab Actions
- Click **New...**
- **Action:** Start a program
- **Program/script:** Duyệt đến file `run_scraper.bat`
- **Start in:** Thư mục chứa file `.bat`

### Tab Conditions
- ❌ Bỏ tick: **Start only if AC power** (nếu dùng laptop)
- ✅ Tick: **Wake the computer to run this task** (quan trọng!)

### Tab Settings
- ✅ Tick: **Allow task to be run on demand**
- ✅ Tick: **If the task fails, restart every:** `5 minutes`
- **Attempt to restart up to:** `3` times

---

## Bước 4: Test

1. Trong Task Scheduler, click chuột phải vào task vừa tạo
2. Chọn **Run**
3. Kiểm tra file log (`rpa_log.txt`) xem có ghi SUCCESS không

---

## Troubleshooting

| Vấn đề | Nguyên nhân | Giải pháp |
|---|---|---|
| Task không chạy | Thiếu quyền | Tick "Run with highest privileges" |
| Script lỗi import | Sai Python path | Dùng đường dẫn tuyệt đối: `C:\Python312\python.exe` |
| File không download | Timeout | Tăng `DEFAULT_TIMEOUT` trong script |
| Máy ngủ không chạy | Chưa bật wake | Tick "Wake the computer" trong Conditions |
