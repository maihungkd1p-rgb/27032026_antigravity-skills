@echo off
REM ============================================================
REM  RPA Runner — Dùng với Windows Task Scheduler
REM  Skill: bot-tu-dong
REM
REM  Cách dùng:
REM    1. Sửa đường dẫn PYTHON_PATH và SCRIPT_PATH bên dưới
REM    2. Test bằng cách double-click file này
REM    3. Nạp vào Task Scheduler (xem resources/task_scheduler_guide.md)
REM ============================================================

REM === CẤU HÌNH ===
SET PYTHON_PATH=python
SET SCRIPT_PATH=D:\AI Agent\Khóa Antigravity\02_Process\odoo_scraper.py
SET LOG_PATH=D:\AI Agent\Khóa Antigravity\03_Outputs\rpa_log.txt

REM === GHI LOG BẮT ĐẦU ===
echo [%date% %time%] START RPA >> "%LOG_PATH%"

REM === CHẠY SCRIPT ===
"%PYTHON_PATH%" "%SCRIPT_PATH%" --headless 2>> "%LOG_PATH%"

REM === GHI LOG KẾT THÚC ===
IF %ERRORLEVEL% EQU 0 (
    echo [%date% %time%] SUCCESS >> "%LOG_PATH%"
) ELSE (
    echo [%date% %time%] FAILED with code %ERRORLEVEL% >> "%LOG_PATH%"
)

echo [%date% %time%] =============================== >> "%LOG_PATH%"
