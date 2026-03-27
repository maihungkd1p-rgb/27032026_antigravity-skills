---
name: social-scraper
description: Scrapes top posts from social media platforms (Facebook, Reddit, TikTok) and generic websites. Supports persistent login sessions to bypass basic auth walls.
---

# Social Media Scraper Skill

This skill allows you to extract the top 3 posts or articles from a targeted URL. It is designed to handle modern dynamic websites and social media platforms by using a real browser (Playwright) with a persistent context.

## Capabilities

*   **Facebook**: Extracts posts from Fanpages (requires one-time manual login).
*   **Reddit**: Extracts top posts from subreddits.
*   **TikTok**: Extracts latest videos from user profiles.
*   **Generic**: heuristic extraction for blogs, news sites, etc.

## Setup & Usage

The core logic resides in `scripts/universal_scraper.js`.

### 1. Prerequisites
Ensure Playwright dependencies are installed in the root workspace (already done if you see `node_modules`).

### 2. Running the Scraper
Use the `run_command` tool to execute the script.

**Command:**
```bash
node .agent/skills/social-scraper/scripts/universal_scraper.js <URL>
```

**Example:**
```bash
node .agent/skills/social-scraper/scripts/universal_scraper.js https://www.facebook.com/VnExpress
```

### 3. Handling Authentication (Important)
The scraper uses a persistent browser data directory (`browser_data`).
*   **First Run**: The browser window will appear. If the site (e.g., Facebook) requires login, the Agent should instruct the User to **manually log in** within that window.
*   **Subsequent Runs**: The script will reuse the cookies/session, skipping the login screen.

### 4. Output
*   Results are printed to the console (STDOUT).
*   Results are also saved to `scrape_results.json` in the current working directory.
*   Format: JSON array of objects `{ rank, title/content, link }`.

## Troubleshooting
*   **"Browser not found"**: Run `npx playwright install`.
*   **"Timeout"**: The site might be loading too slowly or is blocking automation. Try running in headed mode (default) to debug visually.
