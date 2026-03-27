"""
Playwright Skeleton — Boilerplate RPA Script
Skill: bot-tu-dong

Usage:
    python playwright_skeleton.py
    python playwright_skeleton.py --headless
    python playwright_skeleton.py --url "https://erp.example.com"

Lưu ý: Cần cài Playwright trước:
    pip install playwright
    python -m playwright install chromium
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("❌ Cần cài playwright: pip install playwright")
    print("   Sau đó chạy: python -m playwright install chromium")
    sys.exit(1)


# === CONFIGURATION ===
DEFAULT_URL = "https://erp.example.com/web/login"
DEFAULT_TIMEOUT = 30000  # 30 seconds
LOG_FILE = "rpa_log.txt"
DOWNLOAD_DIR = Path("03_Outputs/downloads")


def setup_logging():
    """Setup logging to both console and file."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger(__name__)


def run_automation(url, headless=True):
    """Main automation flow."""
    logger = setup_logging()
    logger.info(f"🚀 Bắt đầu RPA | URL: {url} | Headless: {headless}")

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # --- Block 1: Setup Browser (Stealth Mode) ---
        browser = p.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            accept_downloads=True,
        )
        page = context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        logger.info("✅ Browser đã khởi tạo")

        try:
            # --- Block 2: Login ---
            page.goto(url, wait_until="networkidle")
            logger.info("📄 Đã mở trang login")

            # TODO: Điền credentials thực tế
            page.fill('input[name="login"]', 'your_email@company.com')
            page.fill('input[name="password"]', 'your_password')
            page.click('button[type="submit"]')

            # Wait for dashboard to load
            page.wait_for_load_state("networkidle")
            logger.info("✅ Đăng nhập thành công")

            # --- Block 3: Navigate to Data Page ---
            # TODO: Thay URL và selector thực tế
            # page.goto("https://erp.example.com/web#action=pos_report")
            # page.wait_for_selector("table.o_list_table", timeout=DEFAULT_TIMEOUT)
            # logger.info("📊 Đã load bảng dữ liệu")

            # --- Block 4: Export/Download File ---
            # TODO: Click nút export và chờ download
            # with page.expect_download() as download_info:
            #     page.click('button:has-text("Export")')
            # download = download_info.value
            # save_path = DOWNLOAD_DIR / f"data_{datetime.now():%Y%m%d_%H%M}.xlsx"
            # download.save_as(str(save_path))
            # logger.info(f"📥 Đã tải file: {save_path}")

            logger.info("✅ RPA hoàn thành thành công!")

        except PlaywrightTimeout as e:
            logger.error(f"⏰ Timeout: {e}")
            # Take screenshot for debugging
            screenshot_path = f"error_{datetime.now():%Y%m%d_%H%M%S}.png"
            page.screenshot(path=screenshot_path)
            logger.error(f"📸 Screenshot lỗi: {screenshot_path}")

        except Exception as e:
            logger.error(f"❌ Lỗi: {e}")

        finally:
            # --- Block 5: Cleanup ---
            context.close()
            browser.close()
            logger.info("🔒 Browser đã đóng")


def main():
    parser = argparse.ArgumentParser(description="RPA Skeleton — Playwright Automation")
    parser.add_argument("--url", default=DEFAULT_URL, help="URL trang đăng nhập")
    parser.add_argument("--headless", action="store_true", help="Chạy ẩn (không hiện trình duyệt)")

    args = parser.parse_args()
    run_automation(args.url, args.headless)


if __name__ == "__main__":
    main()
